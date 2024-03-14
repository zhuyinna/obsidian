---
Authors: Xingran Zhou; Bo Zhang; Ting Zhang; Pan Zhang; Jianmin Bao; Dong Chen; Zhongfei Zhang; Fang Wen
Date: 2021-03-30
Topics: CPIS
DOI: 10.48550/arXiv.2012.02047
Keywords: Refining warp image with PatchMatch
---
tags: #论文笔记 

# CoCosNet v2: Full-Resolution Correspondence Learning for Image Translation

和CocosNet同一作者--微软研究院
## Abstract
We present the full-resolution correspondence learning for cross-domain images, which aids image translation. We adopt a hierarchical strategy that uses the correspondence from coarse level to guide the fine levels. At each hierarchy, the correspondence can be efficiently computed via PatchMatch that iteratively leverages the matchings from the neighborhood. Within each PatchMatch iteration, the ConvGRU module is employed to refine the current correspondence considering not only the matchings of larger context but also the historic estimates. The proposed CoCosNet v2, a GRU-assisted PatchMatch approach, is fully differentiable and highly efficient. When jointly trained with image translation, full-resolution semantic correspondence can be established in an unsupervised manner, which in turn facilitates the exemplar-based image translation. Experiments on diverse translation tasks show that CoCosNet v2 performs considerably better than state-of-the-art literature on producing high-resolution images.

## Files and Links
- **Url**: [Open online](http://arxiv.org/abs/2012.02047)
- **zotero entry**: [Zotero](zotero://select/library/items/VBRIP8RW)
- **open pdf**: [arXiv.org Snapshot](zotero://open-pdf/library/items/UIN5Z4XQ); [Zhou et al_2021_CoCosNet v2.pdf](zotero://open-pdf/library/items/JIMWHWX4)

## Comments
Comment: CVPR 2021 oral presentation

---

## Summary

  
## Research Objective(s)


## Background / Problem Statement

style-transfer存在的问题：
1）生成的图风格不可预知，用户无法指定具体实例的样式（如红色的法拉利、橘红的天空）；2）图片往往有较明显的瑕疵， 影响用户体验。

针对上述问题，微软亚洲研究院的研究员们在 CVPR 2020 上提出了基于样例的[[@zhang2020CVPR-CocosNet]]，算法按照用户给定样例生成多模态结果， 解决了图像生成过程中风格精细控制的难题，在一系列图片翻译任务中取得大幅领先的生成质量。

CocosNet存在的问题：
但是由于较大的计算内存开销，这个方法并不能很好地拓展到高清图生成领域  ----  第一代 CoCosNet 与最近大火的视觉 Transformer 类似，直接在高分辨率图片（或特征空间）上计算注意力矩阵会带来极大的内存开销，例如，在1024x1024分辨率图片上，计算注意力矩阵会占用 1T 大小的显存。另外，CoCosNet 仅在64x64的分辨率上构建语义对应，而低分辨率下的对应关系使得样例图片中的精细纹理并不能很好的保留在最终的生成结果中。


## Method(s)

**核心思想：借鉴了 PatchMatch 的思想，** CoCosNet v2 充分利用了自然图片特征空间局部连续的特点，用迭代的方法换取内存开销，实现了在原高清分辨率下高效近似注意力（attention）机制，在高清大图的生成上取得了惊艳的效果。
### coarse-to-fine： 减小显存占用率

针对上述注意力矩阵显存占用率问题，CoCosNet v2 用两个技术对此进行了处理。首先，利用 coarse-to-fine 的思想，构建多层级特征空间金字塔，在高层次低分辨率空间构建的对应关系中，指导下一层在更高分辨率下进行更精细的搜索。
![[Pasted image 20240112182737.png]]



### PatchMatch

尽管有来自上一层的对应初始化，但在高分辨率上的密集对应依然有挑战性。对此，研究员们借用了 PatchMatch 的思想，考虑到对应关系的局部平滑性，因而可以将最近邻搜索用迭代搜索的方法快速逼近。如图3所示，初始时刻（左图）的蓝色图块的对应关系并不可靠，当发现其临近图块（绿色框）有优质的对应结果后，研究员们便对蓝色图块的候选区域进行了更新（中间图），得到更合理的对应，从而传播到当前图块（matching propagation）。最后在候选区域附近扰动搜索（local random searching），至此完成一次迭代搜索。随着迭代的进行，可靠图块的对应关系会迅速传播给附近图块，整个搜索过程可以在几次迭代后迅速收敛。

![[Pasted image 20240112182918.png]]


具体实现时，研究员们为每个图块匹配到 K 个对应区域，进而图片扭转（image warping）可以写成 softmax 的形式，整个迭代搜索过程梯度可导为：

![[Pasted image 20240112182932.png]]

但是这样的实验并不理想，图片扭转的结果显示输入图片的语义并不能很好的对应起来。![[Pasted image 20240112182942.png|500]]
研究员们猜测其原因是 PatchMatch 之前的特征提取模块没有很好的更新，造成了语义特征提取不准确。这是因为每个图块的梯度只能反传到稀疏的 K 个候选区域，而不能像注意力矩阵那样每个位置都可以得到梯度更新。

另一个猜测的原因是，PatchMatch 迭代每次仅仅考虑临近图块，需要很多次迭代才能利用到远处图块的对应关系。所以，研究员们利用几层卷积来提前处理每次迭代的结果，等同于增大了每层 match propagation 的感受野 （图5）。

![[Pasted image 20240112182958.png]]


此外，如果迭代搜索认为是 recurrent（递归）过程，那么则可以采用 GRU 来更好地修正下次搜索位置。因此，研究员们提出了 ConvGRU-assisted PatchMatch，不仅能利用更大视野内所有图块的对应，也能利用历史迭代结果，大大缩短了 PatchMatch 所需的迭代次数。每一层的搜索过程，可以用图6表示。

==GRU？==

![[Pasted image 20240112183039.png]]

至此，研究员们可以在 N 个层级上得到语义对应，每层的图片扭转注入到生成网络可得到最终的生成结果。值得注意的是，端到端训练网络同时实现语义对应和图片生成，其中语义对应并没有 ground truth，而是通过弱监督信号间接习得的。

![[Pasted image 20240112183059.png|475]]


## Evaluation


## Conclusion
为了解决先前图像翻译方法无法生成高清图的痛点问题，研究员们在 CoCosNet v2 中构建了多分辨率金字塔，并借鉴传统方法 PatchMatch 的方法，将其作为可微分模块与图像生成端到端训练，同时额外引入 ConvGRU 模块帮助了梯度反传，帮助迭代搜索更快收敛。值得注意的是，CoCosNet v2 有效解决了高清图中注意力模块的平方级内存开销问题。与近期一系列高效（efficient）Transformer，如 BigBird、Linformer、Performer 相比，CoCosNet v2 能够更充分的利用图片的局部相关性，用迭代的方法换取更小的内存消耗，可谓另一种另辟蹊径的解决方法。

## Notes


----

## Extracted Annotations

