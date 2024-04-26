import re

def transform_markdown(file_path):
    # 读取原始Markdown文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    transformed_lines = []
    # 使用正则表达式匹配并替换格式
    pattern = r'- \[ \] \[(\d+-\d+) +([^\]]+)\]\(\#\d+-\d+)'
    for line in content:
        new_line = re.sub(pattern, r'- [ ]<span id="\1"> \2</span>', line)
        transformed_lines.append(new_line)
    new_file_path = file_path.replace('.md', '_modified.md')
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.writelines(transformed_lines)

if __name__=='__main__':
    transform_markdown('C:\Users\祝银那\Documents\Obsidian Vault\20-Chunzhao\C-CV_Interview\machine-learning-interview\README copy.md')