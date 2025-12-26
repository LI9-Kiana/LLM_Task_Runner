from __future__ import annotations

from typing import List, Type
from pydantic import BaseModel, Field

from tasks.base import Task


class ClassifyInput(BaseModel):
    text: str = Field(..., min_length=1, description="Text to classify")


class ClassifyOutput(BaseModel):
    label: str = Field(..., min_length=1, description="One of the allowed labels")


class ClassifyTask(Task):
    name = "classify"

    def __init__(self, labels: List[str]):
        if not labels:
            raise ValueError("labels must be non-empty")
        # optional: normalize labels
        self.labels = [l.strip() for l in labels if l.strip()]
        if not self.labels:
            raise ValueError("labels must contain at least one non-empty label")

    @property
    def input_model(self) -> Type[BaseModel]:
        return ClassifyInput

    @property
    def output_model(self) -> Type[BaseModel]:
        return ClassifyOutput

    def build_prompt(self, inp: ClassifyInput) -> str:
        labels_str = ", ".join(self.labels)

        # Key idea: force STRICT JSON and nothing else.
        return (
            "You are a precise text classifier.\n"
            f"Valid labels: [{labels_str}]\n\n"
            "Classify the input into exactly one label.\n"
            "Return ONLY valid JSON with this exact schema:\n"
            '{ "label": "<one valid label>" }\n'
            "Do not include any extra keys, explanation, markdown, or code fences.\n\n"
            f"Input text:\n{inp.text}\n"
        )
