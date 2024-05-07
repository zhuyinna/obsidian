import os

# 打开文件夹，遍历所有md结尾的文件
def add_tag(path):
    # 用os.walk遍历文件夹中所有md文件，并得到相对路径
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, 'a') as f:
                    f.write("#")

add_tag(".")