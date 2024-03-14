---
Authors: Fei Shen; Hu Ye; Jun Zhang; Cong Wang; Xiao Han; Wei Yang
Date: 2023-10-16
Topics: pose-transfer
DOI: {{DOI}}
Keywords:
---
tags: #论文笔记 

# Advancing Pose-Guided Image Synthesis with Progressive Conditional Diffusion Models


## Abstract
Recent work has showcased the significant potential of diffusion models in pose-guided person image synthesis. However, owing to the inconsistency in pose between the source and target images, synthesizing an image with a distinct pose, relying exclusively on the source image and target pose information, remains a formidable challenge. This paper presents Progressive Conditional Diffusion Models (PCDMs) that incrementally bridge the gap between person images under the target and source poses through three stages. Specifically, in the first stage, we design a simple prior conditional diffusion model that predicts the global features of the target image by mining the global alignment relationship between pose coordinates and image appearance. Then, the second stage establishes a dense correspondence between the source and target images using the global features from the previous stage, and an inpainting conditional diffusion model is proposed to further align and enhance the contextual features, generating a coarse-grained person image. In the third stage, we propose a refining conditional diffusion model to utilize the coarsely generated image from the previous stage as a condition, achieving texture restoration and enhancing fine-detail consistency. The three-stage PCDMs work progressively to generate the final high-quality and high-fidelity synthesized image. Both qualitative and quantitative results demonstrate the consistency and photorealism of our proposed PCDMs under challenging scenarios.The code and model will be available at https://github.com/muzishen/PCDMs.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2310.06313)
- **zotero entry**: [Zotero](zotero://select/library/items/5A2LNLMI)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/CIT7BH9K); [Shen et al_2023_Advancing Pose-Guided Image Synthesis with Progressive Conditional Diffusion.pdf](zotero://open-pdf/library/items/9NK6DWMX)
- code: 未开源
## Comments


---

## Summary

  
## Research Objective(s)


## Background / Problem Statement

### 现有方法

**介绍现有方法的优缺点，逐步引出扩散模型。**

之前的工作通常集中在生成对抗网络（GAN）（Creswell et al., 2018）、变分自动编码器（VAE）（Kingma et al., 2019）和基于流的模型（Li et al., 2019）。 

GANbase 方法（Zhu et al., 2019；Tang et al., 2020）插入多个重复模块来挖掘源和目标姿态图像特征之间的稀疏对应关系。这些方法产生的输出通常表现出扭曲的纹理、不切实际的身体形状和局部模糊，特别是在生成被遮挡的身体部位的图像时。此外，由于对抗性最小-最大目标的性质，基于 GAN 的方法容易受到不稳定的训练动态的影响，从而限制了生成样本的多样性。

基于 VAE 的方法（Siarohin et al., 2018；Esser et al., 2018）相对稳定，但由于依赖代理损失进行优化，因此会出现细节模糊和目标姿态未对准的问题。

基于流的方法（Li et al., 2019; Ren et al., 2021）的出现就是为了解决这个问题，它指导源通过预测源姿态和目标姿态之间的对应关系，将图像特征扭曲为合理的目标姿态。然而，当源和目标姿势发生较大变形或遮挡时，这很容易导致生成的图像中出现明显的伪影。

同样，一些方法（Lv et al., 2021；Zhang et al., 2021）利用人类解析图来学习图像语义和姿势之间的对应关系，以确保生成的图像与目标姿势一致。尽管这些方法可以生成满足姿势一致性要求的图像，但它们仍然难以保持一致的风格并捕获逼真的纹理细节。

### 扩散模型及问题

最近，扩散模型（Bhunia et al., 2023；Zhang & Zhou, 2023）在人物图像合成领域取得了重大进展。他们利用源图像和目标姿态作为条件，通过多步去噪过程生成目标图像，而不是一步完成。因此，这些方法有助于更好地保留输入信息。然而，如图1（a）所示，由于源图像和目标图像之间的姿态不一致，这本质上构成了条件级别上未对齐的图像到图像生成任务。此外，源图像和目标图像之间在图像、姿势和外观方面缺乏密集的对应关系通常会导致结果不太真实。


## Method(s)

本文提出了渐进条件扩散模型（PCDM），通过三个阶段解决上述问题，如图 1（b）所示。最初，我们提出了一个先验条件扩散模型来预测给定目标姿势的全局特征。这种预测比直接生成目标图像要简单得多，因为我们允许先前的模型仅专注于一项任务，从而不必担心实际详细的纹理生成。给定源图像和姿态坐标作为条件，先验条件扩散模型采用transformer网络来预测目标姿态下的全局特征。在第二阶段，我们使用前一阶段的全局特征来建立源图像和目标图像之间的密集对应关系，并提出修复条件扩散模型以进一步对齐和增强上下文特征，生成粗粒度合成图像。最后，我们开发了一个精炼的条件扩散模型。该模型利用前一阶段生成的粗粒度图像，并应用后图像到图像技术来恢复纹理并增强细节一致性。 PCDM 的三个阶段逐步运行，以产生视觉上更具吸引力的结果，特别是在处理复杂的姿势时。

![[Pasted image 20240116112654.png]]



### prior

在第一阶段，作者提出了一个简单的先验条件扩散模型，旨在预测目标图像的全局嵌入。该阶段，选择从CLIP图像编码器中提取的图像嵌入作为目标图像的全局嵌入。CLIP是通过对大规模图像文本配对数据集进行对比学习而训练的，**因此，图像嵌入可以捕捉丰富的图像内容和风格信息，用来引导随后的目标图像合成。** 如图3所示，先验条件扩散模型是一个变换器网络，以源图像的姿势、目标图像的姿势和源图像为条件。作者首先采用OpenPose来获取源图像和目标图像的姿势坐标，再使用由3个线性层组成的紧凑可训练姿势网络来将姿势坐标投影到姿势嵌入。对于源图像，还使用了一个CLIP图像编码器来提取图像嵌入，并添加一个线性层来投影图像嵌入。此外，添加了额外的嵌入来预测目标的全局嵌入，该嵌入以及时间步嵌入和目标图像的嘈杂图像嵌入被连接成一个嵌入序列，作为变换器网络的输入。

![[Pasted image 20240116113623.png|267]]
遵循unCLIP的方法，先验扩散模型被训练来直接预测未受噪声干扰的图像嵌入，而不是图像嵌入中添加的噪声。
![[Pasted image 20240116113640.png|475]]


==一旦模型学习了条件分布，推理根据如下公式：==
![[Pasted image 20240116113650.png]]


### inpainting

通过在第一阶段获取目标图像的全局特征，作者提出了一个修复条件扩散模型，以建立源图像和目标图像之间的密集对应关系，并将非对齐的img2img生成任务转化为对齐的任务。如图4所示，沿宽度维度连接了源图像和目标图像、源姿势和目标姿势，以及源蒙版图像。==为了防止源图像和目标图像之间的黑白混淆，添加了一个单通道的标记符号，其宽度和高度与输入相同，且使用0和1来表示蒙版和未蒙版的像素。==然后，连接了从先验条件扩散模型（先验模型）获得的目标的全局特征和源图像的局部特征。这确保了模型的输入条件包括源图像和目标图像的全部内容，并在三个级别上对齐：图像、姿势和特征，这是现有工作中忽视的。

![[Pasted image 20240116114037.png|500]]

具体来说，使用一个与ControlNet类似的具有四个卷积层的姿势编码器，从姿势骨架图像中提取姿势特征。

与先验模型使用姿势坐标不同，作者期望该模型在整个学习过程中保持图像模态的对齐，尤其是空间信息。对于源图像，使用一个冻结的图像编码器和一个可训练的MLP来提取源图像的细粒度特征。

为了更好地利用从前一阶段获得的目标图像的全局特征，选择DINOv2作为图像编码器，并添加到时间步嵌入中。

![[Pasted image 20240116114443.png]]

在推断阶段，使用无分类器引导（classifier-free guidance），公式如下所示：

![[Pasted image 20240116114453.png]]

### refining

在第二阶段之后，获得了一个初步生成的粗粒度目标图像。为了进一步提高图像质量和细节纹理，如图5所示，提出了一个精化条件扩散模型。这个模型使用前一阶段生成的粗粒度图像作为条件，以提高合成图像的质量和保真度。==首先，将粗粒度目标图像与嘈杂图像沿通道连接，可以通过修改基于UNet架构的扩散模型的第一个卷积层来轻松实现。==然后，==使用DINOv2图像编码器和一个可学习的MLP层来提取源图像的特征==。最后，==通过交叉注意机制将纹理特征引入网络，以引导模型进行纹理修复和增强细节一致性==.

![[Pasted image 20240116114559.png]]


![[Pasted image 20240116114622.png]]






## Evaluation

- **数据集**。DeepFashion, Market-1501
- 骨架提取：OpenPose
- **度量标准**：结构相似性指数（SSIM）、学习感知图像块相似性（LPIPS）和Frechet Inception 距离（FID）。并且，主观评估优先考虑面向用户的度量标准，包括将真实图像误分类为生成图像的百分比（R2G），将生成图像误分类为真实图像的百分比（G2R）和在所有模型中被视为优越的图像的百分比（Jab）
- 硬件：8台NVIDIA V100 GPU上进行实验。配置总结如下：（1）先验模型的变换器有20个变换器块，每个块的宽度为2,048。对于修复模型和精化模型，使用了预训练的stable diffusionV2.1，并修改第一个卷积层以适应额外的条件。（2）在所有阶段，均使用AdamW优化器，学习率固定为 1e−4 。（3）使用大小为256×176和512×352的图像训练DeepFashion数据集。对于Market-1501数据集，使用大小为128×64的图像


![[Pasted image 20240116114822.png]]


![[Pasted image 20240116114847.png]]


## Conclusion


## Notes


----

## Extracted Annotations

