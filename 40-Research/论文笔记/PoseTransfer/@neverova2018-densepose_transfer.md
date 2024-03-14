---
Authors: Natalia Neverova; Rıza Alp Güler; Iasonas Kokkinos
Date: "2018"
Topics: CPIS
DOI:
  "{ DOI }": 
Keywords:
---
tags: #论文笔记 

# Dense Pose Transfer


## Abstract
In this work we integrate ideas from surface-based modeling with neural synthesis: we propose a combination of surface-based pose estimation and deep generative models that allows us to perform accurate pose transfer, i.e. synthesize a new image of a person based on a single image of that person and the image of a pose donor. We use a dense pose estimation system that maps pixels from both images to a common surface-based coordinate system, allowing the two images to be brought in correspondence with each other. We inpaint and reﬁne the source image intensities in the surface coordinate system, prior to warping them onto the target pose. These predictions are fused with those of a convolutional predictive module through a neural synthesis module allowing for training the whole pipeline jointly end-to-end, optimizing a combination of adversarial and perceptual losses. We show that dense pose estimation is a substantially more powerful conditioning input than landmark-, or mask-based alternatives, and report systematic improvements over state of the art generators on DeepFashion and MVC datasets.

## Files and Links
- **Url**: [Open online](https://link.springer.com/10.1007/978-3-030-01219-9_8)
- **zotero entry**: [Zotero](zotero://select/library/items/TQNJISAB)
- **open pdf**: [Neverova 等 - 2018 - Dense Pose Transfer.pdf](zotero://open-pdf/library/items/6SAJ9GAG)

## Comments
神经场作为输入，而不是heatmap或者sketlon，所以暂时不细看了。

---

## Summary
0. Facebook 和 Inria France 的研究人员分别在 CVPR 2018 和 ECCV 2018 相继发表了两篇有关「人体姿态估计」(human pose estimation) 的文章 [1] [2]，用于介绍他们提出的 Dense Pose 系统以及一个应用场景「密集姿态转移」（dense pose transfer）。DensePose见[[@guler2018-densepose]]
1. 该篇论文中将基于表面模型的姿态估计方法（surface-based pose estimation）和深度生成模型（deep generative model）结合起来，提出了精确的姿态转化（pose transfer）方法。该方法利用SMPL模型和DensePose system，通过基于表面的神经合成（neural synthesis），渲染new pose的人物模型，从而生成pose-transfered图像
2. 

## Relative work
### 1. Deep generative models
生成模型（Generative Model）是相对于判别模型（Discriminative Model）定义的。他们两个都用于有监督学习：

- 判别模型主要是根据原始图像推测图像具备的一些性质，例如根据数字图像推测数字的名称，根据自然场景图像推测物体的边界；
- 生成模型通常给出的输入是图像具备的性质，而输出是性质对应的图像。这种生成模型相当于构建了图像的分布，因此利用这类模型可以完成图像自动生成（采样）、图像信息补全等工作。

Deep generative models表示的是基于深度学习的生成模型，常用作一种无监督的特征学习的方法。

### 2.Image inpainting
图像补全(image inpainting)就是还原图像中缺失的部分。基于图像中已有信息，去还原图像中的缺失部分。这项技术可以帮助估测被遮挡的部分的模样，通常使用生成模型来补全信息

### 3. STN
空间变换网络（Spatial Transformer Net，STN）让网络明确地利用了数据的空间信息，可以在网络中对数据进行空间变换操作。这种可导的模块可以插入到现有的卷积结构中，赋予网络在不需要额外训练监督或者修改优化过程的情况下，基于特征图（feature map）本身进行空间变换的能力。

ST的结构分成三部分，分别为Localisation Net, Grid Generator和Sampler，它完成的是一个将输入特征图进行一定的变换的过程，而具体如何变换，是通过在训练过程中学习来的。更通俗地讲，该模块在训练阶段学习如何对输入数据进行变换更有益于模型的分类，然后在测试阶段应用已经训练好的网络对输入数据进行执行相应的变换，从而提高模型的识别率。
![[Pasted image 20231228211820.png|500]]


## Background / Problem Statement


## Method(s)
如图 5 所示，DPT 系统以 Dense Pose[1] 为基础，并且由两个互补的模块组成，分别是（1）推测模块 (predictive module)，用于根据输入图像，预测出具有目标姿态的人体图像；【从而提供了优于稀疏的、基于路标的条件所获得的结果superior results to those ==obtained from sparse, landmark-based conditioning;==】（2）变形模块 (warping module)，负责从输入图像中提取纹理，并「补全」(inpainting) 具有目标姿态的人体表面纹理。此外，系统中还有一个合成模块 (blending module)，通过端对端、可训练的单一框架，将推测和变形模块的输出进行合成，并产生最终的图像。
![[Pasted image 20231228195930.png]]
### predictive module
其余的架构包括一个编码器，后面是一堆残差块，最后是一个解码器，沿着[28]的思路。更详细地说，该网络包含（a）三个卷积层的级联，将 256×256×9 输入编码为 64×64×256 激活，（b）一组具有 3×3×256×256 的六个残差块内核，(c) 两个反卷积层和一个卷积层的级联，提供与输入相同空间分辨率的输出。所有中间卷积层都有 3×3 滤波器，然后是实例归一化 [36] 和 ReLU 激活。最后一层具有 tanh 非线性并且没有归一化。

### warping module
![[Pasted image 20231228205849.png]]
上图：扭曲流上姿态传输的监督信号：左侧的输入图像通过 DensePose 驱动的空间变换器网络扭曲到固有表面坐标。根据此输入，修复自动编码器必须从不同的角度预测同一个人的外观，同时也扭曲到内在坐标。右侧的损失函数仅对纹理图的观察部分的重建进行惩罚。这种形式的多视图监督就像人全身表面（不可用）外观的替代品。

我们的变形模块通过在公共表面 UV 系统上的输入图像和目标图像之间执行显式纹理映射来执行姿态转换。该组件的核心是空间变换网络（STN），它根据 DensePose 将图像观察结果扭曲到每个表面部分的 UV 坐标系；我们对 24 个表面部分中的每一个使用具有 256×256 UV 点的网格，并执行分散插值来处理回归 UV 坐标的连续值。从 UV 到输出图像空间的逆映射由具有双线性内核的第二个 STN 执行。如图 3 所示，直接实现该模块通常会产生较差的结果：源图像上可见的表面部分通常很小，并且通常与身体的部分完全不重叠。在目标图像上可见。这种情况只会因 DensePose 故障或零件接缝周围的系统错误而加剧。这些问题促使在变形模块中使用修复网络，如下所述。




## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

