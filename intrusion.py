import face_recognition
import argparse
import datetime
import imutils
import time
import cv2
from multiprocessing import Process
from lib.send_email import email
from face import face
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
ap.add_argument("-t",default=False)
args = vars(ap.parse_args())

#Video of thief
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
(h, w) = face_recognition.load_image_file('donga.jpg').shape[:2]
# Webcam
cam = cv2.VideoCapture(0)
# initialize the first frame in the video stream
firstFrame = None
count,vid_no=0,0
while True:
	if not os.path.exists(str(vid_no)+'.avi'):
		video=cv2.VideoWriter(str(vid_no)+'.avi',fourcc,15.0,(w,h),True)
	# grab the current frame and initialize the occupied/unoccupied text
	(grabbed, frame) = cam.read()
	text = "Unoccupied"
	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		prevFrame = gray
		continue
	consecDelta = cv2.absdiff(prevFrame,gray)
	consecThresh = cv2.threshold(consecDelta,25,255,cv2.THRESH_BINARY)[1]
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
#	pyautogui.confirm('Shall I confirm?')

	consecThresh=cv2.dilate(consecThresh,None,iterations=2)

	_, fuck, _ = cv2.findContours(consecThresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	# loop over the contours
	detect_face=face(frame)

	for x in fuck:
		# if the contour is too small, ignore it
		if cv2.contourArea(x) < 3000 and not detect_face:
			continue

		text = "Occupied"
	if text=="Occupied":
		if detect_face is 1:
			print("good")
			count=0
		else:
			count+=1
			print('bad')
			video.write(frame)
			if count  >= 50:
				Process(target=email,args=(str(vid_no)+'.avi',)).start()
				vid_no+=1
				count=0
	prevFrame = gray

	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.imshow("Security Feed", frame)
	cv2.imshow('gray',gray)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break


# cleanup the cam and close any open windows
try:
	video.release()
except:
	pass
cam.release()
cv2.destroyAllWindows()
