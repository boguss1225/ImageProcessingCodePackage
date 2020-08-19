import numpy as np
import glob
import os
from PIL import Image

# PATH of file directory
# DIRECTORY_PATH = 'C:/Users/younh/OneDrive - University of Tasmania/MasterProject_Mouse_Brain_Atlas/Data/ROI_examples_annotation'
DIRECTORY_PATH = 'C:\\Users\\younh\\Desktop\\brain_rot_test\\'
TARGET_PATH = DIRECTORY_PATH

# get list of images in a directory 
files = [f for f in glob.glob(DIRECTORY_PATH+"*.jpg", recursive=True)]
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
    #how many
    for i in range(1,11):
	    # rotate image with 2 interver Right and Left
	    rotated_imgL = img.rotate(i*2,expand=True)
	    rotated_imgR = img.rotate(360-(i*2),expand=True)
	    # save resized image
	    rotated_imgL.save(TARGET_PATH+filename.split('.')[0]+"+r"+str(i*2)+".vsi.jpg")
	    rotated_imgR.save(TARGET_PATH+filename.split('.')[0]+"-r"+str(i*2)+".vsi.jpg")
    # print process
    print("[",cnt,"/",total,"]",filename)
    cnt +=1

print("<<finish>>")