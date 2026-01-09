from __future__ import annotations

import json
import re
from typing import Type
from pydantic import BaseModel, ValidationError


class SchemaValidationError(Exception):
    pass


_JSON_BLOCK = re.compile(r"\{.*\}", re.DOTALL)


def parse_and_validate(output_text: str, model_cls: Type[BaseModel]) -> BaseModel:
    """
    Extract first JSON object from output_text, parse it, validate with Pydantic.
    """
    m = _JSON_BLOCK.search(output_text.strip())
    if not m:
        raise SchemaValidationError("No JSON object found in model output")

    json_str = m.group(0)
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise SchemaValidationError(f"Invalid JSON: {e}") from e

    try:
        return model_cls.model_validate(data)
    except ValidationError as e:
        raise SchemaValidationError(f"Schema validation failed: {e}") from e
