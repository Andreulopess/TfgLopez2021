import cv2
import cv2
import numpy as np

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('jo.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(30, 30),
                                     maxSize=(200, 200))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 0, 0), -1)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
