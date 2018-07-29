import cv2

cam = cv2.VideoCapture(0)

while(True):
    grabbed, frame = cam.read()
    cv2.imshow('frame',frame)
    k=cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break

cv2.destroyAllWindows()
