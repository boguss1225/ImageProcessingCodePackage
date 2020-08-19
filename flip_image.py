import numpy as np
import glob
import os
from PIL import Image, ImageOps

# PATH of file directory
# DIRECTORY_PATH = 'C:/Users/younh/OneDrive - University of Tasmania/MasterProject_Mouse_Brain_Atlas/Data/ROI_examples_annotation'
DIRECTORY_PATH = 'C:\\Users\\younh\\Desktop\\brain_rot_test\\'
TARGET_PATH = DIRECTORY_PATH

# get list of images in a directory 
files = [f for f in glob.glob(DIRECTORY_PATH+"*.vsi.jpg", recursive=True)]
total = len(files)
cnt = 1;
if total == 0 : print("probably wrong Path : ", DIRECTORY_PATH)

print("<<start>>")

for f in files:
    # import image
    img = Image.open(f)
    filename = f.split('\\')[5]
    # get image file name
    print(filename, len(f.split('\\')))
    
    # flip image with 2 interver Right and Left
    # flipped_img = ImageOps.flip(img)
    mirrored_img = ImageOps.mirror(img)
    
    # save flipped image
    # flipped_img.save(TARGET_PATH+filename.split('.')[0]+"f"+".vsi.jpg")
    mirrored_img.save(TARGET_PATH+filename.split('.')[0]+"m"+".vsi.jpg")
    
    # print process
    print("[",cnt,"/",total,"]",filename)
    cnt +=1

print("<<finish>>")