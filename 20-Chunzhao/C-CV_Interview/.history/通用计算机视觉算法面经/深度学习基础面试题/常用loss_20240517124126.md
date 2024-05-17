## MSE
Mean Squared Error: 均方误差
可以评价数据的变化程度, 越小说明拟合效果越好
$$
MSE=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}
$$
## RMSE
Root Mean Squared Error: 均方根误差

$$
RMSE=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}}
$$
## MAE
Mean Absolute Error: 平均绝对误差
能更好的反映预测值和真实值之间的误差
$$
MAE=\frac{1}{n} \sum_{i=1}^{n}\left|y_{i}-\hat{y}_{i}\right|
$$
## R2
R Squared: 决定系数
决定系数是用来评估模型的拟合程度, 越接近1说明拟合效果越好
$$
R^{2}=1-\frac{\sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}}{\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}
$$
## MAPE
Mean Absolute Percentage Error: 平均绝对百分比误差

$$
MAPE=\frac{1}{n} \sum_{i=1}^{n}\left|\frac{y_{i}-\hat{y}_{i}}{y_{i}}\right| \times 100
$$
## SD
Standard Deviation: 标准差
反应数据集的离散程度. 平均数相同的两组数据,标准差未必相同
$$
SD=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}
$$
其中$\bar{y}$ 表示真实值的均值, $\bar{y}=\frac{1}{N}(x_1+x_2+...x_N)$
