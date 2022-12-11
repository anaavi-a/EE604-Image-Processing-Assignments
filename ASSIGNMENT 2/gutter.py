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
pth = pth + "/cleaned-gutter.jpg"
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
dilated_img = cv.dilate(gray, np.ones((7,7), np.uint8))
bg_img = cv.medianBlur(dilated_img, 25)
diff_img = 255 - cv.absdiff(gray, bg_img)
norm_img = cv.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
cv.imwrite(pth,norm_img)
