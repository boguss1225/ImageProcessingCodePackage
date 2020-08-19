import numpy as np
import glob
import os
from PIL import Image

# PATH of file directory
DIRECTORY_PATH = 'C:/Users/younh/OneDrive - University of Tasmania/MasterProject_Mouse_Brain_Atlas/Data/ROI_examples_annotation'

# get list of images in a directory 
files = [f for f in glob.glob(DIRECTORY_PATH+"/*.jpg", recursive=True)]
total = len(files)
cnt = 1;
if total == 0 : print("probably wrong Path : ", DIRECTORY_PATH)

print("<<start>>")

for f in files:
    # import image
    filename = f.split('\\')[1]
    renamed_filename = f.split('.jpg')[0]+".jpeg"
    # get image file name
    print(filename, len(filename))
    # rename image
    os.rename(f, renamed_filename)
    # print process
    print("[",cnt,"/",total,"]",filename)
    cnt +=1

print("<<finish>>")