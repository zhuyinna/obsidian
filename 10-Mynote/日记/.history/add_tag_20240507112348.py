import os

# 打开文件夹，遍历所有md结尾的文件
def add_tag(path):
    for file in os.walk(path):
        print(file)

add_tag("C:\Users\祝银那\Documents\Obsidian Vault\10-Mynote\日记")