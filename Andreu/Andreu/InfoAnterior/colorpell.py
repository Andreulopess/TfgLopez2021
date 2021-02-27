#Rangos de colores en HSV a detectar
#loweryellow = [18, 100, 100]
#upperyellow = [30, 255, 255]
#lowergreen = [80,80,50]
#uppergreen = [100,255,255]
#lowerlightgreen = [40, 100, 50]
#upperlightgreen = [75, 255, 255]

#Colors pell amb HSI
#H:[270,310]
#S:[20,110]
#nkin = 272

import numpy as np
import cv2

img = cv2.imread('jo.jpeg')
#img = cv2.imread('nig.jpg')

hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#color pell
lower = np.array([0,10,60], dtype = "uint8")
upper = np.array([20,150,255], dtype = "uint8")

skin_mask = cv2.inRange(hsv_frame, lower,upper)

skin = cv2.bitwise_and(img,img,mask = skin_mask)

#skin2 = cv2.bitwise_and(img1,img1,mask = skin_mask)


cv2.imshow("pell", skin)
#cv2.imshow("pell", skin2)
cv2.waitKey(0)
cv2.destroyAllWindows()
