import numpy as np
import glob
import cv2
from PIL import Image

# PATH of file directory
DIRECTORY_PATH = 'C:/Users/younh/Desktop/fac'
# PATH for saving directory
TARGET_PATH =  'C:/Users/younh/Desktop/fac'

# get list of images in a directory 
files = [f for f in glob.glob(DIRECTORY_PATH+"/*.jpeg", recursive=True)]
total = len(files)
cnt = 1;
if total == 0 : print("probably wrong Path : ", DIRECTORY_PATH)

print("<<start>>")

for f in files:
    # get image file name
    filename = f.split('\\')[1]
    print(filename, len(f.split('\\')))

    # resize image
    bgr = cv2.imread(f)

    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    
    # cv2.imwrite(TARGET_PATH+filename,lab)
    
    lab_planes = cv2.split(lab)

    # clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(32,32))

    # lab_planes[0] = clahe.apply(lab_planes[0])

    lab = cv2.merge(lab_planes)

    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    
    # save resized image
    cv2.imwrite(TARGET_PATH+filename,bgr)
    # print process
    print("[",cnt,"/",total,"]",filename)
    cnt +=1

print("<<finish>>")