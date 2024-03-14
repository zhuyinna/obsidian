---
Authors: Zhongcong Xu; Jianfeng Zhang; Jun Hao Liew; Hanshu Yan; Jia-Wei Liu; Chenxu Zhang; Jiashi Feng; Mike Zheng Shou
Date: 2023-11-27
Topics: pose-transfer
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# MagicAnimate: Temporally Consistent Human Image Animation using Diffusion Model


## Abstract
This paper studies the human image animation task, which aims to generate a video of a certain reference identity following a particular motion sequence. Existing animation works typically employ the frame-warping technique to animate the reference image towards the target motion. Despite achieving reasonable results, these approaches face challenges in maintaining temporal consistency throughout the animation due to the lack of temporal modeling and poor preservation of reference identity. In this work, we introduce MagicAnimate, a diffusion-based framework that aims at enhancing temporal consistency, preserving reference image faithfully, and improving animation fidelity. To achieve this, we first develop a video diffusion model to encode temporal information. Second, to maintain the appearance coherence across frames, we introduce a novel appearance encoder to retain the intricate details of the reference image. Leveraging these two innovations, we further employ a simple video fusion technique to encourage smooth transitions for long video animation. Empirical results demonstrate the superiority of our method over baseline approaches on two benchmarks. Notably, our approach outperforms the strongest baseline by over 38% in terms of video fidelity on the challenging TikTok dancing dataset. Code and model will be made available.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2311.16498)
- **zotero entry**: [Zotero](zotero://select/library/items/C8N6473Z)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/PKD4PX6H); [Xu et al_2023_MagicAnimate.pdf](zotero://open-pdf/library/items/85AMTTCA)

## Comments
Comment: Project Page at https://showlab.github.io/magicanimate

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)
![[Pasted image 20240117121610.png]]

## Evaluation
![[Pasted image 20240117121637.png]]

## Conclusion


## Notes


----

## Extracted Annotations

