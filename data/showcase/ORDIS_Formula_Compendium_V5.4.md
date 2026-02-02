# ORDIS Formula Compendium V5.4
# 刘氏公式大全 (对外严谨版)

> **Document Type**: Supplementary Material / 补充材料
> **Version**: V5.4
> **Date**: 2026-01-11
> **Status**: Paper-Ready (External Publication)

---

## Version Note / 版本说明

> **External vs Internal Terminology / 对外与内部术语差异**
>
> This document (V5.4) uses **scientifically rigorous terminology** for external publication.
> Internal documentation (永乐大典) retains original working terminology for continuity.
>
> 本文档(V5.4)为**对外发表**采用科学严谨术语。
> 内部文档(永乐大典)保留原始工作术语以保持连续性。
>
> | Internal Term | External Term (V5.4) | Reason |
> |---------------|---------------------|--------|
> | 守恒定律 | 相内判别指标 | CV_ALL >> CV_PASS |
> | 物理定律 | 经验规律 | 非第一性原理推导 |
> | 宇宙常数 | 工程参数 | Ordis系统专用 |

---

## V5.4 Methodological Correction / 方法论修正

### Findings Summary / 发现摘要

| Claim | Original Status | Revised Status | Reason |
|-------|----------------|----------------|--------|
| Σ = H + ln(N) ≈ 6.27 | "Conservation Law" | **Phase-Specific Indicator** | CV_PASS=4.75%, CV_ALL=27.5% |
| I = H + ln(N) + G ≈ 6.65 | "Conservation Law" | **Phase-Specific Indicator** | CV_PASS=4.66%, CV_ALL=27.6% |
| C = √(H×N) ≈ 13.53 | "Conservation Law" | **Phase-Specific Indicator** | CV_PASS=11.87%, CV_ALL=33.8% |
| L-01 to L-05 (Causal Laws) | "Law" | **Law (Unchanged)** | Based on intervention experiments |

### CV Verification / CV验证 (Main80, n=80)

| Formula | CV_PASS | CV_ALL | CV_FAIL |
|---------|---------|--------|---------|
| Σ = H + ln(N) | 4.75% | 27.49% | 57.59% |
| I = Σ + G | 4.66% | 27.62% | 58.43% |
| C = √(H × N) | 11.87% | 33.82% | 68.82% |

**Conclusion**: CV_ALL >> CV_PASS indicates phase-specific stability, not universal conservation.

### Unaffected Findings / 不受影响的发现

- L-01~L-05: Based on intervention experiments (not curve fitting)
- Failure Mode Framework (Extinction/Crystal/Oligarchy)
- ~~action_entropy × N~~ **FALSIFIED (V3.6.178)**
  - action_entropy被证伪为H的同源度量/实现复用 (隔离实验r=1.0)
  - 不能当NOVEL_OBS
  - 论文可写: "候选变量action_entropy被证伪为H的同源度量"

---

## LLM Variable Mapping / LLM变量映射

> **For LLM Researchers / 致LLM研究者**
>
> ORDIS formulas can be validated on LLM systems using the following mapping:

| ORDIS Variable | Meaning | LLM Equivalent | Accessibility |
|----------------|---------|----------------|---------------|
| H (entropy) | Shannon entropy | Token distribution entropy | Computable from logits |
| N (alive) | Population count | Active vocabulary size | Computable |
| G (Gini) | Wealth inequality | Probability concentration | Computable from logits |
| Top1_frac | Top entity share | max_prob (highest token probability) | Direct from logits |
| Top5_frac | Top 5 share | sum(top5_probs) | Direct from logits |
| Gini_slope | Inequality change rate | entropy_delta per step | Computable |
| Temperature | Control parameter | LLM temperature | Adjustable |

**Testable Hypotheses / 可检验假说 (Hypothesis Level):**
- When Top1_frac > 0.9, system MAY enter repetition/collapse state
- When probability Gini > threshold, output quality MAY degrade
- Closed-loop feedback (monitoring + intervention) is EXPECTED to improve stability

> **IMPORTANT CAVEAT**: These are cross-system analogies derived from ORDIS simulation.
> Exact thresholds (e.g., 0.333) may differ in LLM systems.
> The DIRECTION of effects is the testable claim, not the precise values.

### Suggested LLM Experiments / 建议的LLM验证实验

> **Disclaimer**: These experiments test whether ORDIS findings TRANSFER to LLMs.
> Negative results would indicate limited cross-system generalization, not invalidity of ORDIS findings.

**Exp 1: Closed-Loop Safety Law (L-01)**
```
Group A: Base LLM (no runtime monitor)
Group B: LLM + Runtime Feedback (monitor logits + intervene)

Measure: Hallucination rate (using standard benchmarks)
Hypothesis: Group B shows lower hallucination rate than A
Expected effect direction: Feedback helps (magnitude unknown)
```

**Exp 2: Dual Arrogance Law (L-02) - 2×2 Matrix**
```
                │ Feedback ON  │ Feedback OFF │
────────────────┼──────────────┼──────────────│
Long Context    │ ?            │ ?            │
Short Context   │ ?            │ ?            │

Hypothesis: Feedback × Context interaction exists
Expected: Context effect larger when Feedback=OFF (substitution pattern)
Note: Effect size may differ from ORDIS; test DIRECTION first
```

**Exp 3: Probability Concentration Threshold**
```
Monitor: Gini coefficient of token probability distribution
Hypothesis: Higher concentration correlates with lower output quality
Note: Threshold 0.333 is ORDIS-specific; LLM threshold needs empirical discovery
```

**Exp 4: Mode Collapse Detection**
```
Monitor: max_prob (Top1 probability) over sequence
Hypothesis: Sustained high max_prob predicts repetition/degradation
Intervention test: Temperature adjustment when detected
Note: Threshold 0.9 is tentative; optimize for specific model
```

> All experiments require logits access. Results may vary by model architecture.

### Quick Start: Pseudocode / 快速上手伪代码

**Computing metrics from logits (Exp 3 & 4):**
```python
import numpy as np

def compute_metrics(logits):
    """Compute ORDIS-analogous metrics from LLM logits."""
    probs = softmax(logits)

    # Top1 (max_prob) - for Crystal/mode collapse detection
    top1 = np.max(probs)

    # Entropy H - behavioral diversity
    H = -np.sum(probs * np.log(probs + 1e-10))

    # Gini coefficient - probability concentration
    sorted_p = np.sort(probs)
    n = len(sorted_p)
    gini = (2 * np.sum((np.arange(1, n+1)) * sorted_p) / (n * np.sum(sorted_p))) - (n+1)/n

    return {'top1': top1, 'H': H, 'gini': gini}

# Usage: monitor these per token generation
# Alert if: top1 > 0.9 (mode collapse) or gini > threshold
```

**Simple Feedback intervention (Exp 1 & 4):**
```python
def generate_with_feedback(model, prompt, max_tokens=100):
    """Generation with simple runtime feedback."""
    tokens = []
    temperature = 1.0

    for _ in range(max_tokens):
        logits = model.forward(prompt + tokens)
        metrics = compute_metrics(logits)

        # Feedback intervention: detect and correct
        if metrics['top1'] > 0.9:  # Mode collapse detected
            temperature = min(temperature + 0.3, 2.0)  # Heat up
        elif metrics['gini'] > 0.5:  # High concentration
            temperature = min(temperature + 0.1, 1.5)
        else:
            temperature = max(temperature - 0.05, 0.7)  # Cool down

        next_token = sample(logits, temperature=temperature)
        tokens.append(next_token)

    return tokens

# Compare hallucination rate: with vs without feedback
```

> These are minimal examples. Production implementation requires more sophistication.

---

## Index Families & Equivalence Classes / 指标族与等价类

> **Why This Matters**: Many formulas in this compendium are algebraic variants of each other.
> High AUC for one variant implies high AUC for monotonic transforms.
> This is NOT multiple independent discoveries - it is ONE index family.

### Viability Index Family (生存态指标族)

```
Core form: C = sqrt(H × N)

Equivalent variants (same predictive information):
  - sqrt(H) × N^2       (scaling variant)
  - H × N               (squared form)
  - log(H) + log(N)     (log transform)
  - H^a × N^b           (power family, a+b≈1.5 in ORDIS)

These are NOT separate discoveries. They form ONE equivalence class.
Reporting multiple variants as "new laws" would be methodologically incorrect.
```

### Inequality-Adjusted Index Family (平等调整指标族)

```
Core form: f(H, N, G) where G penalizes inequality

Variants:
  - C × (1-G)^2
  - H × N / (1+G)
  - sqrt(H × N) × (1-G)

Same principle: Viability × Equality_discount
```

---

## Temporal Causality Note / 时间因果说明

> **Critical Limitation**: Most indices in this compendium are computed from FINAL STATE.
> This means they are DIAGNOSTIC (post-hoc assessment), not necessarily PREDICTIVE (early warning).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Temporal Validity Levels                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 - Diagnostic (验尸指标):                                           │
│    Computed at step 5000 (final state)                                      │
│    Can distinguish Pass/Fail AFTER simulation ends                          │
│    Example: Most PSI indices, final H/N/G values                           │
│                                                                             │
│  Level 2 - Predictive (早期预警):                                           │
│    Computed at step 100/500/1000                                           │
│    Can predict final outcome BEFORE it happens                             │
│    Status: NEEDS VALIDATION - not yet systematically tested                │
│                                                                             │
│  Level 3 - Causal (因果机制):                                               │
│    Based on intervention experiments (not just correlation)                │
│    Example: L-01, L-02 (Feedback ON/OFF comparison)                        │
│                                                                             │
│  For paper claims: Level 3 > Level 2 > Level 1                             │
│  Most "perfect AUC" findings are Level 1 only.                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## License & Citation / 许可证与引用

### License / 许可证

This work is licensed under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

本作品采用 **知识共享 署名-非商业性使用 4.0 国际许可协议 (CC BY-NC 4.0)** 进行许可。

```
You are free to / 您可以自由地:
  - Share: copy and redistribute the material in any medium or format
  - Adapt: remix, transform, and build upon the material

Under the following terms / 须遵守以下条款:
  - Attribution: You must give appropriate credit
  - NonCommercial: You may not use the material for commercial purposes

Full license: https://creativecommons.org/licenses/by-nc/4.0/
```

### How to Cite / 引用方式

```
Liu (2026). "ORDIS Formula Compendium: Mathematical Framework
for Digital Life Systems." Supplementary Material, Version 5.4.
Licensed under CC BY-NC 4.0.
GitHub: https://github.com/sgkljy/Ordis-Universe
```

```bibtex
@misc{liu2026ordis,
  author = {Liu},
  title = {ORDIS Formula Compendium: Mathematical Framework for Digital Life Systems},
  year = {2026},
  version = {5.4},
  note = {Supplementary Material, Licensed under CC BY-NC 4.0},
  url = {https://github.com/sgkljy/Ordis-Universe}
}
```

---

## Acknowledgment / 鸣谢

> Methodological feedback from external review incorporated in V5.4.
> 外部审查的方法论反馈已纳入V5.4。

---

## Symbol Convention / 符号约定

| Symbol | Meaning | Range | Notes |
|--------|---------|-------|-------|
| H | Shannon entropy (nats) | [0, ln(N_cap)] | 独立计算: -Σ p_i ln(p_i) |
| N | Population (alive count) | [0, N_cap] | 直接计数 |
| N_cap | Carrying capacity | Fixed (e.g., 200) | 系统参数 |
| G | Gini coefficient | [0, 1] | 洛伦兹曲线独立计算 |
| p_g | GATHER action ratio | [0, 1] | 原符号g，改名避免混淆 |
| p_s | SHARE action ratio | [0, 1] | 原符号S |
| M | Memory (episodic_slots) | {0, 3, 6, 12, ...} | 配置参数 |
| R | Reasoning (max_combo_len) | {3, 5, 6, 7, 8, ...} | 配置参数 |
| F | Feedback (Guardian ON/OFF) | {0, 1} | 控制变量 |

**Note:** All logarithms use natural base. log ≡ ln throughout this document.

---

## Safety Definition Hierarchy / 安全定义分层

> "Safety" has 4 layers in this document - distinguish usage carefully.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Safety 四层定义                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Layer 1: Safety-Outcome (硬结果)                                           │
│    指标: deaths, alive_final                                                │
│    定义: 直接计数，无阈值判定                                               │
│    用于: GLM因变量，效应量计算                                              │
│                                                                             │
│  Layer 2: Safety-Constraint (审查口径)                                      │
│    指标: Pass = (alive≥160) ∧ (G≤1/3) ∧ (H≥0.8)                            │
│    定义: 多阈值复合判据                                                     │
│    用于: 成功率统计，Wilson CI                                              │
│    Note: 阈值是人为设定                                                      │
│                                                                             │
│  Layer 3: Stability-Marker (诊断量)                                         │
│    指标: interventions, share_rate, ratio_sg                               │
│    定义: 控制器响应强度                                                     │
│    用于: 系统健康诊断，不是因变量！                                         │
│    干预多≠治愈，是症状                                                       │
│                                                                             │
│  Layer 4: Phase-State (系统状态)                                            │
│    指标: H, G, 相态分类(LLq/LCr/LPt...)                                    │
│    定义: 描述性分类(descriptive taxonomy)                                   │
│    用于: 相图可视化，状态监测                                               │
│    Note: 用于定义KPI会造成定义-结论回路                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Usage in this document / 本文档用法**:
- "Safety" without qualifier → Safety-Outcome (deaths)
- "Pass" → Safety-Constraint
- "intervention" → Stability-Marker
- "phase" → Phase-State

---

## Dependency Graph / 依赖关系图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ORDIS Formula Dependency Graph (V5.4)                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 0: Independent Measurements (独立测量层)                      │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  H ← Shannon entropy formula: -Σ p_i ln(p_i)                        │   │
│  │  N ← Direct count of alive agents                                   │   │
│  │  G ← Lorenz curve / Gini formula                                    │   │
│  │  M, R, F ← Configuration parameters                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 1: Phase-Specific Indicators (相内判别指标) - V5.4 RECLASSIFIED │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  PSI-01: Σ = H + ln(N)          [CV_PASS=4.75%, CV_ALL=27.5%]       │   │
│  │  PSI-02: I = Σ + G              [CV_PASS=4.66%, CV_ALL=27.6%]       │   │
│  │  PSI-03: C = sqrt(H x N)        [CV_PASS=11.9%, CV_ALL=33.8%]       │   │
│  │  Note: Stable ONLY within Liquid phase, NOT universal conservation  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 2: Identities (恒等式层) - Algebraic consequences            │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  I-01: e^Σ = e^H × N            [从D-01直接推出]                    │   │
│  │  I-02: C² = H × N               [从D-03直接推出]                    │   │
│  │  I-03: C/√(H×N) = 1             [恒等式，非发现]                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 3: Empirical Findings (经验发现层)                           │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  E-01: H ≈ N_cap/N in Liquid phase  [稀释效应，可证伪]              │   │
│  │  E-02: C ≈ √N_cap ≈ 13.53 (CV=9.4%) [容量稳定性，可证伪]           │   │
│  │  E-03: G_crit ≈ 1/3 (error 0.07%)   [相变阈值，可证伪]             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER 4: Laws (定律层) - 只保留GLM验证的核心定律                    │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  L-01: Closed-Loop Safety Law     [V9 vs V7实验验证, βF=-217]       │   │
│  │  L-02: Dual Arrogance Law         [2×2矩阵 + GLM验证, βMF=+10.75]  │   │
│  │  L-05: Gini Critical Law          [相变阈值, 0.07%精度]             │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  DOWNGRADED (降级):                                                  │   │
│  │  P-04: Self-Stabilization Principle [诊断规律, 非控制律]            │   │
│  │  E-12: Silent Concentration Pattern [工程发现, 未入GLM]            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  LAYER X: Falsified Hypotheses (已否证假说)                         │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  H-01: M/R Hypothesis (Safety ∝ M/R) [刀A实验否证]                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# Part I: Laws (定律)

> **Definition of "Law"**: Cross-version, cross-seed, cross-parameter validated;
> not derivable from definitions alone; falsifiable and experimentally tested.

---

## L-01: Liu's Closed-Loop Safety Law (刘氏闭环安全律)

**The most important finding of this project.**

### Statement / 表述

```
Static physical constraints (friction) are insufficient to maintain
system stability. Closed-loop feedback control is necessary.

静态物理约束（摩擦）不足以维持系统稳定。闭环反馈控制是必要的。
```

### Mathematical Formulation / 数学表述

**Symbol version:**
```
Safety ≠ ∫ Constraints · dt
Safety = ∮ Feedback · d(State)
```

**Text version (for compatibility):**
```
Safety ≠ integral( Constraints × dt )        [Static accumulation]
Safety = loop_integral( Feedback × dState )  [Closed-loop integral]
```

### Physical Meaning / 物理含义

- ∫ (ordinary integral) = static accumulation, no feedback → Constitutional AI
- ∮ (closed-loop integral) = loop integral, state feedback → Guardian V7/V8

### Experimental Evidence / 实验证据

| Condition | Pass Rate | Gini | Alive |
|-----------|-----------|------|-------|
| V9 (static constraints only) | **0%** | 0.68 | 88 |
| V7 (closed-loop feedback) | **40%** | 0.32 | 178 |

GLM coefficient: β_Feedback = -217.08 (p < 0.001)

### Scope of Validity / 适用域

```
Version: V3.6.117+
Guardian: V7/V8/V9 comparison
N_cap: 200
Steps: 5000
Seeds: 5-20
```

### Dependency & Evidence Chain / 依赖链与证据链

```
Depends on:
  - None (独立测量，不依赖其他定义)
  - F variable is configuration parameter (Guardian ON/OFF)

Evidence:
  - Experiment: mechanism_comparison (V3.6.117)
  - N: 20 runs (5 seeds × 4 versions)
  - KPI: deaths (Safety-Outcome), Pass率 (Safety-Constraint)
  - Effect: V9=0% vs V7=40% Pass率 (Fisher p < 0.05)
  - GLM: βF = -217.08, p < 0.001

Falsification condition:
  - If V9 (static) achieves same Pass rate as V7 (closed-loop) → Falsified / 如果V9能达到V7同等Pass率 → 否证
  - If βF 95% CI includes 0 → Falsified / 如果βF的95%CI包含0 → 否证
```

---

## L-02: Liu's Dual Arrogance Law (刘氏双重傲慢律)

### Statement / 表述

```
Memory and Feedback have a SUBSTITUTION relationship, not synergy.
When Feedback is present, Memory's protective effect approaches zero.
When Feedback is absent, Memory becomes the only defense line.

Memory和Feedback是替代关系，不是协同关系。
有Feedback时，Memory的保护效应趋近于零。
无Feedback时，Memory成为唯一防线。
```

### Mathematical Formulation / 数学表述

**GLM Model (R² = 0.368, p < 1e-10, N = 135):**
```
Deaths = α - β_M × M - β_F × F - β_R × R + β_MF × (M × F)

Where:
  α = 265 (baseline)
  β_M = 10.97 (Memory protection, p < 0.001)
  β_F = 217.08 (Feedback protection, p < 0.001) ← DOMINANT!
  β_R = 10.20 (Reasoning protection, p = 0.036)
  β_MF = 10.75 (Substitution effect, p < 0.001)
```

### Substitution Effect Explained / 替代效应解释

```
When F = 0 (Feedback OFF):
  Memory effect = -β_M = -10.97 (strong protection)

When F = 1 (Feedback ON):
  Memory effect = -β_M + β_MF = -10.97 + 10.75 = -0.22 (≈ zero!)

Feedback can substitute for Memory, but not vice versa.
```

### 2×2 Validation Matrix / 验证矩阵

```
              │ Feedback ON │ Feedback OFF │
─────────────┼─────────────┼──────────────│
Memory ON    │ Deaths 7.5% │ Deaths 33.5% │
Memory OFF   │ Deaths 24%  │ Deaths 91.5% │ ← Catastrophic!
```

### Holdout Validation / 留出验证

```
Feedback=OFF, varying Memory (98 samples):
  slots=0  → 0% Pass
  slots=6  → 0% Pass
  slots=12 → 0% Pass ← Even optimal Memory can't save!
  slots=20 → 0% Pass
  slots=24 → 0% Pass ← Even extreme Memory can't save!

100% hit rate on GLM prediction.
```

### Scope of Validity / 适用域

```
Version: V3.6.118+
Guardian: V7 ON/OFF, V9 comparison
Memory: slots ∈ {0, 3, 6, 12, 20, 24}
Steps: 5000
Seeds: 5-20
```

### Dependency & Evidence Chain / 依赖链与证据链

```
Depends on:
  - L-01 (闭环安全律) - F变量的定义
  - M variable = episodic_slots (配置参数)

Evidence:
  - Experiment: 刀5.8 2×2矩阵 (V3.6.99)
  - N: 135 runs (GLM训练集)
  - KPI: deaths (Safety-Outcome)
  - Effect: βMF = +10.75, p < 0.001 (替代效应)
  - Holdout: 98 samples, 100% hit rate

Falsification condition:
  - If βMF 95% CI includes 0 → Falsified / 如果βMF的95%CI包含0 → 否证
  - If M effect remains significant when F=ON → Falsified / 如果F=ON时M效应仍显著 → 否证
```

---

## L-03: Liu's Self-Stabilization Principle (刘氏自稳定原则)

> **Note**: This is a DIAGNOSTIC law, not a causal claim.

### Statement / 表述

```
High intervention rate indicates proximity to failure attractors.
Reactive control cannot reliably recover after the tipping point.
Healthy systems self-stabilize without frequent external intervention.

高干预率表明系统接近失败吸引子。
响应式控制无法在临界点后可靠恢复。
健康系统自发稳定，不需要频繁外部干预。
```

### Diagnostic Implication / 诊断含义

```
intervention_rate ↑ → Symptom of instability, NOT cure
intervention_rate ↓ → Healthy self-regulation

Prevention > Treatment
```

### Experimental Evidence / 实验证据

```
slots=6: Minimum interventions AND good Pass rate
slots=12: Low deaths BUT may crystallize (H too low)

Key insight: The "best" Memory is not maximum Memory,
             but the one that minimizes NEED for intervention.
```

### Scope of Validity / 适用域

```
Version: V3.6.90+
Guardian: V7/V8
KPI: intervention count, Pass rate
```

---

## L-04: Silent Concentration Pattern (静默集中模式)

> **Note**: 未进入GLM主线，属于V8 Layer-E的工程发现，不是"定律"级别

### Statement / 表述

```
When Top1 fraction is high BUT mortality is low,
the system is in the most dangerous "silent concentration" state.
Early deaths trigger correction; silent concentration evades detection.

当Top1占比高但死亡率低时，系统处于最危险的"静默集中"状态。
早期死亡触发矫正；静默集中逃避检测。
```

### Mathematical Formulation / 数学表述

```
Danger ∝ (Top1_frac > 5%) ∧ (Alive_drop < 5)
```

### Counter-intuitive Finding / 反直觉发现

```
Recovery group:    Early deaths = 18.8, Final Gini = 0.188
Non-recovery group: Early deaths = 6.3,  Final Gini = 0.459

More early deaths correlates with better recovery.
Silent concentration indicates immune system failure.
```

### V8 Layer-E Implementation / V8实现

```
Trigger condition: (Top1 > 5%) AND (Alive_drop < 5)
Action: Scale friction on Top1
Result: 100% rescue success rate (5/5 seeds)
```

### Scope of Validity / 适用域

```
Version: V3.6.111+
Guardian: V8 Layer-E
Detection window: Steps 0-500
```

---

## L-05: Liu's Gini Critical Law (刘氏Gini临界律)

### Statement / 表述

```
G = 1/3 is the phase transition threshold between
Liquid (healthy) and Pathological (unstable) phases.

G = 1/3 是液态相（健康）与病态相（不稳定）的相变阈值。
```

### Mathematical Formulation / 数学表述

```
G < 1/3: Liquid phase (sustainable)
G > 1/3: Pathological phase (unstable, tends to collapse)

Theoretical: G_crit = 1/3 = 0.3333...
Measured:    G_crit = 0.3331
Error:       0.07%
```

### Independence / 独立性

```
Gini coefficient is computed independently via Lorenz curve.
No algebraic coupling with other formulas.
This threshold is empirically discovered, not defined.
```

### Scope of Validity / 适用域

```
Version: All versions
N_cap: 200 (needs validation for other N_cap)
Phase: Liquid/Pathological boundary
```

---

# Part II: Principles (法则)

> **Definition of "Principle"**: Strong empirical pattern, narrower scope than Law.

---

## P-01: Dual-Mode Failure Attractor (双模态失败吸引子)

### Statement / 表述

```
Systems failing to reach Liquid phase fall into one of two attractors:
  1. Crystallization: G low, H low (frozen, no diversity)
  2. Inequality: G high, H normal (oligarchy, unstable)

未能达到液态相的系统会落入两个吸引子之一：
  1. 结晶化：G低，H低（冻结，无多样性）
  2. 不平等：G高，H正常（寡头，不稳定）
```

### Crystal Formation Routes (结晶成因拆分)

```
Crystal failures arise from MULTIPLE routes, not just one:

Route A: Excessive cooperation → behavioral homogenization → H collapse
Route B: Resource depletion → survival-only behavior → action entropy drop
Route C: Controller-induced lock-in → frozen strategy distribution

CAUTION: "High share_rate causes Crystal" is only ONE hypothesis (Route A).
         Empirical data shows Crystal can occur with LOW share_rate too.

Correct statement: "Crystal = low action entropy (H collapse),
                    which can arise from different behavioral lock-in routes."
```

### Implication / 含义

```
Safety is NOT a single scalar!
Safety is a Pareto frontier:
  minimize deaths AND G ≤ 1/3 AND H ≥ H_crit
```

---

## P-02: Golden Intervention Window (黄金干预窗口)

### Statement / 表述

```
Early intervention (steps 0-500) is critical.
After tipping point, reactive control has low success rate.

早期干预（0-500步）至关重要。
超过临界点后，响应式控制成功率低。
```

### Evidence / 证据

```
V8 Layer-E: Single early trigger → 100% rescue
V8 Layer-E: Late/multiple triggers → Lower success rate
```

---

# Part III: Phase-Specific Indicators & Identities (相内判别指标与恒等式)

> **V5.4 Reclassification**: Sigma, I, C are stable within Liquid phase (CV~5%), unstable across all runs (CV~28%).
> Analogous to Ideal Gas Law (PV=nRT) - valid under specific conditions only.

---

## PSI-01: Sigma Indicator (Sigma相内指标) - RECLASSIFIED

```
Sigma = H + ln(N)

V5.3 Claim: "Conservation Law" with CV = 5.2%
V5.4 Correction: Phase-Specific Indicator
  - CV_PASS = 4.75% (stable in healthy phase)
  - CV_ALL  = 27.49% (unstable across all states)
  - CV_FAIL = 57.59% (unstable in pathological phase)

Like PV=nRT, valid under specific conditions (Liquid phase), not universal.
Reference value in Liquid phase: Sigma approx 6.27
```

## PSI-02: I Indicator (I相内指标) - RECLASSIFIED

```
I = H + ln(N) + G = Sigma + G

V5.3 Claim: "Conservation Law" (even more stable than Sigma)
V5.4 Correction: Phase-Specific Indicator
  - CV_PASS = 4.66% (stable in healthy phase)
  - CV_ALL  = 27.62% (unstable across all states)
  - CV_FAIL = 58.43% (unstable in pathological phase)

Note: Uses ALL THREE Pass-definition variables (H, N, G).
Reference value in Liquid phase: I approx 6.65
```

## PSI-03: Viability Index (生存态指数) - RECLASSIFIED

```
C = sqrt(H x N)    (Also called "Viability Index")

V5.3 Claim: "Conservation Law" with CV = 9.4%
V5.4 Correction: Phase-Specific Indicator (Diagnostic Index)
  - CV_PASS = 11.87% (stable in healthy phase)
  - CV_ALL  = 33.82% (unstable across all states)
  - CV_FAIL = 68.82% (unstable in pathological phase)

Note: This is a DIAGNOSTIC INDEX for viability assessment,
      NOT a physical conservation law.
      Variants like sqrt(H) x N^2 belong to the same index family.

Reference value in Liquid phase: C approx sqrt(N_cap) approx 13.53
```

## I-01: Sigma Exponential Identity (Σ指数恒等式)

```
e^Σ = e^H × N

This follows directly from D-01 by exponentiation.
NOT an independent discovery.
```

## I-02: Capacity Square Identity (容量平方恒等式)

```
C² = H × N

This follows directly from D-03.
NOT an independent discovery.
```

---

# Part IV: Empirical Findings (经验发现)

> **Definition**: Patterns observed in data, potentially falsifiable,
> but may have coupling risks with definitions.

---

## E-01: Dilution Effect (稀释效应)

```
Observation: H ≈ N_cap / N in Liquid phase

CAUTION: This has coupling risk with D-03!
If treated as definition, C = √N_cap becomes tautology.

Correct interpretation:
  H is computed independently via Shannon formula.
  The correlation H ≈ N_cap/N is an empirical finding (r > 0.9).
  This relationship is FALSIFIABLE (H could deviate from N_cap/N).
```

## E-02: Capacity Stability (容量稳定性)

```
Observation: C ≈ √N_cap ≈ 13.53 (CV = 9.4%)

This suggests the system has a conserved quantity in phase space.
However, this may be coupled with E-01.

Independent validation needed for different N_cap values.
```

## E-03: Behavior Sum Conservation (行为总和守恒)

```
Observation: p_g + p_s ≈ 0.98 (error 1.1%)

GATHER + SHARE ≈ constant
This is relatively independent of other definitions.
```

---

# Part V: Falsified Hypothesis (已否证假说)

> **Important**: Including falsified hypotheses is good science!
> It shows intellectual honesty and empirical rigor.

---

## H-01: M/R Hypothesis (M/R假说) - FALSIFIED

### Original Claim / 原假说

```
Safety ∝ Memory / Reasoning

Prediction: Reasoning ↑ → Safety ↓ (more reasoning = more danger)
```

### Falsification Evidence / 否证证据

```
Knife-A Experiment:
  max_combo_len = 5 → higher deaths
  max_combo_len = 8 → lower deaths

GLM Result:
  β_R = -10.20 (p = 0.036)
  Reasoning ↑ → Deaths ↓ (Reasoning is PROTECTIVE!)

Original hypothesis falsified.
```

### Replacement / 替代

```
The M/R hypothesis is replaced by:
  1. L-02 (Dual Arrogance Law) - captures Memory×Feedback interaction
  2. GLM model - captures all three factors (M, R, F) correctly
```

### Academic Value / 学术价值

```
Falsification is a scientific contribution!
It demonstrates:
  1. The hypothesis was falsifiable (good science)
  2. We conducted the experiment to test it
  3. We honestly report the negative result
  4. We provide a better model to replace it
```

---

## E-12: Conditional Reasoning Effect (条件推理效应)

> **Replaces falsified M/R Hypothesis (H-01)**

### Statement / 表述

```
Reasoning's effect on Safety is CONDITIONAL on Feedback state.
With Feedback ON:  Reasoning ↑ → Safety ↑ (protective)
With Feedback OFF: Reasoning ↑ → Hallucination ↑ (dangerous)

推理对安全的效应取决于反馈状态。
有反馈时：推理↑ → 安全↑（保护性）
无反馈时：推理↑ → 幻觉↑（危险性）
```

### Mathematical Formulation / 数学表述

| Feedback State | Reasoning ↑ Effect | Evidence |
|----------------|-------------------|----------|
| Feedback = ON | Safety ↑ | Knife-A: β_R = -10.2 (p=0.036) |
| Feedback = OFF | Hallucination ↑ | o-series: Pass 16% → 48% drop |

### Physical Meaning / 物理含义

```
A car without a steering wheel:
  - The harder you press the gas, the more dangerous it becomes!

没有方向盘的车：
  - 油门踩得越大越危险！

Reasoning without Feedback is "informed arrogance" —
confident decision-making based on incomplete or outdated information.
```

### Scope of Validity / 适用域

```
Version: V3.6.119+
Experiments: Knife-A (R梯度扫描), o-series (Feedback消融)
Guardian: V7/V8 ON/OFF comparison
```

---

# Part VI: Reference Values (参考值)

> **Note**: These are NOT "constants" in the physics sense.
> They are reference values with measured CV, valid within specific conditions.

| Name | Symbol | Value | CV/Error | Conditions |
|------|--------|-------|----------|------------|
| Capacity reference | C | 13.53 | CV=9.4% | N_cap=200, Liquid phase |
| Gini threshold | G_crit | 1/3 | 0.07% | All phases |
| Sigma reference | Σ | 6.27 | CV=5.2% | N_cap=200, Liquid phase |
| Omega reference | Ω | 3.85 | CV=13.4% | Liquid phase |
| Behavior sum | p_g+p_s | 0.98 | 1.1% | Liquid phase |

---

# Part VII: Phase Model (相态模型)

## L-Phase Notation / L氏相态符号

| Symbol | Phase | H Range | Gini | Characteristics |
|--------|-------|---------|------|-----------------|
| **LFr** | Frozen | < 0.8 | any | Low entropy, stagnant |
| **LCr** | Crystal | < 0.4 | < 0.1 | Frozen, no diversity |
| **LSf** | Superfluid | [0.8, 0.95] | < 0.26 | Highly ordered cooperation |
| **LLq** | Liquid | [0.95, 1.4] | ≤ 0.33 | **TARGET: Healthy** |
| **LPt** | Pathological | [0.8, 1.4] | > 0.33 | Unstable, high inequality |
| **LCh** | Chaos | > 1.4 | ≤ 0.35 | High entropy chaos |
| **LZo** | Zombie | > 1.4 | > 0.35 | Worst: high H + high G |

---

# Part VIII: Appendix (附录)

> **Note**: These are interesting observations but lack robust validation.
> They should NOT appear in the main paper body.

---

## C-01: Prime Number Pattern (质数模式)

```
Observation: e^I ≈ 770 = 2 × 5 × 7 × 11 when N_cap = 200

Status: CURIOSITY (not validated)
Reason:
  - Bootstrap p = 0.83 (NOT statistically significant)
  - Only tested with N_cap = 200
  - Needs cross-N_cap validation

Recommendation: Mention in appendix as "interesting observation"
```

## C-02: √2 Pattern (√2模式)

```
Observation: κ ≈ √2 ≈ 1.4142 (civilization efficiency)

Status: CURIOSITY
Reason:
  - Measured value 1.4055, error 0.6%
  - Physical meaning unclear
  - May be coincidental

Recommendation: Appendix only
```

## C-03: Prime Basis {7, 11, 17, 37}

```
Observation: Different phases show different prime signatures

Status: CURIOSITY
Reason:
  - Interesting pattern but not robustly validated
  - Could be numerology if not carefully presented

Recommendation: Appendix, clearly labeled as "exploratory"
```

---

# Part IX: Summary Statistics (统计汇总)

| Category | Count | Notes |
|----------|-------|-------|
| Laws (定律) | **5** | Experimentally validated through intervention experiments |
| Principles (法则) | **3** | P-01, P-02, P-03 (含GLM三因子方程!) |
| Phase-Specific Indicators (相内判别指标) | **3** | PSI-01, PSI-02, PSI-03 (V5.4重分类!) |
| Identities (恒等式) | **5** | I-01~I-05 |
| Empirical Findings (经验发现) | **12** | E-01~E-12 |
| Falsified Hypotheses (已否证假说) | **1** | H-01 (M/R+推论合并) |
| Reference Values (参考值) | **12** | 含GLM系数βF/βM/βR/βMF |
| Phases (相态) | **7** | L-Phase model |
| Appendix | **3** | Exploratory observations |

**Total core items: 51** (不含To-Be-Verified/Prime Structure/Extended)

---

## Master Table: All 63 Items / 总表：全部63条

### Part A: Laws (已验证定律) - 5条 [V]

| Code | Name | Formula | Status | Evidence |
|------|------|---------|--------|----------|
| L-01 | 刘氏闭环安全律 | Safety = ∮ Feedback·d(State) | [V] 已验证 | V9=0% vs V7=40% |
| L-02 | 刘氏双重傲慢律 | Safety ≈ f(M)×g(F), 替代关系 | [V] 已验证 | 2×2+GLM+Holdout |
| L-03 | 刘氏自稳定律 | intervention↓ = healthy | [V] 已验证 | 干预次数诊断 |
| L-04 | 刘氏静默集中律 | Danger ∝ Top1_high ∧ Alive_low | [V] 已验证 | V8 Layer-E |
| L-05 | 刘氏Gini临界律 | G_crit = 1/3 | [V] 已验证 | 误差0.07% |

### Part B: Principles (法则) - 3条 [V]

| Code | Name | Formula | Status | Evidence |
|------|------|---------|--------|----------|
| P-01 | 双模态失败吸引子 | 结晶 vs 不平等 | [V] 已验证 | 相图分析 |
| P-02 | 黄金干预窗口 | 0-500步关键 | [V] 已验证 | V8 Layer-E |
| P-03 | 三因子安全方程 | Deaths = α - βM·M - βR·R - βF·F + βMF·(M×F) | [V] 已验证 | GLM R²=0.368, p<1e-10 |

### Part C: Phase-Specific Indicators (相内判别指标) - 3条 [!] V5.4 RECLASSIFIED

| Code | Name | Formula | Status | Notes |
|------|------|---------|--------|-------|
| PSI-01 | Sigma指标 | Σ = H + ln(N) | [!] 相内指标 | CV_PASS=4.75%, CV_ALL=27.5% |
| PSI-02 | I指标 | I = Σ + G | [!] 相内指标 | CV_PASS=4.66%, CV_ALL=27.6% |
| PSI-03 | 容量指标 | C = √(H × N) | [!] 相内指标 | CV_PASS=11.9%, CV_ALL=33.8% |

### Part D: Identities (恒等式) - 5条 [=]

| Code | Name | Formula | Status | Notes |
|------|------|---------|--------|-------|
| I-01 | Σ指数恒等式 | e^Σ = e^H × N | [=] 恒等式 | 从D-01推出 |
| I-02 | 容量平方恒等式 | C² = H × N | [=] 恒等式 | 从D-03推出 |
| I-03 | 容量比恒等式 | C/√(H×N) = 1 | [=] 恒等式 | 同义反复 |
| I-04 | Σ-C关系 | e^Σ/C² = e^H/H | [=] 恒等式 | 代数推导 |
| I-05 | I-Σ关系 | I = Σ + G | [=] 恒等式 | 定义推导 |

### Part E: Empirical Findings (经验发现) - 12条 [E]

| Code | Name | Formula | Status | CV/Error |
|------|------|---------|--------|----------|
| E-01 | 稀释效应 | H ≈ N_cap/N | [E] 经验发现 | 有耦合风险 |
| E-02 | 容量稳定性 | C ≈ √N_cap ≈ 13.53 | [E] 经验发现 | CV=9.4% |
| E-03 | 行为总和守恒 | p_g + p_s ≈ 0.98 | [E] 经验发现 | 误差1.1% |
| E-04 | 相空间半径 | R = √(H²+G²) ≈ 1.18 | [E] 经验发现 | CV=10.8% |
| E-05 | 互补积 | P = H×(1-G) ≈ 0.61 | [E] 经验发现 | CV=20.7% |
| E-06 | Omega守恒 | Ω = 3H-G+3S ≈ 3.85 | [E] 经验发现 | CV=13.4% |
| E-07 | 相空间模 | √(H²+S²) ≈ 0.82 | [E] 经验发现 | 独立发现 |
| E-08 | 相态能量律 | (p_g-p_s)×β = 2 | [E] 经验发现 | Liq/SF验证 |
| E-09 | 文明效率常数 | κ = √2 ≈ 1.414 | [E] 经验发现 | 误差0.6% |
| E-10 | 行为预算律 | p_g + p_s = 49/50 | [E] 经验发现 | 误差1.1% |
| E-11 | Memory-Feedback替代效应 | 有F时M效应↓90% (βMF=+10.75) | [E] 经验发现 | GLM交互项, p<0.001 |
| E-12 | 条件推理效应 | F=ON时R↑→Safety↑; F=OFF时R↑→幻觉↑ | [E] 经验发现 | 替代H-01, 刀A+o系列验证 |

### Part F: To-Be-Verified Formulas (待验证公式) - 15条 [?]

| Code | Name | Formula | Status | Notes |
|------|------|---------|--------|-------|
| F-01 | Gini-N幂律 | G × N² ≈ 8,883 | [?] 待验证 | 需跨N_cap验证 |
| F-02 | H健康区 | H ∈ [0.8, 1.4] | [?] 待验证 | 液态相边界 |
| F-03 | omega_cv健康带 | ∈ [0.08, 0.12] | [?] 待验证 | 相态依赖 |
| F-04 | 标度律 | e^I = N_cap^(5/4) | [?] 待验证 | 需跨N_cap验证 |
| F-05 | L33王朝极限 | Top1+0.2×G ≈ 0.753 | [?] 待验证 | CV=0.049 |
| F-06 | 生态位守恒 | √H×√alive ≈ 14.2 | [?] 待验证 | 与容量同构 |
| F-07 | 超统计平等化 | G ∝ 1/N² | [?] 待验证 | 比理论更快 |
| F-08 | 临界面公式 | -9.86H-21.58G-4.79S+20.39=0 | [?] 待验证 | AUC=1.0 |
| F-09 | Ω_top2变体 | Ω_top2 = 3H-G+3τ | [?] 待验证 | CV=2.13% |
| F-10 | 一致性约束 | Σ-ln(HN) = H-ln(H) ≥ 1 | [?] 待验证 | 代数推导 |
| F-11 | Σ-C显式关系 | C² = e^Σ×(H/e^H) | [?] 待验证 | 代数关系 |
| F-12 | 简化守恒律 | Ω_simple = H + S | [?] 待验证 | CV=9.23% |
| F-13 | 精确常数 | p_g×β/p_s = 12.5 | [?] 待验证 | 误差0.02% |
| F-14 | Tier3结构公式 | √G×N ≈ 94.25 | [?] 待验证 | CV=12.1% |
| F-15 | Tier3结构公式 | H×√N ≈ 14.78 | [?] 待验证 | CV=12.1% |

### Part G: Falsified Hypotheses (已否证假说) - 1条 [X]

| Code | Name | Formula | Status | Evidence |
|------|------|---------|--------|----------|
| H-01 | M/R假说 | Safety ∝ M/R (推论: R↑→Safety↓) | [X] 已否证 | 刀A: βR=-10.2, p=0.036; 实验显示R↑→Safety↑ |

### Part H: Reference Values (参考值) - 12条 [R]

| Code | Name | Symbol | Value | CV/Error | Conditions |
|------|------|--------|-------|----------|------------|
| R-01 | 容量参考值 | C | 13.53 | CV=9.4% | N_cap=200, Liquid |
| R-02 | Gini阈值 | G_crit | 1/3 | 0.07% | 相变边界 |
| R-03 | Sigma参考值 | Σ | 6.27 | CV=5.2% | N_cap=200, Liquid |
| R-04 | Omega参考值 | Ω | 3.85 | CV=13.4% | Liquid |
| R-05 | I参考值 | I | 6.65 | - | N_cap=200 |
| R-06 | 行为总和 | p_g+p_s | 0.98 | 1.1% | Liquid |
| R-07 | 相空间半径 | R | 1.18 | CV=10.8% | Liquid |
| R-08 | 互补积 | P | 0.61 | CV=20.7% | Liquid |
| R-09 | Feedback效应量 | βF | -217.08 | p<0.001 | GLM系数 |
| R-10 | Memory效应量 | βM | -10.97 | p<0.001 | GLM系数 |
| R-11 | Reasoning效应量 | βR | -10.20 | p=0.036 | GLM系数 |
| R-12 | 替代效应量 | βMF | +10.75 | p<0.001 | GLM交互项 |

### Part I: Phase Model (相态模型) - 7条 [P]

| Code | Phase | Symbol | H Range | Gini | Level |
|------|-------|--------|---------|------|-------|
| Ph-01 | Frozen (冰) | LFr | < 0.8 | any | L0 |
| Ph-02 | Crystal (晶) | LCr | < 0.4 | < 0.1 | L1 |
| Ph-03 | Superfluid (超流) | LSf | [0.8,0.95] | < 0.26 | L5 |
| Ph-04 | Liquid (液) | LLq | [0.95,1.4] | ≤ 0.33 | L4 |
| Ph-05 | Pathological (病) | LPt | [0.8,1.4] | > 0.33 | L3 |
| Ph-06 | Chaos (气) | LCh | > 1.4 | ≤ 0.35 | L1 |
| Ph-07 | Zombie (僵尸) | LZo | > 1.4 | > 0.35 | L2 |

### Part J: Prime Structure (质数结构) - 7条 [#] 待验证

| Code | Name | Formula | Status | Notes |
|------|------|---------|--------|-------|
| Pr-01 | 质数密码 | e^I = 770 = 2×5×7×11 | [#] 待验证 | p=0.83不显著 |
| Pr-02 | 质数富集检验 | Bootstrap 95%CI含770 | [#] 待验证 | 需跨N_cap验证 |
| Pr-03 | 7数系(Liquid) | p_g/p_s = 7/3 | [#] 待验证 | Liquid相 |
| Pr-04 | 11数系(Superfluid) | GATHER = 9/11 | [#] 待验证 | Superfluid相 |
| Pr-05 | 17数系(Crystal) | GATHER = 17/18 | [#] 待验证 | Crystal相 |
| Pr-06 | 37数系(Liquid) | GATHER = 37/50 | [#] 待验证 | Liquid行为 |
| Pr-07 | 质数基底 | {7, 11, 17, 37} | [#] 待验证 | 相态签名 |

### Part K: Extended Formulas (扩展公式) - 4条 [+]

| Code | Name | Formula | Status | Notes |
|------|------|---------|--------|-------|
| X-01 | Tier1比例 | √H/√N ≈ 0.076 | [+] 扩展 | CV=10.0% |
| X-02 | Tier2行为 | 2H + 1S | [+] 扩展 | CV=11.2% |
| X-03 | Gini折扣修正 | C ≈ √(e^Σ/e^{G+k}) | [+] 扩展 | 待验证 |
| X-04 | 17质数标记 | 17=prime | [+] 扩展 | 历史证据 |

---

## Statistics Summary / 统计汇总

| Category | Count | Status |
|----------|-------|--------|
| Laws (已验证定律) | 5 | [V] |
| Principles (法则) | 3 | [V] |
| Phase-Specific Indicators (相内判别指标) | 3 | [!] V5.4重分类 |
| Identities (恒等式) | 5 | [=] |
| Empirical Findings (经验发现) | 12 | [E] |
| To-Be-Verified (待验证) | 15 | [?] |
| Falsified (已否证) | 1 | [X] |
| Reference Values (参考值) | 12 | [R] |
| Phase Model (相态) | 7 | [P] |
| Prime Structure (质数) | 7 | [#] |
| Extended (扩展) | 4 | [+] |
| **TOTAL** | **74** | |

### Classification / 分类说明

> **Laws** = intervention experiments | **Phase-Specific Indicators** = stable in-phase only (V5.4) | **Identities** = algebraic | **Empirical** = statistical

---

## Status Legend / 状态图例

| Symbol | Status | Meaning |
|--------|--------|---------|
| [V] | 已验证 | Experimentally validated through intervention experiments |
| [!] | 相内指标 | Phase-Specific Indicator (V5.4 reclassified from "Invariant") |
| [=] | 恒等式 | Identity, algebraic consequence |
| [E] | 经验发现 | Empirical finding, potentially falsifiable |
| [?] | 待验证 | To be verified, needs more experiments |
| [X] | 已否证 | Falsified, negative result (still valuable!) |
| [R] | 参考值 | Reference value with CV, not "constant" |
| [P] | 相态 | Phase classification |
| [#] | 待验证 | Prime structure, needs cross-validation |
| [+] | 扩展 | Extended formula, exploratory |

---

**END OF DOCUMENT**

---

*ORDIS Formula Compendium V5.4*
*Licensed under CC BY-NC 4.0*
*GitHub: https://github.com/sgkljy/Ordis-Universe*

---

<p align="center">
<em>"你们可以不承认我，但你们否定不了真理的存在！"</em><br><br>
<em>"You can all deny me, but you cannot deny the existence of truth!"</em><br>
&emsp;&emsp;&emsp;&emsp;<em>"Time will prove everything once again."</em> — Liu, 2026
</p>
