import numpy as np
import cv2

cap = cv2.VideoCapture('/home/rohan/github/home/videos/2018-04-12 16:10:13.150897.avi')

# fgbg = cv2.createBackgroundSubtractorMOG2()
def play_video():
	while(1):
	    ret, frame = cap.read()

	    # fgmask = fgbg.apply(frame)

	    cv2.imshow('frame',frame)
	    k = cv2.waitKey(500) & 0xff
	    if k == 27:
	        break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	play_video()