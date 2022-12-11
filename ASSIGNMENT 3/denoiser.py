import numpy as np
import cv2 as cv
import os
import sys
import math as mth
if len(sys.argv) > 1:
    filen = sys.argv[1]
else:
    print("image file not found please check the file name :(")
pth = os.path.dirname(os.path.realpath(__file__))
pth1 = pth + filen[1:]
img = cv.imread(pth1)
if img is None:
    sys.exit("Could not read the image.")
pth = pth + "/denoised.jpg"
b,g,r = cv.split(img)
siz1 = b.shape
b1 = cv.bilateralFilter(b,20,20,20)
g1 = cv.bilateralFilter(g,20,20,20)
r1 = cv.bilateralFilter(r,20,20,20)
imf = cv.merge([b1,g1,r1])
output = cv.normalize(imf, None, 0, 255, cv.NORM_MINMAX)
cv.imwrite(pth,output)
