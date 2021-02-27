import argparse
import glob
'''import os

import cv2

from yolo import YOLO

def treurecoords(nomFOTO):
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--images', default="images", help='Path to images or image file')
    ap.add_argument('-n', '--network', default="normal", help='Network Type: normal / tiny / prn / v4-tiny')
    ap.add_argument('-d', '--device', default=0, help='Device to use')
    ap.add_argument('-s', '--size', default=416, help='Size for yolo')
    ap.add_argument('-c', '--confidence', default=0.25, help='Confidence for yolo')
    args = ap.parse_args()

    yolo = YOLO("models/cross-hands.cfg", "models/cross-hands.weights", ["hand"])

    yolo.size = int(args.size)
    yolo.confidence = float(args.confidence)
    #   Carrega de imatges


    cv2.imshow(nomFOTO)

    width, height, inference_time, results = yolo.inference(mat)

    print("%s in %s seconds: %s classes found!" %
          (os.path.basename(nomFOTO), round(inference_time, 2), len(results)))

    output = []
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 848, 640)

    detection_count = 0

    for detection in results:
        id, name, confidence, x, y, w, h = detection
        cx = x + (w / 2)
        cy = y + (h / 2)


        detection_count += 1

        # draw a bounding box rectangle and label on the image
        color = (255, 0, 255)
        cv2.rectangle(mat, (x, y), (x + w, y + h), color, 1)
        text = "%s (%s)" % (name, round(confidence, 2))
        cv2.putText(mat, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                    0.25, color, 1)

        print("%s with %s confidence" % (name, round(confidence, 2)))
        print(x, y)
        # cv2.imwrite("export.jpg", mat)

    # show the output image
    cv2.imshow('image', mat)
    return cx, cy
    cv2.waitKey(0)'''
#cv2.destroyAllWindows()
