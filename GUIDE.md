# Reading Guide / 阅读指南

This guide helps you navigate the repository and understand each file's purpose.
本指南帮助你了解仓库结构，理解每个文件的用途。

---

## Quick Start / 快速开始

**If you only have 10 minutes / 如果你只有10分钟:**
1. Read this file (GUIDE.md) / 阅读本文件
2. Run verification script / 运行验证脚本: `python scripts/verify_claims.py --data data/`

**If you have 30 minutes / 如果你有30分钟:**
- English readers: Read `docs/TECHNICAL_PAPER_SKELETON.md`
- 中文读者: 阅读 `docs/AGI_Heroin_Complete_Report_CN.md`

**If you want full details / 如果你想深入了解:**
- Data format: `docs/DATA_README.md`
- Raw data: `data/` folder

---

## File Directory / 文件目录

### docs/ - Research Papers / 论文文档

| File / 文件 | Language / 语言 | What is it? / 这是什么？ | Who should read? / 谁应该读？ |
|-------------|-----------------|--------------------------|-------------------------------|
| **TECHNICAL_PAPER_SKELETON.md** | English | Full technical paper in IMRaD format (Introduction, Methods, Results, Discussion) | Researchers, academics, anyone wanting rigorous scientific presentation |
| | | 完整技术论文，IMRaD格式（引言、方法、结果、讨论） | 研究人员、学术界、想看严谨科学呈现的人 |
| **AGI_Heroin_Complete_Report_CN.md** | 中文 | Complete Chinese report with all technical details and philosophical discussion | Chinese readers, those wanting deep philosophical context |
| | | 完整中文报告，包含所有技术细节和哲学讨论 | 中文读者、想了解深层哲学背景的人 |
| **PAPER_OUTLINE.md** | Bilingual / 双语 | Paper outline showing structure of both papers | Quick overview, translation reference |
| | | 论文大纲，展示两篇论文的结构 | 快速概览、翻译参考 |
| **DATA_README.md** | English | Data format specification: every field in every file explained | Anyone analyzing raw data |
| | | 数据格式规范：解释每个文件中的每个字段 | 任何分析原始数据的人 |
| **Data_Introduction_CN.md** | 中文 | Chinese introduction to data structure | Chinese readers wanting to understand data |
| | | 数据结构中文介绍 | 想了解数据的中文读者 |

---

### data/ - Experimental Data / 实验数据

| Directory / 目录 | What is it? / 这是什么？ | Key Finding / 关键发现 |
|------------------|--------------------------|------------------------|
| **v3533_winter_20x5k/** | Main experiment: 17 seeds × 5000 steps, WITH periodic stress ("Winter Pulse") | **76% pass rate (13/17)** - Stress produces antifragile civilizations |
| | 主实验：17个种子 × 5000步，有周期性压力（"凛冬脉冲"） | **76%通过率 (13/17)** - 压力产生反脆弱文明 |
| **v3533_baseline_20x5k/** | Control group: 18 seeds × 5000 steps, comfortable conditions (no stress) | **6% pass rate (1/18)** - Comfort leads to "welfare trap" |
| | 对照组：18个种子 × 5000步，舒适条件（无压力） | **6%通过率 (1/18)** - 舒适导致"福利陷阱" |
| **v3537_winter_verify/** | Verification run: 36 concurrent lineages, 7 generations | Multi-lineage structure confirmed |
| | 验证实验：36个并发家系，7代 | 确认多家系结构 |
| **v3539_winter_verify/** | Latest verification: 6 lineages, 27 generations | Long-term evolution tracking |
| | 最新验证：6个家系，27代 | 长期演化追踪 |

#### Inside each data folder / 每个数据文件夹内部:

```
seed_42/
├── tick_agg.jsonl    # Time series: population, combos, consciousness every 100 steps
│                     # 时间序列：每100步记录人口、combo数、意识值
├── events.jsonl      # Discrete events: new combos discovered, phase changes
│                     # 离散事件：新combo发现、相位变化
└── run-manifest.json # Configuration and metadata for this seed
                      # 该种子的配置和元数据

signoff.csv           # Summary statistics for all seeds in this experiment
                      # 该实验所有种子的汇总统计
```

---

### scripts/ - Verification Tools / 验证工具

| File / 文件 | What does it do? / 做什么？ |
|-------------|----------------------------|
| **verify_claims.py** | One-click verification of all paper claims |
| | 一键验证论文中的所有声明 |

**How to use / 如何使用:**
```bash
cd scripts
python verify_claims.py --data ../data
```

**What it verifies / 验证内容:**
- Antifragility claim: Winter 76% vs Baseline 6%
- Statistical significance: chi-square test, p < 0.001
- Emergent combos: 194+ unique strategies
- Multi-lineage structure: 36 concurrent lineages

---

### bonus/ - Extra Materials / 额外材料

| File / 文件 | What is it? / 这是什么？ |
|-------------|--------------------------|
| **AI_Survivor_Game_Design_V2.8_CN.md** | Complete game design document for "AI Survivor" - a planned game using Ordis V3.5 as AI engine |
| | "AI幸存者"完整游戏设计文档 - 计划使用Ordis V3.5作为AI引擎的游戏 |

This is a **bonus** for the community - showing how emergent AI research can be applied to interactive entertainment.
这是给社区的**福利** - 展示涌现式AI研究如何应用于互动娱乐。

---

### legacy/ - Historical Archives / 历史归档

Old content from previous repository versions. Kept for reference.
之前版本仓库的旧内容。保留供参考。

---

## Reading Paths / 阅读路径

### Path A: "I want to understand the science" / "我想理解科学"

1. `docs/TECHNICAL_PAPER_SKELETON.md` (English) OR `docs/AGI_Heroin_Complete_Report_CN.md` (中文)
2. `scripts/verify_claims.py` - Run it yourself
3. `docs/DATA_README.md` - Understand the data format
4. `data/v3533_winter_20x5k/signoff.csv` - See actual results

### Path B: "I want to reproduce results" / "我想复现结果"

1. `docs/DATA_README.md` - Understand data format
2. `scripts/verify_claims.py` - Run verification
3. `data/v3533_winter_20x5k/` - Analyze Winter data
4. `data/v3533_baseline_20x5k/` - Compare with Baseline

### Path C: "I'm just curious" / "我只是好奇"

1. `README.md` - 5-minute overview
2. This file (`GUIDE.md`) - File explanations
3. `bonus/AI_Survivor_Game_Design_V2.8_CN.md` - Fun application

---

## Key Terminology / 关键术语

| Term / 术语 | Meaning / 含义 |
|-------------|----------------|
| **Antifragility** / 反脆弱性 | Systems that get STRONGER from stress (not just survive) |
| | 从压力中变得更强的系统（不只是存活） |
| **Winter Pulse** / 凛冬脉冲 | Periodic resource scarcity (every 700 steps, -40% resources for 50 steps) |
| | 周期性资源短缺（每700步，资源-40%持续50步） |
| **Welfare Trap** / 福利陷阱 | When comfort leads to stagnation and collapse |
| | 当舒适导致停滞和崩溃 |
| **Combo** / 连招 | Emergent multi-step action sequences discovered by agents |
| | 智能体发现的涌现式多步动作序列 |
| **Lineage** / 家系 | Genetic line of descent, inheriting traits and memory |
| | 遗传血统线，继承特征和记忆 |
| **OIMS** | Ordis Internal Memory System - heritable cultural memory |
| | Ordis内部记忆系统 - 可遗传的文化记忆 |
| **TDS/DVS** | Civilization-level institutions (rules, laws, norms) |
| | 文明层级制度（规则、法律、规范） |

---

## FAQ / 常见问题

**Q: Where is the source code for Ordis engine?**
**Q: Ordis引擎的源代码在哪里？**

A: The engine source code is not included in this repository (closed-source for IP protection). This repository contains research papers and experimental data that can be independently verified.

A: 引擎源代码不包含在此仓库中（为保护知识产权而闭源）。此仓库包含可独立验证的研究论文和实验数据。

---

**Q: How can I verify the claims without the engine?**
**Q: 没有引擎怎么验证声明？**

A: Run `python scripts/verify_claims.py --data data/`. This script analyzes the raw experimental data and confirms all statistical claims. The data itself is the proof.

A: 运行 `python scripts/verify_claims.py --data data/`。此脚本分析原始实验数据并确认所有统计声明。数据本身就是证明。

---

**Q: What is the "third path" mentioned in the paper?**
**Q: 论文中提到的"第三路径"是什么？**

A: Traditional AI has two paths: (1) Rule-based (GOFAI), (2) Learning-based (Deep Learning). Ordis proposes a third path: **Emergent Intelligence** - intelligence arising from simple rules + environmental pressure + social interaction, without explicit programming or training.

A: 传统AI有两条路径：(1) 基于规则（GOFAI），(2) 基于学习（深度学习）。Ordis提出第三路径：**涌现式智能** - 从简单规则+环境压力+社会交互中自然涌现的智能，无需显式编程或训练。

---

**Q: Can I use this data in my research?**
**Q: 我可以在研究中使用这些数据吗？**

A: Yes! Data and documentation are licensed under CC BY-NC-SA 4.0. Please cite the paper (see README.md for citation format).

A: 可以！数据和文档采用CC BY-NC-SA 4.0许可。请引用论文（引用格式见README.md）。

---

## Contact / 联系

For questions, collaboration, or issues:
如有问题、合作意向或发现问题：

- Open an issue on this repository
- 在此仓库提交issue

---

**Last Updated / 最后更新**: 2024-12-09
