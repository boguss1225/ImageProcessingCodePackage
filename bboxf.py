import cv2
import numpy as np
import glob
import csv

# PATH of file directory
DIRECTORY_PATH = 'C:/Users/younh/Desktop/STUDY/Projects/Mouse_Brain/data/DATASETsubmit/resized/train_mask'

# get list of images in a directory 
files = [f for f in glob.glob(DIRECTORY_PATH+"/*.png", recursive=True)]
total = len(files)
cnt = 1;
if total == 0 : print("probably wrong Path : ", DIRECTORY_PATH)


print("<<start>>")

# coloums for CSV
arr1 = [
	["xmin", "ymin", "xmax", "ymax", "Frame"]
]

for f in files:
    # import image
    img2 = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    filename = f.split('/')[len(f.split('/'))-1]

    ys, xs = np.nonzero(img2)
    ymin, ymax = ys.min(), ys.max()
    xmin, xmax = xs.min(), xs.max()
    
    pos_arry = [xmin, ymin, xmax, ymax, filename]
    arr1.append(pos_arry)

    print("[",cnt,"/",total,"]",filename," >> crop: xm-",xmin," ym-",ymin," xx-",xmax," yx-",ymax)
    cnt +=1

# create CSV file
with open(DIRECTORY_PATH+'/train_mask.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(arr1)
print("CSV file saved!!")

print("<<finish>>")

# check the output
'''
cv2.imshow("bbox", img2)
while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break

cv2.destroyAllWindows()
'''