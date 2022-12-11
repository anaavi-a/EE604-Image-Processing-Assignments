import numpy as np
import cv2 as cv
import os
import sys
import math as mth
if len(sys.argv) > 1:
    filen_1 = sys.argv[1]
    filen_2 = sys.argv[2]
    filen_3 = sys.argv[3]
else:
    print("image file not found please check the file name :(")
pth = os.path.dirname(os.path.realpath(__file__))
pth_1 = pth + filen_1[1:]
pth_2 = pth + filen_2[1:]
pth_3 = pth + filen_3[1:]
img1 = cv.cvtColor(cv.imread(pth_1), cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(cv.imread(pth_2), cv.COLOR_BGR2GRAY)
img3 = cv.cvtColor(cv.imread(pth_3), cv.COLOR_BGR2GRAY)
if img1 is None:
    sys.exit("Could not read the image of 1st argument")
if img2 is None:
    sys.exit("Could not read the image of 2nd argument")
if img3 is None:
    sys.exit("Could not read the image of 3rd argument")
pth = pth + "/flyingelephant.jpg"
s1 = img1.shape
s2 = img2.shape

K = s2[1]/s1[1]
Cbn = np.zeros(s1)
Cbr = np.zeros(s1)
Cb = np.zeros(s1,dtype=np.uint8)
Cr = np.zeros(s1,dtype=np.uint8)
imgb = cv.blur(img1,(3,3))

for j in range(0,s1[1]):
    for i in range(0,s1[0]):
        s = img1[i,j]/imgb[i,j]
        Cb[i,j] = int(img2[mth.floor(i*K), mth.floor(j*K)]*s)
        Cr[i,j] = int(img3[mth.floor(i*K), mth.floor(j*K)]*s)

Cb = cv.blur(Cb,(3,3))
Cr = cv.blur(Cr,(3,3))

for j in range(0,s1[1]):
    for i in range(0,s1[0]):
        Cb[i,j] = int((Cb[i,j]))
        Cr[i,j] = int((Cr[i,j]))

im = cv.merge([img1,Cr,Cb])
xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
rgb = im.astype(np.float64)
rgb[:,:,[1,2]] -= 128
rgb = rgb.dot(xform.T)
np.putmask(rgb, rgb > 255, 255)
np.putmask(rgb, rgb < 0, 0)
im = np.uint8(rgb)
cv.imwrite(pth,im)