from __future__ import annotations

from typing import Optional
from tasks.base import Task
from runner.executor import call_llm, LLMCallError
from runner.schema import parse_and_validate, SchemaValidationError


class TaskExecutionError(Exception):
    pass


def run_with_retries(
    task: Task,
    raw_input: dict,
    primary_model: str,
    fallback_model: Optional[str] = None,
    max_attempts: int = 3,
):
    inp = task.validate_input(raw_input)
    prompt = task.build_prompt(inp)

    last_error = None

    # Try primary model
    for attempt in range(1, max_attempts + 1):
        try:
            raw_text, latency_ms = call_llm(prompt, model=primary_model)
            output = parse_and_validate(raw_text, task.output_model)
            return {
                "output": output,
                "model": primary_model,
                "attempts": attempt,
                "latency_ms": latency_ms,
            }
        except (SchemaValidationError, LLMCallError) as e:
            last_error = e

    # Fallback model
    if fallback_model:
        try:
            raw_text, latency_ms = call_llm(prompt, model=fallback_model)
            output = parse_and_validate(raw_text, task.output_model)
            return {
                "output": output,
                "model": fallback_model,
                "attempts": max_attempts + 1,
                "latency_ms": latency_ms,
            }
        except (SchemaValidationError, LLMCallError) as e:
            last_error = e

    raise TaskExecutionError(f"Task failed after retries: {last_error}")
