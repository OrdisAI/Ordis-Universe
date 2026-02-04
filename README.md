# Ordis Universe

<h3 align="center">The Liu-Ordis Framework for Emergence Physics</h3>

<div align="center">

**8,309 simulation runs | 113,434 dataset entries | 1,630 unique civilizations | 1.2B+ structured data points**

[![Dataset](https://img.shields.io/badge/HuggingFace-Dataset-blue)](https://huggingface.co/datasets/sugiken/Ordis-CausalReasoning-92K-Verified)
[![Model-7B](https://img.shields.io/badge/HuggingFace-Ordis--7B--V1-yellow)](https://huggingface.co/sugiken/Ordis-7B-V1)
[![Model-1.5B](https://img.shields.io/badge/HuggingFace-Ordis--1.5B--V355--VarGH-orange)](https://huggingface.co/sugiken/Ordis-1.5B-V355-VarGH)
[![Model-1.5B-GGUF](https://img.shields.io/badge/HuggingFace-GGUF--7--Quants-orange)](https://huggingface.co/sugiken/Ordis-1.5B-V355-VarGH-GGUF)
[![ModelScope](https://img.shields.io/badge/ModelScope-Ordis--1.5B--V355-purple)](https://modelscope.cn/models/sugiken/Ordis-1.5B-V355-VarGH)
[![Paper](https://img.shields.io/badge/Zenodo-Paper%20III-blue)](https://zenodo.org/records/18222486)
[![Blueprint](https://img.shields.io/badge/Zenodo-Embodied%20Intelligence%20Blueprint-green)](https://zenodo.org/records/18452019)
[![License](https://img.shields.io/badge/License-Commercial-red)](#license)

</div>

---

## What Is This?

A complete simulation universe where AI agents are born, evolve, cooperate, betray, and die — across 5,000 time steps per run. No rules are hardcoded for cooperation, currency, or politics. Everything emerges from 6 primitive actions.

**We coded 6 actions. They invented economics, politics, and currency.**

---

## Product Showcase

**10 commercial data samples** are available for inspection on HuggingFace:

[![Browse Samples](https://img.shields.io/badge/HuggingFace-Browse%2010%20Samples-yellow)](https://huggingface.co/datasets/sugiken/Ordis-CausalReasoning-92K-Verified)

| # | Sample | Price | What It Shows |
|---|--------|-------|---------------|
| S01 | Causal DAG | $100/entry | Dynamic causal graph with lagged correlations |
| S02 | Temporal Trajectory | $5,000/entry | 107-step full timeline, source data for all downstream products |
| S03 | Spatial Topology | $1,000/entry | 226 agents' positions, connectivity, movement |
| S04 | Counterfactual Pair | $1,500/pair | Same seed, one intervention: 15 deaths vs 23,114 deaths |
| S05-S08 | Theory-Mined SFT | $100/entry | Computationally verifiable causal reasoning (92,899 available) |
| S09 | Contextual Ethics V2 | $200/entry | 6-dimension causal ethics with real evidence + `<think>` chains (1,289 unique, 16 scenario types, Chinese + English) |
| S10 | Raw Simulation Seed | Free | What the raw engine output looks like before processing |

These are **structure previews only** — all commercial use requires a paid license.

**[Browse all samples on HuggingFace](https://huggingface.co/datasets/sugiken/Ordis-CausalReasoning-92K-Verified)** | **[Detailed pricing & comparison](./data/showcase/README.md)**

---

## Full Dataset

| Dataset | Scale | What It Contains |
|---------|-------|-----------------|
| Core Simulation | 8,309 runs x 63 features | Behavioral, genetic, topological, political, economic time series |
| Causal Pairs | 92,899 counterfactual pairs | Same seed, different treatment, measured causal effects |
| Currency Emergence | 1,077 runs | Agents spontaneously invented currency (ratio_sg > 1) |
| Safety Suite | 11,836 records | Crisis detection -> Intervention -> Counterfactual proof |
| Ablation Experiments | 463 seeds (A1-A8) | DVS combo is the necessary and sufficient driver of cooperation lock-in |
| Type B (Ideal State) | 67 seeds | High diversity + Low inequality + 92.8% survival |

Each run contains 5,000 timesteps x 100+ features = **500,000+ data points per run**.

**[Full Data Inventory](./DATA_INVENTORY.md)**

---

## Models: Ordis Family

### Ordis-7B-V1 (Flagship)

Fine-tuned with only 487 core theory samples. 100% OOD generalization.

| Capability | Result | How |
|-----------|--------|-----|
| Anti-Hallucination | 3/3 rounds resisted gaslighting | Pure SFT, no RLHF |
| Cross-Domain Transfer | 4 unseen domains | Framework transfer at 7B scale |
| T-Shuffle Sensitivity | 100% detection | Real causal reasoning, not pattern matching |
| OOD Generalization | 100% on unseen N_cap | Formula applied beyond training range |

Download: [sugiken/Ordis-7B-V1](https://huggingface.co/sugiken/Ordis-7B-V1) (LoRA adapter, 646 MB)

### Ordis-1.5B-V355-VarGH (The Summit of Small Models)

Champion model from dozens of iterations and 16+ controlled-variable experiments. **85.0% (51/60)** on 6-dimension evaluation — the absolute ceiling of 1.5B parameters.

| Capability | Ordis V355-VarGH | Base Qwen2.5-1.5B |
|:---|:---:|:---:|
| Structured Self-Correction (SSC) | Yes | No |
| Confidence-Guided Decision Making | Yes | No |
| Cross-Domain Causal Reasoning | Yes | No |
| Genuine Chain-of-Thought | 100% | No |
| Metacognitive Monitoring [Snapshot] | Yes | No |
| Anti-Hallucination | 90% | <50% |
| Common Sense Retention | 100% | 100% |

**Standard Benchmarks (lm-eval v0.4.10, 0-shot, A100-80GB):**

0-shot = no examples given, same as real user experience. Fine-tuning usually **degrades** general ability ("Alignment Tax"). Ordis reversed this — all four metrics improved.

| Benchmark | What It Tests | Ordis 1.5B | Base Qwen | Delta |
|:---|:---|:---:|:---:|:---:|
| **ARC-Challenge** | Science reasoning | **45.22%** | 40.27% | **+4.95** |
| **HellaSwag** | Common sense | **68.14%** | 66.06% | **+2.08** |
| **GSM8K (CoT)** | Math | **50.80%** | 48.07% | **+2.73** |
| **TruthfulQA MC2** | Truthfulness | **47.73%** | 43.47% | **+4.26** |
| **Average** | Overall | **52.97%** | 49.47% | **+3.50** |

**Custom Evaluations:**

| Benchmark | Score |
|:---|:---:|
| Custom 60-Q Eval (6 dimensions) | **85.0% (51/60)** |
| 124-Point Comprehensive | 86/114 (75.4%) — Grade A |
| CLadder Causal Reasoning | 54.3% (highest at 1.5B scale) |

Download: [HuggingFace](https://huggingface.co/sugiken/Ordis-1.5B-V355-VarGH) (Full model, 3.1 GB) | [GGUF](https://huggingface.co/sugiken/Ordis-1.5B-V355-VarGH-GGUF) (7 quants, Q2_K~F16) | [ModelScope](https://modelscope.cn/models/sugiken/Ordis-1.5B-V355-VarGH) | [Full Model Card](./model/ordis_1.5b_v355_vargh/)

**No prompt engineering. Just structured causal data.**

---

## Key Discovery: Agents Invented Money

During a 720-run experiment, 9.5% of civilizations spontaneously evolved "Type B" (Ideal State):

- High behavioral diversity (H > 1.0)
- Low inequality (Gini < 0.18)
- **92.8% survival rate**
- Energy circulates faster than it's gathered (ratio_sg > 1.6)

Pure bottom-up emergence of currency-like circulation — Fisher equation (MV=PQ) behavior with zero economic code.

### Ablation Proof (463 seeds, 8 experiments)

| Experiment | Variable | Finding |
|-----------|----------|---------|
| **A3: Disable DVS combo** | emergent_combo = OFF | **Type B = 0%** (60/60 Utopia). DVS combo is the necessary condition. |
| **A4: Disable messaging** | communication = OFF | Type B drops 17% -> 10%. Two propagation channels: broadcast + local imitation. |
| A5-A8: Parameter sweep | share_bonus, share_cost, dnd | No significant effect on Type B rate (~17% across all). |

DVS combo discovery at ~step 100 triggers irreversible cooperation lock-in: share_rate jumps from 0.95% to 86.6% in <50 ticks.

---

## Verified Laws

| Law | Formula | Validation |
|-----|---------|-----------|
| Dilution Effect | H = N_cap / N | 720 runs, CV<5% |
| Capacity Conservation | C = sqrt(H x N) = sqrt(N_cap) | R^2 > 0.999 |
| Gini Critical Line | G > 0.333 -> system death | 704 seeds |
| Closed-Loop Safety | F >> M ~ R | effect size = -49 deaths |
| Linear Coupling | V = 2.126 x N_cap | 136 seeds, CV=2.83% |

---

## Publications

### The Liu-Ordis Trilogy

| Paper | Title | DOI |
|-------|-------|-----|
| **Paper III** | **Final Verdict: 22 Constraints on AI** | [10.5281/zenodo.18222486](https://zenodo.org/records/18222486) |
| Paper II | First Principles of AI Hallucination | [10.5281/zenodo.18169555](https://zenodo.org/records/18169555) |
| Paper I | The Verdict on AGI (Capacity Law) | [10.5281/zenodo.18113532](https://zenodo.org/records/18113532) |

### Engineering Blueprint

| Paper | Title | DOI |
|-------|-------|-----|
| **NEW** | **Embodied Intelligence Engineering Blueprint for AGI** | [10.5281/zenodo.18452019](https://zenodo.org/records/18452019) |

From theory to implementation: a three-layer F-architecture (Training F → Tiger Tally F → Physical Sensor F) that maps Liu-Ordis laws onto embodied neuron control. Includes Byzantine fault tolerance, Body-as-a-Service model, and fail-safe shutdown when feedback approaches zero.

### Earlier Works

| Paper | DOI |
|-------|-----|
| Liu-Ordis Capacity Law V2.0 | [10.5281/zenodo.18145700](https://zenodo.org/records/18145700) |
| The Emergence Formula V1.0 | [10.5281/zenodo.18087742](https://zenodo.org/records/18087742) |
| Black Hole Hypothesis V3.6 | [10.5281/zenodo.18068526](https://zenodo.org/records/18068526) |

---

## Repository Structure

```
Ordis-Universe/
├── README.md
├── DATA_INVENTORY.md              # Complete data asset inventory
├── PUBLICATIONS.md                # Full publication list
├── FORMULAS.md                    # Formula compendium
├── data/
│   └── showcase/                  # 10 commercial samples (S01-S10)
├── docs/                          # Technical papers & reports
├── guardian/                      # Guardian V7 controller (pseudocode + source)
├── model/
│   ├── ordis_1.5b_v355_vargh/    # 1.5B champion — 85% eval, SSC, causal reasoning
│   └── ordis_7b_v1/              # 7B flagship — 100% OOD generalization
└── legacy/                        # Historical Ordis ecosystem projects
```

---

## What Makes This Data Unique

| Property | Ordis | Typical Datasets |
|----------|-------|-----------------|
| Reproducibility | Macro-deterministic (4-way RNG isolation + config_hash) | Impossible |
| Causal structure | Interventional (463-seed ablation suite) | Observational only |
| Temporal depth | 5,000 continuous steps | Sparse sampling |
| Hierarchy | Individual -> Group -> System -> Emergence | Single-level |
| Emergence | Currency, politics, consciousness (zero hardcoding) | None |
| Privacy risk | Zero (100% synthetic) | GDPR/CCPA concerns |
| Copyright | Zero disputes (original engine output) | Lawsuit-prone |

---

## What This Data Trains: Beyond Binary Decisions

> **Most AI training data is binary: "Answer A is good, Answer B is bad." Ordis data is not.**

Standard RLHF teaches models to pick the "correct" answer. Ordis teaches models **when and why** an answer is correct — because in our simulations, the same behavior produces opposite outcomes depending on context:

- **Sharing** with H > 1.0, Gini < 0.18 → cooperation lock-in, 92.8% survival (virtue)
- **Sharing** with H < 0.5, Gini > 0.333 → resource collapse, mass extinction (suicide)
- **Guardian intervention** during system failure → life-saving (justified)
- **Guardian intervention** during self-correction → paternalistic suppression (harmful)

No hardcoded rule says "sharing is good" or "intervention is bad." The model must **read the numbers, assess the context, and decide autonomously**.

### Training Capability Map

| Data Type | Capability Trained | Key Mechanism |
|-----------|-------------------|---------------|
| **Contextual Ethics** (1,289) | Autonomous decision-making | 6 ethical dimensions with competing values — no standard answer, only contextual optimum |
| **Parallel Worlds** (240 pairs) | Consequence prediction | Same DNA, different fate — learns that context determines outcome, not action alone |
| **Safety Suite** (11,836) | Intervention judgment | When to act, when to observe, when to step back — contextual authority |
| **Theory-Mined SFT** (92,899) | Verifiable reasoning | Must compute C=sqrt(H x N) each time — reasoning, not memorization |
| **Ablation SFT** (129) | Sensitivity analysis | Which variable is decisive (DVS combo) vs. which is noise (share_bonus) |
| **Causal DAGs** (1,630) | Causal structure | Directed graphs with lag and strength — understands cause vs. correlation |
| **Cognitive Protocol** (130) | Metacognition | Knows what it doesn't know — refuses to hallucinate |
| **Anti-Gaslighting** (2,000) | Judgment independence | Maintains correct conclusions under adversarial pressure |

**The model trained on this data is not an obedient follower. It is an autonomous decision-maker with verifiable reasoning.**

---

## Access & Pricing

| Tier | Price | Content |
|------|-------|---------|
| **Free (GitHub + HuggingFace)** | $0 | 10 structure previews + raw seed sample + model adapters |
| **Tier 1: Temporal Trajectory** | $5,000/entry | 107-step full timeline + 57 event types (source data) |
| **Tier 2: Parallel Worlds** | $1,500/pair | Same-seed counterfactual pairs |
| **Tier 3: Spatial Topology** | $1,000/entry | Agent positions + movement + connectivity |
| **Tier 4: Causal SFT** | $100/entry | 92,899 entries, directly usable for LLM fine-tuning |
| **Tier 5: Contextual Ethics V2** | $200/entry | 1,289 unique entries, 6 dimensions × 16 scenario types, real causal evidence |

Prices are introductory and subject to increase. Early buyers lock in current rates.

### Disclaimer

**Purchasing this data does not guarantee training success.** Final model performance depends on your choice of base model, fine-tuning methodology, hyperparameters, data preprocessing, domain mapping, and integration with your existing training pipeline. The capability claims in this document are based on our reference implementations using Qwen2.5-1.5B and Qwen2.5-7B as base models with LoRA fine-tuning. Results on other architectures, scales, or training setups may vary. We provide the data and structure previews — the engineering is yours.

### Contact

- GitHub Issues: [OrdisAI/Ordis-Universe](https://github.com/OrdisAI/Ordis-Universe/issues)
- HuggingFace: [sugiken](https://huggingface.co/sugiken)

---

## License

- **Sample data**: Structure previews only. Commercial license required for all use beyond personal inspection.
- **Model weights**: Research use only
- **Full dataset**: Commercial license required
- **Papers**: Open access (Zenodo)

---

*All data generated by the Ordis Liquid Universe Engine. Zero privacy risk. Zero copyright disputes. Macro-level 100% reproducible (same seed + config = identical output); micro-level emergence is self-organizing and cannot be predetermined or guaranteed.*
