---
 Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, Illia Polosukhin
 Date: 2017
 Date Added: 2022-10-18
 Topics: Transformer
 Keywords: Self-Attention;
---
tags:  #深度学习

## Metadata
 Authors: "[[Ashish Vaswani]], [[Noam Shazeer]], [[Niki Parmar]], [[Jakob Uszkoreit]], [[Llion Jones]], [[Aidan N Gomez]], [[Łukasz Kaiser]], [[Illia Polosukhin]]"
 Date: [[2017]] 
 Date Added: [[2022-10-18]] 
 Topics: "[[Transformer]]"
 URL: [https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)

## Zotero Links 
 PDF Attachments
	- [Full Text PDF](zotero://open-pdf/library/items/RI5HPDQN) 
 [Local library](zotero://select/items/1_4GB5ZVZW) 


## Abstract

The dominant sequence transduction models are based on complex recurrent orconvolutional neural networks in an encoder and decoder configuration. The best performing such models also connect the encoder and decoder through an attentionm echanisms.  We propose a novel, simple network architecture based solely onan attention mechanism, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superiorin quality while being more parallelizable and requiring significantly less timeto train. Our single model with 165 million parameters, achieves 27.5 BLEU onEnglish-to-German translation, improving over the existing best ensemble result by over 1 BLEU. On English-to-French translation, we outperform the previoussingle state-of-the-art with model by 0.7 BLEU, achieving a BLEU score of 41.1.


## Summary
  Transformer 是一个利用注意力机制来提高模型训练速度的模型。关于注意力机制可以参看 [[02-Seq2Seq]]，trasnformer 可以说是完全基于自注意力机制的一个深度学习模型，因为它适用于并行化计算，和它本身模型的复杂程度导致它在精度和性能上都要高于之前流行的 RNN 循环神经网络。

```ad-note
与seq2seq的区别：
**The difference from the Seq2Seq model is that, at each timestep, we re-feed the entire output sequence generated thus far, rather than just the last word.**
```
## Conclusion
  In this work, we presented the Transformer, the first sequence transduction model based entirely on attention**, replacing the recurrent layers** most commonly used in encoder-decoder architectures with **multi-headed self-attention**.
  
  plan: plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours. 🔤我们计划将 Transformer 扩展到涉及除文本以外的输入和输出模式的问题，并研究局部的、受限的注意力机制以有效处理图像、音频和视频等大型输入和输出。减少生成顺序是我们的另一个研究目标。🔤



## Background / Problem Statement
  作者采用 Attention 机制的原因是考虑到 RNN（或者 LSTM，GRU 等）的计算限制为是顺序的，也就是说 RNN 相关算法只能从左向右依次计算或者从右向左依次计算，这种机制带来了两个问题：

1.  时间片 $t$ 的计算依赖 $t-1$ 时刻的计算结果，这样限制了模型的并行能力；
2.  顺序计算的过程中信息会丢失，尽管 LSTM 等门机制的结构一定程度上缓解了长期依赖的问题，但是对于特别长期的依赖现象, LSTM 依旧无能为力。


## Method (s)

### encoder
1. Encoder
     **QKV？**
         Q 是一组查询语句，V 是数据库，K 是一组钥匙，代表了 V 中每一项的某种查询特征。所以 K 和 V 的数量一定是相等的，维度则没有严格限制。做 attention 时维度和 Q 一样只是为了在做点积时方便，不过也存在不用点积的 attention。对于每一个 Q 中的 q，求和每一个 k 的 attention，作为对应 value 的加权系数，并用它来加权数据库中 V 中的每一项，就得到了 q 期望的查询结果。
         e.g. 
             (1) 对于一个文本，希望找到某张图片中和文本描述相关的局部图像：文本做 query，图像做 value
             (2) 对于一个图像，希望找到一个文本中和图像所含内容有关的局部文本：图像做 query，文本做 value
             (3) 自注意力：句子中某个词在整个句子中的分量（或者相关文本）：句子本身乘以三个矩阵得到 QKV，每个词去查完整的句子
             (4) 交叉注意力：transformer 模型的 decoder 中，由 decoder 的输入经过变换作为 query，由 encoder 的输出作为 key 和 value（数据库）。value 和 query 来自不同的地方，就是交叉注意力。可以看到 key 和 value 一定是代表着同一个东西。即: $[Q,(K,V)]$
        $W_QW_KW_V$ 矩阵随机初始化得到，训练过程梯度下降更新
    
    **Add&Norm**
        **Add**指 **X**+MultiHeadAttention (**X**)，是一种残差连接，通常用于解决多层网络训练的问题，可以让网络只关注当前差异的部分，在 ResNet 中经常用到：![[Pasted image 20230322153328.png|500]]
        **Norm**指 Layer Normalization，通常用于 RNN 结构，Layer Normalization 会将每一层神经元的输入都转成均值方差都一样的，这样可以加快收敛。
    ![[Pasted image 20230323105713.png|525]]
        
    **Self-Attention**
        举例：The animal didn't cross the street because it was too tired，怎么判断 it 指代 animal 还是 street
        **first step: create three vectors from each of the encoder’s input vectors**
        ![[Pasted image 20230323102910.png|525]]
        **second step: calculate a score** (We need to score each word of the input sentence against this word. The score determines how much focus to place on other parts of the input sentence as we encode a word at a certain position)
        ![[Pasted image 20230323103417.png|525]]
        **third step:  divide the scores by 8**(the square root of the dimension of the key vectors used in the paper – 64. This leads to having more stable gradients. There could be other possible values here, but this is the default)
        **forth step: softmax operation**
        ![[Pasted image 20230323103707.png|525]]
        **fifth step: multiply each value vector by the softmax score**
        **sixth step: sum up the weighted value vectors**. This produces the output of the self-attention layer at this position (for the first word).
        
		![[Pasted image 20231007160636.png]]
		注意力计算得分：
		![[Pasted image 20231007160623.png]]
		![[Pasted image 20231007160805.png]]
		![[Pasted image 20231007160957.png]]



    **Multi-Head Self Attention**
    Transformer 将每个注意力计算单元称为注意力头（Attention Head ）。多个注意力头并行运算，即所谓的多头注意力--Multi-head Attention。它通过融合几个相同的注意力计算，使注意力计算具有更强大的分辨能力。
    整体框架
        ![[Pasted image 20230323104326.png|500]]
    分解
        ![[Pasted image 20230323104144.png|500]]
        ![[Pasted image 20230323104150.png|500]]
        ![[Pasted image 20230323104230.png|500]]
    

### decoder

2. Decoder
     The output of the top encoder is then transformed into a set of attention vectors K and V
     
     Self-Attention
        当前翻译和已经翻译的前文之间的关系
        不同于 Encoder 中的 attention，the self-attention layer is only allowed to attend to earlier positions in the output sequence. This is done by **masking future positions**
     Encoder-Decoder Attention
        当前翻译和编码的特征向量之间的关系，just like multiheaded self-attention, except it creates its Queries matrix from the layer below it, and takes the Keys and Values matrix from the output of the encoder stack.
        输出：a vector of floats
    ![[transformer_decoding.gif|600]]
     ![[transformer_decoding_2.gif|650]]
    ![[Pasted image 20231007154700.png|500]]
    
        
    Linear & Softmax
        输入： a vector of floats from the decoder
        输出：turn that into a word
        - linear：simple fully connected neural network that projects the vector produced by the stack of decoders, into a much, much larger vector called a **logits vector.**（a vector of width *vocab_size*）
        - Softmax: The softmax layer then turns those scores into **probabilities** (all positive, all add up to 1.0). The cell with the highest probability is chosen, and the word associated with it is produced as the output for this time step.
    ![[Pasted image 20230323133559.png|525]]

   

### embedding 
input embedding：
	输入序列->映射成词汇表的单词 ID 的数字序列->每个数字序列射成一个嵌入向量
output embedding：右移一个位置，并加上一个$<start>$
	训练-对 target 进行 embedding；推理-对 encoder 的输出进行其 embedding；
![[Pasted image 20231007151434.png]]

### position encoding

![[Pasted image 20231007151126.png|350]]
![[Pasted image 20231007151133.png|375]]

### 矩阵维度

![[Pasted image 20231007152928.png|500]]


## 训练&推理

### 训练
Transformer 训练的目标是通过对源序列与目标序列的学习，生成目标序列。
![[Pasted image 20231007140238.png]]

![[Pasted image 20231007140400.png]]

### 推理
![[Pasted image 20231007140549.png]]
![[Pasted image 20231007140557.png]]
![[Pasted image 20231007140707.png]]


**为什么训练的时候不像推理：target 逐词输入？
原因：**
![[Pasted image 20231007143338.png]]


## Model usage
1. Encoder-decoder
   这通常用于序列到序列建模（例如神经机器翻译）。
2. encoder only
   仅使用编码器，并且编码器的输出被用作输入序列的表示。这通常用于自然语言理解 (NLU) 任务（例如文本分类和序列标记）。
3. decoder only
   仅使用解码器，其中编码器解码器交叉注意模块也被删除。这通常用于序列生成（例如，语言建模）。

## transformer 变体
### 概览
![[Pasted image 20231008135139.png]]

![[Pasted image 20231008141434.png]]


### sparse attention
#### position-based sparse
- 稀疏注意力
![[Pasted image 20231008145540.png]]

- 复合稀疏注意力
![[Pasted image 20231008162240.png]]

- 注意力的选择
  对于具有周期性的图像：band+strided
  对于没有周期性的文本：block+global

- 其他注意力（extended attention）
![[Pasted image 20231008163213.png]]

#### content-based sparse

另一项工作是根据输入内容创建稀疏图，即稀疏连接以输入为条件。构建基于内容的稀疏图的一种直接方法是选择那些可能与给定查询具有较大相似度分数的键。为了有效地构建稀疏图，我们可以递归到最大内积搜索（MIPS）问题，其中尝试通过查询找到具有最大点积的键，而不计算所有点积项。

方法：k 均值聚类

### Linearized attention

降低 attention 的复杂度

![[Pasted image 20231010154800.png]]
### Query prototyping and memory compression
1. 减少查询
2. 减少 key-value pairs--内存压缩
   方法：内存压缩注意力 MCA：可以处理更长序列；sources. Set Transformer (Lee et al., 2019) and Luna (Ma et al., 2021)；Linformer (Wang et al., 2020a)；Poolingformer (Zhang et al., 2021)；





## 参考博客
[参考博客：The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)


## 改进
### multi-attention
[Adaptive Attention Span in Transformers](https://browse.arxiv.org/pdf/1905.07799.pdf)
1. 出发点
   不同 head，特征提取方式不同，有些因为注意力特征的衰减而产生差距：
   ![[Pasted image 20231007165555.png|500]]
   ![[Pasted image 20231007165620.png|500]]
   ![[Pasted image 20231007165704.png|550]]
### self-attention
[Augmenting Self-attention with Persistent Memory](https://www.arxiv-vanity.com/papers/1907.01470/)

通过优化 FFN 层来减少模型特征的参数数量

![[Pasted image 20231007193511.png]]

