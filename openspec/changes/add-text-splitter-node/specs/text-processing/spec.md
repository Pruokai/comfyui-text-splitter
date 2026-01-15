## ADDED Requirements
### Requirement: 文本文件拆分 (Text File Splitting)
系统必须提供一个节点，将文本文件读取并拆分为字符串列表。

#### Scenario: 按换行符拆分
- **WHEN** 提供了一个文本文件 AND 拆分方法为 "newline"
- **THEN** 返回一个字符串列表，其中每一行作为一个项（去除空行）

#### Scenario: 按编号列表拆分
- **WHEN** 提供了一个包含 "1. Item", "2. Item" 的文本文件 AND 拆分方法为 "numbered_list"
- **THEN** 返回一个列表，其中每一项对应一个编号条目

#### Scenario: 编码回退
- **WHEN** 提供了一个文件
- **THEN** 允许选择编码（默认为 utf-8）以支持中文字符

### Requirement: 循环集成 (Loop Integration)
系统必须提供适合迭代的输出。

#### Scenario: 输出列表和数量
- **WHEN** 文本被拆分
- **THEN** 输出字符串列表 AND 项目总数
