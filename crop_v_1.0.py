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

import ctypes

def timer():
    for num in range(2,0,-1):   # 3 seconds
        os.system('cls')
        print("--------------------------------------------")
        print("    please switch to the capture screen!")
        print("     this will start in {} second(s).".format(num))
        print("--------------------------------------------")
        if num == 1:
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),6)        # minimis
            # refer to: https://www.cnblogs.com/candyzkn/p/4428590.html
        else:
            pass
        time.sleep(1)
    os.system('cls')
    print("--------------------------------------------")
    print("                  doing                     ")
    print("--------------------------------------------")

def getBookSize(picture_i):
    image = cv2.imread(picture_i)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    global height
    global weight   
    height = np.array(gray).shape[0]        # y
    weight = np.array(gray).shape[1]        # x
    # print(weight, height)                   # 2560 1600
    gray_edges_x = []
    gray_edges_y = []
    # # print(gray)
    # gray[y,x]
    # print(gray[100,500])      # 255
    # print(gray[500,100])      # 136
    # print(gray[500,300])      # 252

    # gray regtangular
    for j in range(int(weight/5)):
        time = 0
        for i in range(int(height/5)):
            if 130 <=gray[i*5][j*5] <= 140:       # find gray
                # print(i,j,"gray")
                time = time + 1
                if time > 0.80 * height / 5:
                    gray_edges_x.append(j*5)                          
                    break
    gray_left = min(gray_edges_x)
    gray_right = max(gray_edges_x)
    # print("gray_left,gray_right = ",gray_left,gray_right)
    for j in range(int(height/5)):
        time = 0
        for i in range(int(weight/5)):
            if 130 <=gray[j*5][i*5] <= 140:       # find gray
                # print(j,i,"gray")
                time = time + 1
                if time > 0.80 * weight / 5:
                    gray_edges_y.append(j*5)                          
                    break
    gray_top = min(gray_edges_y)
    gray_bottom = max(gray_edges_y)
    # print("gray_top,gray_bottom  = ",gray_top,gray_bottom)

    # white regtangular
    white_edges_x = []
    white_edges_y = []
    for j in range(int(gray_left/5),int(gray_right/5)):
        time = 0
        for i in range(int(gray_top/5),int(gray_bottom/5)):
            if gray[i*5][j*5] >= 245:       # find white
                # print(i,j,"gray")
                time = time + 1
                if time > 0.60 * height / 5:
                    white_edges_x.append(j*5)                          
                    break
    white_left = min(white_edges_x)
    white_right = max(white_edges_x)
    # print("white_left,white_right = ",white_left,white_right)

    for j in range(int(gray_top/5),int(gray_bottom/5)):
        time = 0
        for i in range(int(gray_left/5),int(gray_right/5)):
            if gray[j*5][i*5] >= 245:       # find white
                # print(j,i,"gray")
                time = time + 1
                if time > 0.50 * weight / 5:
                    white_edges_y.append(j*5)                          
                    break
    white_top = min(white_edges_y)
    white_bottom = max(white_edges_y)
    # print("white_top,white_bottom = ",white_top,white_bottom)
    pic_size = (white_left, white_top, white_right, white_bottom)
    # print(pic_size)
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

def PageUp():
    win32api.keybd_event(0x21,0,0,0)    # use PageUp to changge code is 33(0x21)
    win32api.keybd_event(0x21,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1.2)

def PageDown():
    win32api.keybd_event(0x22,0,0,0)    # use PageDown to changge code is 34(0x22)
    win32api.keybd_event(0x22,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1.2)


try:
    ####################################################
    pages_str = input("please input the number of total pages (with 0~9) = ")
    while not pages_str.isdigit() or not int(pages_str):
        pages_str = input("input erro! please input the number (with 0~9) = ")
    pages = int(pages_str)
    ####################################################
    # screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    # screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    # print(screen_x,screen_y)

    hDC = win32gui.GetDC(0)
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    # print(w,h)

    timer()
    date_now = datetime.datetime.now().strftime('%Y%m%d')
    File_Path = os.getcwd() + "\\"  #获取到当前文件的目录
    img_temp_path = File_Path + "temp\\"

    #采取新建文件夹的方式避免删除已有temp文件夹中的文件
    for i in range(1,100):
        if os.path.exists(img_temp_path):
            img_temp_path = File_Path + "temp_" + str(str(i).zfill(2)) + "\\"
        elif not os.path.exists(img_temp_path):
            os.makedirs(img_temp_path)                         
            break
    height = 0
    weight = 0

    x = range(1,pages + 1)
    # default_size = (0,0,weight,height)
    default_size = (0,0,w,h)
    # print(default_size)
    size_all = default_size

    for num in range(1,6):
        if num <= 3:
            PageDown()
        elif num == 4:
            picture_temp = img_temp_path + str(date_now) + "_size_crop.png"
            picGrab(picture_temp,default_size)
            size_all = (x0,y0,x1,y1) =  getBookSize(picture_temp)
            size_left = (x0,y0,int((x1+x0)/2),y1)
            size_right = (int((x1+x0)/2),y0,x1,y1)
            size_center = (int((3*x0+x1)/4),y0,int((3*x1+x0)/4),y1)
            os.remove(picture_temp)
            PageUp()
            PageUp()
            PageUp()
        else:
            for i in x:
                picture_i = img_temp_path + str(date_now) + "_" + str(str(i).zfill(4)) + ".png"
                if i == 1:
                    picGrab(picture_i,size_center)
                    PageDown()
                elif  i == pages:
                    picGrab(picture_i,size_center)
                elif i % 2 == 0:
                    picGrab(picture_i,size_left)
                else:
                    picGrab(picture_i,size_right)
                    PageDown()
    os.system('cls')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),9)        # 3
    # 20201002 changed the name of pdfFile
    auto_pdfFile = File_Path + str(date_now) + "_00.pdf"
    for i in range(1,100):
        if os.path.isfile(auto_pdfFile):
            auto_pdfFile = File_Path + str(date_now) + "_" + str(str(i).zfill(2)) + ".pdf"
        else:
            break
    check_box = ['y','Y','n','N']
    rename_check = str(input("Do you want to rename the file? [y]/n "))[0]
    while rename_check not in check_box:
        rename_check = str(input("please input [y]/n "))

    # bugreport: when input chinese book name, there would be some error leading to save file failed. / 2nd.Oct.2020
    # add error char

    error_char = ["\\","/","：","*","？","<",">","|","\"","“","”","'","‘","’","?",]
    if rename_check == 'y' or rename_check == 'Y':
        name_temp = str(input("please input the name of this book: "))
        flag = 0
        while not flag:
            while not len(name_temp):
                name_temp = str(input("please input the name of this book (not blank): "))
            for char in error_char:
                # print(flag)
                flag = flag + 1         # 8
                if char in name_temp:
                    print("文件名不能包含下列字符：")
                    print(error_char)
                    name_temp = str(input("please input the name of this book: "))
                    flag = 0
                    break
        file_name = File_Path + name_temp + ".pdf"
    else:
        file_name = auto_pdfFile

    os.system('cls')
    combine2Pdf(img_temp_path, file_name)
    print("-------------------------------------------------------------------")
    print("file has been saved as: \n" + file_name)
    print("-------------------------------------------------------------------")
    del_file(img_temp_path)
    os.rmdir(img_temp_path)

except:
    os.system('cls')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),9)
    # https://www.cnblogs.com/daofaziran/p/9015284.html
    print("-------------------------------------------------------------------")
    print("\033[1;31m                           !!!except!!!                            \033[0m")
    print("-------------------------------------------------------------------")