# Motion CLIP

![[Pasted image 20230919105011.png]]


## Framework
![[Pasted image 20230919105309.png]]

CLIP 让图像和文本两个不同模态分别对应的特征，共享同一个特征空间，从而建立两模态之间的映射关系。motionclip 则希望 human motion 的特征空间和 CLIP 的特征空间对齐，从而建立文本和 human motion 之间的对应映射关系。

一旦建立映射关系，就可以通过文本去查询对应的 human motion，同时借助文本表达的丰富性以及 CLIP 特征空间的泛化性，可以根据文本得到除了训练数据集以外的 human motion。

![[Pasted image 20230919161751.png]]
### Encoder

Maps a motion sequence 𝑝1:𝑇 to its latent representation 𝑧𝑝
𝑧𝑝 = 𝐸 (𝑧𝑡𝑘, 𝑝1:𝑇 )
### Decoder
the query sequence is simply the positional encoding of 1 : 𝑇
We further use a differentiable SMPL layer to get the mesh vertices locations, ˆ 𝑣1:𝑇 .

### Losses
由三部分组成：
![[Pasted image 20230919162339.png]]
Lrecon：该自动编码器经过训练，通过关节方向、关节速度和顶点位置上的重建 L2 损失来表示运动。明确地说
![[Pasted image 20230919162358.png]]
![[Pasted image 20230919162412.png]]

### setting细节
![[Pasted image 20230919161851.png]]

## Result
- Action
  与 JL2P 比较：因为两个模型在不同的数据集上训练，所以建立了新的样本集，用户评判生成序列质量
  效果好于 JL2P
  ![[Pasted image 20230919165446.png|525]]
- style
  风格迁移方面，效果不如 Alberman
![[Pasted image 20230919164825.png|500]]
![[Pasted image 20230919164745.png|500]]
- abstract language
  通过 CLIP 可以生成训练集以外的动作

## Applications
- Latent-Based Editing
  可以在学习得到的特征空间上进行特征向量加减操作实现动作组合，风格迁移以及插值等效果
- Action Recognition
  可以看成 motion-text？但是 motionclip 设计不是为了 recognition，所以精度不足
![[Pasted image 20230919170220.png]]


## Related work
- CVAE
  Kihyuk Sohn, Honglak Lee, and Xinchen Yan. 2015. Learning structured output representation using deep conditional generative models. Advances in neural information processing systems 28 (2015).
- seq2seq RNN
  Matthias Plappert, Christian Mandery, and Tamim Asfour. 2018. Learning a bidirectional mapping between human whole-body motion and natural language using deep recurrent neural networks. Robotics and Autonomous Systems 109 (2018), 13–26.
- latent space+text and motion pairs
  Tatsuro Yamada, Hiroyuki Matsunaga, and Tetsuya Ogata. 2018. Paired recurrent autoencoders for bidirectional translation between robot actions and linguistic descriptions. IEEE Robotics and Automation Letters 3, 4 (2018), 3441–3448.
- JL2P 模型在文本的细微概念（即速度、轨迹和动作类型）改进的结果
  Chaitanya Ahuja and Louis-Philippe Morency. 2019. Language2pose: Natural language grounded pose forecasting. In 2019 International Conference on 3D Vision (3DV). IEEE, 719–728
![[Pasted image 20230919154812.png]]

## 不足
MotionCLIP (Tevet et al., 2022) could generate stylized motions, but **it is still limited to short text inputs and fails to handle complicated motion descriptions.** In addition, they (Petrovich et al., 2022; Tevet et al., 2022) typically only **accept a single text prompt, which greatly limits users’ creativity.**

