---
Authors: Pengze Zhang; Lingxiao Yang; Jianhuang Lai; Xiaohua Xie
Date: 6/2022
Topics: pose-transfer
DOI: 10.1109/CVPR52688.2022.00756
Keywords: Spatial transform with self and cross attention
---
tags: #论文笔记 

# Exploring Dual-task Correlation for Pose Guided Person Image Generation


## Abstract
Pose Guided Person Image Generation (PGPIG) is the task of transforming a person image from the source pose to a given target pose. Most of the existing methods only focus on the ill-posed source-to-target task and fail to capture reasonable texture mapping. To address this problem, we propose a novel Dual-task Pose Transformer Network (DPTN), which introduces an auxiliary task (i.e., source-tosource task) and exploits the dual-task correlation to promote the performance of PGPIG. The DPTN is of a Siamese structure, containing a source-to-source self-reconstruction branch, and a transformation branch for source-to-target generation. By sharing partial weights between them, the knowledge learned by the source-to-source task can effectively assist the source-to-target learning. Furthermore, we bridge the two branches with a proposed Pose Transformer Module (PTM) to adaptively explore the correlation between features from dual tasks. Such correlation can establish the fine-grained mapping of all the pixels between the sources and the targets, and promote the source texture transmission to enhance the details of the generated target images. Extensive experiments show that our DPTN outperforms state-of-the-arts in terms of both PSNR and LPIPS. In addition, our DPTN only contains 9.79 million parameters, which is significantly smaller than other approaches. Our code is available at: https:// github.com/PangzeCheung/Dual-task-PoseTransformer-Network.

## Files and Links
- **Url**: [Open online](https://ieeexplore.ieee.org/document/9878918/)
- **zotero entry**: [Zotero](zotero://select/library/items/SRWF2R2D)
- **open pdf**: [Zhang 等 - 2022 - Exploring Dual-task Correlation for Pose Guided Pe.pdf](zotero://open-pdf/library/items/958N5QGI)

## Comments


---

## Summary

  
## Research Objective(s)


## Background / Problem Statement

姿势引导人物图像生成是将人物图像从源姿势转换为给定目标姿势的任务，==作者认为现有的方法大多只针对不适定的源到目标任务，无法捕捉到合理的纹理映射。为了解决这个问题==，提出了一种新的双任务姿势变换网络（Dual-task Pose Transformer Network，DPTN），引入了源到源的辅助任务，并通过姿势变换模块（Pose Transformer Module，PTM） 充分利用双任务的相关性来提高姿态迁移的性能，


## Method(s)


### Dual-task

**Siamese Structure for Dual Tasks（孪生）**

- source-to-source task： 源图像到源图像自重构分支，即生成原图
- source-to-target task： 源图像到目标图像的转换分支，即生成有原图像纹理和目标姿态的图像
![[Pasted image 20240112220559.png]]

作者认为，从源到目标任务的学习不能很好利用源图像的细节，并通过实验验证了，在不修改传统姿态迁移网络的前提下，单纯加入源到源的训练。

![[Pasted image 20240112220750.png|500]]

优势
1. 共享权重，因此学习的知识可以在两个任务之间轻松地转移，并且引入的Self-reconstruction Branch 不会大幅增加额外的参数
2. 连体结构使双任务的中间输出在特征分布上接近，便于PTM 探索双任务的相关性


### 姿势变换模块（Pose Transformer Module，PTM）

捕获双任务特征之间的对应关系，改善Fs-t。

![[Pasted image 20240112220928.png]]

1. 上下文增强模块（Context Augment Block，CAB），整合来自 Fs→s的信息
2. 纹理迁移模块（Texture Transfer Block，TTB），根据 Fs 中的真实源图像纹理来优化Fs→t ，使其捕获双重任务中特征之间的相关性。

具体分析两个模块

1. 上下文增强模块（Context Augment Block，CAB）
   ![[Pasted image 20240112221221.png|600]]

2. 纹理迁移模块（Texture Transfer Block，TTB）
​![[Pasted image 20240112221351.png]]

### 损失函数

见图1.
注意两个task的损失函数有所区别：Ladv

![[Pasted image 20240112221427.png]]




## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

