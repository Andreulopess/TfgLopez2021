# import the necessary packages
import numpy as np
import cv2
import imutils

##Arxiu per trobar cara
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frame = cv2.imread('jo.jpeg')

framecopia = frame

#RANGS PER SA FOTO
#lower = np.array([0, 54, 21], dtype = "uint8")
#upper = np.array([184, 255, 153], dtype = "uint8")

lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

##gray per cara
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

##copy paste
#faces = faceClassif.detectMultiScale(gray,
#	scaleFactor=1.1,
#	minNeighbors=5,
#	minSize=(30,30),
#	maxSize=(200,200))

#for (x,y,w,h) in faces:
#	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)

#cv2.imshow("1", frame)

#for (x,y,w,h) in faces:
#	cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+50),(0,0,0),-1)



##gray per cara
gray = cv2.cvtColor(framecopia, cv2.COLOR_BGR2GRAY)

##copy paste
faces = faceClassif.detectMultiScale(gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30,30),
	maxSize=(200,200))


for (x,y,w,h) in faces:
	cv2.rectangle(framecopia,(x-20,y-20),(x+w+20,y+h+50),(0,0,0),-1)

img = imutils.resize(frame, width = 400)


imgcopia = imutils.resize(framecopia, width = 400)


converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
skinMask = cv2.inRange(converted, lower, upper)


kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
skinMask = cv2.erode(skinMask, kernel, iterations = 1)
skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
skin = cv2.bitwise_and(img, img, mask = skinMask)

cv2.imshow("2", np.hstack([img, skin]))

cv2.waitKey(0)
cv2.destroyAllWindows()
