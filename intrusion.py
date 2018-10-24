import face_recognition
import argparse
import datetime
import imutils
import time
import cv2
from multiprocessing import Process
from send_email import email
from face import face
import os
import random

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=20000, help="minimum area size")
ap.add_argument("-t","--test",default=False)
args = vars(ap.parse_args())
fgbg = cv2.createBackgroundSubtractorMOG2()
#Video of thief
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#(h, w) = face_recognition.load_image_file('donga.jpg').shape[:2]
(h,w) = (375,500)
# Webcam
if args.get("video",None) is None:
	cam = cv2.VideoCapture(0)
else:
	cam = cv2.VideoCapture(args['video'])
# initialize the first frame in the video stream
firstFrame = None
count,vid_no,y=0,0,0

while True:
	if not os.path.exists(str(vid_no)+'.avi'):
		video=cv2.VideoWriter(str(vid_no)+'.avi',fourcc,30.0,(w,h),True)

	# grab the current frame and initialize the occupied/unoccupied text
	(grabbed, frame) = cam.read()

	if not grabbed:
		break
	fgmask = fgbg.apply(frame)
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
#	frameDelta = cv2.absdiff(firstFrame, gray)
	consecDelta = cv2.absdiff(prevFrame,gray)
#	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	consecThresh = cv2.threshold(consecDelta, 25, 255, cv2.THRESH_BINARY)[1]

	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
#	pyautogui.confirm('Shall I confirm?')
#	thresh = cv2.dilate(thresh, None, iterations=2)
	consecThresh = cv2.dilate(consecThresh, None, iterations=2)
#	_, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	_, fuck, _ = cv2.findContours(consecThresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	detect_face = face(frame)

	for x in fuck:
		y=cv2.contourArea(x)
		if cv2.contourArea(x) < 3000 and not detect_face:
			text = "Unoccupied"
			continue
		else:
			text="Occupied"

	if text=="Occupied":
		if detect_face:
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
	prevFrame=gray
	cv2.imshow('frame',fgmask)
	if args['test']:
		cv2.putText(frame, "Room Status: {},{},{}".format(text,y,count), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		cv2.imshow("Security Feed", frame)
		cv2.imshow("Prev",prevFrame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("w"):
		break

# cleanup the cam and close any open windows
try:
	video.release()
except:
	pass
cam.release()
cv2.destroyAllWindows()
