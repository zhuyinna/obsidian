---
Authors: Bin Xiao; Haiping Wu; Yichen Wei
Date: 2018
Topics: 2D; HPE
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# Simple Baselines for Human Pose Estimation and Tracking


## Abstract
There has been signiﬁcant progress on pose estimation and increasing interests on pose tracking in recent years. At the same time, the overall algorithm and system complexity increases as well, making the algorithm analysis and comparison more diﬃcult. This work provides simple and eﬀective baseline methods. They are helpful for inspiring and evaluating new ideas for the ﬁeld. State-of-the-art results are achieved on challenging benchmarks. The code will be available at https://github. com/leoxiaobin/pose.pytorch.

## Files and Links
- **Url**: [Open online](https://link.springer.com/10.1007/978-3-030-01231-1_29)
- **zotero entry**: [Zotero](zotero://select/library/items/KYS553MZ)
- **open pdf**: [Xiao 等 - 2018 - Simple Baselines for Human Pose Estimation and Tra.pdf](zotero://open-pdf/library/items/Q4HD6PNN)

## Comments
- 很基础的网络，可以用于后续模块的增加。
- 在 ResNet 的基础上，增加了反卷积模块（转置卷积+BatchNorm+ReLu），取得了很好的效果
- 还可用于姿态跟踪

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)
![[Pasted image 20231226214701.png]] 
### 基于反卷积Head网络的姿态估计
在 ResNet 的基础上，增加了三个反卷积层：本文方法只是在 ResNet 的最后一个卷积阶段(C5)后面添加几个反卷积层。完整网络结构如图1(c)所示。采用这种结构是因为这是从深度及低分辨率特征生成 heatmap 的最简单方法，也是 SOTA Mask R-CNN 采用的方法。默认情况下，使用三层带有 BN 和 ReLU 层的反卷积层。每层有256个 filters，kernel 为4×4。步长为2。最后添加一个1x1卷积层，负责生成 k 个关键点的预测 heatmap {h1, ..., hk}。

均方差(MSE)用作预测heatmap和目标heatmap之间的损失。关节k的目标heatmap Ĥk是以第k个关节gt位置为中心的2D高斯来生成的。


### 基于光流的姿态跟踪

暂时没看，感觉只是 HPE 的拓展。

## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

