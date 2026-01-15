# ComfyUI Text File Splitter

A custom node for ComfyUI that allows reading and splitting text files into lists. This is particularly useful for batch processing workflows (e.g., iterating through prompts or parameters using a For Loop).

## Features

- **File Loading**: Load text files from any path (supports absolute paths).
- **Flexible Splitting**:
  - **Newline**: Split content by line.
  - **Numbered List**: Automatically detect and split numbered lists (e.g., `1. `, `2. `, `1、`) and strip the numbering.
- **Loop Compatible**: Outputs a `LIST` (list of strings) and `COUNT` (integer), ready for standard ComfyUI loop nodes (like *Impact Pack* or *ComfyUI-Loop*).
- **Encoding Support**: Supports `utf-8` and `gbk` encodings to handle various text files, including those with Chinese characters.

## Installation

### Method 1: Git Clone (Recommended)
1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/comfyui-text-splitter.git
   ```
3. Restart ComfyUI.

### Method 2: Manual Install
1. Download the repository as a ZIP file.
2. Extract it into `ComfyUI/custom_nodes/`.
3. Restart ComfyUI.

## Usage

1. Search for the node **"Text File Splitter"** in the node menu (Category: `utils/text`).
2. Enter the absolute path to your text file in the `file_path` widget.
3. Select the `split_method`:
   - Use `newline` for simple line-by-line processing.
   - Use `numbered_list` if your file is formatted like "1. Prompt A", "2. Prompt B".
4. Connect the `text_list` output to any node that accepts a list or iterates over inputs.

## Requirements

- ComfyUI
- Python 3.x (Standard libraries only)

## License

MIT License
