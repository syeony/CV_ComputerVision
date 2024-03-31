import cv2 as cv
import sys

img = cv.imread('./soccer.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_small=cv.resize(gray, dsize=(0,0), fx=0.5,fy=0.5)

cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)

cv.imshow('img', img)
cv.imshow('gray', gray)
cv.imshow('gray_small', gray_small)