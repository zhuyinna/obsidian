---
time: 2022-10-03
publish: ICLR'2023
---
# MDM

![[Pasted image 20230918200159.png]]
## Introduction

## Architecture
- Framework不是 Unet，而是 transformer


![[Pasted image 20230918201011.png]]
- 加噪过程
  ![[Pasted image 20230918202219.png|500]]
  t 表示扩散的时间步，1: N 表示序列长度
  
- 去噪过程
```ad-question
什么是预测ε，什么是预测signal本身？两者区别是什么？
```
  ![[Pasted image 20230918202537.png|500]]
  - 损失函数
    ![[Pasted image 20230918203000.png|500]]
    Lpos: FK 函数 denotes the forward kinematic function converting joint rotations into joint positions (otherwise, it denotes the identity function).
    Lfoot：防止脚滑？
    ![[Pasted image 20230918203106.png|500]]


- Model




## 不足

MDM 使用几何损失作为训练约束来对样本本身进行预测。虽然这些方法取得了令人印象深刻的结果，但它们对于不常见的条件信号来说不够通用。

## 展望
1. Diffusion 的推理过程加速
2. 在生成过程中加入更多控制（比如物理后处理，还有我想的姿势微调，也可能仅仅是条件）