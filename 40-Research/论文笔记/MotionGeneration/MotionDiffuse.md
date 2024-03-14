---
time: 2022-08-04
publish: arxiv
---
# MotionDiffuse
![[Pasted image 20230918205031.png]]


## Background
1. CLIP
见 [[09-CLIP]]

2. Motion CLIP
见[[MotionCLIP]]
text encoder+motion decoder
其中 text encoder 采用 CLIP
**但是存在不足：不能处理长文本；不能处理复杂的运动描述；**

3. TEMOS
[[TEMOS]]
TEMOS 和 Motion CLIP 非常类似，都是基于 text-motion 映射，且利用了大模型作为 text encoder——TEMOS 使用了 BERT 大模型，这玩意其实就是升级版 transformer encoder，TEMOS 结构如下：
![[Pasted image 20230920142800.png]]


![[Pasted image 20230920153611.png]]


## Toread
- Dhariwal P, Nichol A (2021) Diffusion models beat gans on image synthesis. Advances in Neural Information Processing Systems 34
- Nichol AQ, Dhariwal P (2021) Improved denoising diffusion probabilistic models. In: International Conference on Machine Learning, PMLR, pp 8162–8171
- Nichol A, Dhariwal P, Ramesh A, Shyam P, Mishkin P, McGrew B, Sutskever I, Chen M (2021) Glide: Towards photorealistic image generation and editing with text-guided diffusion models. arXiv preprint arXiv:211210741
- Ramesh A, Dhariwal P, Nichol A, Chu C, Chen M (2022) Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:220406125

