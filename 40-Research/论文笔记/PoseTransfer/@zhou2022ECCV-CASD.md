---
Authors: Xinyue Zhou; Mingyu Yin; Xinyuan Chen; Li Sun; Changxin Gao; Qingli Li
Date: 2022-08-01
Topics: CPIS
DOI: 10.48550/arXiv.2208.00712
Keywords:
---
tags: #论文笔记 

# Cross Attention Based Style Distribution for Controllable Person Image Synthesis


## Abstract
Controllable person image synthesis task enables a wide range of applications through explicit control over body pose and appearance. In this paper, we propose a cross attention based style distribution module that computes between the source semantic styles and target pose for pose transfer. The module intentionally selects the style represented by each semantic and distributes them according to the target pose. The attention matrix in cross attention expresses the dynamic similarities between the target pose and the source styles for all semantics. Therefore, it can be utilized to route the color and texture from the source image, and is further constrained by the target parsing map to achieve a clearer objective. At the same time, to encode the source appearance accurately, the self attention among different semantic styles is also added. The effectiveness of our model is validated quantitatively and qualitatively on pose transfer and virtual try-on tasks.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2208.00712)
- **zotero entry**: [Zotero](zotero://select/library/items/M5XVVQ85)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/5W7ZRE2U); [Zhou et al_2022_Cross Attention Based Style Distribution for Controllable Person Image Synthesis.pdf](zotero://open-pdf/library/items/MS8EKAA3)

## Comments
Comment: Accepted by ECCV 2022

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)

作者认为，像AD-GAN中使用的模块（如AdaIN等）都是“common operations”（有点伤人哈），所以会特征对齐的不好（lacks the ability to align source style with target pose）。

![[Pasted image 20240111105701.png]]
所以作者提出了一个coarse-to-fine的结构（如上）：先用那些“common operations”（图中的AdaIN ResBlks）得到粗糙的对齐特征 Fcrs，再用自己设计的CASD Blocks来refine这样的特征得到更好的、对齐的特征 Fps 。再将这样对齐好的特征作为Style输入AFN ResBlks得到输入Decoder的特征。

其中的Style Encoder即为AD-GAN中设计的结构；AdaIN ResBlks即为AdaIN residual blocks，就是一个Style Block加上残差连接；AFN ResBlks即为Aligned Feature Normalization (AFN) residual blocks，结构如上图。其中的SPADE即为Spatially-Adaptive Normalization，可以看成是AdaIN的改进版本，结构如下，其实就是normalization其中的 γ β不再是vector而是有空间信息的tensor。
![[Pasted image 20240111105929.png|375]]


CASD block：

![[Pasted image 20240111105710.png]]
![[Pasted image 20240111110022.png]]


## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

