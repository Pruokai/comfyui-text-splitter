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
    OUTPUT_IS_LIST = (True, False) # text_list is a list, count is not
    FUNCTION = "process_file"
    CATEGORY = "utils/text"

    def process_file(self, file_path, split_method, encoding, strip_whitespace):
        if not os.path.exists(file_path):
            # Try looking in ComfyUI input directory if relative path
            # But for now, just return empty list or raise error
            # We will assume absolute path or handle error gracefully
            print(f"File not found: {file_path}")
            return ([], 0)

        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
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
            # Split by patterns like "1. ", "2. ", "1、"
            # Regex: look for newline followed by digit + dot/comma
            # Or just start of string
            # Strategy: find all matches of the pattern, then slice text
            
            # Pattern: (Start of line)(Digits)(Dot or Chinese Comma)(Whitespace)
            # We use re.split but need to keep content.
            # Simpler: Iterate lines and group
            
            lines = content.split('\n')
            current_item = []
            
            # Regex for start of a numbered item: ^\d+[.、]\s*
            pattern = re.compile(r'^\d+[.、]\s*')
            
            for line in lines:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                
                if pattern.match(stripped_line):
                    # If we have a current item accumulating, save it
                    if current_item:
                        result_list.append("\n".join(current_item))
                        current_item = []
                    
                    # Remove the numbering for the content? 
                    # Usually users want the content. Let's strip the numbering.
                    # Or keep it? The prompt implies splitting "according to... inputs". 
                    # Usually clean content is preferred. Let's keep full line for now or optional?
                    # Let's keep the full line to be safe, or just the content. 
                    # "Splitting text content" implies getting the items.
                    # Let's clean the number marker to make it clean.
                    clean_line = pattern.sub('', stripped_line, count=1)
                    current_item.append(clean_line)
                else:
                    # Append to current item (multiline content within a numbered item)
                    if current_item:
                        current_item.append(stripped_line)
                    else:
                        # Content before first number, or simple append if treating as loose text
                        # If we assume the file IS a numbered list, this might be preamble.
                        # We'll skip preamble if result_list is empty.
                        pass
            
            # Append last item
            if current_item:
                result_list.append("\n".join(current_item))

        count = len(result_list)
        return (result_list, count)

# Mapping for __init__.py
NODE_CLASS_MAPPINGS = {
    "TextFileSplitter": TextFileSplitter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextFileSplitter": "Text File Splitter"
}
