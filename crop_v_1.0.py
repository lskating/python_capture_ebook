# Author: Simon
# Date  : 2020/09/30
# Function: lots of pics croping to a pdf file
 
from PIL import Image
from PIL import ImageGrab
import numpy as np
import os
import cv2
import time
import datetime

import win32api
import win32con
import win32print
import win32gui

####################################################
pages = int(input("pages = "))
n = int(pages / 2)	# times, the prtscr times you want
####################################################
# screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
# print(screen_x,screen_y)
hDC = win32gui.GetDC(0)
w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
print(w,h)

for num in range(5,0,-1):
	os.system('cls')
	print("--------------------------------------------")
	print("    please switch to the capture screen!")
	print("     this will start in {} second(s).".format(num))
	print("--------------------------------------------")
	time.sleep(1)
os.system('cls')
print("--------------------------------------------")
print("                  doing                     ")
print("--------------------------------------------")


File_Path = os.getcwd()	+ "\\"	#获取到当前文件的目录
img_temp_path = File_Path + "temp\\"

if not os.path.exists(img_temp_path):
	os.makedirs(img_temp_path)

date_now = datetime.datetime.now().strftime('%Y%m%d')


def getBookSize(picture_i):
    image = cv2.imread(picture_i)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height = np.array(gray).shape[0]
    weight = np.array(gray).shape[1]
    print(weight, height)    
    edges_x = []
    edges_y = []

    for j in range(int(300/2560*weight),int(2300/2560*weight)):
        time = 0
        for i in range(height):
            if gray[i][j] >= 240:       # find white
                time = time + 1
                if time > 0.3 * height:
                    edges_x.append(j)
                    break
    left = min(edges_x)
    right = max(edges_x)
    # print(left,right)

    for i in range(int(150/1600 * height), int(1545 / 1600 * height)):
        time = 0
        for j in range(weight):
            if gray[i][j] >= 240:    # white
                # print(i,j,gray[i][j],">=")
                time = time + 1
                if time >= 0.30 * weight:# and time < 0.45 * weight:
                    edges_y.append(i)
                    break
    # print(edges_y)
    top = min(edges_y)
    bottom= max(edges_y)
    # print(top,bottom)
    pic_size = (left, top, right, bottom)
    print(pic_size)
    return pic_size

def combine2Pdf(folderPath, pdfFilePath):
    files = os.listdir(folderPath)
    pngFiles = []
    sources = []
    for file in files:
        if 'png' in file:
            pngFiles.append(folderPath + file)
    pngFiles.sort()
    output = Image.open(pngFiles[0])
    pngFiles.pop(0)
    for file in pngFiles:
        pngFile = Image.open(file)
        if pngFile.mode == "RGB":
            pngFile = pngFile.convert("RGB")
        sources.append(pngFile)
    output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def picGrab(picture_i,pic_size):
    pic = ImageGrab.grab(pic_size)   #default as full screeen, also a rectangle (x0,y0,x1,y1)
    pic.save(picture_i)


x = range(1,n+1)
default_size = (0,0,w,h)
size_all = default_size
for i in x:
    picture_i = img_temp_path + str(date_now) + "_" + str(str(i).zfill(4)) + ".png"
    if i == 1:
        picGrab(picture_i,default_size)
        picGrab(picture_i,getBookSize(picture_i))
    elif i == 2:
        picGrab(picture_i,default_size)
        size_all = getBookSize(picture_i)
        picGrab(picture_i,size_all)
        
    elif i >=3:
        picGrab(picture_i,size_all)
    else:
        pass
    win32api.keybd_event(0x22,0,0,0)    # use PageDown to changge code is 34(0x22)
    win32api.keybd_event(0x22,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1.5)


pdfFile = File_Path + str(date_now) + "_00.pdf"
for i in range(1,100):
	if os.path.isfile(pdfFile):
		pdfFile = File_Path + str(date_now) + "_" + str(str(i).zfill(2)) + ".pdf"
	else:
		break
os.system('cls')
combine2Pdf(img_temp_path, pdfFile)
print("-------------------------------------------------------------------")
print("file has been saved as " + pdfFile)
print("-------------------------------------------------------------------")
del_file(img_temp_path)
os.rmdir(img_temp_path)
