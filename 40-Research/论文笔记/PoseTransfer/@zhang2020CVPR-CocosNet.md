---
Authors: Pan Zhang; Bo Zhang; Dong Chen; Lu Yuan; Fang Wen
Date: 2020-04-12
Topics: CPIS
DOI: 10.48550/arXiv.2004.05571
Keywords: transferring based on correlation matrix
---
tags: #论文笔记 

# Cross-domain Correspondence Learning for Exemplar-based Image Translation

基于范例(exempler-based)的精细可控图像翻译


## Abstract
We present a general framework for exemplar-based image translation, which synthesizes a photo-realistic image from the input in a distinct domain (e.g., semantic segmentation mask, or edge map, or pose keypoints), given an exemplar image. The output has the style (e.g., color, texture) in consistency with the semantically corresponding objects in the exemplar. We propose to jointly learn the crossdomain correspondence and the image translation, where both tasks facilitate each other and thus can be learned with weak supervision. The images from distinct domains are first aligned to an intermediate domain where dense correspondence is established. Then, the network synthesizes images based on the appearance of semantically corresponding patches in the exemplar. We demonstrate the effectiveness of our approach in several image translation tasks. Our method is superior to state-of-the-art methods in terms of image quality significantly, with the image style faithful to the exemplar with semantic consistency. Moreover, we show the utility of our method for several applications

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2004.05571)
- **zotero entry**: [Zotero](zotero://select/library/items/7UAQ3FTA)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/ZGQUKUVJ); [Zhang et al_2020_Cross-domain Correspondence Learning for Exemplar-based Image Translation.pdf](zotero://open-pdf/library/items/66H2WDLW)

## Comments
Comment: Accepted as a CVPR 2020 oral paper

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement
![[Pasted image 20240112173722.png]]

### 跨域对应（cross-domain correspondence）子网络

其用于找到输入 x_A 与范例 y_B 之间的密集对应。然而，与一般的语义对应方法（如 SFNet [2]）不同的是，这两种输入来自于不同的域——如图3中 x_A 是语义分割，y_B 是一张自然室内场景，而我们无法用预先训练的分类特征提取器（如 pretrained VGG/ResNet）来提取两种输入的特征。

于是，我们想到利用训练集中 x_A 和它在目标域的配对 x_B，来训练两个域的特征提取器 （F_(A→B) 和 F_(B→A)），使得他们提取到的特征可以适应到一个对齐的隐空间，我们定义域自适应损失函数为：

![[Pasted image 20240112173838.png|375]]




### 图像转换子网络（translation network）

这个网络尝试从输入 x_A 和与它对齐的范例 r_(y→x) 生成最终图像。这里我们采用改进的空间自适应去正则化层（spatially-variant denormalization layer）[3]：利用简单变换将 x_A 和 r_(y→x) 映射为正则化层的调制系数，通过调制正则化层来实现对生成图片的风格调制。这也类似于 StyleGAN [[@men2020CVPR-ADGAN]] 利用条件正则化层（BN）来改变生成风格，而我们做法区别在于，条件输入 x_A 和 r_(y→x) 为二维图像，正则化统计量（μ_(h,w)，σ_(h,w)）、去正则化系数（α_(h,w)，β_(h,w)）都是空间自适应的：

![[Pasted image 20240112174048.png|450]]



==什么是空间自适应？==

空间自适应在我们的任务中非常重要，它有助于将范例图像中的风格精细迁移到最终生成图片中，且通过反传，前面的跨域对应子模块能学到精细的语义对应。


为了学到正确的对应关系，我们对输出图像施加以下约束。**1）特征匹配损失（perceptual loss）**：输出图像必须符合输入图片的语义约束，因此，我们要求它们经过预训练 VGG19 后的高层特征——Relu4-2层——应保持一致；2）上下文损失（contextual loss）[5]：输出图像应和范例图的对应物体风格相一致，为此我们在 VGG19 的低层特征图（Relu2-1, …. Relu5-2，更多的包含颜色，纹理信息）上匹配二者的统计分布。3) 对抗损失函数（adversarial loss）：我们联合训练判别器 D，使得最终的输出图片难以与真实图片区分开来；4）特征匹配（feature matching）：我们将 x_B 做形变增强，构造为 x_A 的伪范例，这样的伪范例对（pseudo exemplar pair）的输出应能完美重建 x_B，这里我们采用 VGG 特征匹配损失函数。

综上，总的训练目标为：
![[Pasted image 20240112175927.png]]


```ad-note
title: VGGNet

在ALexNet上进行改进：

VGG16相比AlexNet的一个改进是**采用连续的几个3x3的卷积核代替AlexNet中的较大卷积核（11x11，7x7，5x5）**。对于给定的感受野（与输出有关的输入图片的局部大小），采用堆积的小卷积核是优于采用大的卷积核，因为多层非线性层可以增加网络深度来保证学习更复杂的模式，而且代价还比较小（参数更少）。

  

简单来说，在VGG中，使用了3个3x3卷积核来代替7x7卷积核，使用了2个3x3卷积核来代替5*5卷积核，这样做的主要目的是在保证具有相同感知野的条件下，提升了网络的深度，在一定程度上提升了神经网络的效果。

  

比如，3个步长为1的3x3卷积核的一层层叠加作用可看成一个大小为7的感受野（其实就表示3个3x3连续卷积相当于一个7x7卷积），其参数总量为 3x(9xC^2) ，如果直接使用7x7卷积核，其参数总量为 49xC^2 ，这里 C 指的是输入和输出的通道数。很明显，27xC^2小于49xC^2，即减少了参数；而且3x3卷积核有利于更好地保持图像性质。


```

![[Pasted image 20240112180924.png|375]]







## Method(s)


## Evaluation


## Conclusion


## Limitations

1. 由于一对多映射（第一行），我们的方法可能会产生混合颜色伪影。此外，在多对一映射的情况下，多个实例（图中的枕头）可以使用相同的样式（第2行）
![[Pasted image 20240112182149.png|500]]
2. 计算量
   另一个限制是相关矩阵的计算需要巨大的 GPU 内存，这使得我们的方法很难扩展到高分辨率图像。我们把这个问题的解决留到以后的工作中 [[@zhou2021CVPR-CocosnetV2]]



----

## Extracted Annotations

