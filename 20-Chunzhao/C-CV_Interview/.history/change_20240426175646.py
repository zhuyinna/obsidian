import re

def transform_markdown(file_path):
    # 读取原始Markdown文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式匹配并替换格式
    pattern = r'- \[ \] \[(\d+-\d+) +([^\]]+)\]\(#\1\)'
    replacement = r'- [ ]

if 