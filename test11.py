"""
matplotlib learning
3D画图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""

import matplotlib.pyplot as plt
import numpy as np

#3D图标必须的模块，project='3D'的定义
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = Axes3D(fig)
ax1 = fig.gca(projection = '3d')#1行1列第一个


x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]

ax1.plot(x,y,z)
#ax1.plot_wireframe(x,y,z)
ax1.set_xlabel('x_axis')
ax1.set_ylabel('y_axis')
ax1.set_zlabel('z_axis')

plt.show()

