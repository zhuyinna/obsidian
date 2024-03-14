# DDIM - 去噪扩散隐式模型

****去噪扩散隐式模型（Denoising Diffusion Implicit Models,DDIM）****

## DDPM：马尔科夫链分解

前提知识：原始DDPM的前向扩散过程，用了马尔科夫链假设，具体来说：

![Untitled](Untitled%2041.png)

![Untitled](Untitled%2042.png)

![Untitled](Untitled%2043.png)

![Untitled](Untitled%2044.png)

上面从x0直接到xt，进一步采用马尔科夫链的形式分解：

![Untitled](Untitled%2045.png)

![Untitled](Untitled%2046.png)

## DDIM：非马尔科夫链分解

1. 扩散过程

![Untitled](Untitled%2047.png)

![Untitled](Untitled%2048.png)

![Untitled](Untitled%2049.png)

![Untitled](Untitled%2050.png)

![Untitled](Untitled%2051.png)

1. 采样去噪

![Untitled](Untitled%2052.png)

## 加速采样

![Untitled](Untitled%2053.png)

![Untitled](Untitled%2054.png)

**DDIM 可以看做是 DDPM 的扩展， DDPM 是 DDIM 的一个特例**。

**如果方差为0？——能够加速采样过程。**

![Untitled](Untitled%2055.png)

## 兼顾多样性和速度：自适应调度

如果保留方差，多样性更好，但是收敛速度下降。

能不能兼顾多样性和速度呢？——显然是可以的，设计一个动态自适应的调度算法。

![Untitled](Untitled%2056.png)

疑问：

- 为什么要用非马尔科夫的假设来进行分解？