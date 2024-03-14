---
Authors: Xiao Han; Xiatian Zhu; Jiankang Deng; Yi-Zhe Song; Tao Xiang
Date: {{date}}
Topics: CPIS
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# Controllable Person Image Synthesis with Pose-Constrained Latent Diffusion


## Abstract
Controllable person image synthesis aims at rendering a source image based on user-speciﬁed changes in body pose or appearance. Prior art approaches leverage pixel-level denoising diffusion models conditioned on the coarse skeleton via cross-attention. This leads to two limitations: low efﬁciency and inaccurate condition information. To address both issues, a novel Pose-Constrained Latent Diffusion model (PoCoLD) is introduced. Rather than using the skeleton as a sparse pose representation, we exploit DensePose which offers much richer body structure information. To effectively capitalize DensePose at a low cost, we propose an efﬁcient pose-constrained attention module that is capable of modeling the complex interplay between appearance and pose. Extensive experiments show that our PoCoLD outperforms the state-of-the-art competitors in image synthesis ﬁdelity. Critically, it runs 2× faster and consumes 3.6× smaller memory than the latest diffusion-model-based alternative during inference. Our code and models are available at https://github.com/BrandonHanx/PoCoLD.

## Files and Links
- **Url**: [Open online]({{url}})
- **zotero entry**: [Zotero](zotero://select/library/items/493GW93R)
- **open pdf**: [Han 等 - Controllable Person Image Synthesis with Pose-Cons.pdf](zotero://open-pdf/library/items/LW8723RE)

## Comments


---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)

可以看出，它和PIDM的结构很相似，区别在于使用的是隐空间 z ，此外pose也改用了dense pose（现在越来越常用了）。但是和PIDM中直接使用交叉注意力机制引入source特征不同，其设计了一个“Pose-constrained Attention”（上图中的黄色模块）：

![[Pasted image 20240117145922.png]]

这个交叉注意力机制有两点改进：

首先仿照我们先前讲过的NTED的线性注意力机制，将原先的交叉注意力机制：

==没看懂==

![[Pasted image 20240117150412.png|300]]

改为

![[Pasted image 20240117150418.png|350]]

![[Pasted image 20240117150424.png|425]]
![[Pasted image 20240117150430.png|425]]
![[Pasted image 20240117150615.png|450]]

## Evaluation

FID不如PIDM：解释为数据集过拟合？
其他都超越了PIDM
![[Pasted image 20240117145900.png|475]]

但是有效降低了模型大小，推理速度和内存占用

![[Pasted image 20240117155100.png|375]]
## Conclusion


## Notes


----

## Extracted Annotations

