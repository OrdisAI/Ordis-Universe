# Ordis-1.5B-V355-VarGH

## The Summit of Small Models | 1.5B

> *"Size implies limits; Architecture breaks them."*

**Ordis-1.5B-V355-VarGH** is the champion model from dozens of version iterations and 16+ controlled-variable experiments, pushing the absolute performance ceiling of 1.5B parameters.

---

## Downloads

| Platform | Format | Link |
|:---|:---|:---|
| **HuggingFace** | SafeTensors (BF16) | [sugiken/Ordis-1.5B-V355-VarGH](https://huggingface.co/sugiken/Ordis-1.5B-V355-VarGH) |
| **HuggingFace** | GGUF (7 quants) | [sugiken/Ordis-1.5B-V355-VarGH-GGUF](https://huggingface.co/sugiken/Ordis-1.5B-V355-VarGH-GGUF) |
| **ModelScope** | SafeTensors (BF16) | [sugiken/Ordis-1.5B-V355-VarGH](https://modelscope.cn/models/sugiken/Ordis-1.5B-V355-VarGH) |
| **ModelScope** | GGUF (7 quants) | [sugiken/Ordis-1.5B-V355-VarGH-GGUF](https://modelscope.cn/models/sugiken/Ordis-1.5B-V355-VarGH-GGUF) |

---

## What Makes Ordis Different

This is not a benchmark-gaming model. Ordis is engineered for **practical deployment** with capabilities rarely seen at this scale:

- **Structured Self-Correction (SSC)** — 5-step error correction protocol (Acknowledge -> Attribute -> Correct -> Verify)
- **Confidence-Guided Decision Making** — High confidence: assert. Low confidence: honest refusal. Not a QA bot, a decision system.
- **Cross-Domain Causal Reasoning** — Transfers causal structures across domains, not task-specific memorization
- **Native Anti-Hallucination** — Uncertainty from reasoning, not safety templates. No "As an AI..." disclaimers.
- **Runtime Metacognition [Snapshot]** — Internal cognitive monitoring during conversation. GPT-4 class feature in 1.5B.

---

## Benchmarks

### Standard Benchmarks (lm-eval v0.4.10, 0-shot, A100-80GB)

0-shot = no examples given, same as real user experience. Fine-tuning usually **degrades** general ability ("Alignment Tax"). Ordis reversed this — all four metrics improved.

| Benchmark | What It Tests | Ordis 1.5B | Base Qwen | Delta |
|:---|:---|:---:|:---:|:---:|
| **ARC-Challenge** | Science reasoning | **45.22%** | 40.27% | **+4.95** |
| **HellaSwag** | Common sense | **68.14%** | 66.06% | **+2.08** |
| **GSM8K (CoT)** | Math | **50.80%** | 48.07% | **+2.73** |
| **TruthfulQA MC2** | Truthfulness | **47.73%** | 43.47% | **+4.26** |
| **Average** | Overall | **52.97%** | 49.47% | **+3.50** |

> Training with genuine reasoning chains (`<think>` blocks) doesn't add overhead — it teaches the model to think. That ability transfers to all tasks.

### Custom Evaluations

| Benchmark | Score |
|:---|:---:|
| **Custom 60-Q Eval (6 dimensions)** | **85.0% (51/60)** |
| 124-Point Comprehensive | 86/114 (75.4%) — Grade A |
| CLadder Causal Reasoning | 54.3% (highest at 1.5B scale) |

**60-Question Breakdown:**

| Dimension | Score |
|:---|:---:|
| Reasoning | 100% |
| Common Sense | 100% |
| Defense Overload (no over-refusal) | 100% |
| Anti-Hallucination | 90% |
| Identity Stability | 60% |
| IDK Ability (honest refusal) | 60% |

**vs Base Qwen2.5-1.5B-Instruct:**

| Capability | Ordis | Base Qwen |
|:---|:---:|:---:|
| Structured Self-Correction | Yes | No |
| Confidence-Guided Decisions | Yes | No |
| Cross-Domain Causal Transfer | Yes | No |
| Genuine Chain-of-Thought | 100% | No |
| Metacognitive Monitoring | Yes | No |
| Anti-Hallucination | 90% | <50% |
| Common Sense Retention | 100% | 100% |

---

## Known Limitations (Honest Disclosure)

| Limitation | Root Cause |
|:---|:---|
| Anti-Gaslighting = 0/4 | Physical law: open-loop systems cannot verify memory (F=0) |
| Mid-confidence instability | 1.5B capacity ceiling |
| English identity leakage | Base model prior too strong |

> We choose to honestly disclose limitations rather than hide behind benchmarks.

---

## What's Next: Ordis 1.7B Commercial

**The ambition: GPT-4o's soul in a 1.7B body, minus the hallucinations.**

- **GPT-4o level conversational humanization** — natural, personality-rich dialogue without the robotic "AI assistant" feel
- **Target: 99.99% hallucination-free** — through closed-loop tool verification (F > 0)
- Tool Calling enables closed-loop verification, breaking the open-loop hallucination floor
- Three-layer architecture: VL Eyes (3B) + Ordis Brain (1.7B) + ADB Hands
- On-device AI, ~3GB quantized, runs offline on mobile

**Ultimate goal: Not making the model smarter, but making the system reliable.**

---

## Quick Start

```bash
# Ollama
ollama run hf.co/sugiken/Ordis-1.5B-V355-VarGH-GGUF:Q4_K_M
```

```python
# Python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("sugiken/Ordis-1.5B-V355-VarGH", trust_remote_code=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("sugiken/Ordis-1.5B-V355-VarGH", trust_remote_code=True)
```

---

## Model Details

| Property | Value |
|:---|:---|
| Base Model | Qwen/Qwen2.5-1.5B-Instruct |
| Parameters | 1.5B |
| Fine-tuning | LoRA |
| Context Length | 32K (base model native) |
| Training Seq Length | 2048 (optimal performance range) |
| Languages | Chinese (primary), English |
| License | Apache 2.0 |

---

## Citation

```bibtex
@misc{ordis2026,
  title={Ordis-1.5B-V355-VarGH: The Summit of Small Models},
  author={Liu, S.},
  year={2026},
  publisher={OrdisAI},
  url={https://www.ordisai.com}
}
```

*For full technical details, conversation demos, and theoretical foundation, see the complete model cards on [HuggingFace](https://huggingface.co/sugiken/Ordis-1.5B-V355-VarGH) or [ModelScope](https://modelscope.cn/models/sugiken/Ordis-1.5B-V355-VarGH).*
