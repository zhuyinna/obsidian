---
 Authors: Matthew Loper, Naureen Mahmood, Javier Romero, Gerard Pons-Moll, Michael J. Black
 Date: 2015-11
 Date Added: 2023-03-05
 Topics: 3Dmesh
 Keywords: 
---
tags: #论文笔记 

## Metadata
 Authors: "[[Matthew Loper]], [[Naureen Mahmood]], [[Javier Romero]], [[Gerard Pons-Moll]], [[Michael J. Black]]"
 Date: [[2015-11-04]] 
 Date Added: [[2023-03-05]] 
 Topics: "[[3Dmesh]]"
 URL: [https://dl.acm.org/doi/10.1145/2816795.2818013](https://dl.acm.org/doi/10.1145/2816795.2818013)

## Zotero Links 
 PDF Attachments
	- [Loper 等 - 2015 - SMPL a skinned multi-person linear model.pdf](zotero://open-pdf/library/items/JBXHCELF) 
 [Local library](zotero://select/items/1_UH2NJ384) 

## Abstract

We present a learned model of human body shape and posedependent shape variation that is more accurate than previous models and is compatible with existing graphics pipelines. Our Skinned Multi-Person Linear model (SMPL) is a skinned vertexbased model that accurately represents a wide variety of body shapes in natural human poses. The parameters of the model are learned from data including the rest pose template, blend weights, pose-dependent blend shapes, identity-dependent blend shapes, and a regressor from vertices to joint locations. Unlike previous models, the pose-dependent blend shapes are a linear function of the elements of the pose rotation matrices. This simple formulation enables training the entire model from a relatively large number of aligned 3D meshes of different people in different poses. We quantitatively evaluate variants of SMPL using linear or dual-quaternion blend skinning and show that both are more accurate than a BlendSCAPE model trained on the same data. We also extend SMPL to realistically model dynamic soft-tissue deformations. Because it is based on blend skinning, SMPL is compatible with existing rendering engines and we make it available for research purposes.

![[Pasted image 20230318214455.png]] 


## Summary
写完笔记之后最后填，概述文章的内容，以后查阅笔记的时候先看这一段。 
注：写文章summary切记需要通过自己的思考，用自己的语言描述。忌讳直接ctrl+c原文。


## Conclusion
作者给出了哪些结论？哪些是 strong conclusions，哪些又是 weak 的 conclusions（即作者并没有通过实验提供 evidence，只在 discussion 中提到；或实验的数据并没有给出充分的 evidence）？


## Research Objective(s)
作者的研究目标是什么


## Background / Problem Statement
研究的背景以及问题陈述：作者需要解决的问题是什么？


## Method(s)
  SMPL 的总体模型，这个模型是通过训练得到，就是一些参数，该模型中β和θ是其中的输入参数，其中β代表人体高矮胖瘦、头身比等比例的10个参数，θ是代表人体整体运动位姿和24个关节相对角度的75(24\*3+3;每个关节点3个自由度，再加上3个根节点)个参数，β参数是 ShapeBlendPose 参数，可以通过10个增量模板控制人体形状变化： 具体而言：每个参数控制人体形态的变化可以通过动图来刻画。


## Experiment(s)
作者如何评估自己的方法？实验的setup是什么样的？感兴趣实验数据和结果有哪些？有没有问题或者可以借鉴的地方？


## Notes
(optional)不在以上列表中，但需要特别记录的笔记。


## References
(optional)列出相关性高的文献，以便之后可以继续track下去。