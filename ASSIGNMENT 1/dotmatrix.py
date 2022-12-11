import numpy as np
import cv2 as cv
import os
import sys
img = np.zeros((300,500), np.uint8)
pth = os.path.dirname(os.path.realpath(__file__))
pth = pth + "/dotmatrix.jpg"
#40+40+60*7 = 500; 50*6 = 300
def cir(p,q):
    cv.circle(img,(p,q),25,255,-1) #open to manipulation
def digitise(digit):#correct 100%
    X = [(0,0,0),
         (0,0,0),
         (0,0,0),
         (0,0,0),
         (0,0,0)]
    if(digit == 0):
        X = [(1,1,1),
             (1,0,1),
             (1,0,1),
             (1,0,1),
             (1,1,1)]
    if(digit == 1):
        X = [(0,1,0),
             (1,1,0),
             (0,1,0),
             (0,1,0),
             (1,1,1)]
    if(digit == 2):
        X = [(1,1,1),
             (0,0,1),
             (1,1,1),
             (1,0,0),
             (1,1,1)]
    if(digit == 3):
        X = [(1,1,1),
             (0,0,1),
             (1,1,1),
             (0,0,1),
             (1,1,1)]
    if(digit == 4):
        X = [(1,0,1),
             (1,0,1),
             (1,1,1),
             (0,0,1),
             (0,0,1)]
    if(digit == 5):
        X = [(1,1,1),
             (1,0,0),
             (1,1,1),
             (0,0,1),
             (1,1,1)]
    if(digit == 6):
        X = [(1,1,1),
             (1,0,0),
             (1,1,1),
             (1,0,1),
             (1,1,1)]
    if(digit == 7):
        X = [(1,1,1),
             (1,0,1),
             (0,0,1),
             (0,0,1),
             (0,0,1)]
    if(digit == 8):
        X = [(1,1,1),
             (1,0,1),
             (1,1,1),
             (1,0,1),
             (1,1,1)]
    if(digit == 9):
        X = [(1,1,1),
             (1,0,1),
             (1,1,1),
             (0,0,1),
             (1,1,1)]
    return X
def draw(col,row, M):
    for i in range(5):
        for j in range(3):
            if(M[i][j]==1):
                cir((col+j*60),(row+i*60))#open to manipulation
if len(sys.argv) > 1:
    num = int(sys.argv[1])
else:
    num = int(input("Enter a 2 digit number: "))
num1 = num//10
num2 = num%10
A = digitise(num1)
Y = digitise(num2)
draw(70,30,A)#open to manipulation
draw(310,30,Y)#open to manipulation
cv.imwrite(pth,img)
