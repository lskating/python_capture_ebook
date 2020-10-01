# Author: Simon
# Date  : 2020/09/30
# Function: lots of pics croping to a pdf file
 
from PIL import Image
from PIL import ImageGrab
import os

import time
import datetime

import win32api
import win32con


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


File_Path = os.getcwd()	+ "\\"	#获取到当前文件的目录
img_temp_path = File_Path + "temp\\"

if not os.path.exists(img_temp_path):
	os.makedirs(img_temp_path)

date_now = datetime.datetime.now().strftime('%Y%m%d')

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

x = range(1,n+1)
for i in x:
	pic = ImageGrab.grab((410,185,2145,1520))	#default as full screeen, also a rectangle (x0,y0,x1,y1)
	picture_name = img_temp_path + str(date_now) + "_" + str(str(i).zfill(4)) + ".png"
	pic.save(picture_name)
	win32api.keybd_event(0x22,0,0,0)	# use PageDown to changge code is 34(0x22)
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
