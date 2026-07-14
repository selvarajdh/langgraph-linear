# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the workflow (builds and compiles the graph on import)
python src/linear.py

# Run all test cases
python src/test_linear.py
```

## Architecture

`src/linear.py` is both a module and a runnable script. At import time it:
1. Defines `AgentState` — the shared state TypedDict that flows through every node
2. Defines the four node functions
3. Immediately builds and compiles the LangGraph `StateGraph` into `app`
4. Exposes `run_workflow(user_input: str)` for callers

The graph is a fixed linear pipeline with no branching:

```
START -> input_node -> analyze_node -> process_node -> output_node -> END
```

**State fields:**
- `messages` — uses `operator.add` as a reducer, so each node appends rather than overwrites
- `processing_step` — tracks which node last ran (`input_received` → `analyzed` → `processed` → `completed`)
- `result` — set by `process_node`, read by `output_node`
- `user_input` — set once at invocation, never mutated by nodes

**Keyword matching** in `analyze_node` and `process_node` uses `re.findall(r'\b\w+\b', user_text)` for whole-word detection. Use this pattern (not `"word" in user_text`) when adding new keyword checks to avoid substring false positives.

`src/test_linear.py` imports `run_workflow` from `linear` and runs 15 hand-labelled cases. To add new cases, append to the `test_cases` list — each entry is `(input_string, label_string)`.
