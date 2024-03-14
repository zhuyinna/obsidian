# Stable Diffusion Model

## 0. 产生原因

DDPM 存在的问题：xt的尺寸 = x0的尺寸——**训练成本高昂**

![Untitled](Untitled%2081.png)

## ****1. 潜在扩散模型（Latent diffusion model,LDM）****

### 1.1 潜在空间

潜在空间：低维？

021年德国慕尼黑路德维希-马克西米利安大学计算机视觉和学习研究小组（原海德堡大学计算机视觉小组）， 简称 CompVis 小组，发布了论文 **High-Resolution Image Synthesis with Latent Diffusion Models** [[1]](https://www.zhangzhenhu.com/aigc/%E7%A8%B3%E5%AE%9A%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B.html#footcite-rombach2021highresolution)，针对这个问题做了一些改进， 主要的改进点有：

- 引入一个自编码器，先对原始对象进行压缩编码，编码后的向量再应用到扩散模型。
- 通过在 UNET 中加入 Attention 机制，处理条件变量 y。

编码器：降维；解码器：升维；

![Untitled](Untitled%2082.png)

![Untitled](Untitled%2083.png)

正向扩散过程→给潜在数据增加噪声，逆向扩散过程→从潜在数据中消除噪声。 整个 DDPM 的过程都是在潜在空间执行的， 所以这个算法被称为潜在扩散模型（Latent diffusion model,LDM）。 增加一个自编码器并没有改变 DDPM 的算法过程，所以并不需要对 DDPM 算法代码做任何改动。

### 1.2 条件处理

![Untitled](Untitled%2084.png)

![Untitled](Untitled%2085.png)

关于注意力机制的实现细节，可以直接参考论文代码， LDM模型论文的代码和预训练的模型已经在 Github 开源，地址为： https://github.com/CompVis/latent-diffusion 。

### 1.3 训练过程

![Untitled](Untitled%2086.png)

### 1.4 采样过程

![Untitled](Untitled%2087.png)

![Untitled](Untitled%2088.png)

## 2. ****稳定扩散模型（Stable diffusion,SD）****

LDM 本身是由 CompVis 提出并联合 Runway ML进行开发实现，后来 Stability AI 也参与进来并提供了一些资源， 联合搞了一个预训练的 LDM 模型，称为 Stable diffusion。 **所以，Stable diffusion 是 LDM 的一个开源预训练模型，**由于它的开源迅速火爆起来。 目前 Stable diffusion 已经占据了图像生成开源领域的主导地位。

由于 Stable diffusion 只是LDM的一个开源预训练模型，没有额外的复杂数学公式需要讨论， 这里我们就直接上代码吧。 我们不用 Stable diffusion 的官方代码库 [stablediffusion](https://github.com/Stability-AI/stablediffusion) ，而是 huggingface 开源库 diffusers 中的实现， 它的易读性更好一些。

### 2.1 推理过程代码

![Untitled](Untitled%2089.png)