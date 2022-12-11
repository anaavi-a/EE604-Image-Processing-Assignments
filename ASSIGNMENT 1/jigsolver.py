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
pth = pth + "/jigsolved.jpg"

# code begins here#
# dimensions = img.shape
# height = img.shape[0] #421
# width = img.shape[1]  #797
# i = 0
# while(i<=width):
#     cv.line(img,(i,0),(i,height),0,1)
#     i = i+10
# i = 0
# while(i<=width):
#     cv.line(img,(0,i),(width,i),0,1)
#     i = i+10
   
img_1 = img[0:200,0:190]    #pink bird
img_2 = img[200:410,0:190]  #eye
img_3 = img[370:,370:]  #bottom strip
img_4 = img[150:331,515:700]   #yellow bird

#manipulations
img_3 = cv.flip(img_3,0)
img_4 = cv.flip(img_4,1)
img_2 = cv.flip(img_2,0)
B,G,R = cv.split(img_1)
img_1 = cv.merge((G,B,R))
img_1 = cv.copyMakeBorder(img_1, 0,10,0,0,cv.BORDER_REPLICATE, None, 0)

#image addition
img[370:,370:] = img_3
img[150:331,515:700] = img_4
img[200:410,0:190] = img_1
img[0:210,0:190] = img_2
#code ends here
cv.imwrite(pth,img)
