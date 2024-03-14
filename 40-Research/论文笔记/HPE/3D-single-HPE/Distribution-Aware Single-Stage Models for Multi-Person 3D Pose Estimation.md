---
Authors: Zitian Wang, Xuecheng Nie, Xiaochao Qu, Yunpeng Chen, Si Liu
Date: 2022-03-22
Topics: HPE
Keywords: 一次网络前向推理; 同时获取3D空间人体位置信息及相应关键点信息;
---
tags: #论文笔记 

## Zotero Links 
* PDF Attachments
	- [arXiv Fulltext PDF](zotero://open-pdf/library/items/RUZ3YVW7) 
* [Local library](zotero://select/items/1_N5DXTNEE) 

## Abstract

In this paper, we present a novel Distribution-Aware Single-stage (DAS) model for tackling the challenging multi-person 3D pose estimation problem. Different from existing top-down and bottom-up methods, the proposed DAS model simultaneously localizes person positions and their corresponding body joints in the 3D camera space in a one-pass manner. This leads to a simplified pipeline with enhanced efficiency. In addition, DAS learns the true distribution of body joints for the regression of their positions, rather than making a simple Laplacian or Gaussian assumption as previous works. This provides valuable priors for model prediction and thus boosts the regression-based scheme to achieve competitive performance with volumetric-base ones. Moreover, DAS exploits a recursive update strategy for progressively approaching to regression target, alleviating the optimization difficulty and further lifting the regression performance. DAS is implemented with a fully Convolutional Neural Network and end-to-end learnable. Comprehensive experiments on benchmarks CMU Panoptic and MuPoTS-3D demonstrate the superior efficiency of the proposed DAS model, specifically 1.5x speedup over previous best model, and its stat-of-the-art accuracy for multi-person 3D pose estimation.


## Summary
写完笔记之后最后填，概述文章的内容，以后查阅笔记的时候先看这一段。 
注：写文章summary切记需要通过自己的思考，用自己的语言描述。忌讳直接ctrl+c原文。


## Conclusion
在本论文中，来自美图和北航的研究者们创新性地提出了一种分布感知式单阶段模型，用于解决极具挑战性的多人3D人体姿态估计问题。与已有的自顶向下和自底向上这种两阶段模型相比，该模型可以通过一次网络前向推理同时获取人体位置信息以及所对应的人体关键点位置信息，从而有效地简化预测流程，同时克服了已有方法在高计算成本和高模型复杂度方面的弊端。另外，该方法成功将标准化流引进到多人3D人体姿态估计任务中以在训练过程中学习人体关键点分布，并提出迭代回归策略以缓解分布学习难度来达到逐步逼近目标的目的。通过这样一种方式，该算法可以获取数据的真实分布以有效地提升模型的回归预测精度。


## Background / Problem Statement
   目前，通常采用两阶段方法来解决该问题：自顶向下方法，即先检测图片多个人体的位置，之后对检测到的每个人使用单人3D 姿态估计模型来分别预测其姿态；自底向上方法，即先检测图片中所有人的3D 关键点，之后通过相关性将这些关键点分配给对应的人体。
  
  尽管两阶段方法取得了良好的精度，但是需要通过冗余的计算和复杂的后处理来顺序性地获取人体位置信息和关键点位置信息，这使得速率通常难以满足实际场景的部署需求，因此多人3D姿态估计算法流程亟需简化。另一方面，在缺少数据分布先验知识的情况下，从单张RGB图片中估计3D关键点位置，特别是**深度信息**，是一个病态问题。这使得传统的应用于2D场景的单阶段模型无法直接向3D场景进行扩展，因此学习并获取3D关键点的数据分布是进行高精度多人3D人体姿态估计的关键所在。

## Method(s)
1. **单阶段多人3D姿态估计模型**
    DAS 模型基于回归预测框架来构建，对于给定图片，DAS 模型通过一次前向预测输出图片中所包含人物的3D 人体姿态。DAS 模型将人体中心点表示为中心点置信度图和中心点坐标图两部分，如图1 (a) 和 (b) 所示，其中，DAS 模型使用中心点置信度图来定位2D 图片坐标系中人体投影中心点的位置，而使用中心点坐标图来预测3D 相机坐标系内人体中心点的绝对位置。DAS 模型将人体关键点建模为关键点偏移图，如图1 (c) 所示。
  
    DAS 模型将中心点置信度图建模为二值图，图中每个像素点表示人体中心点是否在该位置出现，如果出现则为1，否则为0。DAS 模型将中心点坐标图以稠密图的方式进行建模，图中每个像素点编码了出现在该位置的人物中心在 x、y 和 z 方向的坐标。关键点偏移图和中心点坐标图建模方式类似，图中每个像素点编码了出现在该位置的人体关键点相对于人体中心点在 x、y、z 方向的偏移量。DAS 模型可以在网络前向过程中以并行的方式输出以上三种信息图，从而避免了冗余计算。

![[Pasted image 20230305214931.png]]

2. 分布感知学习模型
    对于回归预测框架的优化，已有工作多采用传统的 L1或者 L2损失函数，但研究发现这类监督训练实际上是在假设人体关键点的数据分布满足拉普拉斯分布或者高斯分布的前提下进行的模型优化[12]。然而在实际场景中，人体关键点的真实分布极为复杂，以上简单的假设与真实分布相距甚远。与现有方法不同，DAS 模型在优化过程中学习3D 人体关键点分布的真实分布，指导关键点回归预测的过程。考虑到真实分布不可追踪的问题，DAS 模型利用标准化流（Normalizing Flow）来达到对于模型预测结果概率估计的目标，以生成适合模型输出的分布，如图2所示。该分布感知模块可以同关键点预测模块一起在训练过程中通过最大似然估计的方法进行学习，完成学习之后，该分布感知模块会在预测过程中进行移除，这样一种分布感知式算法可以在不增加额外计算量的同时提升回归预测模型的精度。此外，用于人体关键点预测的特征提取于人体中心点处，这一特征对于远离中心点的人体关键点来说表示能力较弱，和目标在空间上的不一致问题会引起预测的较大误差。为了缓和这一问题，该算法提出了迭代更新策略，该策略利用历史更新结果为出发点，并整合中间结果附近预测值以逐步逼近最终目标，如图3所示。
   ![[Pasted image 20230305215559.png]]
   
