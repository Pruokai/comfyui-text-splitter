import os
import re

class TextFileSplitter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": "", "multiline": False}),
                "split_method": (["newline", "numbered_list"],),
                "encoding": (["utf-8", "gbk"],),
                "strip_whitespace": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("text_list", "count")
    OUTPUT_IS_LIST = (True, False) # text_list 是列表，count 不是
    FUNCTION = "process_file"
    CATEGORY = "utils/text"

    def process_file(self, file_path, split_method, encoding, strip_whitespace):
        if not os.path.exists(file_path):
            # 尝试在 ComfyUI 输入目录中查找（如果是相对路径）
            # 但目前直接返回空列表或报错
            # 我们假设是绝对路径或优雅地处理错误
            print(f"文件未找到: {file_path}")
            return ([], 0)

        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
        except Exception as e:
            print(f"读取文件出错: {e}")
            return ([], 0)

        result_list = []

        if split_method == "newline":
            lines = content.split('\n')
            for line in lines:
                if strip_whitespace:
                    line = line.strip()
                    if not line:
                        continue
                result_list.append(line)
        
        elif split_method == "numbered_list":
            # 按 "1. ", "2. ", "1、" 等模式拆分
            # 正则表达式：查找换行符后跟数字+点/顿号
            # 或者字符串开头
            
            lines = content.split('\n')
            current_item = []
            
            # 匹配编号项开头的正则: ^\d+[.、]\s*
            pattern = re.compile(r'^\d+[.、]\s*')
            
            for line in lines:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                
                if pattern.match(stripped_line):
                    # 如果当前已有累积的内容，先保存
                    if current_item:
                        result_list.append("\n".join(current_item))
                        current_item = []
                    
                    # 是否去除内容的编号？
                    # 通常用户只想要内容。让我们去除编号标记。
                    clean_line = pattern.sub('', stripped_line, count=1)
                    current_item.append(clean_line)
                else:
                    # 追加到当前项（编号项内的多行内容）
                    if current_item:
                        current_item.append(stripped_line)
                    else:
                        # 第一个编号之前的内容，或者如果未视为编号列表则简单追加
                        pass
            
            # 追加最后一项
            if current_item:
                result_list.append("\n".join(current_item))

        count = len(result_list)
        return (result_list, count)

# 映射到 __init__.py
NODE_CLASS_MAPPINGS = {
    "TextFileSplitter": TextFileSplitter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextFileSplitter": "文本文件拆分 (Text File Splitter)"
}
