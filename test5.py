"""
matplotlib learning
面向对象的方式画散点图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1,10,50)
y = np.random.randint(1,10,50)

x1 = np.random.randint(1,10,30)
y1 = np.random.randint(1,10,30)

fig,ax = plt.subplots()#初始化了一个绘图对象,fig代表画布，ax代表图像
ax.scatter(x,y)
plt.show()