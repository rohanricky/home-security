import numpy as np
import cv2

cap = cv2.VideoCapture('2018-03-09 23:29:00.812935.avi')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(500) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
