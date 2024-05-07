#-*- coding : utf-8-*-
# coding:unicode_escape

import os

# 打开文件夹，遍历所有md结尾的文件
def add_tag(path):
    # 用os.walk遍历文件夹中所有md文件，并得到相对路径
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
               
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        if lines:
                            lines = lines[:-1]
                            lines.append("#日记")
                    with open(path, 'w', encoding='utf-8') as f:  # Open with UTF-8 encoding for writing
                        f.writelines(lines)
                except UnicodeDecodeError as e:

                    print(f"Error processing {path}:{e}")
                
    
add_tag(".")