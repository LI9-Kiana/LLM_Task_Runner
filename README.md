# Reliable LLM Task Runner

A lightweight framework for running LLM tasks with **structured prompting, schema validation, retries, logging, and evaluation**.

This project focuses on making LLM-based workflows **reliable, testable, and measurable** by enforcing explicit input and output contracts and providing a clean evaluation pipeline.

---

## Motivation

Large Language Models are powerful but inherently probabilistic. In practice, this often leads to:

- Outputs that do not follow the expected format
- Silent failures that are hard to detect
- Difficulty measuring correctness and reliability
- Tight coupling between prompts, execution, and evaluation

This project explores how to design a **production-style LLM execution pipeline** that emphasizes correctness, observability, and clean abstractions.

---

## Core Features

- **Task abstraction**  
  Define LLM tasks with explicit input and output schemas.

- **Structured prompting**  
  Prompts are programmatically generated to constrain model behavior.

- **Schema validation**  
  Raw LLM responses are parsed and validated using Pydantic models.

- **Retries and fallback**  
  Failed generations are retried automatically, with optional fallback to a secondary model.

- **Structured logging**  
  Task runs and failures can be logged for debugging and analysis.

- **Evaluation pipeline**  
  Run tasks over labeled datasets and compute accuracy, failure rate, and latency.

- **Configuration-driven models**  
  Model selection and parameters are defined via configuration rather than hard-coded.

---

## Project Structure

### Tasks
- `tasks/base.py`  
  Abstract task interface and shared schema definitions.

- `tasks/classify.py`  
  Example text classification task implementation.

### Runner
- `runner/executor.py`  
  Low-level LLM invocation logic.

- `runner/schema.py`  
  JSON extraction and Pydantic schema validation.

- `runner/retry.py`  
  Retry and fallback logic for failed generations.

- `runner/logger.py`  
  Structured logging utilities for task runs.

### Evaluation
- `eval/dataset.py`  
  Dataset loading and validation.

- `eval/metrics.py`  
  Accuracy, failure rate, and latency metrics.

- `eval/evaluate.py`  
  Evaluation orchestration and reporting.

### Data
- `data/sample.json`  
  Small, human-labeled dataset used for evaluation.

### Configuration
- `configs/models.yaml`  
  Model configuration (provider, parameters).

- `configs/load.py`  
  Configuration loading utilities.

### Entry Point
- `main.py`  
  Example task execution entry point.

---