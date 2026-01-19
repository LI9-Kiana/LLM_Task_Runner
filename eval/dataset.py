from __future__ import annotations

import json
from pathlib import Path
from typing import List
from pydantic import BaseModel, Field


# Path to the dataset file
DATA_PATH = Path("data/sample.json")


class ClassificationExample(BaseModel):
    """
    One evaluation example for the classification task.
    """
    text: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)


def load_classification_dataset(
    path: Path = DATA_PATH,
) -> List[ClassificationExample]:
    """
    Load and validate the classification evaluation dataset.

    Returns a list of ClassificationExample objects.
    """
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at {path}")

    with path.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)

    if not isinstance(raw_data, list):
        raise ValueError("Dataset must be a list of examples")

    examples: List[ClassificationExample] = []
    for i, item in enumerate(raw_data):
        try:
            example = ClassificationExample.model_validate(item)
            examples.append(example)
        except Exception as e:
            raise ValueError(f"Invalid example at index {i}: {item}") from e

    return examples
