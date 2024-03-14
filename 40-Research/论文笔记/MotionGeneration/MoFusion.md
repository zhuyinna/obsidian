---
time: 2023-05-15
publish: CVPR'2023
---

# MoFusion

![[Pasted image 20230918190031.png]]


## MoFusion Architecture
模型的目标：在 Reverse Diffusion 过程中，预测 Forward Diffusion 加的 noise

![[Pasted image 20230918170555.png|425]]
具体用公式表示：
![[Pasted image 20230918184505.png|425]]

Reverse 的过程具体如下：
通过三次下采样，图像的特征长度从 N 降低到了 N/8，每一个 residual block 后都紧跟跨模态 transformer，用来将 context 合并到网络中。时间嵌入是通过两层 MLP 实现。
![[Pasted image 20230918170215.png|725]]
transformer 里的 QKV：
![[Pasted image 20230918184932.png]]
其中，x 和 c 分别表示：
![[Pasted image 20230918184955.png|475]]
n 为当前层的特征的长度，d 是特征维度，注意力计算如下：
![[Pasted image 20230918185058.png|500]]
## Text-to-Motion Synthesis
CLIP 获得 tokenised embedding for each word -> MLP\

## Dataset&Evalustion
- HumanML3D: 取自 AMASS
- Average Pairwise Euclidean Distance (Diversity) and Multi-Modality.
	🔤多模态度量通过对相同文本输入对该方法进行 N 次采样并计算合成运动的平均成对欧几里得距离来评估该方法的每个提示多样性声明；欧几里得距离越高意味着变化越大。🔤
	R-precise：衡量预训练分类器上合成运动的分类准确性

```ad-question
从结果来看，相比较Guo的TM2T，只有多模态这一指标比较好，多样性和精确度都不如，可以再参考TM2T
```
![[Pasted image 20230918185731.png|500]]
## Toread
Very recently, MDM [Tevet et al. 2023], MotionDiffuse [Zhang et al. 2022], MoFusion [Dabral et al. 2023], and FLAME [Kim et al. 2022] successfully implemented motion generation neural models using the Denoising Diffusion Probabilistic Models (DDPM) [Ho et al. 2020] setting, which was originally suggested for image generation. MDM enables both high-quality generation and generic conditioning that together comprise a good baseline for new motion generation tasks. EDGE [Tseng et al. 2022] followed MDM by extending it for the music-to-motion task. SinMDM [Raab et al. 2023] adapted MDM to non-human motions using a single-sample learning scheme. PhysDiff [Yuan et al. 2022] added to MDM a pre-trained physical model based on reinforcement learning which enforces physical constraints during the sampling process. These examples demonstrate the flexibility of MDM to novel tasks

- human Motion Diffusion as a Generative Prior

