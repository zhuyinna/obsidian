---
DESC: linux命令语句
---

# 基本语句
---
**基本命令**

| 操作               | 命令                                                           |
| ---------------- | ------------------------------------------------------------ |
| 修改文件/文件夹名称       | `mv file1 file2`                                             |
| 解压/压缩 .tar.gz    | `tar -zxvf filename.tar.gz`                                  |
| 解压/压缩 .zip       | `unzip FileName.zip;  zip FileName.zip DirName`              |
| 筛选相关文件           | `ls \| grep tar`                                             |
| CUDA 版本          | `ncvv --version`                                             |
| pytorch 版本       | `python -c 'import torch;` <br>`print (torch.__version__)' ` |
| 查看历史命令           | ` history [n] `                                              |
| 测试网络连接           | `curl -v  `                                                  |
| 检查网络连接           | `ping  www.baidu.com`                                        |
| 检查指定 ip 是否开放指定端口 | `telnet://github.com: 443` or  `telnet www.baidu.com 80`     |
| 删除指定后缀           | `find . -name "*.png" \|xargs rm -rf`                        |
| 统计行数             | `find /path/to/your/directory -type f \| wc -l`              |

**特殊操作**
1. 重置密码
![[Pasted image 20230409133146.png]]



# Conda
***
**基本命令**

| 操作   | 命令                                        |
| ---- | ----------------------------------------- |
| 新建   | `conda create --name env_name python=3.9` |
| 查找包  | `conda search package_name`               |
| 显示环境 | `conda env list `                         |
| 激活   | `conda activate env_name`                 |
| 删除   | ` conda env remove -n env_name`           |
| 退出   | `conda deactivate`                        |
| 显示所有 | `conda info --envs`                       |
| 安装包  | `conda install package_name`              |
| 列出包  | `conda list `                             |
|      |                                           |
**特殊命令**

1. 查看源
`conda config --show-sources`
2. 换回原默认源
`conda config --remove-key channels` 
3. 升级 conda(升级 Anaconda 前需要先升级 conda)
`conda update conda `
4. 升级 anaconda
`conda update anaconda`
5. 升级 spyder
`conda update spyder`
6. 更新所有包
`conda update --all `
7. 安装包
`conda install package`
8. 更新包
`conda update package`
9. 查询某个 conda 指令使用-h 后缀，如
`conda update -h`
10. 改变下载源：阿里云
~/.condarc文件中添加：

```bash
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/bioconda/
```

11. 清除condarc
`conda config --remove-key channels`
   
# pip
1. upgrade
`python3 -m pip install --upgrade pip`

# CUDA
1. 查看 torch 版本和 cuda 版本是否一致
```python
import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())
```




# git
***
**常用语句**

1.创建仓库

| 命令      | 说明                             |
| --------- | -------------------------------- |
| git init  | 初始化仓库                       |
| git clone | 拷贝一份远程仓库（下载一个项目） | 

2.提交与修改

| 命令                                    | 说明                                                       |
| --------------------------------------- | ---------------------------------------------------------- |
| git add `filename`                      | 添加文件到暂存区(`add *` 表示添加全部文件)                 | 
| git status                              | 查看仓库当前的状态(untracked:从未提交过;modified:刚改过)   |
| git diff `filename`                     | 比较不同                                                   |
| git commit [-m "xxx"]                   | 提交暂存区当本地仓库,-m后接本次提交说明                    |
| git reset                               | 回退版本                                                   |
| git rm                                  | 将文件从暂存区和工作区删除                                 |
| git mv                                  | 移动或重命名工作区文件                                     |
| git reset --hard HEAD^ [filename]       | 回退到上一个版本（HEAD^^上上个版本，HEAD~n前n个版本）      |
| git reset --hard `commitID` [filenmame] | 回退到指定版本，commitID不需要写全                         |
| git checkout -- `filename`              | 还未add，撤销工作区的修改;若已add，先执行reset，再执行本条 |

3.远程操作

| 命令                                                       | 说明                             |     |
| -------------------------------------------------------- | ------------------------------ | --- |
| git remote                                               | 远程仓库操作                         |     |
| git fetch                                                | 从远程获取代码库                       |     |
| git pull                                                 | 下载远程代码并合并                      |     |
| git push [origin master]                                 | 上传远程代码并合并                      |     |
| git remote add origin git@server-name:path/repo-name.git | 关联一个远程库                        |     |
| git push -u origin master                                | 关联后，第一次推送master分支所有内容          |     |
| git clone `URL`                                          | URL形式：git://（ssh协议，快）或https:// |     |

4.查看

| 命令                       | 说明                       |
| -------------------------- | -------------------------- |
| git log [--pretty=oneline] | 查看提交修改日志，简化输出 |
| git reflog                 | 显示所有历史命令           | 

5.删除

本地工作库删除了filename
	情况一、确实要从版本库删掉该文件
	`git rm filename`
	`git commit -m "remove a file"`
	情况二、误删，从版本库里恢复到本地
	`git checkout -- filename`

6. git pull指定文件夹
设置`$ git config core.sparsecheckout true`为true
- `core.sparsecheckout`用于控制是否允许设置pull指定文件/夹，true为允许。
- 此方法适用于 Git1.7.0 以后版本，之前的版本没有这个功能
在`.git/info/sparse-checkout`文件中（如果没有则创建）添加指定的文件/夹
最后，拉取想要的分支即可实现checkout指定文件/夹
`  $ git pull origin master`


**特殊用法**

1. 将本地代码上传到 github
```
git add *
git commit -m "注释"
git push -u origin master
```

2. 原fork分支更新，同步到本地
```
git remote add upstream "git URL"
git fetch upstream
git merge upstream/main
```

3. 删除已经提交但是需要被ignore的文件/文件夹
```bash
# 首先要配置到.gitignore里
# 接着执行
git rm --cached -r .  
git add .
git commit -am '注释'
```
最后可以进行接下来的add, commit, push

4. fetch和pull区别
<img src=https://s2.loli.net/2024/05/10/vUh4x8zEBn9Qolq.png width='100%'>
可以看到，`git fetch`是将远程主机的最新内容拉到本地，用户在检查了以后决定是否合并到工作本机分支中

而`git pull` 则是将远程主机的最新内容拉下来后直接合并，即：`git pull = git fetch + git merge`，这样可能会产生冲突，需要手动解决

**错误汇总**


```ad-error
在 pull 操作时  error: Your local changes to the following files would be overwritten by merge
```

方法1：stash
```
git stash
git commit
git stash pop
```
方法2：放弃本地修改，直接覆盖
```
git reset --hard
git pull
```

```ad-error
在 git push origin master操作时  error: failed to push some refs to 
'https://github.com/Zhuyinna/Makxxl_Obsidian.git'
```

原因：远程库与本地库不一致造成的，在 hint 中也有提示把远程库同步到本地库就可以了
方法： 
```
git pull --rebase origin master
```

```ad-error
unzip:  cannot find zipfile directory in one of ckpt-20230314T012919Z-002.zip or ckpt-20230314T012919Z-002.zip.zip, and cannot find ckpt-20230314T012919Z-002.zip.ZIP, period.
```

方法：安装 7zip

```ad-error
“fatal: refusing to merge unrelated histories” -(git-github)
```
`git pull origin main --allow-unrelated-histories`



# .bashrc 修改

**文件**

在linux系统普通用户目录（cd /home/xxx）或root用户目录（cd /root）下，用指令ls -al可以看到4个隐藏文件，

| 文件          | 用途                                        |
| ------------- | ------------------------------------------- |
| .bash_history | 记录之前输入的命令                          |
| .bash_logout  | 退出时执行的命令                            |
| .bash_profile | 登入 shell 时执行：只在会话开始读取一次     |
| **.bashrc**       | **登入 shell 时执行：每次打开新的终端都会读取** | 

**PATH路径修改**

1. 作用
     PATH 变量决定了 shell 将到哪些目录中寻找命令或程序
2. 语句、
     (1)定义局部变量
     只在当前终端有效，打开新的终端，运行 echo $PATH 仍为旧的 PATH。
     
| 语句                              | 用途                |
| --------------------------------- | ------------------- |
| PATH=/usr/bin:/usr/local/bin:/bin | 修改：注意开头没有$ |
| echo $PATH                        | 注意开头有\$        |
| PATH=$PATH:/some/directory        | 添加 path           |
    (2) 输出局部变量 export
    打开新的终端也会生效
        `export PATH=$PATH:/some/directory`
    (3) 永久生效
    将 (2) 添加到 `~/.bashrc` 中


**alias 别名**
写在. bashrc 中
`alias rm='rm -i'`

**最后需要运行命令生效**
`$source ~/.bashrc`

# 进程管理

| 命令                   | 操作                          |
| -------------------- | --------------------------- |
| `ctrl+Z`             | 前台进程：挂起                     |
| `stop %num `         | 后台进程：挂起                     |
| `ctrl+C`             | 前台进程：终止                     |
| `kill %num [or PID]` | 后台进程：终止                     |
| `jobs`               | 查看 jobs，+表示当前，-表示是当前作业之后的作业 |
| `jobs -l`            | 查看 PID                      |

1. &
    以& 结尾   run.sh &，缺点是退出终端就退出执行
2. nohup: 记录发生日志
    nohup  run.sh &  --> 输入 exit 退出，会自动将输出写到当前目录下的 nohup.txt 里
    指定文件：nohup ./start.sh >output 2>&1 &  指定输出到output文件
3. tmux: 保存上次工作流
    -  new session 
        tmux new -s  demo 进入 tmux 
    - run.sh 执行程序
    - 退出  ctrl + b  --> 输入 d
    - 查看 tmux 列表， tmux ls
    - 进入 demo session
    - tmux at -t demo
    - 杀死 session  , tmux kill-session -t demo




tags: #LUT