import numpy as np
import cv2 as cv
import os
import sys
if len(sys.argv) > 1:
    filen = sys.argv[1]
else:
    print("image file not found please check the file name :(")
pth = os.path.dirname(os.path.realpath(__file__))
pth1 = pth + filen[1:]
img = cv.imread(pth1)
if img is None:
    sys.exit("Could not read the image.")
dimensions = img.shape
height = dimensions[0]
width = dimensions[1]
#print(img[0][0])
b,g,r = cv.split(img)
sumb = 0
sumg = 0
sumr = 0 
for i in range(0,height):
    for j in range(0,width):
        sumb = sumb + b[i,j]
        sumg = sumg + g[i,j]
        sumr = sumr + r[i,j]
sumb = sumb/(height*width)
sumg = sumg/(height*width)
sumr = sumr/(height*width)
k1 = abs(sumg-sumb)
k2 = abs(2*sumg - sumr - sumb)
check = -1
err1 =0
err2 =0

if k1>=0 and k1<=6 and k2>=1 and k2<=8 :
    check = 1
elif k1>=0 and k1<=80 and k2>12 and k2<=85 :
    check = 2
elif k1>6 and k1<=20 and k2>=0 and k2<=12:
    check = 3
else:
    err1 = k1-80
    err2 = k2-85
    
if err1>0 and err2>0:
    check = 2    
elif err1>0 and err2<0:
    check = 2
elif err1<0 and err2>0:
    check = 2
elif err1<0 and err2<0:
    check = 1

print(check)
