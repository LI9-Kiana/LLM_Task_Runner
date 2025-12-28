from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Type

from pydantic import BaseModel


class Task(ABC):
    """
    Base interface for all tasks.

    A Task must define:
      - name: unique identifier
      - input_model: Pydantic model for validating inputs
      - output_model: Pydantic model for validating outputs
      - build_prompt(): how to turn validated input into an LLM prompt

    The runner can then execute any Task generically.
    """

    name: str  # Each subclass should set this, e.g. "classify"

    @property
    @abstractmethod
    def input_model(self) -> Type[BaseModel]:
        """Return the Pydantic model class used to validate task inputs."""
        raise NotImplementedError

    @property
    @abstractmethod
    def output_model(self) -> Type[BaseModel]:
        """Return the Pydantic model class used to validate task outputs."""
        raise NotImplementedError

    @abstractmethod
    def build_prompt(self, inp: BaseModel) -> str:
        """Build the prompt for the LLM using validated input."""
        raise NotImplementedError

    def validate_input(self, raw: Dict[str, Any]) -> BaseModel:
        """Helper to validate raw dict input into a typed Pydantic object."""
        return self.input_model.model_validate(raw)
