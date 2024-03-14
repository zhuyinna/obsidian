![[Pasted image 20230918205239.png]]

CLIP 模型——constrastive language-image pre-training，该模型提出的出发点是假设在实际应用中训练了分类1000类图像的网络，现在要新增一类，那么就要再去添加标签、重新训练，很难拓展，而 CLIP 模型的目的就是 zero-shot，利用文本的监督信号训练一个迁移能力强的视觉模型（类似 CV 中的 GPT），CLIP 爬取网络图片和对应描述用来训练

具体训练和推理过程如下图所示。训练过程是对比学习，text encoder 可以是 transformer，image encoder 可以是 CNN，将编码后的 vector 计算余弦相似度，那么形成的表格中对角线即是对比学习的 $N$ 个正样本，而负样本有 $N^2-N$  个；推理过程则需提供图片并人为规定 label text。CLIP 在 imagenet 的 zero-shot 结果和 resnet 一样

