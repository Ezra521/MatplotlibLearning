"""
matplotlib learning
画直方图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1,100,100)
bins = [0,10,20,30,40,50,60,70,80,90,100]#给一个划分，让直方图显示范围。用list来定义
plt.hist(x,bins,rwidth=0.7)#rwidth参数不是必选  默认1 为了看起来好看
plt.show()