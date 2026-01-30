"""
Ordis-7B V1 Interactive Chat
=============================
A 7B model fine-tuned with Liu-Ordis Theory data for structured causal reasoning.

Usage:
    python chat_ordis.py --model_path ./checkpoint-1250
    python chat_ordis.py --model_path ./checkpoint-1250 --temperature 0.5

Requirements:
    pip install transformers peft torch bitsandbytes accelerate

Commands during chat:
    /clear  - Clear conversation history
    /test   - Run quick capability test
    /quit   - Exit
"""

import argparse
import sys

def load_model(model_path):
    """Load base model + LoRA adapter"""
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import PeftModel

    print("Loading base model (Qwen2.5-7B-Instruct 4-bit)...")
    base_model = AutoModelForCausalLM.from_pretrained(
        "unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit",
        device_map="auto"
    )

    print(f"Loading LoRA adapter from {model_path}...")
    model = PeftModel.from_pretrained(base_model, model_path)

    tokenizer = AutoTokenizer.from_pretrained(
        "unsloth/qwen2.5-7b-instruct-unsloth-bnb-4bit"
    )

    return model, tokenizer


def generate_response(model, tokenizer, history, max_tokens=512, temperature=0.7):
    """Generate a response given conversation history"""
    inputs = tokenizer.apply_chat_template(history, return_tensors="pt").to("cuda")
    outputs = model.generate(
        inputs,
        max_new_tokens=max_tokens,
        temperature=temperature,
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.1
    )
    response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
    return response


def run_test(model, tokenizer, max_tokens, temperature):
    """Run a quick capability test"""
    test_questions = [
        "Why does a company become rigid after implementing perfect rules?",
        "用H=N_cap/N分析为什么微信群超过500人就变成广告群",
        "天上有多少颗星星？"
    ]

    print("\n" + "="*60)
    print("  Quick Capability Test")
    print("="*60)

    for i, q in enumerate(test_questions, 1):
        print(f"\n--- Test {i} ---")
        print(f"Q: {q}\n")
        history = [{"role": "user", "content": q}]
        response = generate_response(model, tokenizer, history, max_tokens, temperature)
        print(f"A: {response}\n")


def main():
    parser = argparse.ArgumentParser(description="Ordis-7B V1 Interactive Chat")
    parser.add_argument("--model_path", default="./checkpoint-1250",
                        help="Path to LoRA checkpoint directory")
    parser.add_argument("--max_tokens", type=int, default=512,
                        help="Maximum tokens to generate")
    parser.add_argument("--temperature", type=float, default=0.7,
                        help="Generation temperature (0.1-1.5)")
    args = parser.parse_args()

    model, tokenizer = load_model(args.model_path)

    print("\n" + "="*60)
    print("  Ordis-7B V1 Interactive Chat")
    print("="*60)
    print("  Commands:")
    print("    /clear  - Clear conversation history")
    print("    /test   - Run quick capability test")
    print("    /quit   - Exit")
    print("="*60 + "\n")

    history = []

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input in ["/quit", "/exit", "quit", "exit"]:
            print("Goodbye!")
            break

        if user_input == "/clear":
            history = []
            print("[Conversation history cleared]\n")
            continue

        if user_input == "/test":
            run_test(model, tokenizer, args.max_tokens, args.temperature)
            continue

        history.append({"role": "user", "content": user_input})
        response = generate_response(
            model, tokenizer, history,
            args.max_tokens, args.temperature
        )
        history.append({"role": "assistant", "content": response})
        print(f"\nOrdis: {response}\n")


if __name__ == "__main__":
    main()
