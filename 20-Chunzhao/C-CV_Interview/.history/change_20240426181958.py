import re

def transform_markdown(file_path, output_path):
    # 读取原始Markdown文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    transformed_lines = []
    # 使用正则表达式匹配并替换格式
    pattern = r'- \[ \] \[(\d+-\d+) +([^\]]+)\]\(#(\d+-\d+)\)'
    replacement = r'- [ ] <span id="\3">\1  \2</span>'
    
    # 处理每一行，查找和替换特定格式的文本
    for line in content:
        new_line = re.sub(pattern, replacement, line)
        transformed_lines.append(new_line)

    # 将替换后的内容写入新文件
    with open(output_path, 'w', encoding='utf-8') as new_file:
        new_file.writelines(transformed_lines)
    
    print(f"Transformed markdown has been saved to: {output_path}")

if __name__ == '__main__':
    # 调用函数
    input_path = './machine-learning-interview/README copy.md'  # 假设原始文件名为 'original.md'
    output_path = './transformed.md'  # 输出文件名为 'transformed.md'
    transform_markdown(input_path, output_path)


