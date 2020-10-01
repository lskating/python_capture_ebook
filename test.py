"""author:youngkun;date:20180608;function:裁剪照片的黑边"""
 
import cv2
import os
import datetime
 
def change_size(read_file):
    image = cv2.imread(read_file,1) #读取图片 image_name应该是变量
    img = cv2.medianBlur(image,5) #中值滤波，去除黑色边际中可能含有的噪声干扰
    b = cv2.threshold(img,15,255,cv2.THRESH_BINARY)          #调整裁剪效果
    binary_image = b[1]               #二值图--具有三通道
    binary_image = cv2.cvtColor(binary_image,cv2.COLOR_BGR2GRAY)
    print(binary_image.shape)       #改为单通道
 
    x = binary_image.shape[0] # height
    y = binary_image.shape[1] # weight
    print("宽度y=",y)
    edges_x = []
    edges_y = []
    for i in range(x):
        for j in range(y):
            if binary_image[i][j] == 0:
             edges_x.append(i)
             edges_y.append(j)

 
    left = min(edges_x)               #左边界
    right = max(edges_x)              #右边界
    width = right-left                #宽度
    bottom = min(edges_y)             #底部
    top = max(edges_y)                #顶部
    height = top-bottom               #高度
    
    print(left,right,top,bottom)
    pre1_picture=image[left:left+width,bottom:bottom+height]        #图片截取
    return pre1_picture                                             #返回图片数据
 
change_size("pic_20200930_004.png")