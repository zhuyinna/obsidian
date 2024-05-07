## batch, mini-batch


mini-batch
需要先介绍下梯度下降的两种方法。

批梯度下降（batch gradient decent）
这种方法每次使用整个batch计算损失，调整参数。性能相对较好，但是计算量大，速度慢。

随机梯度下降（stochastic gradient decent）
每次选取一个数据调整参数，计算很快，但是收敛性能不好，容易在最优点附近震荡。

小批量梯度下降（mini-batch gradient decent）
现在解释mini-batch。这里指的是一种梯度下降的方法，算是融合了上述两种方法的优点。也就是说把batch分成小batch，在小batch上梯度下降。

