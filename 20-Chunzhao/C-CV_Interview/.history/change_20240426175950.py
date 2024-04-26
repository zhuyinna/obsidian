import re

def transform_markdown(file_path):
    # 读取原始Markdown文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式匹配并替换格式
    pattern = r'- \[ \] \[(\d+-\d+) +([^\]]+)\]\(\\d+-\d+)'
    replacement = r'- [ ]

if __name__=='__main__':
    transform_markdown('C:\Users\祝银那\Documents\Obsidian Vault\20-Chunzhao\C-CV_Interview\machine-learning-interview\README copy.md')