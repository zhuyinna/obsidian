---
Authors: Saeed Saadatnejad, Ali Rasekh, Mohammadreza Mofayezi, Yasamin Medghalchi, Sara Rajabzadeh, Taylor Mordan, Alexandre Alahi
Date: 2022-10
Topics: DM+HPE
Keywords: first DM+HPE; TCD(short&longterm);pre&postprocess;
---
tags: #论文笔记 

## Zotero Links 
* PDF Attachments
	- [arXiv Fulltext PDF](zotero://open-pdf/library/items/MQLSYR3V) 
* [Local library](zotero://select/items/1_FA9RPBAC) 


## Abstract

3D human pose forecasting, i.e., predicting a sequence of future human 3D poses given a sequence of past observed ones, is a challenging spatio-temporal task. It can be more challenging in real-world applications where occlusions will inevitably happen, and estimated 3D coordinates of joints would contain some noise. We provide a unified formulation in which incomplete elements (no matter in the prediction or observation) are treated as noise and propose a conditional diffusion model that denoises them and forecasts plausible poses. Instead of naively predicting all future frames at once, our model consists of two cascaded sub-models, each specialized for modeling short and long horizon distributions. We also propose a generic framework to improve any 3D pose forecasting model by leveraging our diffusion model in two additional steps: a pre-processing step to repair the inputs and a post-processing step to refine the outputs. We investigate our findings on four standard datasets (Human3.6M, HumanEva-I, AMASS, and 3DPW) and obtain significant improvements over the state-of-the-art. The code will be made available online.


## Summary
  第一个提出在 HPE 中运用 DM 的研究，主要创新点：
  1. TCD
     时间级联扩散
       - short-term 预测
       - long-term 预测
  2. pre & post process
     能够用在任意模型上，提升效果
       - pre-process: 对图像进行噪声和遮挡进行处理（用到了DM）
       - post-process：finetuning，更接近真实分布（TCAD）
  


## Conclusions
  1. a stochastic diffusion model suitable to imperfect input data observations happening in the wild-----two levels: short term and long term
  2. create a black-box:  improve any state-of-the-art model in a black-box manner ---It adds two additional stages: a pre-processing to rectify noisy observations before feeding them to the predictor, and a post-processing to finetune the predicted poses.
 

## Method(s)
  ![[Pasted image 20230302185641.png]]
### A. notation
  $[X]$  **clean complete normalized sequence** of human body poses with J joints in O frames of observation
  $[\widetilde{X}]$ 遮挡+加噪
  $[\hat{X}]$ 预测
  $M\in\{0,1\}^{(O+P) \times J \times 3}$ The availability mask is a binary matrix, M correspondent to P future frames are always zero （）
  
  Q: M 由什么确定？X 怎么来的？
  
### B. Conditional Diffusion Blocks
  ![[Pasted image 20230302185059.png|450]] 
  方差由一个 cosine noise scheduler 生成
  ![[Pasted image 20230302185215.png|450]]
  
### C. Temporal Cascaded Diffusion (TCD)
  包含两部分：
  1. short-term
     predict K 帧
   2. long-term
      input: short-term 的 K 帧和加了噪声的 observation
      output: 总共 P 帧
  两部分独立训练：trained separately using clean complete input, but in inference time, the average of 5 samples of the short-term block is given to the long-term predictor. （？）
  时间级联：将比较长的时间跨度 challeniging behavior 划分成了两部分，所以有了 better overall and specificallly long-term prediction
  
### D. Pre-processing and Post-processing
  1. pre: repairing the input sequence
     a simpler version of our model as a pre-processing step to denoise the observation only. 类似于TCD
      $[\widetilde{X}_{-O+1},\widetilde{X}_{-O},...,\widetilde{X}_{0}]$ $\rightarrow$ $[\hat{X}_{-O+1},\hat{X}_{-O},...,\hat{X}_{0}]$
    2. post: finetuning its outputs
       improve the prediction results of existing models: 将任何模型预测到的 $[\widetilde{X}_{1},\widetilde{X}_{2},...,\widetilde{X}_{P}]$ 和 $[\hat{X}_{-O+1},\hat{X}_{-O},...,\hat{X}_{0}]$ concatenate 串级之后喂入 TCD，并 retrain
       初始预测可以作为 post process 中向真实分布靠近的起点
![[Pasted image 20230302193034.png]]


## Experiment(s)
  数据集
  - Human3.6M [22] is the largest benchmark dataset for human motion analysis, with 3.6 million body poses
  - AMASS (The Archive of Motion Capture as Surface Shapes) [31] is a recently published human motion dataset
  - 3DPW (3D Poses in the Wild) [46] is the first dataset with accurate 3D poses in the wild
  - HumanEva-I [43] includes 3 subjects that perform different actions captured at 60fps. Each person has 15 body joints.
  评估指标
  - DE: Displacement Error (DE), in millimeters (mm)
  - ADE: average of DE for the whole sequence
  - FDE: DE in the final predicted frame
  - MMADE: multi-modal versions of ADE (MMADE) and FDE (MMFDE)
  - MMFDE
  - APD[50]: measure diversity and report the Average Pairwise Distance (APD) between different prediction
  实验结果
  1. ours vs Stochastic Approaches: table 1
  2. ours vs Deterministic Approaches: table 2
       - ours best
       - 在其他已有模型上加上 TCD（post-process），能够提升，并且视频时间越长效果越好（1000ms 是否代表视频时长）
       - 在其他数据集: table 3
       - 定性: 结果可视化
  1. Comparisons on Imperfect Observation Data
       - MT-GCN [12] predicts in incomplete observation settings and reported the performance of some previous models when the input is repaired using their own method，不如ours

![[Pasted image 20230302201349.png]]

![[Pasted image 20230302201358.png]]
![[Pasted image 20230302201822.png|425]]


## Notes


## References
  3D 姿态估计方法
  - RNN: capable of capturing the temporal dependencies in sequential data
      - [16], [23], [35], [9], [17], [10]
      - used only feed-forward networks[25]
  
  - GCN: better capture the spatial dependencies of body poses
      -  [34], [13], [32], [27]
  - Separating temporal and spatial convolution blocks [30]
  - trainable adjacency matrices [44], [51]
  - **Attention-based approaches**
      - [36], [39] 
      - HRI: spatio-temporal self-attention module [32]
  - context information [8], [19], [11]
  - social interactions [1]
  - action class [2], [7]
  
  - VAEs: strengths in learning representations
      - [38], [50], [4], [3]
  - DM: timeseries imputation
      - **repairing the missing elements.[45]**
  
  - incomplete observation 领域
      - a multi-task learning approach---implicitly ignores noise in data [12]
      - **explicitly denoise the input: Ours**

  实验：将主流模型分为以下两种
  - stochastic approaches [33], [50], [42], [29] 
  - deterministic approaches [35], [25], [34], [32], [30], [44], [51]  




