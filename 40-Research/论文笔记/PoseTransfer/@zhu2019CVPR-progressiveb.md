---
Authors: Zhen Zhu; Tengteng Huang; Baoguang Shi; Miao Yu; Bofei Wang; Xiang Bai
Date: 2019-05-13
Topics: pose-transfer
DOI: 10.48550/arXiv.1904.03349
Keywords:
---
tags: #论文笔记 

# Progressive Pose Attention Transfer for Person Image Generation


## Abstract
This paper proposes a new generative adversarial network for pose transfer, i.e., transferring the pose of a given person to a target pose. The generator of the network comprises a sequence of Pose-Attentional Transfer Blocks that each transfers certain regions it attends to, generating the person image progressively. Compared with those in previous works, our generated person images possess better appearance consistency and shape consistency with the input images, thus significantly more realistic-looking. The efficacy and efficiency of the proposed network are validated both qualitatively and quantitatively on Market-1501 and DeepFashion. Furthermore, the proposed architecture can generate training images for person re-identification, alleviating data insufficiency. Codes and models are available at: https://github.com/tengteng95/Pose-Transfer.git.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/1904.03349)
- **zotero entry**: [Zotero](zotero://select/library/items/URJZC82F)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/LZRG2E77); [Zhu et al_2019_Progressive Pose Attention Transfer for Person Image Generation.pdf](zotero://open-pdf/library/items/AZ9MTMMR)

## Comments
Comment: To appear in CVPR 2019, oral presentation (21 pages, 15 figures including the supplementary materials)

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)
![[Pasted image 20240110210442.png]]


在Pose-Attentional Transfer Network中含有多个Pose Attentional Block，其作用是对输入的image pathway和pose pathway按照Pose Mask进行更新，图中Mt即为Pose Mask，它引导网络将图片中人物的不同的部分按照目标姿态进行像素块迁移。

将最后一个Block中Image Pathway的数据经过解码网络，即得到了最终的生成图像。

## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

