import cv2
import numpy as np
'''
'''

########### Imatges ############
'''
#Carregar imatge de color, gris o unchanged
cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
Per mostrar imatges empleam cv2.imshow, on se posa es titol de sa finestra i s'objecte que agafes
cv2.waitKey es temps es en milisegons
cv2.namedWindow('Nom finestra',FLAG) si empleam window Normal se pot tocar sa mida
cv2.imwrite guarda sa imatge
'''
'''

nofre = cv2.imread("exu.jpg")
#cv2.namedWindow('Nofre',cv2.WINDOW_NORMAL)
cv2.imshow('Nofre',nofre)
cv2.waitKey(0)
'''


########### Videos ############

'''
S'ha de crear un objecte VideoCapture, dins es paràmetres se posa o index de camara o direcció del video
Per saber si s'ha llegit es frame correctament usam
cap.read(), torna True o False per saber si s'ha llegit
Si volem guardar video hem de crear un obejcte VideoWriter
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
'''

'''
cap = cv2.VideoCapture(0)

while(1):
    ret,frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

'''


########### Funcions ############

'''
img : The image where you want to draw the shapes
color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.
'''

img = np.zeros((512,512,3),np.uint8)
img = cv2.line(img,(0,0),(511,511),(255,0,0),5) #(imatge,punt1,punt2,color,grossor)
img= cv2.rectangle(img,(0,0),(511,511),(255,0,0),5)

cv2.imshow('Img',img)
cv2.waitKey(0)


cv2.destroyAllWindows()