import numpy as np
import glob
from PIL import Image

# PATH of file directory
DIRECTORY_PATH = 'C:/Users/younh/Desktop/STUDY/Projects/Mouse_Brain/data/DATASETsubmit/mrcnn_val_dataset_images/'
# PATH for saving directory
TARGET_PATH =  'C:/Users/younh/Desktop/STUDY/Projects/Mouse_Brain/data/DATASETsubmit/resized/test_image/'

# Target Size
WIDTH = 960
HEIGHT = 640

# get list of images in a directory 
files = [f for f in glob.glob(DIRECTORY_PATH+"/*.jpg", recursive=True)]
total = len(files)
cnt = 1;
if total == 0 : print("probably wrong Path : ", DIRECTORY_PATH)

print("<<start>>")

for f in files:
    # import image
    img = Image.open(f)
    filename = f.split('\\')[1]
    # get image file name
    print(filename, len(f.split('\\')))
    # resize image
    img = img.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    # save resized image
    img.save(TARGET_PATH+filename)
    # print process
    print("[",cnt,"/",total,"]",filename)
    cnt +=1

print("<<finish>>")