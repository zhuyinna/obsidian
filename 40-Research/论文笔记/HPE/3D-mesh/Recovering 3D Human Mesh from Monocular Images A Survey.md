---
Authors: Yating Tian, Hongwen Zhang, Yebin Liu, Limin Wang
Date: 2022-03
Topics: 3Dmesh
Keywords: 综述；
---
tags: #论文笔记 


## Zotero Links 
* PDF Attachments
	- [arXiv Fulltext PDF](zotero://open-pdf/library/items/VV899FQI) 
* [Local library](zotero://select/items/1_CU6B626X) 

## Abstract

Estimating human pose and shape from monocular images is a long-standing problem in computer vision. Since the release of statistical body models, 3D human mesh recovery has been drawing broader attention. With the same goal of obtaining well-aligned and physically plausible mesh results, two paradigms have been developed to overcome challenges in the 2D-to-3D lifting process: i) **an optimization-based paradigm**, where different data terms and regularization terms are exploited as optimization objectives; and ii) a regression-based paradigm, where deep learning techniques are embraced to solve the problem in an end-to-end fashion. Meanwhile, continuous efforts are devoted to improving the quality of 3D mesh labels for a wide range of datasets. Though remarkable progress has been achieved in the past decade, the task is still challenging due to flexible body motions, diverse appearances, complex environments, and insufficient in-the-wild annotations. To the best of our knowledge, this is the first survey to focus on the task of monocular 3D human mesh recovery. We start with the introduction of body models and then elaborate recovery frameworks and training objectives by providing in-depth analyses of their strengths and weaknesses. We also summarize datasets, evaluation metrics, and benchmark results. Open issues and future directions are discussed in the end, hoping to motivate researchers and facilitate their research in this area. A regularly updated project page can be found at https://github.com/tinatiansjz/hmr-survey.

## 2. Human Modeling
  内容： 在第2节中，我们简要介绍了人类模型的发展历史，并提供了关于 SMPL 模型的详细信息，它是人类推理中使用最广泛的模板。
### Statistical Modeling
1. body modeling
![[Pasted image 20230318163345.png|600]]
2. whole body modeling
    eg: SMPL+H: SMPL+MANO 手部模型

## 3. Human Mesh Recovery
  内容：第3节描述了身体恢复和全身（whole-body）恢复的方法(包含手和脸)。方法分为基于优化的范式和基于回归的范式。
### 3.1 Body Recovery
**3.1.1 Optimization-based Paradigm**
1. The objective function typically contains two parts: data terms and regularization terms.
     - 正则项：introduce regularization terms to favor probable poses over improbable ones
     - **SMPLify**  
         - iteratively fits the SMPL model to detected 2D keypoints of an unconstrained image
         - 2D pose Convolutional Network (ConvNet) to detect the keypoints and then perform gradient-based optimization
         - 数据项：penalizes the distance between detected 2D joints and the projected SMPL joints
         - pose priors:
         - shape priors: 
     - SMPLify 存在的问题：the shape remains highly unconstrained since the connection length between two keypoints is the only indicator that can be used to estimate the body shape
        -  解决：add constraints instead of relying solely on one geometric term
        - combine multiple cues for optimization, including 2D keypoints, silhouettes, and segmentations. (2D 关键点、轮廓和分割)
     

**3.1.1 Regression-based Paradigm**


## 4. Multi-person Recovery
  内容：在第4节和第5节中，我们将整理出有助于处理视频或多人恢复的新模块。



## 5. Recovery From monoclular Videos



## 6. Physical Plausibility
  内容：但是，如果仅仅用常规的数据项来监督人体，结果可能存在生理上的不合理和视觉上的缺陷。因此，在第6节中，我们讨论了通过涉及现实相机模型（realistic camera models）、接触约束（contact constraints）和人类先验（human priors）来增强物理合理性的策略。


## 7. Dataset And Evaluation
  内容：常用的数据集和评估标准，以及基准排行榜，在第7节中进行了总结。



## 8. Conclusion and Future Directions