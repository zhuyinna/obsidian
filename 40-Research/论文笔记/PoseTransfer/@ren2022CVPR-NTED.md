---
Authors: Yurui Ren; Xiaoqing Fan; Ge Li; Shan Liu; Thomas H. Li
Date: 2022-04-12
Topics: CPIS
DOI: 10.48550/arXiv.2204.06160
Keywords: Attention mechanism with StyleGan-generator
---
tags: #论文笔记 

# Neural Texture Extraction and Distribution for Controllable Person Image Synthesis


## Abstract
We deal with the controllable person image synthesis task which aims to re-render a human from a reference image with explicit control over body pose and appearance. Observing that person images are highly structured, we propose to generate desired images by extracting and distributing semantic entities of reference images. To achieve this goal, a neural texture extraction and distribution operation based on double attention is described. This operation first extracts semantic neural textures from reference feature maps. Then, it distributes the extracted neural textures according to the spatial distributions learned from target poses. Our model is trained to predict human images in arbitrary poses, which encourages it to extract disentangled and expressive neural textures representing the appearance of different semantic entities. The disentangled representation further enables explicit appearance control. Neural textures of different reference images can be fused to control the appearance of the interested areas. Experimental comparisons show the superiority of the proposed model. Code is available at https://github.com/RenYurui/Neural-Texture-Extraction-Distribution.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2204.06160)
- **zotero entry**: [Zotero](zotero://select/library/items/SPR6WEVU)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/USA43AT4); [Ren et al_2022_Neural Texture Extraction and Distribution for Controllable Person Image.pdf](zotero://open-pdf/library/items/E7XEEU3B)

## Comments


---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)

我们知道Pose-guided Person Image Synthesis其实就是希望将source图像的texture“填”到pose上面去，但是先前很多工作都是两眼一闭，将两个图像扔到网络中，做注意力机制学到这样“填空”的方法。但是这篇文章不一样！作者自己设计了一个“neural texture extraction and distribution operation”，来让网络学到“neural texture”和它的distribution，通过较为显式的方法进行填补。这样的方法能让我们不要摸黑地做纹理转换，也能有效可视化网络学到了什么。

我们先看看NTED(neural texture extraction and distribution operation)具体是怎么做的！
![[Pasted image 20240110222543.png]]
![[Pasted image 20240110222614.png|475]]

![[Pasted image 20240110222624.png|500]]

![[Pasted image 20240110222637.png|475]]


比如上图， k 取值仍然为5，但是网络自己就学到了5个不同的texture（头发，背景，上衣，下装，皮肤）。

最后我们再看一看网络总体结构：

![[Pasted image 20240110222650.png]]

其实就是一个常见的多尺度结构，最后的The Target Image Renderer其实也是使用的StyleGAN-2的结构。


## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

