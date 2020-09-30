# Author: Simon
# Date  : 2020/09/30
# Function: lots of pics croping to a pdf file
 
import numpy as np
from PIL import Image
from PIL import ImageGrab
import cv2
import os

import time
import datetime
import progressbar

import win32api
import win32con

input_img_path = "E:/01. pic/pics_crop/origin/"
output_img_path = "E:/01. pic/pics_crop/target/"
date_now = datetime.datetime.now().strftime('%Y%m%d')

####################################################
pages = int(input("pages = "))
n = int(pages / 2)	# times, the prtscr times you want
####################################################

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

x = np.arange(1,n+1,1)
for i in x:
	pic = ImageGrab.grab((410,185,2145,1520))	#default as full screeen, also a rectangle (x0,y0,x1,y1)
	picture_name = input_img_path + str(date_now) + "_" + str(str(i).zfill(4)) + ".png"
	pic.save(picture_name)
	win32api.keybd_event(0x22,0,0,0)	# use PageDown to changge code is 34(0x22)
	win32api.keybd_event(0x22,0,win32con.KEYEVENTF_KEYUP,0)
	time.sleep(1.5)

pdfFile = output_img_path + str(date_now) + ".pdf"
for i in range(100):
	if os.path.isfile(pdfFile):
		pdfFile = output_img_path + str(date_now) + "_" +str(i) + ".pdf"
	else:
		break

combine2Pdf(input_img_path, pdfFile)
print("file has been saved as " + pdfFile)



# ------------------------------------------------------------------------------
# ### size crop
# def update(input_img_path, output_img_path):
#     image = cv2.imread(input_img_path)
#     print(image.shape)

#     # inpur your target size here
#     cropped = image[60:1520, 300:2260] # 裁剪坐标为[y0:y1, x0:x1]
#     cv2.imwrite(output_img_path, cropped)

# dataset_dir = input_img_path
# output_dir  = output_img_path
 
# # 获得需要转化的图片路径并生成目标路径
# image_filenames = [(os.path.join(dataset_dir, x), os.path.join(output_dir, x))
#                     for x in os.listdir(dataset_dir)]
# # 转化所有图片
# for path in image_filenames:
#     update(path[0], path[1])
# ###
# ------------------------------------------------------------------------------