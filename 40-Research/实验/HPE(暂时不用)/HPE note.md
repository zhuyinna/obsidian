# 总述

## 问题
  - 人体姿态估计——图像
  - 人体姿态跟踪——视频

## 概念
  人体姿态估计 (HPE) 是计算机视觉中的一项任务，专注于识别特定场景中人体的位置。大多数 HPE 方法都是基于使用光学传感器记录 RGB 图像来检测身体部位和整体姿势。这可以与其他计算机视觉技术结合使用，用于健身和康复、增强现实应用和监控。
  
  人体模型有三种常见类型：基于骨骼的模型、基于轮廓的模型和基于体积的模型。基于骨架的模型因其灵活性而成为人体姿态估计中最常用的模型。这是因为它由一组关节组成，如脚踝、膝盖、肩部、肘部、手腕和构成人体骨骼结构的肢体方向。
1.  骨架模型
     代表一系列的关节位置和相应的遵从人体骨架结构的肢体方向
     也可以描述为一个图，顶点代表关节，用边代表骨架结构中关节的链接和约束
2. 轮廓模型
    早期用的比较多
3.  体模型
    早期是圆锥圆柱，现在都用mesh
  ![[Pasted image 20230305220236.png]]

## 应用
1. 人体的动作行为估计
      要理解行人，人体的姿态估计其实是一个非常重要的中间层信息。目前有蛮多基于人体姿态估计直接做 action recogntion 的工作，比如把关键点当成 graph 的节点，然后是使用 graph convolution network 来整合各种信息做动作分类。我博士的研究课题是 action recognition，我读完四年博士的一个总结是 action 这个问题，如果需要真正做到落地，人体姿态估计算法是必不可少的组成部分。
2. 偏娱乐类
    比如人体交互，美体等。比如可以通过3D姿态估计来虚拟出一个动画人物来做交互，使用真实人体来控制虚拟人物。另外比如前一段时间比较火热的瘦腰，美腿等操作背后都可能依赖于人体姿态估计算法。
3. 作为其他算法的辅助环节
    比如 Person ReID 可以基于人体姿态估计来做 alignment，姿态估计可以用来辅助行人检测，杀掉检测的 FP 之类的。


## 分类
**分类I**
1.  generative（human body model-based)：  
    人体模型结构作为先验，几何上从不同视角投影到二位或三维空间，高维参数空间用回归的方式优化
2.  discriminative (human body model-free)  
    从输入源直接学习一个映射，或者搜索现有案例(不用人体模型)；更快但是对没有训练过的姿态健壮性不足
**分类 II**
  适用：多人 pose estimation
1.  top-down  
    先探测人，产生位置的bounding box
2.  bottom-up
    先预测每个人所有的身体部位，再用人体模型拟合或者其他算法进行分组
    当人变多时top-down计算花费明显提高，但如果有大规模的重叠，bottom-up方法在重组肢体上可能会遇到问题
**分类Ⅲ**
1.  regression-based  
    直接从输入图片map关节坐标，或则得到人体模型参数
2.  dectection-based(中间生成关节位置图像块或热图)
    将身体部位当作探测目标依据两个经常使用概念：关节部位的图像块和热图
    小区域表示鲁棒性更强；小区域的检测结果限制了最终关节坐标的精度
**分类Ⅳ**
1.  one-stage
2.  multi-stage
    有中间监督；例如先检测人的位置再顾及人体姿势
    3D的HPE先在2d表面预测关节位置再将它们拓展到3D空间


# 算法概述

## 2D 单人HPE
**特点**
  先检测出单人，依据标注的人的中心位置和身体比例从原始图像中剪裁
**方法**
1. regression-based
    通过一个端到端的框架直接学习和预测坐标位置
2. detection-based
    先通过学习关节的或身体部位的矩形框，或者热图(每个都通过一个一关节位置为中心的2D 高斯分布来显式一个关节位置)预测出身体部位的大致位置，再进行回归
    Soft-argmax函数能将热图转化为关节坐标；将一个dectection-based网络变成一个可微分的回归网络
**评价**
1. regression-based
    直接回归出坐标，缺点太多
2. detection-based
    每个关节占据一个热图通道用一个一目标关节位置为中心的2D 高斯分布
    因为热图表示比坐标表示更有鲁棒性，大部分最近的研究都基于热图表示
    有大量的工作在做这个方向
**代表算法**
  单人：CPM, Hourglass, CPN, MSPN, HRNet
**必读论文**
  **[[必读论文#2D HPE]]**
  ![[Pasted image 20230305224309.png]]

## 2D 多人 HPE
**特点**
  需要同时进行 detection 和 localization
**方法**
1. Top-down methods
    效果依赖人体目标检测的结果，速度较慢，大都是非实时的
2.  Bottom-up methods
    需要进行 joint dection 和 joint candiate grouping
    速度快，但是容易收到复杂背景和人体遮挡的影响
    SOTA 是 top-down 但是速度慢
**代表算法**
  多人
1. Top-down methods
    AlphaPose
2. Bottom-up methods
    OpenPose

## 3D 单人HPE
**特点**
  单眼相机应用非常广泛，深度神经网络有能力预测 dense depth 和 sparse depth points
**方法**
1. Model-free methods
    直接将图片映射到3D 位置
    从预测的 2D 姿态上接着预测深度信息
2. Model-based methods
    很多工作基于 SMPL(一个人体模型)，估计人体3D 参数
    运动学模型的运用也很广泛
    还有自监督学习（可以研究的一个方向)
    latent 3D pose model

## 3D 多人HPE
**特点**
1.  研究方向很新工作较少
2.  大都是多阶段

## 3D HMR
**方法**
1. Optimization-based Paradigm 基于优化
    Optimization-based approaches attempt to estimate a 3D body mesh that is consistent with 2D image observations.( 2D keypoints, silhouettes, segmentations.)即根据2D 检测结果优化生成3Dmseh. 代表作：[SMPLify](https://link.zhihu.com/?target=https%3A//smplify.is.tue.mpg.de/) (ECCV'2016).
2. Regression-based Paradigm 基于回归
    Regression-based methods take advantage of the thriving deep learning techniques to directly process pixels.即使用深度学习技术直接处理图像像素生成3Dmesh。代表作：[HMR](https://link.zhihu.com/?target=https%3A//akanazawa.github.io/hmr/) (CVPR'2018)
3. 基于优化+回归
    代表作: [SPIN](https://link.zhihu.com/?target=https%3A//www.seas.upenn.edu/~nkolot/projects/spin/) (ICCV'2019)（相当于HMR+SMPLify）
**必读论文**
    ![[Pasted image 20230305224738.png]]
    
 ```ad-cite
 [1] [SMPLify](https://link.zhihu.com/?target=https%3A//smplify.is.tue.mpg.de/) (ECCV'2016):《Keep it SMPL: Automatic Estimation of 3D Human Pose and Shape from a Single Image》 
 
 [2] [SMPLify-X](https://link.zhihu.com/?target=https%3A//smpl-x.is.tue.mpg.de/) (CVPR'2019):《Expressive Body Capture: 3D Hands, Face, and Body from a Single Image》
 
 [3] [HMR](https://link.zhihu.com/?target=https%3A//akanazawa.github.io/hmr/) (CVPR'2018):《End-to-end Recovery of Human Shape and Pose》  
  
  [4] [SPIN](https://link.zhihu.com/?target=https%3A//www.seas.upenn.edu/~nkolot/projects/spin/) (ICCV'2019):《Learning to Reconstruct 3D Human Pose and Shapevia Model-fitting in the Loop》  
  
  [5] [VIBE](https://link.zhihu.com/?target=https%3A//github.com/mkocabas/VIBE) (CVPR'2020):《 Video lnference for Human Body Pose and Shape Estimation》  
  
  [6] [HybrIK](https://link.zhihu.com/?target=https%3A//jeffli.site/HybrIK/) (CVPR'2021):《HybrIK: A Hybrid Analytical-Neural Inverse Kinematics Solution for 3D Human Pose and Shape Estimation》  
  
  [7] [PARE](https://link.zhihu.com/?target=https%3A//pare.is.tue.mpg.de/) (ICCV'2021):《PARE: Part Attention Regressor for 3D Human Body Estimation》  
  
  [8] [HuMoR](https://openaccess.thecvf.com/content/ICCV2021/papers/Rempe_HuMoR_3D_Human_Motion_Model_for_Robust_Pose_Estimation_ICCV_2021_paper.pdf) (2021) :《3D Human Motion Model for Robust Pose Estimation》  
  
  [9] [DeciWatch](https://link.zhihu.com/?target=https%3A//ailingzeng.site/deciwatch) (ECCV'2022):《DeciWatch: A Simple Baseline for 10× Efficient 2D and 3D Pose Estimation》  
  
  [10] [SmoothNet](https://link.zhihu.com/?target=https%3A//ailingzeng.site/smoothnet) (ECCV'2022):《SmoothNet: A Plug-and-Play Network for Refining Human Poses in Videos》  
  
  [11] [ExPose](https://link.zhihu.com/?target=https%3A//expose.is.tue.mpg.de/) (ECCV'2020):《Monocular Expressive Body Regression through Body-Driven Attention》  
  
  [12]  [BalancedMSE](https://link.zhihu.com/?target=https%3A//sites.google.com/view/balanced-mse/home) (CVPR'2022):《Balanced MSE for Imbalanced Visual Regression》

```


# 发展历程

## 过去
  这部分主要用于描述在深度学习之前，我们是如何处理人体姿态估计这个问题。从算法角度来讲，这部分的工作主要是希望解决单人的人体姿态估计问题，也有部分工作已经开始尝试做3D 的人体姿态估计。可以粗略的方法分成两类。
1. 第一类
    直接通过一个全局 feature，把姿态估计问题当成分类或者回归问题直接求解 [^1][^2]。但是这类方法的问题在于精度一般，并且可能比较适用于背景干净的场景。
2. 第二类
    基于一个 graphical model，比如常用 pictorial structure model。一般包含 unary term,是指对单个 part 进行 feature 的 representation，单个 part 的位置往往可以使用 DPM (Deformable Part-based model)来获得。同时需要考虑 pair-wise 关系来优化关键点之间的关联。基于 Pictorial Structure，后续有非常多的改进，要么在于如何提取更好的 feature representation [^3][^4]，要么在于建模更好的空间位置关系[^5][^6]。
  总结一下，在传统方法里面，需要关注的两个维度是： **feature representation**以及**关键点的空间位置关系**。特征维度来讲，传统方法一般使用的 HOG, Shape Context, SIFT 等 shallow feature。空间位置关系的表示也有很多形式，上面的 Pictorial structure model 可能只是一种。

  这两个维度在深度学习时代也是非常至关重要的，只是深度学习往往会把特征提取，分类，以及空间位置的建模都在一个网络中直接建模，所以不需要独立的进行拆解，这样更方便设计和优化。
  
## 现在
  从2012年 AlexNet 开始，深度学习开始快速发展，从最早的图片分类问题，到后来的检测，分割问题。在2014年，[^7]第一次成功引入了 CNN 来解决单人姿态估计的问题。因为当时的时代背景，整体网络结构比较简单，同时也沿用了传统骨架的思路。首先是通过 slide-window 的方式，来对每个 patch 进行分类，找到相应的人体关键点。因为直接 sliding-window 少了很多 context 信息，所以会有很多 FP 的出现。所以在 pipeline 上面加上了一个 post-processing 的步骤，主要是希望能抑制部分 FP，具体实现方式是类似一个空间位置的模型。所以从这个工作来看，有一定的传统姿态估计方法的惯性，改进的地方是把原来的传统的 feature representation 改成了深度学习的网络，同时把空间位置关系当成是后处理来做处理。总体性能在当时已经差不多跑过了传统的姿态估计方法。
  
  2014年的另外一个重要的进展是引入了 [MPII](https://link.zhihu.com/?target=http%3A//human-pose.mpi-inf.mpg.de/%23overview) 的数据集。此前的大部分 paper 都是基于 FLIC 以及 LSP 来做评估的，但是在深度学习时代，数据量还是相对偏少（K 级别）。MPII 把数据量级提升到 W 级别，同时因为数据是互联网采集，同时是针对 activity 来做筛选的，所以无论从难度还是多样性角度来讲，都比原来的数据集有比较好的提升。
  
  一直到2016年，随着深度学习的爆发，单人姿态估计的问题也引来了黄金时间。这里需要重点讲一下两个工作，一个工作是 Convolutional Pose Machine (CPM）[^8]，另外一个是 Hourglass [^9]。

**DeepPose (2014)**
**CPM (2016)**
**Hourglass**
**OpenPose**
**Hourglass + Associative Embedding**
**CPN**
**MSPN**
**HRNet**
**Simple Baselines**
**3D Skeleton**
  


## 未来
  深度学习带来了学术界以及工业界的飞速发展，极大的提升了目前算法的结果，也使得我们开始关注并尝试解决一些更有挑战性的问题。

  下面的几点我是侧重于把人体姿态估计真正落地到产品中而展开的。当然也可以换个维度考虑更长线的研究发展，这个可能希望以后有机会再一起讨论。

-   Data Generation

  我觉得这个是一个非常重要的研究方向，不管是对2d 还是3d。以2d 为例，虽然目前数据量已经非常的大，比如 COCO 数据，大概有6w+的图片数据。但是大部分 pose 都是正常 pose，比如站立，走路等。对于一些特殊 pose,比如摔倒，翻越等并没有多少数据。或者可以这么理解，这些数据的收集成本很高。如果我们可以通过生成数据的方法来无限制的生成出各种各样的数据的话，这个对于算法的提升是非常的关键。虽然目前 GAN 之类的数据生成质量并不高，但是对于人体姿态估计这个问题来讲其实已经够了，因为我们不需要清晰真实的细节，更多的是需要多样性的前景（不同着装的人）和 pose。但是数据生成的方式对于人体姿态估计本身也有一个非常大的挑战，这个可以留做作业，感兴趣的同学可以在留言区回复。

-   Crowd的问题

  这个问题其实是行人检测的问题。目前市面上没有能针对拥挤场景很 work 的行人检测算法。这个问题的主要瓶颈在于行人检测的一个后处理步骤：NMS （Non-maximum suppression)。这个其实是从传统物体检测方法时代就有的问题。因为目前大部分算法不能区分一个行人的两个框还是两个不同行人的两个框，所以使用 NMS 来基于 IOU 用高分框抑制低分框。这个问题在传统的 DPM 以及 ACF 时代问题并不突出，因为当时算法精度远没有达到需要考虑 NMS 的问题。但是随着技术的进步，目前 NMS 已经是一个越来越明显的瓶颈，或者说也是行人检测真正落地的一个很重要的障碍。最近我们提出了一个新的数据集 CrowdHuman，希望引起大家对于遮挡拥挤问题的关注。从算法上面来讲，最近也陆续开始由蛮多不错的工作在往这个方向努力，但是离解决问题还是有一定的距离。回到人体姿态估计这个问题，目前 top-down 方法依赖于检测，所以这个问题避免不了。 bottom-up 可能可以绕开，但是从 assemble 行人的角度，拥挤场景这个问题也非常有挑战。

-   Multi-task Learning

  刚刚我们讲到，2D 以及3D 人体姿态估计可以联合 training，从而提升整体结果。同样，其实可以把人体姿态估计跟人体相关的其他任务一起联合做数据的标注以及训练。这里可以考虑的包括人体分割(human segmentation)，人体部位的 parse (human parse)等。可以这么理解，human seg 本身的标注可以认为是多边形的标注，我们可以在多边形轮廓上面进行采点，这几个任务可以很自然的联合起来。人体多任务的联合训练我觉得对于充分理解行人是非常有意义的，同时也可以提升各个任务本身的精度。当然潜在的问题是数据标注的成本会增加。另外可以考虑的是跨数据集的联合 training，比如某个数据集只有 skeleton 标注，有个数据集只有 seg 标注等，这个问题其实也是工业界中很常见的一个问题。

-   Speed

  速度永远是产品落地中需要重点考虑的问题。目前大部分学术 paper 可能都是在 GPU 做到差不多实时的水平，但是很多应用场景需要在端上，比如手机的 ARM 上面进行实时高效的处理。我们之前有尝试过使用我们自己的 ThunderNet [24]做人体检测，然后拼上一个简化版的 CPN 来做人体姿态估计，可以做到端上近似实时的速度，但是效果跟 GPU 上面还是有一定差距。所以速度的优化是非常有价值的。

-   UnConstrained 3D skeleton Benchmark

  这个我上面也有提到，3D 人体姿态估计急需一个更大更有挑战的 benchmark 来持续推动这个领域的进步。随着很多3d sensor 的普及，我理解我们不一定需要依赖传统的多摄像头的 setting 来做采集，这个使得我们能获得更真实，更 wild 的数据。


# 相关模块
## 数据集
**2D**
|   数据集    | DESC |
|:-----------:|:----:|
|    FILC     |      |
|     LSP     |      |
|     LIP     |      |
|    MPII     |      |
|    COCO     |      |
|   AIC-HKD   |      |
| Penn Action |      |
|   J-HMDB    |      |
|  PoseTrack  |      |

**3D**
|           数据集           |                                                                                        DESC                                                                                         |                                          链接                                          |
|:--------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
|         Human3.6M          | the largest benchmark dataset for human motion analysis, with 3.6 million body poses; <br> It comprises 15 complex action categories, each one performed by seven actors individually | [Paperswithcode](https://paperswithcode.com/sota/3d-human-pose-estimation-on-human36m) |
|           AMASS            |                                            The Archive of Motion Capture as Surface Shapes is a recently published human motion dataset                                             |                                                                                        |
| DPW (3D Poses in the Wild) |                                                               s the first dataset with accurate 3D poses in the wild                                                                |                                                                                        |
|      HumanEva-I & II       |                                        includes 3 subjects that perform different actions captured at 60fps. Each person has 15 body joints                                         |                                                                                        |
|       TNT15 Dataset        |                                                                                                                                                                                     |                                                                                        |
|        MPI-INF-3DHP        |                                                                                                                                                                                     |                                                                                        |
|    TotalCapture Dataset    |                                                                                                                                                                                     |                                                                                        |
|    MARCOnI Dataset (乱)    |                                                                                                                                                                                     |                                                                                        |
|      Panoptic Dataset      |                                                                                                                                                                                     |                                                                                        |
|        3DPW Dataset        |                                                                                                                                                                                     |                                                                                        |
|         DensePose          |                                                                                     3D 的 shape                                                                                     |                                                                                        |

**单人**
| 数据集 | DESC |
|:------:|:----:|
|  FILC  |      |
|  LSP   |      |
|  LIP   |      |
|  MPII  |      |

**多人**
|  数据集   | DESC |
|:---------:|:----:|
|   COCO    |      |
| CrowdPose |      |

**人体姿态跟踪**
|  数据集   | DESC |
|:---------:|:----:|
| PoseTrack |      |

**人体 HMR**
| 数据集 | DESC | 链接 |
| ------ | ---- | ---- |
| 3DPW   |- 3D POSES IN THE WILD DATASET     | [paperswithcode](https://paperswithcode.com/sota/3d-human-pose-estimation-on-3dpw?metric=MPJPE)     |


## 评估指标
**2D**
1.  Percentage of Correct Parts(PCP)
2.  Percentage of Correct Keypoints(PCK)
3.  AP
    每个点是单独算precision的，最后算所有点的平均
4.  GFLOPs(速度)
**3D**
  displacement error (DE)
  1,2,3 来自 [[A generic diffusion - based approach for 3D human pose prediction in the wild]]
  4,5 来自[[DiffuPose - Monocular 3D Human Pose Estimation via Denoising Diffusion Probabilistic Model]]
1. Average Displacement Error (ADE) 
    the average of DE for the whole sequence
2. Final Displacement Error (FDE) 
    as DE in the final predicted frame
3. multi-modal versions of ADE (MMADE) and FDE (MMFDE)
4. MPJPE(Mean Per Joint Position Error)----protocal #1 $\downarrow$ 
    is computed as the mean Euclidean distance between the estimated and ground-truth 3D joints in millimeters
     - ![[Pasted image 20230304171445.png|325]]
5. P-MPJPE (Procrustes MPJPE) ----protocal #2 
    which is computed the same as MPJPE after rigidly aligning the estimated 3D joints to the groundtruth
    先经过旋转、对齐等变换再进行 MPJPE
6. N-MPJPE----Protocol #3 
    aligns predicted poses with the ground-truth only in scale (N-MPJPE) following [45] for semi-supervised experiments
    先进行规模对齐再进行 MPJPE
7. PCK 和 AUC


## 调研
[2021人体姿态综述](https://blog.csdn.net/flyfor2013/article/details/120465629)
宏观：
目前，通常采用两阶段方法来解决该问题：自顶向下方法，即先检测图片多个人体的位置，之后对检测到的每个人使用单人3D 姿态估计模型来分别预测其姿态；自底向上方法，即先检测图片中所有人的3D 关键点，之后通过相关性将这些关键点分配给对应的人体。


# Reference

[^1]: Randomized Trees for Human Pose Detection, Rogez etc, CVPR 2018
[^2]: Local probabilistic regression for activity-independent human pose inference, Urtasun etc, ICCV 2009
[^3]: Strong Appearance and Expressive Spatial Models for Human Pose Estimation, Pishchulin etc, ICCV 2013
[^4]: Pictorial Structures Revisited: People Detection and Articulated Pose Estimation, Andriluka etc, CVPR 2009
[^5]: Latent Structured Models for Human Pose Estimation, Ionescu etc, ICCV 2011
[^6]: Poselet Conditioned Pictorial Structures, Pishchulin etc, CVPR 2013
[^7]: Learning Human Pose Estimation Features with Convolutional Networks, Jain etc, ICLR 2014
[^8]: Convolutional Pose Machines, Wei etc, CVPR 2016
[^9]: Stacked Hourglass Networks for Human Pose Estimation, Newell etc, ECCV 2016
[^10]: Multi-Context Attention for Human Pose Estimation, Chu etc, CVPR 2017
[^11]: Deeply Learned Compositional Models for Human Pose Estimation, ECCV 2018
[^12]: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields, Cao etc, CVPR 2017
[^13]: Associative Embedding: End-to-End Learning for Joint Detection and Grouping, Newell etc, NIPS 2017
[^14]: DeepCut: Joint Subset Partition and Labeling for Multi Person Pose Estimation, Pishchulin etc, CVPR 2016
[^15]: DeeperCut: A Deeper, Stronger, and Faster Multi-Person Pose Estimation Model, Insafutdinov, ECCV 2016
[^16]: Cascaded Pyramid Network for Multi-Person Pose Estimation, Chen etc, CVPR 2017
[^17]: Rethinking on Multi-Stage Networks for Human Pose Estimation, Li etc, Arxiv 2018
[^18]: Deep High-Resolution Representation Learning for Human Pose Estimation, Sun etc, CVPR 2019
[^19]: Simple Baselines for Human Pose Estimation and Tracking, Xiao etc, ECCV 2018
[^20]: 3D Human Pose Estimation = 2D Pose Estimation + Matching, Chen etc, CVPR 2017
[^21]: A simple yet effective baseline for 3d human pose estimation, Martinez, ICCV 2017
[^22]: Compositional Human Pose Regression, Sun etc, ICCV 2017
[^23]: Densepose: Dense Human Pose Estimation in the Wild, Guler etc, CVPR 2018
[^24]: ThunderNet: Toward Real-time Generic Object Detection, Qin etc, ICCV 2019
