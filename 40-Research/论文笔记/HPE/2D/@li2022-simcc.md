---
Authors: Yanjie Li; Sen Yang; Peidong Liu; Shoukui Zhang; Yunxiao Wang; Zhicheng Wang; Wankou Yang; Shu-Tao Xia
Date: 2022-07-05
Topics: 2D; HPE
DOI: 10.48550/arXiv.2107.03332
Keywords:
---
tags: #论文笔记 

# SimCC: a Simple Coordinate Classification Perspective for Human Pose Estimation


## Abstract
The 2D heatmap-based approaches have dominated Human Pose Estimation (HPE) for years due to high performance. However, the long-standing quantization error problem in the 2D heatmap-based methods leads to several well-known drawbacks: 1) The performance for the low-resolution inputs is limited; 2) To improve the feature map resolution for higher localization precision, multiple costly upsampling layers are required; 3) Extra post-processing is adopted to reduce the quantization error. To address these issues, we aim to explore a brand new scheme, called \textit{SimCC}, which reformulates HPE as two classification tasks for horizontal and vertical coordinates. The proposed SimCC uniformly divides each pixel into several bins, thus achieving \emph{sub-pixel} localization precision and low quantization error. Benefiting from that, SimCC can omit additional refinement post-processing and exclude upsampling layers under certain settings, resulting in a more simple and effective pipeline for HPE. Extensive experiments conducted over COCO, CrowdPose, and MPII datasets show that SimCC outperforms heatmap-based counterparts, especially in low-resolution settings by a large margin.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2107.03332)
- **zotero entry**: [Zotero](zotero://select/library/items/4V6I2TMX)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/9A3PQUFC); [Li et al_2022_SimCC.pdf](zotero://open-pdf/library/items/8L3NIINX)

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

注释(2023/4/19 下午9:42:39)

<mark style="background: red;">1) The performance for the low-resolution inputs is limited; 2) To improve the feature map resolution for higher localization precision, multiple costly upsampling layers are required; 3) Extra post-processing is adopted to reduce the quantization error</mark> [(Li 等, 2022, p. 1)](zotero://open-pdf/library/items/8L3NIINX?page=1&annotation=Z3V2P2KB)   
> 🔤1）低分辨率输入的性能有限； 2）为了提高特征图分辨率以获得更高的定位精度，需要多个昂贵的上采样层； 3）采用额外的后处理来减少量化误差🔤  

<mark style="background: green;">which reformulates HPE as two classification tasks for horizontal and vertical coordinates. The proposed SimCC uniformly divides each pixel into several bins, thus achieving sub-pixel localization precision and low quantization error.</mark> [(Li 等, 2022, p. 1)](zotero://open-pdf/library/items/8L3NIINX?page=1&annotation=L359495D)   
> 🔤它将 HPE 重新表述为水平和垂直坐标的两个分类任务。所提出的 SimCC 将每个像素统一划分为多个 bin，从而实现亚像素定位精度和低量化误差。🔤  

<mark style="background: yellow;">Extensive experiments conducted over COCO, CrowdPose, and MPII datasets</mark> [(Li 等, 2022, p. 1)](zotero://open-pdf/library/items/8L3NIINX?page=1&annotation=PH269VL8)   
> 🔤在 COCO、CrowdPose 和 MPII 数据集上进行了大量实验🔤  

<mark style="background: yellow;">1) a backbone to extract keypoint representations; 2) a regression head to generate the 2D heatmap, which may consist of multiple time-consuming upsampling layers; 3) extra post-processing to refine the predictions, such as empirical shift and DARK</mark> [(Li 等, 2022, p. 2)](zotero://open-pdf/library/items/8L3NIINX?page=2&annotation=HR5I643L)   
> 🔤1）提取关键点表示的主干； 2) 一个回归头来生成二维热图，它可能由多个耗时的上采样层组成； 3) 额外的后处理以改进预测，例如经验偏移和 DARK🔤  

<mark style="background: green;">Different from these heatmap-based schemes, the proposed SimCC is much simpler, which only needs two classifier heads for coordinate classification and excludes the costly refinement post-processing and extra upsampling layers.</mark> [(Li 等, 2022, p. 2)](zotero://open-pdf/library/items/8L3NIINX?page=2&annotation=79NCKBP7)   
> 🔤与这些基于热图的方案不同，所提出的 SimCC 更简单，它只需要两个分类器头进行坐标分类，并且不包括昂贵的细化后处理和额外的上采样层。🔤  

<mark style="background: green;">we propose a simple yet effective coordinate classification pipeline, namely SimCC, which regards HPE as two classification tasks for horizontal and vertical coordinates.</mark> [(Li 等, 2022, p. 2)](zotero://open-pdf/library/items/8L3NIINX?page=2&annotation=NDN3PB4V)   
> 🔤我们提出了一个简单而有效的坐标分类管道，即 SimCC，它将 HPE 视为水平和垂直坐标的两个分类任务。🔤  

<mark style="background: yellow;">SimCC firstly employs a Convolutional Neural Network (CNN) or Transformer-based backbone to extract keypoint representations. Given the obtained keypoint representations, SimCC then performs coordinate classification for vertical and horizontal coordinates independently to yield the final predictions.</mark> [(Li 等, 2022, p. 2)](zotero://open-pdf/library/items/8L3NIINX?page=2&annotation=P7BXH95R)   
> 🔤SimCC 首先采用卷积神经网络 (CNN) 或基于 Transformer 的主干来提取关键点表示。给定获得的关键点表示，SimCC 然后独立地对垂直和水平坐标进行坐标分类以产生最终预测。🔤  

<mark style="background: yellow;">SimCC uniformly divides each pixel into several bins, which achieves sub-pixel localization precision.</mark> [(Li 等, 2022, p. 3)](zotero://open-pdf/library/items/8L3NIINX?page=3&annotation=WN4TXEME)   
> 🔤SimCC 将每个像素统一划分为多个 bin，从而实现了亚像素定位精度。🔤  

<mark style="background: green;">reformulating the problem as two classification tasks for horizontal and vertical coordinates. SimCC serves as a general scheme and can be easily applied to existing CNN-based or Transformer-based HPE models.</mark> [(Li 等, 2022, p. 3)](zotero://open-pdf/library/items/8L3NIINX?page=3&annotation=UQHUECUA)   
> 🔤将问题重新表述为水平和垂直坐标的两个分类任务。 SimCC 作为一种通用方案，可以轻松应用于现有的基于 CNN 或基于 Transformer 的 HPE 模型。🔤  

<mark style="background: green;">SimCC achieves high efficiency by omitting the extra time-consuming upsampling and post-processing in heatmap-based methods.</mark> [(Li 等, 2022, p. 3)](zotero://open-pdf/library/items/8L3NIINX?page=3&annotation=GJE3BZB9)   
> 🔤SimCC 通过省略基于热图的方法中额外耗时的上采样和后处理来实现高效率。🔤  

<mark style="background: green;">verify the effectiveness of the proposed SimCC with different backbones and multiple input sizes.</mark> [(Li 等, 2022, p. 3)](zotero://open-pdf/library/items/8L3NIINX?page=3&annotation=47YPRJAE)   
> 🔤验证所提出的具有不同主干和多个输入大小的 SimCC 的有效性。🔤  

<mark style="background: yellow;">Coordinate classification. Concurrent to our work, Chen et al. [5] propose Pix2Seq to casts object detection as a language modeling task, where an object is described as sequences of five discrete tokens for further classification. In Pix2Seq, the Transformer decoder architecture is essential to “read out” each object (yield the predictions)</mark> [(Li 等, 2022, p. 4)](zotero://open-pdf/library/items/8L3NIINX?page=4&annotation=RLLC2UWI)    

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/3CRES83X%5Cimage.png)[ ](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=UMDRQBRU)

<mark style="background: orange;">CNNbased or Transformer-based network (e.g., HRNet [29], TokenPose [18])</mark> [(Li 等, 2022, p. 5)](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=P6QSCEFE)   
> 🔤基于 CNN 或基于 Transformer 的网络（例如，HRNet [29]、TokenPose [18]）🔤  

<mark style="background: orange;">after the backbone to perform coordinate classification</mark> [(Li 等, 2022, p. 5)](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=N3N2M2PA)   
> 🔤在主干之后进行坐标分类🔤  

<mark style="background: orange;">For the CNN-based backbone, we simply flatten the outputted keypoint representations from (n, H′, W ′) to (n, H′ × W ′) for classification.</mark> [(Li 等, 2022, p. 5)](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=XPKWXY2L)   
> 🔤对于基于 CNN 的主干，我们简单地将输出的关键点表示从 (n, H', W ') 展平到 (n, H' × W ') 以进行分类。🔤  

<mark style="background: gray;">Compared to heatmap-based approach [38] which uses multiple costly deconvolution layers as head</mark> [(Li 等, 2022, p. 5)](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=MN6LA2CY)   
> 🔤与使用多个昂贵的反卷积层作为头部的基于热图的方法[38]相比🔤  

<mark style="background: orange;">To achieve classification, we propose to uniformly discretize each continuous coordinate value into an integer as class label for model training:</mark> [(Li 等, 2022, p. 5)](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=HQ2HCQBV)   
> 🔤为了实现分类，我们建议将每个连续坐标值统一离散化为一个整数作为模型训练的类标签：🔤  

<mark style="background: orange;">To yield the final prediction, SimCC performs vertical and horizontal coordinate classification independently based on the n keypoint representations learnt by the backbone.</mark> [(Li 等, 2022, p. 5)](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=IWAHQUMR)   
> 🔤为了产生最终的预测，SimCC 基于主干学习的 n 个关键点表示独立地执行垂直和水平坐标分类。🔤  

<mark style="background: orange;">In addition, Kullback–Leibler divergence is used as loss function for training.</mark> [(Li 等, 2022, p. 5)](zotero://open-pdf/library/items/8L3NIINX?page=5&annotation=CTPZB94Q)   
> 🔤此外，Kullback–Leibler 散度用作训练的损失函数。🔤  

<mark style="background: orange;">the closer the output category is to the groundtruth, the better. To address this issue, we also explore to use Laplace or Gaussian label smoothing, resulting in smoothed labels following corresponding distribution.</mark> [(Li 等, 2022, p. 6)](zotero://open-pdf/library/items/8L3NIINX?page=6&annotation=VUZFSNDW)   
> 🔤输出类别越接近 groundtruth 越好。为了解决这个问题，我们还探索使用拉普拉斯或高斯标签平滑，从而使平滑标签遵循相应的分布。🔤  

![](file://C:/Users/%E7%A5%9D%E9%93%B6%E9%82%A3/Documents/Obsidian%20Vault/.hidden/zotero/storage/YY4HRNHH%5Cimage.png)[ ](zotero://open-pdf/library/items/8L3NIINX?page=7&annotation=RJJV3Q57)

- [ ] <mark style="background: blue;">5. Chen, T., Saxena, S., Li, L., Fleet, D.J., Hinton, G.: Pix2seq: A language modeling framework for object detection. arXiv preprint arXiv:2109.10852 (2021)</mark> [(Li 等, 2022, p. 16)](zotero://open-pdf/library/items/8L3NIINX?page=16&annotation=F2PBDLMG)  🔤5. Chen, T., Saxena, S., Li, L., Fleet, D.J., Hinton, G.：Pix2seq：用于对象检测的语言建模框架。 arXiv 预印本 arXiv:2109.10852 (2021)🔤 

- [ ] <mark style="background: blue;">32. Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., Wojna, Z.: Rethinking the inception architecture for computer vision. In: Proceedings of the IEEE conference on computer vision and pattern recognition. pp. 2818–2826 (2016)</mark> [(Li 等, 2022, p. 17)](zotero://open-pdf/library/items/8L3NIINX?page=17&annotation=LVXWFG4P)  🔤32. Szegedy, C.、Vanhoucke, V.、Ioffe, S.、Shlens, J.、Wojna, Z.：重新思考计算机视觉的起始架构。在：IEEE 计算机视觉和模式识别会议论文集。第 2818–2826 页（2016 年）🔤 



