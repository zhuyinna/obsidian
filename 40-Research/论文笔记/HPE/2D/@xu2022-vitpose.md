---
Authors: Yufei Xu; Jing Zhang; Qiming Zhang; Dacheng Tao
Date: 2022-10-12
Topics: 2D; HPE
DOI: 10.48550/arXiv.2204.12484
Keywords:
---
tags: #论文笔记 

# ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation


## Abstract
Although no specific domain knowledge is considered in the design, plain vision transformers have shown excellent performance in visual recognition tasks. However, little effort has been made to reveal the potential of such simple structures for pose estimation tasks. In this paper, we show the surprisingly good capabilities of plain vision transformers for pose estimation from various aspects, namely simplicity in model structure, scalability in model size, flexibility in training paradigm, and transferability of knowledge between models, through a simple baseline model called ViTPose. Specifically, ViTPose employs plain and non-hierarchical vision transformers as backbones to extract features for a given person instance and a lightweight decoder for pose estimation. It can be scaled up from 100M to 1B parameters by taking the advantages of the scalable model capacity and high parallelism of transformers, setting a new Pareto front between throughput and performance. Besides, ViTPose is very flexible regarding the attention type, input resolution, pre-training and finetuning strategy, as well as dealing with multiple pose tasks. We also empirically demonstrate that the knowledge of large ViTPose models can be easily transferred to small ones via a simple knowledge token. Experimental results show that our basic ViTPose model outperforms representative methods on the challenging MS COCO Keypoint Detection benchmark, while the largest model sets a new state-of-the-art. The code and models are available at https://github.com/ViTAE-Transformer/ViTPose.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2204.12484)
- **zotero entry**: [Zotero](zotero://select/library/items/L38J526Y)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/RH2NY9CT); [Xu et al_2022_ViTPose.pdf](zotero://open-pdf/library/items/FTNRCR4L)

## Comments


---

## Summary

  
## Research Objective(s)


## Background / Problem Statement


## Method(s)


## Evaluation


## Conclusion


## Notes


----

## Extracted Annotations

注释(2023/4/19 下午9:09:34)

<mark style="background: green;">Specifically, ViTPose employs plain and non-hierarchical vision transformers as backbones to extract features for a given person instance and a lightweight decoder for pose estimation.</mark> [(Xu 等, 2022, p. 1)](zotero://open-pdf/library/items/FTNRCR4L?page=1&annotation=YSWKGTTW)   
> 🔤具体来说，ViTPose 使用普通和非分层视觉转换器作为主干来提取给定人物实例的特征，并使用轻量级解码器进行姿势估计。🔤Vison Transformer 在视觉识别任务中效果优秀，在识别但还没有人在姿态估计任务上验证这种结构的有效性。这篇论文提出了名为VitPose的用于姿态估计的Transformer网络，使用普通ViT结构作为Backbone，结合一个轻量级的Decoder，就能在MS COCO 关键点估计bechmark上达到SOTA。  

<mark style="background: yellow;">To this end, we simply append several decoder layers after the transformer backbone to estimate the heatmaps w.r.t. the keypoints, as shown in Fig. 2 (a)</mark> [(Xu 等, 2022, p. 3)](zotero://open-pdf/library/items/FTNRCR4L?page=3&annotation=TE5REUDQ)   
> 🔤为此，我们简单地在变压器主干之后附加几个解码器层来估计热图 w.r.t。关键点，如图2（a）所示🔤  

<mark style="background: yellow;">e do not adopt skip-connections or cross-attentions in the decoder layers but simple deconvolution layers and a prediction layer,</mark> [(Xu 等, 2022, p. 3)](zotero://open-pdf/library/items/FTNRCR4L?page=3&annotation=X39FUPKP)   
> 🔤e 在解码层中不采用跳跃连接或交叉注意，而是采用简单的反卷积层和预测层，🔤  

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/RYZ39JBS%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=3&annotation=CMLRZGDB)


> embedding:降采样d倍数(default:16)，通道数3-&gt;C;transformer block：包含multi-head self-attention(MHSA)和一个feed-forward network(FFN); [ ](zotero://open-pdf/library/items/FTNRCR4L?page=4&annotation=XYT259F9) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/UHIB2ESF%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=4&annotation=XYT259F9)

<mark style="background: yellow;">The first one is the classic decoder. It is composed of two deconvolution blocks, each of which contains one deconvolution layer followed by batch normalization [19] and ReLU</mark> [(Xu 等, 2022, p. 4)](zotero://open-pdf/library/items/FTNRCR4L?page=4&annotation=BQT2TV5U)   
> 🔤第一个是经典解码器。它由两个反卷积块组成，每个反卷积块包含一个反卷积层，然后是批量归一化 [19] 和 ReLU🔤  

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/FILZKQFA%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=4&annotation=N4BWTNJ3)

<mark style="background: yellow;">try another simpler decoder in ViTPose, which is proved effective thanks to the strong representation ability of the vision transformer backbone. Specifically, we directly upsample the feature maps by 4 times with bilinear interpolation, followed by a ReLU and a convolution layer with the kernel size 3 × 3 to get the heatmaps</mark> [(Xu 等, 2022, p. 4)](zotero://open-pdf/library/items/FTNRCR4L?page=4&annotation=TL76VXZ6)   
> 🔤在 ViTPose 中尝试另一个更简单的解码器，由于 vision transformer backbone 的强大表示能力，它被证明是有效的。具体来说，我们直接使用双线性插值对特征图进行 4 倍上采样，然后使用 ReLU 和内核大小为 3 × 3 的卷积层来获得热图🔤  


> 与描述不符。描述为RELU层在Bilinear层后面。具体看代码 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=4&annotation=EQVFS6UR) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/UKAFYCLR%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=4&annotation=EQVFS6UR)

<mark style="background: yellow;">We empirically demonstrate that with the MHSA module frozen, ViTPose obtains comparable performance to the fully finetuning setting.</mark> [(Xu 等, 2022, p. 5)](zotero://open-pdf/library/items/FTNRCR4L?page=5&annotation=NZQTXVFE)   
> 🔤我们凭经验证明，在 MHSA 模块冻结的情况下，ViTPose 获得了与完全微调设置相当的性能。🔤  

<mark style="background: green;">One common method to improve the performance of smaller models is to transfer the knowledge from larger ones, i.e., knowledge distillation [17, 14]. Specifically, given a teacher network T and student network S, a simple distillation method is to add an output distillation loss Lod t→s to force the student network’s output imitating the teacher network’s output,</mark> [(Xu 等, 2022, p. 5)](zotero://open-pdf/library/items/FTNRCR4L?page=5&annotation=3TR3YBYI)   
> 🔤提高较小模型性能的一种常用方法是从较大模型转移知识，即知识蒸馏 [17、14]。具体来说，给定一个教师网络T和学生网络S，一个简单的蒸馏方法是添加一个输出蒸馏损失Lod t→s来强制学生网络的输出模仿教师网络的输出，🔤这篇论文比较有意思的一个点是提出了一个基于Transformer的蒸馏方法，与常见的用loss来监督Teacher和Student网络的思路不太一样，具体如下: 1. 在大模型的patch embedding后的visual token后面增加一个知识token模块，并进行随机初始化 2. 固定大模型的参数，只训练知识token模块 3. 将训练好的知识token模块接到小模型的visual token后面，且固定知识token的参数，只训练小模型的其他参数。通过这样的流程，将所有的知识都融合到了知识token模块的参数里面，并且从大模型传递到小模型  


> 两种decoder对比:1. 经典Decoder结构，两个Deconv（+BN+ReLU) + 1个1x1 conv，每个deconv上采样2倍，最终输出feature map大小为输入的1/4倍2. 双线性差值上采样4倍，然后是ReLU+3x3conv，不过论文中公式与描述不符，ReLU在双线性上采样之前，需要看代码实现具体是哪一种方案1非线性更高，因此在CNN的结构中使用比较多。而这篇论文也验证了由于Transformer强大的学习能力，即使像方案2这样的的简单decoder，也能达到很高的精度可以看到，ResNet系列在方案1上的结果远高于方案2，说明CNN结构的学习能力需要强有力的decoder来进一步加强，而VitPose结构则不需要，这需要归功于ViT结构的强大学习能力 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=6&annotation=QPVE248H) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/W5ZD87B6%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=6&annotation=QPVE248H)


> 预训练上的灵活性 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=7&annotation=EML6686N) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/D3YJEP27%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=7&annotation=EML6686N)


> 分辨率上的灵活性 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=7&annotation=64J9JWWR) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/XP5XS2IU%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=7&annotation=64J9JWWR)


> attention type上的灵活性 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=7&annotation=C3SS7R6P) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/IQ4XERDW%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=7&annotation=C3SS7R6P)


> finetune的灵活性 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=8&annotation=9RLQYTSA) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/YQETBGUX%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=8&annotation=9RLQYTSA)


> 多任务上的灵活性：作者还尝试了这样一个实验，采用同一个backbone，多个decoder，每个decoder对应一个数据集的任务，实验验证一次训练，多个数据集上的结果都能比较好，且比单个数据集精度有提升 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=8&annotation=68FHNYQW) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/TJGZ7G7L%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=8&annotation=68FHNYQW)


> 知识蒸馏方面的消融实验 [ ](zotero://open-pdf/library/items/FTNRCR4L?page=8&annotation=RDEIUYAS) 

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/KPYMT4KG%5Cimage.png)[ ](zotero://open-pdf/library/items/FTNRCR4L?page=8&annotation=RDEIUYAS)

<mark style="background: red;">complex decoders or FPN structures</mark> [(Xu 等, 2022, p. 10)](zotero://open-pdf/library/items/FTNRCR4L?page=10&annotation=998UWF8N)   
> 🔤复杂解码器或 FPN 结构🔤  

- [ ] <mark style="background: blue;">In addition, we believe ViTPose can also be applied to other pose estimation datasets, e.g., animal pose estimation [47, 9, 45] and face keypoint detection</mark> [(Xu 等, 2022, p. 10)](zotero://open-pdf/library/items/FTNRCR4L?page=10&annotation=U8DYKFRJ)  🔤此外，我们相信 ViTPose 也可以应用于其他姿势估计数据集，例如动物姿势估计 [47, 9, 45] 和人脸关键点检测🔤 



