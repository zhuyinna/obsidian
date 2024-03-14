## 1. DCGAN

1. 判别器
在DCGAN中，**判别器**实际上就是一个CNN网络。输入一张图片，然后输出yes or no的概率。

2. 生成器
而在DCGAN中，G网络的模型是怎么样的？G网络刚好和CNN相反，它是由noise通过G网络生成一张图片，因为图片通过layer逐渐变大，与卷积作用刚好相反——因此我们可以称之为**反卷积**。


当然，DCGAN除了G网络与CNN不同之外，它还有以下的不同：

1. 取消所有pooling层。G网络中使用转置卷积（transposed convolutional layer）进行上采样，D网络中用加入stride的卷积代替pooling。
2. 除了生成器模型的输出层和判别器模型的输入层，在网络其它层上都使用了Batch Normalization，使用BN可以稳定学习，有助于处理初始化不良导致的训练问题。
3. G网络中使用ReLU作为激活函数，最后一层使用tanh
4. D网络中使用LeakyReLU作为激活函数

```ad-note
下采样：池化（下采样是为了降低特征的维度）；卷积（卷积过程导致的图像变小是为了提取特征）；
上采样：反卷积(Deconvolution)、上池化(UnPooling)方法。
```

```ad-note
：反卷积(Deconvolution)也称为分数步长的卷积和 **转置卷积(transposed convolution)** 。两者的kernel size均为3。不过显而易见，反卷积只能恢复图片的尺寸大小，而不能准确的恢复图片的像素值（此时我们想一想，在CNN中，卷积层的kernel我们可以学习，那么在反卷积中的kernel我们是不是也可以学习呢？）。
```
![[Pasted image 20240112214045.png|400]]




## 2. StyleGAN

StyleGAN 的网络结构包含两个部分，第一个是**Mapping network**，即下图 (b)中的左部分，由隐藏变量 z 生成 中间隐藏变量 w的过程，这个 w 就是用来控制生成图像的style，即风格，为什么要多此一举将 z 变成 w 呢，后面会详细讲到。 第二个是**Synthesis network**，它的作用是生成图像，创新之处在于给每一层子网络都喂了 A 和 B，A 是由 w 转换得到的仿射变换，用于控制生成图像的风格，B 是转换后的随机噪声，用于丰富生成图像的细节，即每个卷积层都能根据输入的A来调整"style"。整个网络结构还是保持了  **PG-GAN （progressive growing GAN）**  的结构。最后论文还提供了一个高清人脸数据集**FFHQ。**

（a）传统GAN
（b）styleGAN：传统的GAN网络输入是一个随机变量或者隐藏变量 z，但是StyleGAN 将 z 单独用 mapping网络将z变换成w，再将w投喂给 Synthesis network的每一层，因此Synthesis network中最开始的输入变成了常数张量，见下图b中的Const 4x4x512。


![[Pasted image 20240112214415.png]]

### Mapping network

Mapping network 要做的事就是对隐藏空间（latent space）进行解耦。

latent code 简单理解就是，为了更好的对数据进行分类或生成，需要对数据的特征进行表示，但是数据有很多特征，这些特征之间相互关联，耦合性较高，导致模型很难弄清楚它们之间的关联，使得学习效率低下，因此需要寻找到这些表面特征之下隐藏的深层次的关系，将这些关系进行解耦，得到的隐藏特征，即latent code。由 latent code组成的空间就是 latent space。

**z转换w原因**

![[Pasted image 20240112214758.png]]



### AdaIN

![[Pasted image 20240112214719.png]]



