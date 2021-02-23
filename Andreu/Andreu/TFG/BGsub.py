import imutils
import numpy as np
import argparse
import cv2

maadalt = cv2.imread("Maadalt.jpg")
maabaix =cv2.imread("Mabaix.jpg")
cv2.imshow('Ma adalt normal', maadalt)


#definim array
lower = np.array([0,10,60], dtype = "uint8")
upper = np.array([20,150,255], dtype = "uint8")
#Modificar mida, troba mes punts
frame = imutils.resize(maadalt,width=1200)



converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
skinMask = cv2.inRange(converted, lower, upper)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
skinMask = cv2.erode(skinMask, kernel, iterations = 2)
skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
skinMaadalt = cv2.bitwise_and(frame, frame, mask = skinMask)

	# show the skin in the image along with the mask

cv2.imshow("Ma adalt", skinMaadalt)




cv2.waitKey(0)