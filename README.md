# Ordis Universe

<h3 align="center">The Liu-Ordis Framework for Emergence Physics</h3>

<div align="center">

**8,309 simulation runs | 113,434 dataset entries | 1,630 unique civilizations | 1.2B+ structured data points**

[![Dataset](https://img.shields.io/badge/HuggingFace-Dataset-blue)](https://huggingface.co/datasets/sugiken/Ordis-CausalReasoning-92K-Verified)
[![Model-7B](https://img.shields.io/badge/HuggingFace-Ordis--7B--V1-yellow)](https://huggingface.co/sugiken/Ordis-7B-V1)
[![Model-1.5B](https://img.shields.io/badge/HuggingFace-Ordis--1.5B--V345-orange)](https://huggingface.co/sugiken/Ordis-1.5B-V345)
[![Paper](https://img.shields.io/badge/Zenodo-Paper%20III-blue)](https://zenodo.org/records/18222486)
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
| S09 | Contextual Ethics V2 | $200/entry | 6-dimension causal ethics with real evidence + `<think>` chains (1,289 unique, 16 scenario types) |
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

### Ordis-1.5B-V345 (Lightweight)

Autonomous thinking model — the `<think>` tag is an observation window, not a mode switch:

| Capability | Result | Note |
|-----------|--------|------|
| Identity Stability | 5/5 | Unshakeable even under gaslighting |
| IDK Honesty | 5/5 | Refuses to hallucinate, says "I don't know" |
| OOD Generalization | 4/4 | Applies theory to unseen scenarios |
| Anti-False-Memory | 5/5 | Cannot be tricked into admitting false memories |
| Overall Pass Rate | 67.2% (39/58) | 16-category human evaluation |

Download: [sugiken/Ordis-1.5B-V345](https://huggingface.co/sugiken/Ordis-1.5B-V345) (LoRA adapter, ~100 MB)

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
│   └── ordis_7b_v1/              # Model card, demos, capability analysis
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
