import unittest
import os
import sys

# 添加父目录到路径以导入 nodes
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nodes import TextFileSplitter

class TestTextFileSplitter(unittest.TestCase):
    def setUp(self):
        self.splitter = TextFileSplitter()
        self.test_file_newline = "test_newline.txt"
        self.test_file_numbered = "test_numbered.txt"
        
        # 创建测试文件
        with open(self.test_file_newline, "w", encoding="utf-8") as f:
            f.write("Line 1\nLine 2\n\nLine 3")
            
        with open(self.test_file_numbered, "w", encoding="utf-8") as f:
            f.write("1. First Item\nContent of first item\n2. Second Item\n3、Third Item")

    def tearDown(self):
        # 清理测试文件
        if os.path.exists(self.test_file_newline):
            os.remove(self.test_file_newline)
        if os.path.exists(self.test_file_numbered):
            os.remove(self.test_file_numbered)

    def test_split_newline(self):
        # 测试换行符拆分
        result, count = self.splitter.process_file(self.test_file_newline, "newline", "utf-8", True)
        self.assertEqual(count, 3)
        self.assertEqual(result, ["Line 1", "Line 2", "Line 3"])

    def test_split_numbered(self):
        # 测试编号列表拆分
        result, count = self.splitter.process_file(self.test_file_numbered, "numbered_list", "utf-8", True)
        self.assertEqual(count, 3)
        self.assertEqual(result[0], "First Item\nContent of first item")
        self.assertEqual(result[1], "Second Item")
        self.assertEqual(result[2], "Third Item")

if __name__ == '__main__':
    unittest.main()
