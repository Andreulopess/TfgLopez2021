import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)
while True:

    _, frame = cap.read()
    frame = imutils.resize(frame, width = 400)
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0,10,60])
    upper_blue = np.array([20,150,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
