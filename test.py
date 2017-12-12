"""
matplotlib learning
画线
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""

import matplotlib.pyplot as plt
x = [1,2,9,4]
y = range(5,9)
x1 = range(1,5)
y1 = [5,6,9,12]
plt.plot(x, y, label = 'line1')#plot就是画线图,其中label是可选参数，就是标明这个线段是哪条，区分别的线，必须用plt.legend()函数才显示
plt.plot(x1,y1,label = 'line2')
plt.xlabel('x_data')#表示x轴是什么
plt.ylabel('y_data')
plt.title('title is here')#表头  题目
plt.legend()#显示每条线代表什么，以便于区分
plt.show()#显示
