---
Authors: Jeongjun Choi; Dongseok Shim; H. Jin Kim
Date: 2022-12-08
Topics: DM+HPE
DOI: 10.48550/arXiv.2212.02796
Keywords:
---
tags: #论文笔记 

## Zotero Links 
* PDF Attachments
	- [arXiv Fulltext PDF](zotero://open-pdf/library/items/YP3AHQMF) 
* [Local library](zotero://select/items/1_BPMRIXGV) 

## Abstract

Thanks to the development of 2D keypoint detectors, monocular 3D human pose estimation (HPE) via 2D-to-3D uplifting approaches have achieved remarkable improvements. Still, monocular 3D HPE is a challenging problem due to the inherent depth ambiguities and occlusions. To handle this problem, many previous works exploit temporal information to mitigate such difficulties. However, there are many real-world applications where frame sequences are not accessible. This paper focuses on reconstructing a 3D pose from a single 2D keypoint detection. Rather than exploiting temporal information, we alleviate the depth ambiguity by generating multiple 3D pose candidates which can be mapped to an identical 2D keypoint. We build a novel diffusion-based framework to effectively sample diverse 3D poses from an off-the-shelf 2D detector. By considering the correlation between human joints by replacing the conventional denoising U-Net with graph convolutional network, our approach accomplishes further performance improvements. We evaluate our method on the widely adopted Human3.6M and HumanEva-I datasets. Comprehensive experiments are conducted to prove the efficacy of the proposed method, and they confirm that our model outperforms state-of-the-art multi-hypothesis 3D HPE methods.

## Summary
写完笔记之后最后填，概述文章的内容，以后查阅笔记的时候先看这一段。 
注：写文章summary切记需要通过自己的思考，用自己的语言描述。忌讳直接ctrl+c原文。


## Research Objective(s)
作者的研究目标是什么


## Background / Problem Statement
研究的背景以及问题陈述：作者需要解决的问题是什么？


## Method(s)
作者解决问题的方法/算法是什么？是否基于前人的方法？基于了哪些？


## Experiment(s)
  数据集（和 [[A generic diffusion - based approach for 3D human pose prediction in the wild]] 相同，可以对比一下）
  - Human3.6M
  - HumanEva-I


## Conclusion
作者给出了哪些结论？哪些是strong conclusions，哪些又是weak的conclusions（即作者并没有通过实验提供evidence，只在discussion中提到；或实验的数据并没有给出充分的evidence）？


## Notes
(optional)不在以上列表中，但需要特别记录的笔记。


## References
(optional)列出相关性高的文献，以便之后可以继续track下去。