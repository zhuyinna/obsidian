ShuffleNet是2017年提出的

## 核心思想

ShuffleNet 是 Xiangyu Zhang(旷视)等人于2017年在 ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices 中提出来的。ShuffleNet 的核心思想是对卷积进行分组，从而减少计算量，但是由于分组相当于将卷积操作局限在某些固定的输入上，为了解决这个问题采用 shuffle 操作将输入打乱，从而解决这个问题。

<img src=https://s2.loli.net/2024/05/08/O9Nlwcr8mBhDbAV.png width='100%'>