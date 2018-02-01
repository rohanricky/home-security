import cv2

cap = cv2.VideoCapture('0.avi')
while(cap.isOpened()):
    ret, frame = cap.read()

#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    cv2.waitKey(1000)

cap.release()
cv2.destroyAllWindows()
