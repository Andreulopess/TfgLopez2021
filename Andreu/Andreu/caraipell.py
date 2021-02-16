import cv2
import numpy as np

#faceClassif de haarcascade per sa cara

#hsv per color pell, amb un rang minim i rang maxim

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('jo.jpeg')

#hsv
hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#color pell
lower = np.array([0,10,60], dtype = "uint8")
upper = np.array([20,150,255], dtype = "uint8")

skin_mask = cv2.inRange(hsv_frame, lower,upper)

skin = cv2.bitwise_and(image,image,mask = skin_mask)


#aixo es per detectar sa cara

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30,30),
	maxSize=(200,200))

for (x,y,w,h) in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

#mascara de ses dues mascares
combinat = image & skin 


cv2.imshow('Combinat',combinat) #mescla
cv2.imshow('Pell',skin)		#pell
cv2.imshow('Cara',image)	#cara
cv2.waitKey(0)
cv2.destroyAllWindows()
