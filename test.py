import cv2

image = cv2.imread("E:\\02. repo\\python_capture_ebook\\pic_2021001_001.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# ret,binImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 200, 255), 2)
# plt.imshow(img)
# plt.show()
# hierarchyDF = DataFrame(hierarchy[0], columns = ['pre', 'next', 'child', 'parent'])











# """author:youngkun;date:20180608;function:裁剪照片的黑边"""
# import numpy as np
# import cv2
# import os
# # import datetime
# # import win32api,win32con
# # import tkinter
# picture_i = "20201001_0001.png"
# img = cv2.imread(picture_i)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 色彩空间转换为hsv，便于分离
# lower_hsv = np.array([0, 43, 46])  # 提取颜色的低值
# high_hsv = np.array([10, 255, 255])  # 提取颜色的高值
# mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)

# mediu = cv2.medianBlur(img,19)

# # 直线检测
# img2 = cv2.Canny(img, 20, 250)  #边缘检测
# line = 4
# minLineLength = 50
# maxLineGap = 150
# # HoughLinesP函数是概率直线检测，注意区分HoughLines函数
# lines = cv2.HoughLinesP(img2, 1, np.pi / 180, 120, lines=line, minLineLength=minLineLength,maxLineGap=maxLineGap)
# lines1 = lines[:, 0, :]  # 降维处理
# # line 函数勾画直线
# # (x1,y1),(x2,y2)坐标位置
# # (0,255,0)设置BGR通道颜色
# # 2 是设置颜色粗浅度
# for x1, y1, x2, y2 in lines1:
#     cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)


# # x = tkinter.Tk().winfo_screenwidth()
# # y = tkinter.Tk().winfo_screenheight()
# # print(x,y)

# # screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# # screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
# # # print(screen_x,screen_y)

    
# # def split_array(list_my):
# #     # spliit the continous element from array
# #     print(len(list_my))
# #     temp = []
# #     result = []
# #     for i in range(len(list_my)):
# #         if list_my[i+1] == list_my[i] + 1:
# #             temp = temp.append(list_my[i])
# #             # if len(temp) >= 0.5 * len(list_my):
# #             #     result = temp
# #         else:
# #             temp = []
# #     print(temp)

# #     # for i in list_my:
# #         # if 


# # def getBookSize(picture_i):
# #     image = cv2.imread(picture_i)
# #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# #     height = np.array(gray).shape[0]
# #     weight = np.array(gray).shape[1]
# #     # print(gray)
# #     edges_x = []
# #     edges_y = []

# #     for j in range(weight):
# #         time = 0
# #         for i in range(height):
# #             if gray[i][j] >= 240:       # find white
# #                 time = time + 1
# #                 if time > 0.3 * height:
# #                     edges_x.append(j)
# #                     break

# #                     # print(i,j,gray[i][j],">=")
# #     # print(edges_x)
# #     left = min(edges_x)
# #     right = max(edges_x)
# #     print(left,right)

# #     for i in range(height):
# #         time = 0
# #         for j in range(weight):
# #             if 130 <= gray[i][j] <= 140:    # gray
# #                 # print(i,j,gray[i][j],">=")
# #                 time = time + 1
# #                 if time >= 0.30 * weight:# and time < 0.45 * weight:
# #                     edges_y.append(i)
# #                     break
# #     # print(edges_y)
# #     top = min(edges_y)
# #     bottom= max(edges_y)
# #     print(top,bottom)



#     # def ret_continuous(a, ret):
#     #     if len(a) == 1:
#     #         return a
#     #     if len(ret) == 0:
#     #         ret.append(a[0])
#     #     if a[0] + 1 == a[1] or a[0] - 1 == a[1]:
#     #         ret.append(a[1])
#     #         return ret_continuous(a[1:], ret)
#     #     else:
#     #         return ret
#     # longest = []
#     # for i in range(len(edges_y)):
#     #     ret = ret_continuous(edges_y[i:], [])
#     #     if len(ret) > len(longest):
#     #         longest = ret
#     # print(longest)



#     # left = min(edges_x)               #左边界
#     # right = max(edges_x)              #右边界
#     # width = right-left                #宽度
#     # bottom = min(edges_y)             #底部


#     # print(height,weight)        # 1600 2560
#     # print(gray[200][200])       # gray = 136
#     # for i in range(height):
#     #     for j in range(weight):
#     #         print(gray[i][j])
#     #     # print(pixel.shape)
#     #     # for 
#     #     # print(pixel)
#     #     pass
#     # print(gray



# # getBookSize("pic_20200930_004.png")
