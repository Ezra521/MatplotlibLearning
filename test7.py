"""
matplotlib learning
同一个画布画多图，进行对比
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0,5.0)#生成50个0.0到5.0的数据 第三个参数默认50 也可以自己设置
x2 = np.linspace(0.0,2.0)
x3 = np.linspace(0.0,10.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
y3 = x3*x3 + 2

plt.subplot(2,2,1)#前面两个参数是要画成2行2列的四个子图，1是第一个位置
plt.plot(x1,y1,'o-')#o-线条的形式
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2,2,2)#前面两个参数是要画成2行2列的四个子图，2是第二个位置
plt.plot(x2,y2,'.-')
plt.xlabel('time(s)')
plt.ylabel('Undamped')

plt.subplot(2,1,2)#2行1列的第二列
plt.plot(x3,y3,'^-')
plt.xlabel('x3data')
plt.ylabel('y3data')

plt.show()


