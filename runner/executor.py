from __future__ import annotations

import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

class LLMCallError(Exception):
    pass


def call_llm(prompt: str, model: str = "gpt-4o-mini") -> tuple[str, int]:
    """
    Returns: (text_output, latency_ms)
    """
    start = time.time()
    try:
        resp = client.responses.create(
            model=model,
            input=prompt,
            temperature=0,
        )
        text = resp.output_text
    except Exception as e:
        raise LLMCallError(str(e)) from e
    latency_ms = int((time.time() - start) * 1000)
    return text, latency_ms
