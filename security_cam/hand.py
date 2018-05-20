import cv2
import time

cam = cv2.VideoCapture(0)
x=0
while(1):
    grabbed, frame = cam.read()
    if not grabbed:
        break

    cv2.imshow('hand',frame)
    cv2.imwrite('samples/negatives/'+str(x)+'.jpg',frame)
    x+=1
    time.sleep(0.1)
