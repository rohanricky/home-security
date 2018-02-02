import cv2
from concat import concat

concat()

cam = cv2.VideoCapture('video.avi')
'''
while(1):
    ret, frame = cam.read()

#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    cv2.imshow('frame',frame)
    cv2.waitKey(700)

cam.release()
cv2.destroyAllWindows()
'''
