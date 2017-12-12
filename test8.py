"""
matplotlib learning
面向对象的方法绘制多图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""
import matplotlib.pyplot as plt
import numpy as np

"""
seed( ) 用于指定随机数生成时所用算法开始的整数值，如果使用相同的seed( )值，
则每次生成的随即数都相同，如果不设置这个值，则系统根据时间来自己选择这个值，
此时每次生成的随机数因时间差异而不同。

numpy中rand和randn区别
randn(n)是用于产生均值为0，方差和标准差为1，且正态分布的n*n随机矩阵。
rand(n)是在[0.0,1.0]区间，产生均匀分布的n*n随机矩阵。
"""
np.random.seed(1)
data = np.random.randn(2,100)

fig,axs = plt.subplots(2,2,figsize=(5,5))
axs[0,0].hist(data[0])           #直方图
axs[1,0].scatter(data[0],data[1])#散点图
axs[0,1].plot(data[0],data[1])   #线
axs[1,1].hist2d(data[0],data[1]) #双变量直方图

fig.subplots_adjust(hspace = 0.8)
plt.show()