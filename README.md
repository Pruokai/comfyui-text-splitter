# ComfyUI 文本文件拆分器 (Text File Splitter)

一个用于 ComfyUI 的自定义节点，允许读取文本文件并将其拆分为列表。这对于批处理工作流（例如，使用 For 循环遍历提示词或参数）特别有用。

## 功能特性

- **文件加载**：从任意路径加载文本文件（支持绝对路径）。
- **灵活拆分**：
  - **换行符 (Newline)**：按行拆分内容。
  - **编号列表 (Numbered List)**：自动检测并拆分编号列表（例如 `1. `, `2. `, `1、`）并去除编号。
- **循环兼容**：输出 `LIST`（字符串列表）和 `COUNT`（整数），可直接用于标准的 ComfyUI 循环节点（如 *Impact Pack* 或 *ComfyUI-Loop*）。
- **编码支持**：支持 `utf-8` 和 `gbk` 编码，以处理各种文本文件（包括包含中文字符的文件）。

## 安装

### 方法 1: Git Clone (推荐)
1. 进入你的 ComfyUI `custom_nodes` 目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. 克隆此仓库：
   ```bash
   git clone https://github.com/YOUR_USERNAME/comfyui-text-splitter.git
   ```
3. 重启 ComfyUI。

### 方法 2: 手动安装
1. 下载仓库的 ZIP 文件。
2. 解压到 `ComfyUI/custom_nodes/` 目录下。
3. 重启 ComfyUI。

## 使用方法

1. 在节点菜单中搜索 **"Text File Splitter"** (类别: `utils/text`)。
2. 在 `file_path` 组件中输入文本文件的绝对路径。
3. 选择 `split_method` (拆分方法):
   - 使用 `newline` 进行简单的逐行处理。
   - 如果文件格式如 "1. Prompt A", "2. Prompt B"，使用 `numbered_list`。
4. 将 `text_list` 输出连接到任何接受列表或遍历输入的节点。

## 需求

- ComfyUI
- Python 3.x (仅标准库)

## 许可证

MIT License
