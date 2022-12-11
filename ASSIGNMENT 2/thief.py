import numpy as np
import cv2 as cv
import os
import sys
import math as mth

# taking image as input
if len(sys.argv) > 1:
    filen = sys.argv[1]
else:
    print("image file not found please check the file name :(")
pth = os.path.dirname(os.path.realpath(__file__))
pth1 = pth + filen[1:]
img = cv.imread(pth1)
if img is None:
    sys.exit("Could not read the image.")
pth = pth + "/"+"enhanced-"+filen[2:]
#image manipulation
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
Gaussian = cv.GaussianBlur(gray, (5, 5), 0)
sum = 0
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
for i in range(0,height):
    for j in range(0,width):
        sum = sum + gray[i][j]
s = sum/(height*width)
s = mth.floor(s)
#Clip limit adjuster
if s < 40:
    clp = 20-s/2
else:
    clp = 10
clahe = cv.createCLAHE(clipLimit = clp)
final_img = clahe.apply(Gaussian)
#applying adaptive blur to images 
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image = cv.filter2D(src=final_img, ddepth=-1, kernel=kernel)    #applying sharpening filter 2D
cv.imwrite(pth,image)