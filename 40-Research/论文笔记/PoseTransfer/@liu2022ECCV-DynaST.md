---
Authors: Songhua Liu; Jingwen Ye; Sucheng Ren; Xinchao Wang
Date: 2022/07/13
Topics: pose-transfer
DOI:
  "{ DOI }": 
Keywords: Transferring by Dense and sparse attention block
---
tags: #论文笔记 

# DynaST: Dynamic Sparse Transformer for Exemplar-Guided Image Generation


## Abstract
One key challenge of exemplar-guided image generation lies in establishing fine-grained correspondences between input and guided images. Prior approaches, despite the promising results, have relied on either estimating dense attention to compute per-point matching, which is limited to only coarse scales due to the quadratic memory cost, or fixing the number of correspondences to achieve linear complexity, which lacks flexibility. In this paper, we propose a dynamic sparse attention based Transformer model, termed Dynamic Sparse Transformer (DynaST), to achieve fine-level matching with favorable efficiency. The heart of our approach is a novel dynamic-attention unit, dedicated to covering the variation on the optimal number of tokens one position should focus on. Specifically, DynaST leverages the multi-layer nature of Transformer structure, and performs the dynamic attention scheme in a cascaded manner to refine matching results and synthesize visually-pleasing outputs. In addition, we introduce a unified training objective for DynaST, making it a versatile reference-based image translation framework for both supervised and unsupervised scenarios. Extensive experiments on three applications, pose-guided person image generation, edge-based face synthesis, and undistorted image style transfer, demonstrate that DynaST achieves superior performance in local details, outperforming the state of the art while reducing the computational cost significantly. Our code is available at https://github.com/Huage001/DynaST

## Files and Links
- **Url**: [Open online](https://arxiv.org/abs/2207.06124v3)
- **zotero entry**: [Zotero](zotero://select/library/items/73FJ8WTR)
- **open pdf**: [Liu et al_2022_DynaST.pdf](zotero://open-pdf/library/items/QTDVNA9V)

## Comments


---

## Summary

  
## Research Objective(s)


## Background / Problem Statement

先前简单粗暴地将source图像和pose图像送入transformer来计算attention map，计算复杂度是 n^2 的，那我们能不能尝试利用多尺度的特征图，自底而上进行一个coarse-to-fine的计算attention map捏？
## Method(s)


作者提出了一个多尺度，自下而上计算attention map的结构：
1. 本文提出一种基于动态稀疏注意力的 Transformer 模型，称为 Dynamic Sparse Transformer (DynaST)，以实现具有良好效率的精细匹配。方法核心是一个新的动态注意单元，致力于覆盖一个位置应该关注的最佳tokens数量的变化。具体来说，DynaST 利用了 Transformer 结构的多层特性，并以级联方式执行动态注意方案，以优化匹配结果并合成视觉上令人愉悦的输出。
2. 为 DynaST 引入了统一的训练目标，使其成为适用于有监督和无监督场景的通用基于参考的图像转换框架。在三个应用任务（姿势引导的人物图像生成、基于边缘的人脸合成和不失真的图像风格转移）上的广泛实验表明，DynaST 在局部细节方面取得了卓越的性能，在降低计算成本的同时超越了现有技术。

![[Pasted image 20240112184353.png]]
## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

