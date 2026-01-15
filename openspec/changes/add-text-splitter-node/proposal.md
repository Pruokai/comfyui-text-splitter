# Change: Add Text Splitter Node

## Why
Users need a way to ingest text files and split them into processable chunks (e.g., lines or numbered items) to drive batch workflows (loops) in ComfyUI.

## What Changes
- Create a new ComfyUI custom node structure.
- Implement `TextFileSplitter` node.
- Support splitting by:
  - Newline (`\n`)
  - Numbered List (Regex `^\d+[\.\、]\s*`)
- Outputs compatible with list processing nodes (e.g., standard `LIST` type or custom loop types).

## Impact
- **New Capability**: Text file ingestion and splitting.
- **Affected Files**:
  - `__init__.py` (New)
  - `nodes.py` (New)
