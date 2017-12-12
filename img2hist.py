"""
matplotlib learning
一次画多张图，而不是在一张画布上画多张图
2017.12.12
author:Ezra
email:zgahwuqiankun@qq.com
"""
from skimage import data
"""
skimage模块简介
子模块名称　                    主要实现功能
io                         读取、保存和显示图片或视频
data                       提供一些测试图片和样本数据
color                           颜色空间变换
filters             图像增强、边缘检测、排序滤波器、自动阈值等
draw               操作于numpy数组上的基本图形绘制，包括线条、矩形、圆和文本等
transform          几何变换或其它变换，如旋转、拉伸和拉东变换等
morphology          形态学操作，如开闭运算、骨架提取等
exposure              图片强度调整，如亮度调整、直方图均衡等
feature                        特征检测与提取等
measure                  图像属性的测量，如相似性或等高线等
segmentation                          图像分割
restoration                           图像恢复
util                                  通用函数


skimage程序自带了一些示例图片，如果我们不想从外部读取图片，就可以直接使用这些示例图片：
astronaut     航员图片      coffee     一杯咖啡图片   
lena          lena美女图片   camera   拿相机的人图片   
coins           硬币图片     moon    月亮图片
checkerboard   棋盘图片       horse   马图片   
page   书页图片              chelsea   小猫图片     
hubble_deep_field    星空图片   text   文字图片
clock    时钟图片   immunohistochemistry   结肠图片

"""
import matplotlib.pyplot as plt
img=data.camera()#拿相机的人图片
#这两句话可以把照片显示一下
# plt.imshow(img)
# plt.show()
plt.figure("hist")
arr=img.flatten()#flatten()函数是numpy包里面的，用于将二维数组序列化成一维数组。
#plt.hist()函数介绍在test10中有
n, bins, patches = plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red')
plt.show()