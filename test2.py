"""
matplotlib learning
画条形图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""

import matplotlib.pyplot as plt
x = [1,3,5,7,9]
y = [4,6,2,8,9]
plt.axis([0,12,0,10])#4个参数，分别是x的长度 最低到最高，y轴的长度 最低到最高，可以穿进去一个列表。如果不定义，就会默认最佳
"""
或者用这两个命令来定义
plt.xlim()
plt.ylim()
"""

plt.bar(x,y)
plt.show()