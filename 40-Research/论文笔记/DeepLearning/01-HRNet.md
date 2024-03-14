# HRNet
tags:  #深度学习

## paper
[arXiv Fulltext PDF](zotero://open-pdf/library/items/FBUA3ZST)

![[Pasted image 20230301151053.png|500]]

## Abstract
现有的最先进的框架首先通过串联连接高分辨率到低分辨率卷积形成的子网络将输入图像编码为低分辨率表示（例如，ResNet，VGGNet），然后恢复高分辨率- 来自编码低分辨率表示的分辨率表示。相反，我们提出的名为高分辨率网络 (HRNet) 的网络在整个过程中保持高分辨率表示。

## Network
### Parallel Multi-Resolution Convolutions
### Repeated Multi-Resolution Fusions
![[Pasted image 20230301152501.png|400]]   
### Representation Head
![[Pasted image 20230301204924.png|525]]
HRNetV1：HPE
HRNetV2：semantic segmentation
HRNetV2p：object detection

### Analysis
![[Pasted image 20230301203631.png|400]]
多分辨率并行卷积类似于组卷积，将输入通道划分为多个通道子集，并在不同子集上进行常规卷积（而组卷积中分辨率是相同的）。意味着，多分辨率并行卷积存在组卷积的一些优势。

## HPE application 
![[Pasted image 20230301205152.png|400]]


