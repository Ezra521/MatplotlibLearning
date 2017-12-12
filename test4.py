"""
matplotlib learning
画散点图
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

plt.scatter(x,y,color = 'r')#画散点图,color不是必选参数r代表红色 g是绿色 k是黑色
plt.scatter(x1,y1,color = 'g')

plt.show()