"""
matplotlib learning
画饼图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""

import matplotlib.pyplot as plt

label = 'A','B','C','D'
SIZE = [12,30,45,10]

fig,ax = plt.subplots()
explode = (0,0.1,0,0)
ax.pie(SIZE,labels = label,autopct = '%1.1f%%',shadow = 'True',startangle = 90,explode = explode)#其中的autopct是显示百分比,shadow是显示阴影 startangle开始显示的角度 explode让B突出了 0.1个间距
ax.axis('equal') #每个方向都相等  就是让 圆更圆一点  可以注释看一下变化
plt.show()
