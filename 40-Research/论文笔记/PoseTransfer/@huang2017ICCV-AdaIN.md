---
Authors: Xun Huang; Serge Belongie
Date: 10/2017
Topics: pose-transfer
DOI: 10.1109/ICCV.2017.167
Keywords: IN代替BN：提高训练速度
---
tags: #论文笔记 

# Arbitrary Style Transfer in Real-Time with Adaptive Instance Normalization


## Abstract
Gatys et al. recently introduced a neural algorithm that renders a content image in the style of another image, achieving so-called style transfer. However, their framework requires a slow iterative optimization process, which limits its practical application. Fast approximations with feed-forward neural networks have been proposed to speed up neural style transfer. Unfortunately, the speed improvement comes at a cost: the network is usually tied to a ﬁxed set of styles and cannot adapt to arbitrary new styles. In this paper, we present a simple yet effective approach that for the ﬁrst time enables arbitrary style transfer in real-time. At the heart of our method is a novel adaptive instance normalization (AdaIN) layer that aligns the mean and variance of the content features with those of the style features. Our method achieves speed comparable to the fastest existing approach, without the restriction to a pre-deﬁned set of styles. In addition, our approach allows ﬂexible user controls such as content-style trade-off, style interpolation, color & spatial controls, all using a single feed-forward neural network.

## Files and Links
- **Url**: [Open online](http://ieeexplore.ieee.org/document/8237429/)
- **zotero entry**: [Zotero](zotero://select/library/items/IIM3RCCC)
- **open pdf**: [Huang 和 Belongie - 2017 - Arbitrary Style Transfer in Real-Time with Adaptiv.pdf](zotero://open-pdf/library/items/TLDPE6UZ)

## Comments


---

## Summary


## Research Objective(s)

　惯例先说了一下原来的两种方法的优缺点

### 　　第一种

　　_Gatys et al. recently introduced a neural algorithm that_ _renders a content image in the style of another image,_ _achieving so-called style transfer_ 

　　Gatys等人最近带来了一种神经网络的算法，这个算法可以可以使一张图片用另一张图片的风格表达出来，即样式转换

　　优缺点：风格多样化程度自由，但训练过程比较漫长，原文里说：their frame-work requires a slow iterative optimization process

### 　　第二种

　　由于第一种的方法太慢了，提出了第二种前馈神经网络的的快速逼近方法（Fast approximations with feed-forward neural networks）用来加速风格转换的速度

　　优缺点：训练速度确实快了，但样式转换比较单一

　　接着引出自己的方法In this paper, we present a simple yet effective approach that for the first time enables arbitrary style transfer in real-time

　　在这篇文章中，我们提出了一种简单但是有效的方用来首次实现任意样式的实时风格转换

　　方法的核心是加入了一个adaptive instance normalization (AdaIN) layer，

　　这个层做的事情就是利用待转换风格图片的特征的均值和方差，用来改变原来图片的均值和方差

　　打个比方有x，y两张图片，想把y上的风格转移到x上去，首先吧x，y的encode后的特征提取出来求均值和方差，x做归一化，再用y的均值方差进行分布调整

　　然后就是我们的方法实在是太好了，又快又灵活，作者还用了fastest来修饰，可以说非常自信了


## Background / Problem Statement

### 总结BN&IN&CIN

BN是标准化了一批样本的特征量信息，使得这批样本以某一个样式作为中心，但是毕竟每个样本的样式可能不同，这样标准化下去的样本和在中心的那个样本进行同样的样式转换时，会导致效果不好。虽然卷积层会尽量找补一些这种操作下产生的差异，但是还是比较困难的。回到IN，IN可以专注于处理样式特征，而其他网络可以专注与处理图片的内容特征，同时舍弃样式特征。同理CIN通过操作仿射参数来使得标准化后的特征统计量来改变成需要的特征，从而达成样式转换的目的。

```ad-note
title: Normalization
BN，LN，IN，GN从学术化上解释差异：

BatchNorm：batch方向做归一化，算NHW的均值，对小batchsize效果不好；BN主要缺点是对batchsize的大小比较敏感，由于每次计算均值和方差是在一个batch上，所以如果batchsize太小，则计算的均值、方差不足以代表整个数据分布

LayerNorm：channel方向做归一化，算CHW的均值，主要对RNN作用明显；

InstanceNorm：一个channel内做归一化，算H*W的均值，用在风格化迁移；因为在图像风格化中，生成结果主要依赖于某个图像实例，所以对整个batch归一化不适合图像风格化中，因而对HW做归一化。可以加速模型收敛，并且保持每个图像实例之间的独立。

GroupNorm：将channel方向分group，然后每个group内做归一化，算(C//G)HW的均值；这样与batchsize无关，不受其约束。

SwitchableNorm是将BN、LN、IN结合，赋予权重，让网络自己去学习归一化层应该使用什么方法。

![[Pasted image 20240116103715.png]]
```

### BN

loffe和Szegedy的开创性地引入了批归一化(BN)层，通过对特征统计进行归一化，显著地简化了前馈网络的训练。BN层的设计初衷是为了**加速识别网络的训练**[[@huang2017ICCV-AdaIN#^e16813]]，但后来被发现在生成图像模型中也是有效的。对于给定批处理输入x，BN对每个特征通道的均值和标准差进行归一化：

![[Pasted image 20240116101457.png|375]]


其中μc和σc是batch的均值和标准差，μ和β是从数据中习得。
BN在训练时使用mini-batch统计，在推理时使用常规的统计代替，造成了训练和推理的差异。为了解决这个问题，最近提出了批重正化，在训练期间逐步使用常规的统计数据。Li等人发现BN的另一个有趣应用：BN可以通过重新计算目标域的常规统计数据来减轻域偏移。

```ad-note
title: BN加速网络训练
BN 作用就是如果用_sigmoid_这样的激活函数，且样本点在没有尽量分布在0轴左右的话，就会导致整个训练过程非常缓慢，样本点越远离0轴，越缓慢，BN的操作使得每一层的输出都尽量较为分散的落在数轴0的两端，尽量使得数据处于梯度的敏感区域，加速梯度下降的过程，图如下
![[Pasted image 20240116103607.png|500]]
```

^e16813

### IN

在原始的前馈风格化方法中，风格迁移网络在每个卷积层之后包含一个BN层。令人惊讶的是，Ulyanov等发现，只需将BN层替换为IN层，就可以得到显著的改善：
![[Pasted image 20240116101705.png|425]]
- 和BN不同的是，IN的的μ(x）和σ(x)是对每个通道和每个样本独立计算的
- 另一个区别是，在测试时应用的层不变，而BN层通常使用常规统计代替mini-batch统计。

### CIN

条件实例归一化(CIN)层，该层对每种不同的风格s学习不同的参数集γs和βs：
![[Pasted image 20240116101833.png|500]]


在训练过程中，从一组固定的风格集合s∈1,2,…,S∈1,2,…,(实验中S=32)中随机选取一幅风格图像及其索引s。然后将内容图像输入到一个网络中，在CIN层使用对应的γs和βs。令人惊讶的是，**有着相同卷积参数、不同仿射参数的多个网络，可以生成完全不同风格的图像。**
与没有归一化层的网络相比，有CIN层的网络需要增加2FS2的附加参数，其中F为网络中feature map的数量。由于附加参数的数量与样式的数量成线性关系，因此很难用这个方法生成非常多的风格。而且，每添加一种新的风格，都需要重新训练一次网络。

### AdaIN

如果将输入归一化为由仿射参数指定的单一风格，是否有可能通过自适应仿射变换使其适应任意给定的风格？我们对IN进行了一个简单的扩展。我们称之为自适应实例归一化(AdaIN)。AdaIN接收一个内容输入x和一个样式输入y，并简单地将x的通道平均值和方差与y的平均值和方差匹配。**与BN、IN和CIN不同，AdaIN没有可以学习的仿射参数。相反，它自适应地从风格输入中计算仿射参数**：

![[Pasted image 20240112175444.png|525]]


![[Pasted image 20240112175426.png|375]]

相比于IN，我们仅仅是将两个仿射参数替换成了σ(y)和μ(y)，这两个统计值的依然是在空间位置上进行计算。

假设存在一个检测特定风格纹路的特征通道。具有这种纹路的风格图像将在该层产生较高的平均激活值。AdaIN产生的输出在保持内容图像的空间结构的同时，对该特征具有同样高的平均激活度。纹路特征可以通过前馈解码器转换到到图像空间。该特征通道的方差可以将更细微的风格信息传递到AdaIN输出和最终输出的图像中。

简而言之，AdaIN通过迁移特征统计量，即通道方向上的均值和方差，在特征空间中进行风格迁移。


## Method(s)


我们的风格迁移网络T以一个内容图像c和一个任意风格的图像s作为输入，并合成一个输出图像，该图像重新组合前者的内容和后者的样式。我们采用一种简单的encoder-decoder架构，其中encoder f 固定在预训练VGG-19的前几层（直到relu4_1）。在特征空间中对内容和风格图像进行编码后，我们将这两种特征图输入AdalN层，使内容特征图的均值和方差与风格特征图的均值和方差对齐，生成目标特征图t：

![[Pasted image 20240116102634.png|275]]

训练随机初始化的解码器 g 将 t 映射回图像空间，生成风格化图像 T (c, s)：

![[Pasted image 20240116102651.png|222]]

decoder大部分是encoder的镜像，所有池化层替换为最近的上采样，以减少棋盘效应。

我们在f和g中使用反射填充（torch.nn.ReflectionPad2d)来避免边界失真。

另一个问题是decoder应该使用IN、BN还是不使用标准化层。如第4节所述，IN将每个样本归为单个样式，而BN将一批样本归一化，以单个样式为中心。当我们希望decoder生成风格迥异的图像时，两者都是不可取的。因此，我们在decoder中不使用归一化层。





![[Pasted image 20240112175518.png|500]]


```ad-note
title: 棋盘效应
现象：棋盘效应是由于反卷积的“不均匀重叠”（Uneven overlap）的结果。使图像中某个部位的颜色比其他部位更深
![[Pasted image 20240116105328.png|475]]
原因：因为卷积核无法整除步长，就会导致在重复上采样绘图的部分不均匀
![[Pasted image 20240116105223.png|475]]
解决：“先进行插值Resize操作，再进行反卷积操作”来避免
![[Pasted image 20240116105408.png|500]]
该方式在超分辨率的相关论文中比较常见。例如我们可以用常见的图形学中常用的双线性插值和近邻插值以及样条插值来进行上采样。
```
## Experiment

- Dataset
    - Content: MS-COCO
    - Style: WikiArt
- Sample size: 80000
- Optimizer: adam
- Batch size: 8 content-style image pairs
- Resize: 512, RandomCrop: 256×256
- Model: VGG-19
- Loss: L=Lc+λLs


损失函数为内容损失和风格损失的加权和。这里设计了两个loss，都是利用decoder输出出来的图片再用一个encoder编码回去。

内容损失是目标特征与输出图像特征之间的欧氏距离。　第一个Lc计算和AdaIN输出的loss，这一步用来训练decoder是否正确解码了AdaIN的输出。我们使用AdaIN输出t作为内容目标，而不是内容图像：

![[Pasted image 20240116102939.png|169]]
由于AdaIN层只迁移了风格特征的平均值和标准差，所以我们的风格损失只与这些统计数据匹配。第二个Ls计算了原始图片的编码loss，这一步用来训练encoder是否可以正确编码信息。虽然我们发现常用的Gram矩阵损失可以产生类似的结果，但我们还是使用IN统计，因为它在概念上更清晰。

![[Pasted image 20240116102944.png|375]]
其中ϕ表示VGG-19中用于计算风格损失的层。在我们的实验中，我们在relu1_1, relu2_1, relu3_1, relu4_1中使用了相等的权重。


## Conclusion


## Notes


----

## Extracted Annotations

