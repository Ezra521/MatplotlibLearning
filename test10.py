"""
matplotlib learning
用plt.test()添加文字说明
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""
import matplotlib.pyplot as plt
import numpy as np

mu,sigma = 100,15
x = mu + sigma * np.random.randn(10000)


"""
绘图都可以调用matplotlib.pyplot库来进行，其中的hist函数可以直接绘制直方图。
调用方式：
n, bins, patches = plt.hist(arr, bins=10, normed=0, facecolor='black', edgecolor='black',alpha=1，histtype='bar')

参数：（hist的参数非常多，但常用的就这六个，只有第一个是必须的，后面四个可选）
    arr: 需要计算直方图的一维数组
    bins: 直方图的柱数，可选项，默认为10
    normed: 是否将得到的直方图向量归一化。默认为0
    facecolor: 直方图颜色
    edgecolor: 直方图边框颜色
    alpha: 透明度
    histtype: 直方图类型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’
返回值 ：
    n: 直方图向量，是否归一化由参数normed设定
    bins: 返回各个bin的区间范围
    patches: 返回每个bin里面包含的数据，是一个list
"""
#数据直方图
n, bins,patches = plt.hist(x,50,normed = 1,facecolor = 'g' ,alpha = 0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')

#添加标题
plt.title('Histogram of IQ')

#添加文字
plt.text(60,.025,r'$mu=100,sigma = 156$')#增加注释的坐标是x=60 y=0.25
plt.axis([40,160,0,0.03])
plt.grid(True)#显示网格

plt.show()