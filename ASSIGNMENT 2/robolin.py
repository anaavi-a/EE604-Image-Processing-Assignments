from ctypes import sizeof
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
pth = pth + "/robolin-" + filen[2:]
img = cv.imread(pth1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
kernel_size = 3
blur_gray = cv.GaussianBlur(gray,(kernel_size, kernel_size),0)
low_threshold = 50
high_threshold = 150
edges = cv.Canny(blur_gray, low_threshold, high_threshold)
rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 10  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 100  # minimum number of pixels making up a line
max_line_gap = 20  # maximum gap in pixels between connectable line segments
line_image = np.copy(img)  # creating a blank to draw lines on
lines = cv.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                    min_line_length, max_line_gap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(line_image,(x1,y1),(x2,y2),(255,0,255),3)
cv.imwrite(pth,line_image)
# print(pth)