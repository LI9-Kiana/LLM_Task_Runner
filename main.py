from tasks.classify import ClassifyTask
from runner.executor import call_llm
from runner.schema import parse_and_validate
from runner.retry import run_with_retries

if __name__ == "__main__":
    task = ClassifyTask(labels=["billing", "bug", "feature_request", "other"])
    inp = task.input_model.model_validate({"text": "I was charged twice"})
    prompt = task.build_prompt(inp)

    raw_text, latency_ms = call_llm(prompt, model="gpt-4o-mini")
    print("Raw model output:", raw_text)

    validated = parse_and_validate(raw_text, task.output_model)
    print("Validated output:", validated)
    print("Latency (ms):", latency_ms)

    

    result = run_with_retries(
        task=task,
        raw_input={"text": "I was charged twice"},
        primary_model="gpt-4o-mini",
        fallback_model="gpt-3.5-turbo",
        max_attempts=3,
    )

    print("Final result:", result)



    

