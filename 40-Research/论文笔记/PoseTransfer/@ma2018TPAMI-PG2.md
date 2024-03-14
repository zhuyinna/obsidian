---
Authors: Liqian Ma; Xu Jia; Qianru Sun; Bernt Schiele; Tinne Tuytelaars; Luc Van Gool
Date: 2018-01-28
Topics: CPIS
Keywords: first appearance and pose-guided image generation
---
tags: #论文笔记 

# Pose Guided Person Image Generation


## Abstract
This paper proposes the novel Pose Guided Person Generation Network (PG$^2$) that allows to synthesize person images in arbitrary poses, based on an image of that person and a novel pose. Our generation framework PG$^2$ utilizes the pose information explicitly and consists of two key stages: pose integration and image refinement. In the first stage the condition image and the target pose are fed into a U-Net-like network to generate an initial but coarse image of the person with the target pose. The second stage then refines the initial and blurry result by training a U-Net-like generator in an adversarial way. Extensive experimental results on both 128$\times$64 re-identification images and 256$\times$256 fashion photos show that our model generates high-quality person images with convincing details.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/1705.09368)
- **zotero entry**: [Zotero](zotero://select/library/items/PKQZDRM5)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/59USN5LV); [Ma et al_2018_Pose Guided Person Image Generation.pdf](zotero://open-pdf/library/items/4QRL92YI)

## Comments
Comment: Xu Jia and Qianru Sun contribute equally. Accepted in Proceedings of 31st Conference on Neural Information Processing Systems (NIPS 2017)

---

## Summary
0. 借鉴方法
- 姿态估计网络直接采用：Cao, Z., Simon, T., Wei, S.E., Sheikh, Y.: **Realtime multi-person 2d pose estimation using part affinity fields.** In: CVPR. (2017)
- stage2中采用DCGAN：在第二阶段，使用深度卷积 GAN (DCGAN) 模型的变体来进一步细化初始生成结果。该模型通过对抗训练学习填充更多外观细节并生成更清晰的图像。与常见的 GAN 直接从头开始学习生成图像不同，**在这项工作中，我们训练 GAN 来生成初始生成结果和目标人物图像之间的差异图。训练收敛得更快**，因为这是一项更容易的任务。此外，我们添加了一个 **masked L1 损失来规范生成器的训练**，这样它就不会生成带有许多伪影的图像。在两个数据集（低分辨率行人重识别数据集和高分辨率时尚照片数据集）上的实验证明了该方法的有效性。Alec Radford, Luke Metz, and Soumith Chintala. **Unsupervised representation learning with deep convolutional generative adversarial networks**. arXiv, 1511.06434, 2015

1. 主要方法分为两个阶段：
   - stage1：输入源图像IA和目标关节PB，输出低分辨率~IB
   - stage2：输入~IB，输出高分辨率目标图
   
2. 网络结构
我们总结了所提出的模型 PG2 的网络架构。在阶段 I，G1 的编码器由 N 个残差块和一个全连接层组成，其中 N 取决于输入的大小。每个残差块由两个 stride=1 的卷积层组成，后面跟着一个 stride=2 的子采样卷积层（最后一个块除外）。在第二阶段，G2 的编码器具有包括 N -2 个卷积块的全卷积架构。每个块由两个 stride=1 的卷积层和一个 stride=2 的子采样卷积层组成。 G1和G2中的解码器与相应的编码器对称。此外，解码器和编码器之间存在快捷连接，如图2所示。在G1和G2中，没有应用批量归一化或dropout。所有卷积层均由 3×3 滤波器组成，滤波器数量随每个块线性增加。我们将修正线性单元（ReLU）应用于除全连接层和输出卷积层之外的每一层。对于判别器，我们采用与 DCGAN [21] 相同的网络架构，除了输入卷积层的大小因不同而不同。

3. 数据集
DeepFashion，Market-1501
 
4. 创新点
- 提出了新的任务
- L1 masked loss：鼓励模型专注于传输人体外观而不是背景信息（但只用于stage2。stage1仍采用L1）
- 将问题分为两个阶段，第一阶段专注于人体的整体结构，第二阶段基于第一阶段结果填充外观细节。

5. 相似论文
-  [36]探索仅从单个视图输入生成多视图布料图像，这与我们的任务最相似:  Bo Zhao, Xiao Wu, Zhi-Qi Cheng, Hao Liu, and Jiashi Feng. Multi-view image generation from a single-view. arXiv, 1704.04886, 2017.

## Experiments
### Dataset
- DeepFashion
DeepFashion（店内服装检索基准）数据集 [16] 由 52,712 个店内服装图像和 200,000 个交叉姿势/比例对组成。所有图像均为 256×256 的高分辨率。在训练集中，我们有 146,680 对，每对都由同一个人但不同姿势的两张图像组成。我们从测试集中随机选择 12,800 对进行测试

- Market-1501
我们还对更具挑战性的重新识别数据集 Market-1501 [37] 进行了实验，其中包含从 6 个不相交的监控摄像头捕获的 1,501 人的 32,668 张图像。该数据集中的人物的姿势、光照、视角和背景各不相同，这使得人物生成任务更具挑战性。所有图像的大小均为 128×64，并按照 [37] 分为 12,936/19,732 个训练/测试集。在训练集中，我们有 439,420 对，每对由同一个人但不同姿势的两张图像组成。我们从测试集中随机选择 12,800 对进行测试

### Implemention details
在这两个数据集上，我们使用 Adam [13] 优化器，β1 = 0.5 和 β2 = 0.999。初始学习率设置为2e-5。在 DeepFashion 上，我们设置卷积块的数量 N = 6。模型在第一阶段和第二阶段分别使用大小为 8 的小批量进行 30k 和 20k 迭代的训练。在 Market-1501 上，我们设置卷积块的数量 N = 5。模型在第一阶段和第二阶段分别使用大小为 16 的小批量进行 22k 和 14k 迭代的训练。对于数据增强，我们对两个数据集进行左右翻转。


## Method(s)
![[Pasted image 20231228155740.png]]

## Masked Loss
![[Pasted image 20231228160439.png|450]]

姿势掩模 MB 设置为 1（前景）和 0（背景），通过连接人体部位并应用一组形态学操作来计算，以便能够大致覆盖目标图像中的整个人体，请参阅中的示例图 3.
![[Pasted image 20231228160510.png|350]]
## Results
![[Pasted image 20231228161521.png|450]]

1. 姿态嵌入方式
为了评估我们提出的姿势嵌入方法，我们实现了两种替代方法。对于第一个坐标嵌入（CE），我们将关键点坐标传递给两个全连接层，并在瓶颈全连接层将嵌入特征向量与图像嵌入向量连接起来。第二个称为热图嵌入（HME），我们将 18 个关键点热图提供给独立编码器，并提取全连接层特征以与瓶颈全连接层处的图像嵌入向量连接。图 4 的第 4、5 和 6 列显示了在第一阶段使用时不同姿势嵌入方法的定性结果，即 G1 与 CE (G1-CE-L1)、HME (G1-HME-L1) 和我们的G1（G1-L1）。所有三个都使用标准 L1 损耗。我们可以看到 G1-L1 能够合成看起来合理的图像，捕捉人的整体结构，例如姿势和颜色。然而，另外两种嵌入方法G1-CE-L1和G1-HME-L1相当模糊，并且颜色错误。而且，G1-CE-L1的结果都是错误的姿势。这可以通过将关键点坐标映射到适当的图像位置的额外困难来解释，这使得训练更具挑战性。我们提出的使用 18 个姿势热图通道的姿势嵌入能够有效地指导生成过程，从而正确生成姿势。有趣的是，G1-L1 甚至可以生成合理的面部细节，如眼睛和嘴巴，如 DeepFashion 样本所示。

2. 损失函数
比较 Market-1501 数据集上使用 L1 损失（G1-L1）训练的 G1 和使用poseMaskLoss（G1-poseMaskLoss）训练的 G1 的结果，我们发现姿势掩模损失确实带来了性能的提升（图 6 和 7 列） 4).通过将图像生成集中在人体上，合成的图像变得更清晰，颜色看起来更好。我们可以看到，对于 ID 164 的人，G1-L1 生成的人上半身的颜色比 G1-poseMaskLoss 生成的上半身的颜色更嘈杂。对于人物 ID 23 和 346，具有姿势掩模丢失的方法为肩部和头部生成更清晰的边界。这些比较验证了我们的姿势掩模损失有效地减轻了噪声背景的影响，并引导生成器专注于人体的姿势转移。这两种损失对于 DeepFashion 样本产生相似的结果，因为背景要简单得多。

3. 两阶段还是一阶段
此外，我们还展示了两阶段模型相对于一阶段模型的优势。为此，我们使用 G1 作为生成器，但以对抗方式对其进行训练，以在给定条件图像和目标姿势作为输入的情况下直接生成新图像。该单阶段模型表示为 G1+D，我们的完整模型表示为 G1+G2+D。从图 4 中，我们可以看到我们的完整模型能够生成逼真的结果，其中包含比一级模型更多的细节。

ps评价指标中的masked-SSIM为本文创新的一个评价指标，计算方式参考masked-Loss

## Conclusion
在这项工作中，我们提出了姿势引导人物生成网络（PG2）来解决通过参考图像和目标姿势来合成人物图像的新任务。采用分治策略将生成过程分为两个阶段。第一阶段的目标是捕捉一个人的整体结构并产生初步结果。进一步提出了姿势掩模损失以减轻背景对人物图像合成的影响。第二阶段通过对抗训练填充更多外观细节，以生成更清晰的图像。对两人数据集的大量实验结果表明，我们的方法能够生成既逼真又姿势正确的图像。在未来的工作中，我们计划根据姿势和属性生成更加可控和多样化的人物图像。

