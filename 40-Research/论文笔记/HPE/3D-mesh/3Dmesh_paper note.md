
## Weakly-Supervised 3D Human Pose Learning via Multi-view Images in the Wild

CVPR2020


![[Pasted image 20230912104315.png]]

```ad-question
弱监督？
multi-view？
野外和常见的人体姿态估计有什么区别？
```


## Fusion : Latent Diffusion for Behavior-Driven Human Motion Prediction



## 综述： Deep Generative Models

#### conclusion
深度 3D 生成模型，例如 VAE 和 GAN，旨在表征观察到的 3D 数据的数据分布。 3D 生成任务的一个关键挑战是用于描述 3D 实例的 3D 表示有很多，并且每种表示对于生成建模都有其自身的优点和缺点。本文通过讨论不同的 3D 表示如何与不同的生成模型相结合，对 3D 生成进行了全面的回顾。我们首先介绍 3D 生成模型的基础知识，包括生成模型和 3D 表示的公式。然后，我们回顾了如何在 2D 和 3D 数据的 3D 生成学习任务中分别建模和生成 3D 表示。然后，我们讨论 3D 生成模型的应用，包括形状编辑、3D 感知图像处理、重建和表示学习。最后，我们强调了现有 3D 生成模型的局限性，并提出了几个未来的方向。我们希望这篇综述能够帮助读者更好地理解 3D 生成模型领域，并激发未来新颖、创新的研究。

#### 论文内容

1. Voxel  Grids
   与 2D GAN 相比，3D GAN 中的生成器和鉴别器是使用一系列 3D 卷积块构建的，以实现 3D 体素数据的处理。在实践中，他们构建了一个编码器来将 2D 图像映射到其相应生成器的潜在空间中，与 VAE-GAN [143] 非常相似。除了传统的对抗性损失之外，它们还包含两个用于编码器训练的组件：重建损失和 KL 散度损失。这些附加元素用于约束编码器的输出分布。由于其类似 VAE-GAN 的设计，所提出的模型也可以用于从 2D 观察中恢复 3D 形状。他们还证明，**在没有任何监督的情况下学习的判别器可以成功地转移到多个具有良好性能的 3D 下游任务**。考虑到 GAN 模型的训练不稳定，[138]尝试训练变分自动编码器来对形状分布进行建模。它首先使用由四个 3D 卷积层和全连接层组成的编码器网络将输入体素映射到潜在向量，然后使用具有相同但反转架构的 3D 解码器将潜在向量转换为 3D 体素。

```ad-question
为什么GAN训练不稳定？
```

2. Point Cloud
   作为开创性的工作，Achlioptas 等人。 [27]利用生成对抗网络来学习 3D 点云的分布。它提出了原始点云 GAN (rGAN) 和潜在空间 GAN (l-GAN)。 r-GAN 的生成器是一个具有5个全连接层的 MLP 网络，它将随机采样的噪声向量映射到具有2048个点的点云。相应的鉴别器使用 PointNet [32]作为网络主干。阿克利奥塔斯等人。 [27]发现 r-GAN 很难生成高质量的点云。一个可能的原因是 GAN 很难收敛到一个好的点。为了克服这个问题，他们提出了一种新颖的训练框架，**该框架训练生成对抗网络来对预训练自动编码器的潜在空间进行建模，称为 l-GAN。 l-GAN 的性能比 r-GAN 好得多**。
   
   点云的 GAN 生成器通常实现为全连接网络，**无法有效利用本地上下文来生成点云。为了解决这个问题，一些方法[98]、[149]、[150]、[151]提出基于图卷积构造 GAN 生成器**。例如，给定一个采样的潜在向量，Valsesia 等人。 [149]首先使用 MLP 网络来预测一组点特征，将其视为图并由图卷积网络进行处理。对点云进行上采样时，它将图卷积应用于点特征以获得新的特征向量，将其与原始点特征连接以产生上采样的点集。点云生成的另一个挑战是合成高分辨率点云很容易消耗大量内存。拉马辛格等人。 [152]通过在**谱域中采用 GAN 模型来降低计算复杂度。**它将点云表示为球形

3. Neural Fields
   神经场使用神经网络来预测 3D 空间中任何点的属性。它们大多数采用 MLP 网络来参数化 3D 场景，理论上可以对任意空间分辨率的形状进行建模，这比体素网格和点云具有更高的内存效率。尽管神经表示在形状建模方面具有优越性，**但由于神经表示格式缺乏真实数据以及直接用神经网络处理神经表示的困难，因此在这些表示上应用常见的生成模型（例如 GAN）并不简单**。为了克服这个问题，一些方法使用自动解码器[160]来对分布进行建模。 gDNA [161] 采用自动解码器来生成动态人类。基于 3D CNN 的特征生成器首先将形状潜在代码处理为特征量，然后通过 MLP 网络将其进一步解码为占用值和特征向量。邓等人。 [104] 旨在保护生成形状时的形状对应关系。 MLP 网络用于表示在所有实例之间共享的模板有符号距离场。变形和校正场由模板空间中的另外两个 MLP 建模。 DualSDF [162] 学习共享的潜在空间以实现语义感知的形状操作。采样的潜在代码将由处理不同粒度级别的两个网络进行处理。一种是使用 SDF 来捕捉精细细节，另一种是使用简单的形状基元来表示粗略形状。在给定形状和两个表示的生成形状之间计算两个重建损失。
   
   为了基于生成对抗网络生成隐式字段，一些方法在潜在空间中或使用转换后的显式表示来区分生成的隐式字段。陈等人。 [28]将鉴别器应用于潜在空间。首先使用自动编码器从一组形状中学习特征，**其中编码器可以是 3D CNN 或 PointNet [32]，解码器使用 MLP 网络进行参数化。然后，采用潜在 GAN [27]、[163] 来训练预训练编码器提取的特征。** 伊宾等人。 [164] 也利用潜在 GAN，但提出了一种**混合表示作为学习的中间特征**，以实现对生成形状的空间控制。潜在表示结合了体素网格和隐式场，因此每个单元覆盖了形状的一部分。
   
   hybrid presentation 作为中间特征：克莱内伯格等人[165]生成有符号距离场并设计两种类型的鉴别器，基于体素的（例如，3D CNN）和基于点的（例如，PointNet）用于训练。在基于体素的情况下，固定数量的点被输入生成器以查询带符号的距离值。在基于点的情况下，可以查询任意序列的点以获取带符号的距离值。 SurfGen [166] 开发了一种可微算子，通过行进立方体 [167] 从隐式场中提取表面，然后在表面上执行可微球面投影，这是一种显式的形状表示。球形鉴别器在显式表面上运行以监督形状生成器的学习
   
   扩散模型：随着扩散模型的发展，应用强大的生成模型来学习神经场的分布变得很有趣。 [168]通过使用隐式神经表示来表示数据并直接在隐式函数的调制权重上学习扩散模型来开始最初的尝试。然而，与基于 GAN 的方法的结果相比，生成的结果比较模糊。 [169]和[170]利用自动编码器将 SDF 表示压缩为潜在表示，然后使用扩散模型对潜在空间上的分布进行建模。一些工作[171]、[172]用三平面表示神经场，并首先从多视图数据集中获得三平面表示。然后，采用扩散模型对这些三平面表示的分布进行建模。

4. mesh
   挑战性：由于两个因素。首先，网格是非欧几里得数据，不能直接由卷积神经网络处理。其次，网格生成需要合成具有网格顶点之间合理连接的网格，这是很难实现的。
   
   为了避免处理网格的不规则结构，Ben-Hamu 等人。 [134]提出了一种称为多图表结构的类似图像的表示来参数化网格。它们在基础网格上定义一组标志点，每个标志点三元组对应一个函数，该函数在图像域上的图表和形状表面之间建立对应关系。通过用多图表结构表示网格，该方法可以利用成熟的图像 GAN 技术来生成形状。然而，参数化技巧需要生成的网格与定义多图表结构时使用的基础网格之间具有一致的拓扑。为了使生成过程更容易，SDM-Net [175]将训练网格注册到单位立方体网格中，这使得它们能够具有与模板立方体网格相同的连接性。 SDM-Net 利用变分自动编码器来学习网格的分布，其中编码器和解码器是通过网格上定义的卷积算子实现的。基于 SDM-Net [175]，TM-Net [174]在模板立方体网格上额外定义了纹理空间，并使用基于 CNN 的 VAE 来合成纹理图，将其与生成的网格相结合以产生纹理网格。 PolyGen [204] 尝试基于自回归生成模型来综合网格的连接性。它开发了一个基于变压器的网络来顺序生成网格顶点和面。与 PointGrow [158] 类似，PolyGen 沿垂直轴对网格顶点进行排序，并利用顶点转换器来生成顶点。然后，使用以生成的网格顶点为条件的面变换器来预测网格面。刘等人。 [176]使用四面体网格参数化 3D 网格，每个网格都与变形偏移和 SDF 值相关联。这种表示被视为扩散模型的输入，以对基础分布进行建模。吕等人。相反，[177]引入点云作为中间表示，并利用点云扩散模型来生成形状。

```ad-question
什么是欧几里得数据？
```


![[Pasted image 20230913164734.png]]




#### 2D 数据
与直接使用形状进行训练的 3D 数据监督方法相比，大多数基于 2D 数据的生成方法是通过可微分神经渲染由图像进行监督，因为用于训练生成模型的可渲染 3D 表示的高质量和大规模数据集很少。由于缺乏可渲染的 3D 表示，自动编码器架构很少在此任务中使用。相反，大多数方法采用生成对抗模型，从潜在空间中采样潜在向量并将其解码为目标表示

These include depth/normal maps, voxel grids, and neural fields. **Point clouds and meshes are not well explored in generative image synthesis, partly because current differentiable neural rendering cannot provide effective gradient signals** to optimize these two representations easily.

1. Depth/Normal Maps
   深度和法线贴图是易于访问的表示，可部分揭示 3D 场景或对象的几何形状。由于它们仅显示一侧的几何形状，因此通常称为 2.5D 表示。深度图和法线图可以轻松参与图像生成（即由 2D 卷积神经网络而不是 3D 架构处理），因为它们共享与 2D 图像类似的数据格式。大多数方法 [107]、[178]、[179] 利用 GAN 模型来生成深度或法线图以进行 3D 感知图像合成。


2. Neural Field
   基于神经场的图像合成方法一般采用 MLP 网络隐式表示3D 空间中每个点的属性，然后通过可微渲染器输出特定视点下的图像。体积渲染器[70]是最常用的渲染器用于 3D 感知图像合成。大多数方法使用 GAN 来监督神经领域的学习。 GRAF[29]首先引入了生成神经辐射场的概念。基于 MLP 的生成器以形状噪声和外观噪声为条件，并预测沿每条射线的点的密度和颜色。然后，体积渲染器沿着所有光线收集信息以合成 2D 图像。由于渲染过程缓慢，因此使用基于补丁的鉴别器来区分真假补丁，而不是完整的图像。 π-GAN [30]使用与 GRAF 类似的设置，但它采用 SIREN [212]而不是 ReLU MLP 进行表示，更能够对精细细节进行建模。它利用基于图像的鉴别器进行渐进式训练。此外，π-GAN 没有使用两个潜在代码，而是采用类似 StyleGAN 的映射网络，通过 FiLM 调节 [213]、[214] 在潜在代码上调节 SIREN。尽管上述方法显着提高了 3D 感知图像合成的质量，但它们仍然面临一些挑战。首先，渲染图像的良好质量并不意味着良好的基础形状并保证视图间的一致性。其次，由于沿所有光线查询的点数量巨大且渲染过程复杂，从模型渲染图像需要花费大量时间。因此，很难在高分辨率图像上有效地训练模型。第三，它们都假设数据集上相机姿势的先验分布，这可能不够准确。


 ## 综述：Human Motion Generation
 ![[Pasted image 20230914195659.png]]

 
我们首先介绍人体运动和生成模型的背景，然后检查三个主流子任务的代表性方法：文本条件、音频条件和场景条件人体运动生成。此外，我们还提供了常见数据集和评估指标的概述。最后，我们讨论开放问题并概述未来潜在的研究方向。
   ![[Pasted image 20230914102156.png]]
随着深度学习[17]的兴起，近年来各种生成方法迅速发展，例如自回归模型[18]、变分自编码器（VAE）[19]、归一化流[20]、生成对抗网络（GAN） ）[21]，以及去噪扩散概率模型（DDPM）[22]。这些方法在不同领域取得了巨大成功，包括文本[23]、[24]、图像[25]、[26]、[27]、视频[28]、[29]、[30]和3D 对象[ 31]，[32]。**另一方面，人体建模[33]、[34]、[35]方面的显着进展使得从视频[36]、[37]、[38]中提取人体运动并构建大规模人体运动数据集变得更加容易[39]、[40]、[41]、[42]。**

《人体建模》
[33] M. Loper, N. Mahmood, J. Romero, G. Pons-Moll, and M. J. Black, “Smpl: A skinned multi-person linear model,” ACM Trans. Graph., vol. 34, no. 6, pp. 1–16, 2015. 
[34] G. Pavlakos, V. Choutas, N. Ghorbani, T. Bolkart, A. A. A. Osman, D. Tzionas, and M. J. Black, “Expressive body capture: 3D hands, face, and body from a single image,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2019, pp. 10 975–10 985. 
[35] J. Romero, D. Tzionas, and M. J. Black, “Embodied hands: Modeling and capturing hands and bodies together,” ACM Transactions on Graphics, (Proc. SIGGRAPH Asia), vol. 36, no. 6, 2017.
《从视频中提取 human motion》
[36] J. Martinez, R. Hossain, J. Romero, and J. J. Little, “A simple yet effective baseline for 3d human pose estimation,” in Proc. Int. Conf. Comput. Vis., 2017, pp. 2640–2649.
[37] D. Pavllo, C. Feichtenhofer, D. Grangier, and M. Auli, “3d human pose estimation in video with temporal convolutions and semisupervised training,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2019, pp. 7753–7762. 
[38] M. Kocabas, N. Athanasiou, and M. J. Black, “Vibe: Video inference for human body pose and shape estimation,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2020, pp. 5253–5263. 
《数据集》
[39] C. Ionescu, D. Papava, V. Olaru, and C. Sminchisescu, “**Human3.6m**: Large scale datasets and predictive methods for 3d human sensing in natural environments,” IEEE Trans. Pattern Anal. Mach. Intell., 2014. 
[40] N. Mahmood, N. Ghorbani, N. F. Troje, G. Pons-Moll, and M. J. Black, “**AMASS**: Archive of motion capture as surface shapes,” in Proc. Int. Conf. Comput. Vis., Oct. 2019, pp. 5441–5450. [41] Z. Yu, J. S. Yoon, I. K. Lee, P. Venkatesh, J. Park, J. Yu, and H. S. Park, “**Humbi**: A large multiview dataset of human body expressions,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2020. 
[42] Z. Cai, D. Ren, A. Zeng, Z. Lin, T. Yu, W. Wang, X. Fan, Y. Gao, Y. Yu, L. Pan, F. Hong, M. Zhang, C. C. Loy, L. Yang, and Z. Liu, “**Humman**: Multi-modal 4d human dataset for versatile sensing and modeling,” in Proc. Eur. Conf. Comput. Vis., October 2022.


### Action to Motion
于等人。 [87]介绍了 SA-GAN，它利用具有 GAN 架构的基于自注意力的图卷积网络（GCN）。他们还建议通过使用两种鉴别器来增强生成能力——一种基于帧，另一种基于序列。同样，Kinetic-GAN [91] 结合了 GAN 和 GCN 的优点，并进一步利用潜在空间解缠和随机变化来生成高质量和多样化的人体运动。郭等人。 [7] 介绍了 Action2Motion，一种基于门控循环单元 (GRU) 的每帧 VAE 架构，用于生成运动序列。类似地，ACTOR [89] 采用序列级 CVAE 模型，该模型使用 Transformer 作为非自回归生成运动序列的骨干。这种非自回归方法允许一次性生成运动序列。 ODMO [93]采用了一种在低维潜在空间内应用对比学习的新颖策略，从而生成运动序列的分层嵌入。该模型在生成运动序列之前首先创建运动轨迹，从而有利于轨迹控制。此外，PoseGPT [94] 利用自回归变换器将人体运动编码为量化的潜在表示，随后采用类似 GPT 的模型来预测该离散空间内的下一个运动索引。塞万提斯等人。 [97]介绍了一种使用隐式神经表示（INR）和拟合条件高斯混合模型（GMM）的方法。该方法通过从每个训练序列的变分分布中提取表示来控制序列的长度和动作类别。此外，MDM [14] 利用扩散模型来预测每个扩散步骤的样本，而不仅仅是噪声。 MLD [100] 从潜在扩散模型（LDM）[168] 中汲取灵感，采用潜在水平扩散和 VAE 来生成运动。


![[Pasted image 20230914214251.png]]

