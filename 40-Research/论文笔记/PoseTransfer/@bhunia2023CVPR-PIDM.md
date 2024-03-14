---
Authors: Ankan Kumar Bhunia; Salman Khan; Hisham Cholakkal; Rao Muhammad Anwer; Jorma Laaksonen; Mubarak Shah; Fahad Shahbaz Khan
Date: 2023-02-28
Topics: CPIS; pose-transfer
DOI: 10.48550/arXiv.2211.12500
Keywords: 纹理扩散块：将所需的纹理模式注入到人体姿势迁移的去噪中
---
tags: #论文笔记 

# Person Image Synthesis via Denoising Diffusion Model


## Abstract
The pose-guided person image generation task requires synthesizing photorealistic images of humans in arbitrary poses. The existing approaches use generative adversarial networks that do not necessarily maintain realistic textures or need dense correspondences that struggle to handle complex deformations and severe occlusions. In this work, we show how denoising diffusion models can be applied for high-fidelity person image synthesis with strong sample diversity and enhanced mode coverage of the learnt data distribution. Our proposed Person Image Diffusion Model (PIDM) disintegrates the complex transfer problem into a series of simpler forward-backward denoising steps. This helps in learning plausible source-to-target transformation trajectories that result in faithful textures and undistorted appearance details. We introduce a 'texture diffusion module' based on cross-attention to accurately model the correspondences between appearance and pose information available in source and target images. Further, we propose 'disentangled classifier-free guidance' to ensure close resemblance between the conditional inputs and the synthesized output in terms of both pose and appearance information. Our extensive results on two large-scale benchmarks and a user study demonstrate the photorealism of our proposed approach under challenging scenarios. We also show how our generated images can help in downstream tasks. Our code and models will be publicly released.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2211.12500)
- **zotero entry**: [Zotero](zotero://select/library/items/UJ6GU9CZ)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/H9FEW9CV); [Bhunia et al_2023_Person Image Synthesis via Denoising Diffusion Model.pdf](zotero://open-pdf/library/items/LMZDI5J7)
- code：开源
## Comments
Comment: Accepted to CVPR 2023

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)


![[Pasted image 20240116131627.png]]


损失函数

![[Pasted image 20240116131703.png|475]]
![[Pasted image 20240116131712.png|217]]

## Evaluation
![[Pasted image 20240117144939.png]]

## Conclusion


## Notes


----

## Extracted Annotations

