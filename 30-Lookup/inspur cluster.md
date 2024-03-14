---
DESC: 实验室集群登录方式
---
## 连接到Inspur集群的方式：

前提：连接到校园网
在CMD/Powershell/bash/zsh中输入：
```
ssh 10.134.142.143 -l <你的名字>
```
即可登入节点mu01

节点间关系如下：
```
校园网
|
mu01---io01
|   \ /   |
|    X    |
|   / \   |
gpu01--gpu02
```
其中mu01是管理节点，可通过校园网连入；io01是存储节点，拥有200T左右的存储空间，并且已通过NFS方式挂载到mu01上；gpu01上挂载了8块GeForce2080Ti的卡；gpu02上挂载了4块Tesla V100的卡。<br>
例如要登入gpu01节点，则应当在校园网环境下登入mu02节点（按照上面的代码），然后在命令行中输入
```
ssh gpu01
```
其他节点的进入方式类同。四个节点之间两两连通，可任意切换。

## 账户与初始密码：
每个人的账号是自己名的拼音缩写（区分卷平舌）+姓的拼音缩写，全小写；初始密码是自己的完整名姓拼音，全小写。例如张朕银的账号为zhyzhang，初始密码为zhenyinzhang。（不要尝试用我这个密码登入我的账号，我已经改过了;-)，大家也请尽快修改自己的初始密码）

注意，四个节点上的账户密码并不会同步修改。

如果忘记密码或者遇到权限问题请联系管理员。（丁路昶/高朋/张朕银）

## 其他

目前vnc还在配置，不久将在gpu01和gpu02上配置好相应的vnc服务。

目前除mu01外均不能访问校园网或外网，不久将实现所有节点的对外访问。

## 使用浪潮服务器注意事项
1. 目前只有mu01上可以上网，gpu01/gpu02大部分时候没有网络连接，小部分时候有网络连接。因此使用pip/conda install安装库时应该在mu01节点上安装

2. 使用ssh从当前节点进入另一节点，如从mu01通过ssh gpu02进入gpu02节点之后，如果想返回mu01节点
- 最好使用exit，此时将会从mu01->gpu02回退到mu01。
- 而不是再次使用ssh mu01，因为这会使得mu01->gpu02变成mu01->gpu02->mu01。

3. 可以在服务器上安装anaconda来管理各个环境和库，安装tensorflow和pytorch需要安装GPU版本

可以通过```whereis cuda```找到cuda安装位置，然后在自己~/.bashrc文件最后添加cuda路径，添加完成后需要source ~/.bashrc更新，添加内容类似这样：
```
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda
```
4. 可以通过下述命令查看GPU情况(在gpu01/gpu02节点上)：

```nvidia-smi```或者```watch gpustat -cpu ``` (需要安装gpustat库)
- watch gpustat -cpu 可以看到运行情况，以及进程名称。可以使用```kill -9 pid```将进程杀死

---

5. 运行代码时一般要设定具体使用的GPU卡编号，若没有设置直接使用，则可能会占用所有gpu卡，但实际运算的却只有一张GPU卡。如使用watch gpustat -cpu发现第3张卡是空闲的，你准备使用第3张卡，那么

- 可以在代码中指定使用哪块gpu。这两句话一般要往前面放，因为若之前代码中已经用到了GPU，那么会默认选中第0张卡，此时再去用os指定GPU卡会无效
``` 
import os
os.envron['CUDA_VISIBLE_DEVICES]='3'
```
- 也可以在运行代码时指定具体使用的GPU
```
CUDA_VISIBLE_DEVICES='1' python train.py
```

6. 一般在Terminal运行python文件时，当Terminal关闭时，哪怕这个python文件并没有运行结束，可会被kill掉；这时可以使用nuhup命令进行无间断的运行代码。

7. linux上几个常用快捷键
- ctrl+C 中断命令或进程
- ctrl++Z 暂停命令或进程
- bg 将当前运行程序转移到后台
- fg 将当前后台程序转移到前台运行
- & 在命令后跟&可以使该程序放在后台运行，也可以通过 ctrl+Z 将前台命令暂停，然后使用 bg 将其放到后台运行


 CUDA_VISIBLE_DEVICES='1'  bash ./tools/dist_train.sh  ./configs/wholebody_2d_keypoint/rtmpose/coco-wholebody/rtmpose-m_8xb64-270e_coco-wholebody-256x192.py 1


## 新的服务器
username: ynzhu
passwd: ynzhu123456
ssh ip: 10.134.142.225
port: 9999





tags: #LUT