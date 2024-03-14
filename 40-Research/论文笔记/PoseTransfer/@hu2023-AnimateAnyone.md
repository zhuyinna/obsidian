---
Authors: Li Hu; Xin Gao; Peng Zhang; Ke Sun; Bang Zhang; Liefeng Bo
Date: 2023-12-06
Topics: pose-transfer
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# Animate Anyone: Consistent and Controllable Image-to-Video Synthesis for Character Animation


## Abstract
Character Animation aims to generating character videos from still images through driving signals. Currently, diffusion models have become the mainstream in visual generation research, owing to their robust generative capabilities. However, challenges persist in the realm of image-to-video, especially in character animation, where temporally maintaining consistency with detailed information from character remains a formidable problem. In this paper, we leverage the power of diffusion models and propose a novel framework tailored for character animation. To preserve consistency of intricate appearance features from reference image, we design ReferenceNet to merge detail features via spatial attention. To ensure controllability and continuity, we introduce an efficient pose guider to direct character's movements and employ an effective temporal modeling approach to ensure smooth inter-frame transitions between video frames. By expanding the training data, our approach can animate arbitrary characters, yielding superior results in character animation compared to other image-to-video methods. Furthermore, we evaluate our method on benchmarks for fashion video and human dance synthesis, achieving state-of-the-art results.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2311.17117)
- **zotero entry**: [Zotero](zotero://select/library/items/F3SE7VMY)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/3DXAUD7X); [Hu et al_2023_Animate Anyone.pdf](zotero://open-pdf/library/items/AFVJB5BR)

## Comments
Comment: Page: https://humanaigc.github.io/animate-anyone/

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)

姿势序列最初使用 Pose Guider 进行编码，并与多帧噪声融合，然后由 Denoising UNet 进行视频生成的去噪过程。 Denoising UNet 的计算模块由 Spatial-Attention、Cross-Attention 和 Temporal-Attention 组成，如右侧虚线框所示。参考图像的集成涉及两个方面。首先，通过ReferenceNet提取详细特征并用于空间注意力。其次，通过CLIP图像编码器提取语义特征进行交叉注意力。时间注意力在时间维度上运作。最后，VAE解码器将结果解码为视频剪辑。

![[Pasted image 20240116161114.png]]
## Evaluation

![[Pasted image 20240116161304.png|500]]

![[Pasted image 20240116161313.png|500]]
## Conclusion


## Notes


----

## Extracted Annotations

