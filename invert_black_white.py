import os
import glob
import cv2

# PATH of file directory
DIRECTORY_PATH = 'C:\\Users\\younh\\OneDrive - University of Tasmania\\MasterProject_Mouse_Brain_Atlas\\Data\\ROI examples'

# get list of images in a directory 
files = [f for f in glob.glob(DIRECTORY_PATH+"/*ROI.tif", recursive=True)]
total = len(files)
cnt = 1;
if total == 0 : print("probably wrong Path : ", DIRECTORY_PATH)

# Change the current directory  
# to specified directory  
os.chdir(DIRECTORY_PATH) 

print("<<start>>")

for f in files:
    # import image
    img2 = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    filename = f.split('/')[len(f.split('/'))-1]
    invert = cv2.bitwise_not(img2)
    print("[",cnt,"/",total,"]",filename)
    cnt +=1
    image = cv2.imwrite(filename, invert)

