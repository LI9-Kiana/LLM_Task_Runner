
from tasks.classify import ClassifyTask
from runner.executor import call_llm
from runner.schema import parse_and_validate, SchemaValidationError
from eval.dataset import load_classification_dataset
from eval.metrics import accuracy, failure_rate, average_latency

from eval.dataset import load_classification_dataset

dataset = load_classification_dataset()

for ex in dataset:
    print(ex.text, ex.label)

def main(model: str = "gpt-4o-mini"):
    task = ClassifyTask(labels=["billing", "bug", "feature_request", "other"])
    dataset = load_classification_dataset()

    preds, labels, latencies = [], [], []
    failures = 0

    for ex in dataset:
        labels.append(ex["label"])
        try:
            inp = task.input_model.model_validate({"text": ex["text"]})
            prompt = task.build_prompt(inp)

            raw, latency = call_llm(prompt, model=model)
            out = parse_and_validate(raw, task.output_model)

            preds.append(out.label)
            latencies.append(latency)

        except SchemaValidationError:
            failures += 1
            preds.append(None)

    print("Accuracy:", accuracy(preds, labels))
    print("Failure rate:", failure_rate(failures, len(labels)))
    print("Avg latency:", average_latency(latencies))

if __name__ == "__main__":
    main()
