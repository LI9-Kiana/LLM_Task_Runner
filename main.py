from tasks.classify import ClassifyTask
from runner.executor import call_llm
from runner.schema import parse_and_validate

if __name__ == "__main__":
    task = ClassifyTask(labels=["billing", "bug", "feature_request", "other"])
    inp = task.input_model.model_validate({"text": "I was charged twice"})
    prompt = task.build_prompt(inp)

    raw_text, latency_ms = call_llm(prompt, model="gpt-4o-mini")
    print("Raw model output:", raw_text)

    validated = parse_and_validate(raw_text, task.output_model)
    print("Validated output:", validated)
    print("Latency (ms):", latency_ms)
