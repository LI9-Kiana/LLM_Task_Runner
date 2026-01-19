from typing import List

def accuracy(preds: List[str], labels: List[str]) -> float:
    if not preds:
        return 0.0
    return sum(p == l for p, l in zip(preds, labels)) / len(preds)

def failure_rate(failures: int, total: int) -> float:
    return failures / total if total else 0.0


def average_latency(latencies: List[int]) -> float | None:
    return sum(latencies) / len(latencies) if latencies else None