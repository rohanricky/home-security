import numpy as np
import cv2

cap = cv2.VideoCapture('1.avi')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame,learningRate=0.0001)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(500) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
