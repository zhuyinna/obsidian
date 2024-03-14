---
 Authors: Zhihao Li, Jianzhuang Liu, Zhensong Zhang, Songcen Xu, Youliang Yan
 Date: 2022-09
 Date Added: 2023-03-13
 Topics: 3Dmesh
 Keywords: 
---
tags: #论文笔记 

## Metadata
 Authors: "[[Zhihao Li]], [[Jianzhuang Liu]], [[Zhensong Zhang]], [[Songcen Xu]], [[Youliang Yan]]"
 Date: [[2022-09-21]] 
 Date Added: [[2023-03-13]] 
 Topics: "[[3Dmesh]]"
 URL: [http://arxiv.org/abs/2208.00571](http://arxiv.org/abs/2208.00571)

## Zotero Links 
 
 [Local library](zotero://select/items/1_WTQ9UB7W) 

## Abstract

Top-down methods dominate the field of 3D human pose and shape estimation, because they are decoupled from human detection and allow researchers to focus on the core problem. However, cropping, their first step, discards the location information from the very beginning, which makes themselves unable to accurately predict the global rotation in the original camera coordinate system. To address this problem, we propose to Carry Location Information in Full Frames (CLIFF) into this task. Specifically, we feed more holistic features to CLIFF by concatenating the cropped-image feature with its bounding box information. We calculate the 2D reprojection loss with a broader view of the full frame, taking a projection process similar to that of the person projected in the image. Fed and supervised by global-location-aware information, CLIFF directly predicts the global rotation along with more accurate articulated poses. Besides, we propose a pseudo-ground-truth annotator based on CLIFF, which provides high-quality 3D annotations for in-the-wild 2D datasets and offers crucial full supervision for regression-based methods. Extensive experiments on popular benchmarks show that CLIFF outperforms prior arts by a significant margin, and reaches the first place on the AGORA leaderboard (the SMPL-Algorithms track). The code and data are available at https://github.com/huawei-noah/noah-research/tree/master/CLIFF.


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
作者解决问题的方法/算法是什么？是否基于前人的方法？基于了哪些？


## Experiment(s)
作者如何评估自己的方法？实验的setup是什么样的？感兴趣实验数据和结果有哪些？有没有问题或者可以借鉴的地方？


## Notes
(optional)不在以上列表中，但需要特别记录的笔记。


## References
(optional)列出相关性高的文献，以便之后可以继续track下去。