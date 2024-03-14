---
Authors: Caroline Chan; Shiry Ginosar; Tinghui Zhou; Alexei A. Efros
Date: 2019-08-27
Topics: 重定向
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# Everybody Dance Now


## Abstract
This paper presents a simple method for “do as I do” motion transfer: given a source video of a person dancing, we can transfer that performance to a novel (amateur) target after only a few minutes of the target subject performing standard moves. We approach this problem as video-tovideo translation using pose as an intermediate representation. To transfer the motion, we extract poses from the source subject and apply the learned pose-to-appearance mapping to generate the target subject. We predict two consecutive frames for temporally coherent video results and introduce a separate pipeline for realistic face synthesis. Although our method is quite simple, it produces surprisingly compelling results (see video). This motivates us to also provide a forensics tool for reliable synthetic content detection, which is able to distinguish videos synthesized by our system from real data. In addition, we release a ﬁrstof-its-kind open-source dataset of videos that can be legally used for training and motion transfer.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/1808.07371)
- **zotero entry**: [Zotero](zotero://select/library/items/WNS8QBNF)
- **open pdf**: [Chan 等 - 2019 - Everybody Dance Now.pdf](zotero://open-pdf/library/items/BXKRENU3)

## Comments
Comment: In ICCV 2019

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)
![[Pasted image 20240108110758.png]]
**图2上半部分描述生成式对抗模型训练流程。**

从目标视频中给定一个帧y，使用预训练的姿态检测模型P图获得对应的姿态图形x = P(y)。在训练阶段使用对应的(x, y)图像对去学习从姿态图形x到目标人物合成图像（即：G(x)）的==映射==G。通过在鉴别器D使用对抗训练和在预训练VGGNet使用==感知==重建损失，我们可以优化生成器G，使其输出接近真实图像y。判别器试图区分“真实”的图像对（例如(x, y)）和“伪造”的图像对（例如(x, G(x)）。

**图2下半部分描述迁移流程。**

和训练过程相似，姿态检测模型P从源视频给定帧y'中抽取姿态图形x'。由于x'和目标视频中人物的身体尺寸和位置不同，我们通过全局姿态标准化转换，使其和目标人物更一致，记x。将x推入已训练的模型G中生成目标人物图像G(x)，生成的图像与源视频中的y帧相对应。

## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

