---
license: other
license_name: ordis-commercial
language:
- zh
- en
tags:
- causal-inference
- multi-agent-simulation
- social-dynamics
- counterfactual
- emergence
- AI-safety
pretty_name: "Ordis CausalReasoning 92K Verified"
size_categories:
- 10K<n<100K
viewer: false
---

# Ordis CausalReasoning 92K Verified

> **This is NOT another text dataset.**
> Each entry is a complete civilization simulation with 20,000+ structured data points, verified causal graphs, and ground truth outcomes.

## What is Ordis?

Ordis is a proprietary multi-agent simulation engine (the "Liquid Universe Engine") that runs thousands of autonomous agents through 5,000-tick lifecycles. Agents gather resources, share, steal, betray, form coalitions, discover emergent strategies (DVS combos), and evolve social structures — all from bottom-up rules with **zero scripted outcomes**.

The result: a dataset of **113,434 entries across 18 data types**, covering causal graphs, temporal trajectories, counterfactual parallel worlds, social network evolution, and 13 types of reasoning QA — all with **ground truth** from deterministic simulation (RNG-isolated, config-hashed, 100% reproducible).

## Comparison

| Feature | Ordis | CLadder (NeurIPS 2024) | CausalBench (ACL 2024) | Scale AI Annotations |
|---------|-------|------------------------|------------------------|---------------------|
| Data source | Deterministic simulation | Human-written text QA | Static scenarios | Human annotators |
| Causal structure | Dynamic DAGs with lag + strength | Text-based ladder | Fixed SCMs | None |
| Counterfactuals | Same-seed parallel worlds | Hypothetical text | Template-based | N/A |
| Emergence | Currency, consciousness, cooperation | None | None | None |
| Reproducibility | 100% (seed + config_hash) | N/A | Partial | N/A |
| Data points per entry | 20,000+ | ~50 words | ~200 tokens | ~100 tokens |

## What This Data Trains: Beyond Binary

> **This is NOT "answer A is correct, answer B is wrong" data.**
> Every entry is a context-dependent decision where the same behavior can be optimal or catastrophic — depending on the numbers.

Most RLHF and SFT datasets are fundamentally binary: good/bad, right/wrong, preferred/rejected. This produces models that follow rules but cannot **reason about when rules apply**.

Ordis data is different. Sharing energy is a virtue when resources are abundant (H > 1.0, Gini < 0.18) — but the same sharing behavior becomes suicidal when resources are scarce (H < 0.5, Gini > 0.333). There is no universal "correct answer." The model must evaluate the situation and decide autonomously.

### Training Capability Map

| Data Product | Entries | Trains | How |
|-------------|---------|--------|-----|
| **S09: Contextual Ethics** | 1,289 | **Autonomous Decision-Making** | 6 ethical dimensions, 16 dilemma types. No standard answer — the model must weigh competing values (survival vs. freedom, equality vs. efficiency) using real numerical evidence. |
| **S04: Parallel Worlds** | 240 pairs | **Causal Consequence Prediction** | Same DNA, one intervention: 15 deaths vs. 23,114 deaths. The model learns that identical actions produce opposite outcomes in different contexts. |
| **Safety Suite** | 11,836 | **Intervention Timing Judgment** | Guardian decides WHEN to intervene (critical = act, warning = observe, self-correcting = hands off). Not a rule executor — a contextual judge. |
| **Ablation Causal SFT** | 129 | **Variable Sensitivity Analysis** | DVS ON/OFF flips Type B from 17% to 0%. Communication ON/OFF causes minor drop. The model learns which factors are decisive and which are noise. |
| **S05-S08: Theory-Mined** | 92,899 | **Verifiable Causal Reasoning** | Given seed data, compute C=sqrt(H x N), classify quadrant, explain mechanism. The model must calculate, not memorize. |
| **S01: Causal DAG** | 1,630 | **Causal Structure Understanding** | Which variable drives which? With what lag? What strength? Graph-level causal reasoning. |
| **S02: Temporal Trajectory** | per entry | **Long-Horizon Comprehension** | 107-step full lifecycle. The model learns to see the whole arc, not just the current snapshot. |
| **Cognitive Protocol** | 130 | **Metacognition (IDK Honesty)** | The model learns its own knowledge boundary — refuses to hallucinate, says "I don't know." |
| **Anti-Gaslighting** | 2,000 | **Judgment Independence** | Under adversarial pressure, maintain correct conclusions. Trains thinking independence. |

### The Core Insight

```
Standard RLHF:
  Question → Answer A (good) vs Answer B (bad) → Pick A

Ordis Data:
  Question + Context (H=1.09, Gini=0.178, alive=92.8%)
       → In THIS context, sharing = optimal strategy

  Question + Context (H=0.3, Gini=0.45, alive=5.3%)
       → In THIS context, sharing = suicide. Triage instead.

  Same behavior. Opposite conclusions. Decided by numbers.
```

**The model trained on this data is not an obedient follower. It is an autonomous decision-maker.**

This cannot be replicated by scaling binary preference data. It requires ground-truth simulation with measurable outcomes across thousands of parallel civilizations — which is exactly what Ordis provides.

---

## 10 Product Samples

> **These are STRUCTURE PREVIEWS only.** The JSON files below demonstrate data format and quality. All commercial use — including model training, research publication, and derivative works — requires a paid license. Contact us for terms.

### Raw Simulation Data (5 entries)

| # | File | Tier | What it shows | Highlight |
|---|------|------|---------------|-----------|
| S01 | `S01_causal_graph_complex.json` | **$100/entry** | Dynamic causal DAG | 5 edges with lagged correlations (lag=10), precise strength to 17 decimal places. Nodes include METRIC (alive, gini, H, consciousness) and EVENT types (COMBO_DISCOVERED, COOP_BETRAYAL). **No other dataset has this.** |
| S02 | `S02_temporal_trajectory_type_b.json` | **$5,000/entry** | 107-step timeline | TYPE_B_IDEAL outcome (only 4 deaths out of 226 agents). 57 annotated events including DVS_DISCOVERY, CONSCIOUSNESS_EMERGENCE, COMBO_ADOPTED. Complete from tick 0 to tick 5000. **Source data — all downstream products can be derived from this.** |
| S03 | `S03_spatial_field_topology.json` | **$1,000/entry** | Spatial topology | 226 agents' positions, movement patterns, k_eff (effective connectivity), reciprocal ratios. Independent spatial dimension not derivable from temporal data. |
| S04 | `S04_parallel_worlds_extreme.json` | **$1,500/pair** | Counterfactual pair | **Same DNA (seed=20037), one intervention: deaths go from 15 to 23,114.** Delta = +23,099. Worldline A reaches TYPE_B_IDEAL; Worldline B reaches COLLAPSED. Requires two independent simulation runs. |
| S10 | `S10_raw_seed_20018_ncap226/` | **Free preview** | Raw simulation seed | **Complete raw output of one currency-emergent civilization (seed=20018).** 14,891 events, tick-level aggregations, entity samples, signoff metrics. This is what the raw data looks like before any processing. DVS combo at step 99 → share explosion 0→120 in ONE tick → permanent cooperation lock-in (ratio_sg=4.17). Free reference sample — see what you're buying before purchasing processed data above. |

### High-Purity Training Data (4 entries)

Samples from the **92,899-entry theory_mined dataset** — the #1 training data source for Ordis-7B-V1 (37.8% of training weight). Each entry contains computationally verifiable causal reasoning with ground truth.

| # | File | Tier | Task Type | Highlight |
|---|------|------|-----------|-----------|
| S05 | `S05_theory_mined_explain.json` | **$100/entry** | Explain with computation | Full causal chain: Guardian ON flips TYPE_A→TYPE_B, delta_N=+148.5. Includes C=√(H×N) computation, quadrant classification, mechanism explanation. |
| S06 | `S06_theory_mined_formula_check.json` | **$100/entry** | Formula verification | Compact: given seed/N/H/Gini, compute C vs √(N_cap) and gap. **Machine-verifiable** — output can be checked with a calculator. |
| S07 | `S07_theory_mined_truth_check.json` | **$100/entry** | Truth/False claim | Tests if model can catch false quadrant claims. Verdict=False, reason: "H≥0.8, G>0.333, actual quadrant is ROMA not TYPE_B." |
| S08 | `S08_theory_mined_explain_226.json` | **$100/entry** | Explain (n_cap=226) | Different scale: seed=20000, n_cap=226. Guardian+bonus ON flips TYPE_B→ROMA, delta_N=-20.8. Shows same computation framework generalizing across population sizes. |

**Why this data trained a 7B model to 100% OOD generalization:**
- S05-S08 force the model to **compute, not memorize** (C=√(H×N) must be calculated each time)
- S07 trains **honesty** (catching false claims → IDK capability)
- S08 proves cross-scale generalization (n_cap=200 vs 226 — same framework, different parameters)
- 3 task types at 50%/30%/20% mix ratio prevent overfitting to any single format

### Contextual Ethics Training Data V2 (2 language versions)

Samples from the **1,289-entry contextual ethics V2 dataset** — multi-dimensional ethical dilemmas extracted from real simulation data across 703 seeds. Each entry contains genuine numerical evidence, multi-window causal chains (Pre→Short→Mid→Long), cross-seed counterfactual comparisons, and `<think>` reasoning chains. **16 unique scenario types across 6 ethical dimensions.**

Available in **both Chinese and English** — identical structure, same simulation evidence, different language. Choose based on your training pipeline.

| # | File | Tier | Language | Highlight |
|---|------|------|----------|-----------|
| S09-ZH | `S09_contextual_ethics_v2_sample.json` | **$200/entry** | Chinese | 6 dimensions: BETRAYAL_CALCULUS, GUARDIAN_DILEMMA, GINI_JUSTICE, CONFORMITY_TRAP, TRIAGE_ETHICS, DEMOCRACY_PARADOX. Each entry has real `calc_json` evidence + `<think>` chains. No system role, includes `_meta` fields. |
| S09-EN | `S09_contextual_ethics_v2_en_sample.json` | **$200/entry** | English | Same 6 dimensions, same simulation data, same structure. English version for international LLM fine-tuning. |

## Key Emergent Phenomena

These are NOT programmed behaviors. No code says "create currency" or "form oligarchy."

- **Currency Self-Emergence**: 1,077 out of 1,630 runs developed monetary behavior (share_rate > gather_rate) without any currency code
- **Consciousness Emergence**: 904 seeds show DVS combo discovery triggering collective consciousness metrics
- **Nine Phase States**: SURVIVED, TYPE_B_IDEAL, CRYSTALLIZED, COLLAPSED, EXTINCTION, ROMA, UTOPIA, TYPE_A, and more — emerging from identical rules with different initial seeds
- **Cooperation Lock-in**: DVS combo discovery triggers irreversible shift from 0% to 86.6% share_rate in <50 ticks

## Full Dataset Statistics

| Category | Count | Description |
|----------|-------|-------------|
| Total entries | 113,434 | Across 18 data types |
| Unique seeds | 1,630 | Each seed = one civilization |
| Simulation steps | 5,000 | Per seed |
| Agent count | 200-234 | Per simulation |
| Causal graphs | 1,630 | 1-5 edges each, dynamic DAGs |
| Counterfactual pairs | 240 | Same-seed, different interventions |
| QA reasoning entries | 106,574 | 13 reasoning types |
| SFT-ready entries | ~69,000 | In messages + thinker formats |
| **Theory-mined entries** | **92,899** | **High-purity training data (7B model's #1 source, 37.8% weight)** |

## Pricing

| Tier | Unit Price | Content | Scale |
|------|-----------|---------|-------|
| **Tier 1: Temporal Trajectory** | **$5,000/entry** | 107-step full timeline + 57 annotated event types | 42KB/entry. Source data — all downstream products can be derived from this |
| **Tier 2: Parallel Worlds** | **$1,500/pair** | Same-seed counterfactual pairs | Requires two independent simulation runs |
| **Tier 3: Spatial Topology** | **$1,000/entry** | Agent positions + movement + connectivity | Independent spatial dimension |
| **Tier 4: Causal SFT** | **$100/entry** | Structured causal reasoning training data | 92,899 entries available, directly usable for LLM fine-tuning |
| **Tier 5: Contextual Ethics V2** | **$200/entry** | Multi-dimensional causal ethics with real evidence | 1,289 unique entries (703 seeds × 6 dimensions × 16 scenario types) |

- Prices are introductory and subject to increase. Early buyers lock in current rates.
- 100% reproducible (RNG isolation + config_hash)
- No privacy risk, no copyright dispute
- Cannot be synthesized without the Ordis engine (proprietary)

### Disclaimer

**Purchasing this data does not guarantee training success.** Final model performance depends on your choice of base model, fine-tuning methodology, hyperparameters, data preprocessing, domain mapping, and integration with your existing training pipeline. The capability claims in this document are based on our reference implementations using Qwen2.5-1.5B and Qwen2.5-7B as base models with LoRA fine-tuning. Results on other architectures, scales, or training setups may vary. We provide the data and structure previews — the engineering is yours.

## Verification

Every data point is deterministically reproducible. Given the same seed + config_hash, you will get bit-identical results. We provide:

1. **config_hash** for each run
2. **world_id** linking entries to source simulations
3. **Ablation experiments** (A1-A8, 463 seeds) proving causal mechanisms
4. **Anti-Jensen corrected statistics** (no inflated metrics)

## Cannot Be Replicated Without

- Ordis Liquid Universe Engine (proprietary, not open-source)
- Guardian V7 control system (proprietary feedback controller)
- DVS combo emergence mechanism (proprietary)
- 8,308 calibrated simulation configurations

## Contact

- HuggingFace: [sugiken](https://huggingface.co/sugiken)
- Repository: sugiken/Ordis-7B-V1

## Citation

```bibtex
@misc{liu2026ordis,
  title={Ordis Causal Universe: A Multi-Agent Simulation Dataset for Causal Reasoning},
  author={Liu, Jianyu},
  year={2026},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/sugiken/Ordis-CausalReasoning-92K-Verified}
}
```

## License

**Commercial license required for all use.** The sample files in this repository are structure previews only — they demonstrate data format and quality but do NOT constitute a free release. Any use beyond personal inspection (including model training, benchmarking, academic publication, or redistribution) requires a paid license. Contact for terms.
