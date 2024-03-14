---
Authors: Mengyang Feng; Jinlin Liu; Kai Yu; Yuan Yao; Zheng Hui; Xiefan Guo; Xianhui Lin; Haolan Xue; Chen Shi; Xiaowen Li; Aojie Li; Xiaoyang Kang; Biwen Lei; Miaomiao Cui; Peiran Ren; Xuansong Xie
Date: 2023/12/08
Topics: pose-transfer
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# DreaMoving: A Human Video Generation Framework based on Diffusion Models


## Abstract
In this paper, we present DreaMoving, a diffusion-based controllable video generation framework to produce high-quality customized human videos. Specifically, given target identity and posture sequences, DreaMoving can generate a video of the target identity moving or dancing anywhere driven by the posture sequences. To this end, we propose a Video ControlNet for motion-controlling and a Content Guider for identity preserving. The proposed model is easy to use and can be adapted to most stylized diffusion models to generate diverse results. The project page is available at https://dreamoving.github.io/dreamoving

## Files and Links
- **Url**: [Open online](https://arxiv.org/abs/2312.05107v2)
- **zotero entry**: [Zotero](zotero://select/library/items/2DQZY6SY)
- **open pdf**: [Feng et al_2023_DreaMoving.pdf](zotero://open-pdf/library/items/M22ME5DS)

## Comments


---

## Summary

  
## Research Objective(s)


## Background / Problem Statement

2.1 LivePhoto 把视频中的运动划分为10级，在训练的时候，把运动对应的map与输入噪声latent作cat操作，一起送入Unet网络去噪。待训练完成，在推理阶段就可以通过输入运动的强度来控制生成视频中人物的运动幅度大小。

2.2 DreaMoving 则是专门训练了一个Video ControlNet, 注入控制信息到Unet网络的（mid block 和up block ）中。这里的控制信息可以在姿态图（比如openpose或者DW pose），也可以是深度图。

2.3 MagicAnimate 和DreaMoving 类似，也是利用自己训练的Video ControlNet来控制人物的运动，不同的是，MagicAnimate 只能利用Densepose sequence来作为控制条件。不知为啥，MagicAnimate 这么独特，控制方式与众不同。

2.4 Animate Anyone 和DreaMoving 以及MagicAnimate 又有所不同，虽然也是利用姿态来作为控制条件，但并不是类似文本注入的方式直接注入到Unet网络结构中，而是与噪声一起作为输入进入到Unet网络中。


## Method(s)

![[Pasted image 20240117120741.png]]

## Evaluation

没有定量的结果

## Conclusion


## Notes


----

## Extracted Annotations

