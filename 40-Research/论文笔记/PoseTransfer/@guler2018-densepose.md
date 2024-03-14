---
Authors: Riza Alp Guler; Natalia Neverova; Iasonas Kokkinos
Date: 6/2018
Topics: 2D; HPE
DOI: 10.1109/CVPR.2018.00762
Keywords:
---
tags: #论文笔记 

# DensePose: Dense Human Pose Estimation in the Wild


## Abstract
In this work we establish dense correspondences between an RGB image and a surface-based representation of the human body, a task we refer to as dense human pose estimation. We gather dense correspondences for 50K persons appearing in the COCO dataset by introducing an efﬁcient annotation pipeline. We then use our dataset to train CNN-based systems that deliver dense correspondence ‘in the wild’, namely in the presence of background, occlusions and scale variations. We improve our training set’s effectiveness by training an inpainting network that can ﬁll in missing ground truth values and report improvements with respect to the best results that would be achievable in the past. We experiment with fully-convolutional networks and region-based models and observe a superiority of the latter. We further improve accuracy through cascading, obtaining a system that delivers highly-accurate results at multiple frames per second on a single gpu. Supplementary materials, data, code, and videos are provided on the project page http://densepose.org.

## Files and Links
- **Url**: [Open online](https://ieeexplore.ieee.org/document/8578860/)
- **zotero entry**: [Zotero](zotero://select/library/items/UEEEI82Q)
- **open pdf**: [Guler 等 - 2018 - DensePose Dense Human Pose Estimation in the Wild.pdf](zotero://open-pdf/library/items/3MDM5VS8)

## Comments


---

## Summary

  
## Research Objective(s)
1. 密集姿态估计densepose estimation
密集姿态估计 (dense pose estimation) 将单张 2D 图片中所有描述人体的像素（human pixels），映射到一个 3D 的人体表面模型。如图 1 所示，Facebook 发布了一个名为 DensePose COCO 的大型数据集，包含了预先手工标注的 5 万张各种人类动作的图片
![[Pasted image 20231228195531.png]]
图 1：密集姿态估计的目标是将 2D 图片中描述人体的像素，==映射==到一个 3D 表面模型。左：输入的原始图像，以及利用 [1] 中提出的 Dense Pose-RCNN，获得人体各区域的 UV 坐标。UV 坐标又称纹理坐标 (texture coordinates), 用于控制 3D 表面的纹理==映射==； 中：DensePose COCO 数据集中的原始标注；右：人体表面的分割以及 UV ==参数==化示意图。_

## Background / Problem Statement


## Method(s)


## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

