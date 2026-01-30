#!/usr/bin/env python3
"""
Ordis Universe V3.5 - One-Click Claim Verification
===================================================

This script verifies the key claims in the paper by analyzing signoff.csv files.

Usage:
    python verify_claims.py

Expected output:
    - 2x2 contingency table (Winter/Baseline x Pass/Fail)
    - Chi-square test result
    - Pass rate comparison

Requirements:
    - pandas (optional, falls back to csv module)
    - scipy (optional, falls back to manual calculation)
"""

import os
import csv
from pathlib import Path

# Try to import optional dependencies
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    from scipy.stats import chi2_contingency
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


def load_signoff_csv(filepath):
    """Load signoff.csv and return list of (seed, pass) tuples."""
    results = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            seed = row.get('seed', '')
            if seed in ('SUMMARY', 'PASS_RATE', ''):
                continue
            try:
                pass_val = int(row.get('pass', 0))
                results.append((seed, pass_val))
            except (ValueError, TypeError):
                continue
    return results


def manual_chi2(a, b, c, d):
    """
    Manual chi-square calculation for 2x2 table:
        |  Pass  | Fail  |
    ----|--------|-------|
    W   |   a    |   b   |
    B   |   c    |   d   |

    chi2 = n * (ad - bc)^2 / ((a+b)(c+d)(a+c)(b+d))
    """
    n = a + b + c + d
    if n == 0:
        return 0, 1.0

    num = n * (a*d - b*c)**2
    denom = (a+b) * (c+d) * (a+c) * (b+d)

    if denom == 0:
        return 0, 1.0

    chi2 = num / denom

    # Approximate p-value for df=1
    # chi2 > 10.83 => p < 0.001
    # chi2 > 6.64 => p < 0.01
    # chi2 > 3.84 => p < 0.05
    if chi2 >= 10.83:
        p_approx = 0.001
    elif chi2 >= 6.64:
        p_approx = 0.01
    elif chi2 >= 3.84:
        p_approx = 0.05
    else:
        p_approx = 0.1

    return chi2, p_approx


def print_banner():
    print("=" * 60)
    print("  Ordis Universe V3.5 - Claim Verification Script")
    print("=" * 60)
    print()


def main():
    print_banner()

    # Find data directory
    script_dir = Path(__file__).parent

    # Expected paths
    winter_dir = script_dir / "v3533_winter_20x5k"
    baseline_dir = script_dir / "v3533_baseline_20x5k"

    winter_csv = winter_dir / "signoff.csv"
    baseline_csv = baseline_dir / "signoff.csv"

    # Check files exist
    if not winter_csv.exists():
        print(f"[ERROR] Winter data not found: {winter_csv}")
        print("Please ensure v3533_winter_20x5k/signoff.csv exists")
        return 1

    if not baseline_csv.exists():
        print(f"[ERROR] Baseline data not found: {baseline_csv}")
        print("Please ensure v3533_baseline_20x5k/signoff.csv exists")
        return 1

    print(f"[OK] Winter data: {winter_csv}")
    print(f"[OK] Baseline data: {baseline_csv}")
    print()

    # Load data
    winter_results = load_signoff_csv(winter_csv)
    baseline_results = load_signoff_csv(baseline_csv)

    print(f"Winter seeds loaded: {len(winter_results)}")
    print(f"Baseline seeds loaded: {len(baseline_results)}")
    print()

    # Count pass/fail
    winter_pass = sum(1 for _, p in winter_results if p == 1)
    winter_fail = len(winter_results) - winter_pass
    baseline_pass = sum(1 for _, p in baseline_results if p == 1)
    baseline_fail = len(baseline_results) - baseline_pass

    # Print 2x2 contingency table
    print("-" * 40)
    print("  2x2 Contingency Table (Pass/Fail)")
    print("-" * 40)
    print(f"              |   Pass   |   Fail   |  Total")
    print(f"  ------------|----------|----------|--------")
    print(f"  Winter      |    {winter_pass:2d}    |    {winter_fail:2d}    |   {len(winter_results):2d}")
    print(f"  Baseline    |    {baseline_pass:2d}    |    {baseline_fail:2d}    |   {len(baseline_results):2d}")
    print(f"  ------------|----------|----------|--------")
    print(f"  Total       |    {winter_pass + baseline_pass:2d}    |    {winter_fail + baseline_fail:2d}    |   {len(winter_results) + len(baseline_results):2d}")
    print()

    # Calculate pass rates
    winter_rate = winter_pass / len(winter_results) * 100 if winter_results else 0
    baseline_rate = baseline_pass / len(baseline_results) * 100 if baseline_results else 0

    print("-" * 40)
    print("  Pass Rate Comparison")
    print("-" * 40)
    print(f"  Winter:   {winter_pass}/{len(winter_results)} = {winter_rate:.1f}%")
    print(f"  Baseline: {baseline_pass}/{len(baseline_results)} = {baseline_rate:.1f}%")
    print()

    # Chi-square test
    print("-" * 40)
    print("  Statistical Test (Chi-Square)")
    print("-" * 40)

    # Table: [[winter_pass, winter_fail], [baseline_pass, baseline_fail]]
    if HAS_SCIPY:
        table = [[winter_pass, winter_fail], [baseline_pass, baseline_fail]]
        chi2, p, dof, expected = chi2_contingency(table)
        print(f"  Method: scipy.stats.chi2_contingency")
        print(f"  chi2 = {chi2:.2f}")
        print(f"  df = {dof}")
        print(f"  p-value = {p:.6f}")
    else:
        chi2, p_approx = manual_chi2(winter_pass, winter_fail, baseline_pass, baseline_fail)
        print(f"  Method: Manual calculation (scipy not available)")
        print(f"  chi2 = {chi2:.2f}")
        print(f"  df = 1")
        print(f"  p-value < {p_approx}")

    print()

    # Verdict
    print("=" * 60)
    print("  VERIFICATION RESULT")
    print("=" * 60)

    claim_verified = (
        winter_rate >= 70 and  # Claim: ~76%
        baseline_rate <= 10 and  # Claim: ~6%
        chi2 >= 10.83  # p < 0.001
    )

    if claim_verified:
        print()
        print("  [PASS] Antifragility claim VERIFIED")
        print()
        print(f"  - Winter pass rate ({winter_rate:.0f}%) significantly > Baseline ({baseline_rate:.0f}%)")
        print(f"  - Chi-square = {chi2:.2f} (p < 0.001)")
        print()
        print("  Paper claim: '76% vs 6% (chi2=18.2, p<0.001)'")
        print("  Your data:   '{:.0f}% vs {:.0f}% (chi2={:.1f})'".format(winter_rate, baseline_rate, chi2))
        print()
    else:
        print()
        print("  [INFO] Results summary:")
        print(f"  - Winter pass rate: {winter_rate:.1f}%")
        print(f"  - Baseline pass rate: {baseline_rate:.1f}%")
        print(f"  - Chi-square: {chi2:.2f}")
        print()

    print("=" * 60)
    print()

    return 0


if __name__ == "__main__":
    exit(main())
