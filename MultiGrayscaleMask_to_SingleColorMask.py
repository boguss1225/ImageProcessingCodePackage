# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:51:42 2020

@author: younh
"""

'''
image files : have to be .jpg format
mask files : have to be 'filename_classnumber.png' format (eg. 'picture12_8.png')
               mask file names have to be started with same name of compatble image file name 
               (eg. picture12.jpg -> picture12_m_8.png)
               mask file size has to be same size with image file.
'''
import os
import sys
import cv2
from PIL import Image
import numpy as np

# config these please
NUM_OF_CLASS = 8 #MAX15 if you wanna add-> add RGB array more
IMAGE_PATH= r'C:\Users\younh\Desktop\STUDY\Projects\Mouse_Brain\data\SeBReDATASETsubmit\test_image'
MASK_PATH = r"C:\Users\younh\Desktop\STUDY\Projects\Mouse_Brain\data\SeBReDATASETsubmit\test_mask"
OUT_PATH = r"C:\Users\younh\Desktop\STUDY\Projects\Mouse_Brain\data\SeBReDATASETsubmit\test_out"
RGB = [[255, 0, 0],[255,128,0],[255,255,0],
       [228,255,204],[0,255,0],[0,153,76],
       [0,255,255],[0,128,255],[0,0,255],
       [127,0,255],[255,0,255],[255,204,229],
       [102,0,51],[204,229,255],[153,153,0]]
i=0;

# check PATHs
if not os.path.exists(IMAGE_PATH) :
    print("Image path error")
    sys.exit()
    
if len(os.listdir(IMAGE_PATH)) == 0 :
	print("Image path is empty")
	sys.exit()

if not os.path.isdir(IMAGE_PATH) :
    print("Mask path error")
    sys.exit()

if len(os.listdir(MASK_PATH)) == 0 :
	print("Mask path is empty")
	sys.exit()
    
if not os.path.exists(OUT_PATH) :
	os.makedirs(OUT_PATH)

# get list of images
images_filename = os.listdir(IMAGE_PATH)
NUMB_IMAGES = len(images_filename)
# trim filename of images. abcd.jpg -> abcd
for filename in images_filename:
    if filename[-3:] !='jpg':
      del images_filename[images_filename.index(filename)]
for filename in images_filename:  
    images_filename[images_filename.index(filename)] = filename[0:-4]
images_filename.sort()

# get list of masks
masks_filename = os.listdir(MASK_PATH)
# trim filename of masks. abc_m_1.png -> abc_m_1
for filename in masks_filename:
    if filename[-3:] !='png':
      del masks_filename[masks_filename.index(filename)]
for filename in masks_filename:  
    masks_filename[masks_filename.index(filename)] = filename[0:-4]
masks_filename.sort()

# change_color_of_mask
def change_color_of_mask(mask, class_num, whiteboard):
    data = np.array(mask)
    
    row, col = data.shape
    
    # replace all 0 value with class_num
    for i in range(row) :
        for j in range(col) :
            if 100 < data[i][j] and data[i][j]<=255 :
                whiteboard[i][j][0] = RGB[class_num][0]
                whiteboard[i][j][1] = RGB[class_num][1]
                whiteboard[i][j][2] = RGB[class_num][2]
    
    return whiteboard

# loop for all image files
for img_name in images_filename :
    # set new mask saving name
    new_mask_name = img_name+'.png'
    
    # get image number
    poo, img_numb = img_name.rsplit('_',1)
    
    # oepn image
    img = Image.open(IMAGE_PATH+"\\"+img_name+'.jpg');
    
    # creat white board
    data = np.array(img)
    whiteboard = np.zeros_like(data)
    
    # iterate all mask files
    for mask_name in masks_filename :
        if mask_name.startswith("section_masks_" + img_numb+"_m") :
            print("merge : "+mask_name+" into "+new_mask_name)
            # get class number
            poo, class_num = mask_name.rsplit('_',1)
            class_num = int(class_num)
            
            #get mask png
            mask = Image.open(MASK_PATH+"\\"+mask_name+'.png')

        	# change color and merge mask
            change_color_of_mask(mask, class_num, whiteboard)
    
    # save image
    saveImage = Image.fromarray(whiteboard)
    saveImage.save(OUT_PATH+"\\"+new_mask_name)
    
    # print process
    i=i+1
    print("["+str(i)+"/"+str(NUMB_IMAGES)+"] Creation Finished!"+new_mask_name)










