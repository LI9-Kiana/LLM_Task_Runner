import json
import time
from pathlib import Path

LOG_FILE = Path("logs/runs.jsonl")
LOG_FILE.parent.mkdir(exist_ok=True)


def log_event(event: dict):
    event["timestamp"] = time.time()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
