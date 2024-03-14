# Scorebased - 基于分数的生成模型

****基于分数的生成模型（Score-based generative models）****

## 1. 基于分数

**分数匹配算法（Score Matching)**

### 1.1 基本原理

![Untitled](Untitled%2057.png)

![Untitled](Untitled%2058.png)

但是这个目标函数中data的分布是未知的，所以进行转变得到等价形式：

![Untitled](Untitled%2059.png)

![Untitled](Untitled%2060.png)

### 1.2 解决计算成本高的方法

1. **分层分数匹配（Sliced score matching）**

![Untitled](Untitled%2061.png)

1. **降噪分数匹配（Denoising score matching）**

![Untitled](Untitled%2062.png)

### 1.3 不足

1. 分数匹配算法估计分数的准确性问题
论文中一共提出两个原因会导致分数估计不准确，一个是流体假设问题，一个是低密度区域样本不足的问题。
    1. 首先看流体假设问题，论文指出了流形假设的存在，即现实世界中的数据往往集中在嵌入高维空间的低维流形上。类似于矩阵方程中，Aθ=b。其中A是稀疏矩阵，对应着观测变量的观测值矩阵，或者说特征矩阵。θ是位置参数组成的向量。b是方程组等号右侧值组成的向量，对应着机器学习场景下的 Label 值向量。
    
        
        ![Untitled](Untitled%2063.png)
        
        ![Untitled](Untitled%2064.png)
        
    
    b. 低密度问题
    
    ![Untitled](Untitled%2065.png)
    
2. 基于分数的采样算法的准确性问题

![Untitled](Untitled%2066.png)

### 1.4 改进

1. 改进采样

![Untitled](Untitled%2067.png)

1. 改进整个算法：适应于高分辨率图像

![Untitled](Untitled%2068.png)

## 2. 基于随机微分方程

### 2.1 随机微分方程表示

![Untitled](Untitled%2069.png)

### 2.2 生成模型

![Untitled](Untitled%2070.png)