"""
matplotlib learning
一次画多张图，而不是在一张画布上画多张图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""

import matplotlib.pyplot as plt

plt.figure(1)       #第一张图
plt.subplot(211)    #第一张图的第一个子图
plt.plot([1,2,3])
plt.subplot(212)    #第一张图的第二张子图
plt.plot([4,5,6])

plt.figure(2)       #第二张图
plt.plot([4,5,6])   #默认创建子图
#如果你向plot()指令提供了一维的数组或列表，那么matplotlib将默认它是一系列的y值，并自动为你生成x的值。默认的x向量从0开始并且具有和y同样的长度

plt.figure(1)               #切换到figure 1 ；子图subplot（212）仍旧是当前图
plt.subplot(211)            #令子图subplot（211）成为figure1的当前图
plt.title('Easy as 1,2,3')  #添加subplot 211 的标题
plt.show()