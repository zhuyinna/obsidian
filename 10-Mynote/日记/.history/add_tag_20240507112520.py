import os

# 打开文件夹，遍历所有md结尾的文件
def add_tag(path):
    for file in os.listdir(path):
        
        print(file)

add_tag(".")