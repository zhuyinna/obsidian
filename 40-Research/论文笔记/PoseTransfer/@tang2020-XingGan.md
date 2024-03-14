---
Authors: Hao Tang; Song Bai; Li Zhang; Philip H. S. Torr; Nicu Sebe
Date: 2020-07-17
Topics: pose-transfer
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# XingGAN for Person Image Generation


## Abstract
We propose a novel Generative Adversarial Network (XingGAN or CrossingGAN) for person image generation tasks, i.e., translating the pose of a given person to a desired one. The proposed Xing generator consists of two generation branches that model the person's appearance and shape information, respectively. Moreover, we propose two novel blocks to effectively transfer and update the person's shape and appearance embeddings in a crossing way to mutually improve each other, which has not been considered by any other existing GAN-based image generation work. Extensive experiments on two challenging datasets, i.e., Market-1501 and DeepFashion, demonstrate that the proposed XingGAN advances the state-of-the-art performance both in terms of objective quantitative scores and subjective visual realness. The source code and trained models are available at https://github.com/Ha0Tang/XingGAN.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2007.09278)
- **zotero entry**: [Zotero](zotero://select/library/items/S4HIVV8P)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/VCRC37SR); [Tang et al_2020_XingGAN for Person Image Generation.pdf](zotero://open-pdf/library/items/YWK847Z7)

## Comments
Comment: Accepted to ECCV 2020, camera ready (16 pages) + supplementary (6 pages)

---

## Summary

- 问题：人物图像生成。
- 方法：提出了一种新颖的生成对抗网络（Xing-GAN或CrossingGAN）来完成人物图像生成任务，即将给定的人的姿势转换为期望的姿势。所提出的Xing生成器由两个生成分支组成，分别对人的外貌和形状信息进行建模。此外，提出了两个新的blocks，以交叉的方式有效地转移和更新人的形状和外观嵌入，以相互改进，这是任何现有的基于GAN的图像生成工作所没有考虑的。
## Research Objective(s)

1. 提出了一种新颖的XingGAN（或CrossingGAN）来生成人像。 它探索了两个不同代分支的级联指导，并旨在根据人的形状和外观嵌入逐步生成更详细的综合信息；
2. 提出了SA和AS块，它们以交叉的方式有效地传递和更新人的形状和外观特征，以相互促进，并能够显着提高最终输出的质量；
3. 大量实验清楚地证明了XingGAN的有效性，并在两个具有挑战性的数据集（即Market-1501 和DeepFashion ）上显示了最新的技术成果。

## Background / Problem Statement


## Method(s)
![[Pasted image 20240115135615.png]]

形态引导下外观生成分支（SA branch）： 以一个SA块为例，输入为外观编码特征以及来自AS模块的形态编码特征。关键点在于其中的Softmax layer，能够确定形态特征上的点与外观特征上的点的对应关系，进而确定外观与形态之间的关联。此外，加入了上一SA模块的输出，减少特征的突变。
![[Pasted image 20240115135627.png]]


外观引导下形态生成分支（AS branch）：关键点还是在于外观特征与形态特征之间的关联性
![[Pasted image 20240115135637.png]]


共注意力融合模块（CAF model）：借鉴文献[1]SelectionGAN的做法。 将最终的外观编码与形态编码分别生成N个 中间图像，接着，再利用上述编码特征生成2N+1个共注意力图，最后，利用中间图像和共注意力图生成最终的图像

![[Pasted image 20240115135833.png|450]]



## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

