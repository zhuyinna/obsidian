---
Authors: Yifang Men; Yiming Mao; Yuning Jiang; Wei-Ying Ma; Zhouhui Lian
Date: 2020-07-19
Topics: CPIS
DOI: 10.48550/arXiv.2003.12267
Keywords: Extracting style vector to guide pose transfer
---
	tags: #论文笔记 

# Controllable Person Image Synthesis with Attribute-Decomposed GAN


## Abstract
This paper introduces the Attribute-Decomposed GAN, a novel generative model for controllable person image synthesis, which can produce realistic person images with desired human attributes (e.g., pose, head, upper clothes and pants) provided in various source inputs. The core idea of the proposed model is to embed human attributes into the latent space as independent codes and thus achieve flexible and continuous control of attributes via mixing and interpolation operations in explicit style representations. Specifically, a new architecture consisting of two encoding pathways with style block connections is proposed to decompose the original hard mapping into multiple more accessible subtasks. In source pathway, we further extract component layouts with an off-the-shelf human parser and feed them into a shared global texture encoder for decomposed latent codes. This strategy allows for the synthesis of more realistic output images and automatic separation of un-annotated attributes. Experimental results demonstrate the proposed method's superiority over the state of the art in pose transfer and its effectiveness in the brand-new task of component attribute transfer.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2003.12267)
- **zotero entry**: [Zotero](zotero://select/library/items/GW93SFBV)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/LTCPXCEH); [Men et al_2020_Controllable Person Image Synthesis with Attribute-Decomposed GAN.pdf](zotero://open-pdf/library/items/MAAGQWNT)

## Comments
Comment: Accepted by CVPR 2020 (Oral). Project Page: https://menyifang.github.io/projects/ADGAN/ADGAN.html

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement

### styleGAN

详细见[[11-GAN#StyleGAN]]


![[Pasted image 20240110214206.png|500]]

## Methods


在styleGAN基础上，处理原图像Is，作为w输入GANblock
![[Pasted image 20240110214621.png]]

ADGAN：解耦style属性---AD-GAN的结构确实和这个想法相似，但是关键在于处理最重要的 Is 的时候如何编码？AD-GAN就提出了“Attribute-Decomposed”的思想，设计了Decomposed Component Encoding (DCE)。具体来说，作者认为“人”不同的部位（如脸、衣服、手臂、裤子）需要解耦，才能让网络更好训练，更重要的是解耦之后能有效控制网络输出，如下图。
![[Pasted image 20240110215510.png]]

那如何将不同属性解耦？AD-GAN的方法很简单：那就用一个语义分割网络得到Human Parsing，再对分割出的不同属性得到一个Mask，和原图相乘就能得到一个只有这个属性有色彩，其他区域全黑的图像。再将这样的图像经过一个共享权重的编码器Global Texture Encoder（GTE），得到不同属性的特征向量，再进行concatenate即可。

![[Pasted image 20240110215602.png]]
注意这里还有一个魔鬼细节：因为身体各部分的编码是按特定顺序组件样式编码的，所有位置和部位特征之间有很高的相关性。这种很强的人为干预对网络的学习可能会带来影响。所以作者设计了一个Fusion Module（FM），使用3个全连接层来让网络自由选取特征，然后在最后一层输出我们需要的维度作为参数。

最后就是Global Texture Encoder（GTE）的设计：作者使用一个预训练好的VGG网络和待训练的网络打配合，因为预训练好的VGG见识过了各种各样的图片，对一些罕见的图像纹理有更好的感知能力，但因为我们的任务需要生成固定的、精准的结果，仅仅使用VGG是不足的，因此还要加上一个可学习的编码器来使模型适应复杂的情况。

![[Pasted image 20240110215630.png]]

## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

