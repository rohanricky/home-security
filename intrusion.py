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
args = vars(ap.parse_args())

#Video of thief
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
(h, w) = face_recognition.load_image_file('donga.jpg').shape[:2]
# Webcam
cam = cv2.VideoCapture(0)
# initialize the first frame in the video stream
firstFrame = None
count,vid_no=0,0
y=0
while True:
	if not os.path.exists(str(vid_no)+'.avi'):
		video=cv2.VideoWriter(str(vid_no)+'.avi',fourcc,30.0,(w,h),True)
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
	frameDelta = cv2.absdiff(firstFrame, gray)
	consecDelta = cv2.absdiff(prevFrame,gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	consecThresh = cv2.threshold(consecDelta, 25, 255, cv2.THRESH_BINARY)[1]

	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
#	pyautogui.confirm('Shall I confirm?')
	thresh = cv2.dilate(thresh, None, iterations=2)
	consecThresh = cv2.dilate(consecThresh, None, iterations=2)
	_, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	_, fuck, _ = cv2.findContours(consecThresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	# loop over the contours
	detect_face = face(frame)

	for x in fuck:
		y=cv2.contourArea(x)
		if cv2.contourArea(x) < 3000 and not detect_face:
			text = "Unoccupied"
			continue
		else:
			text="Occupied"

	if text=="Occupied1":
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


	cv2.putText(frame, "Room Status: {},{}".format(text,y), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Prev",prevFrame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
#	process(text,frame)
#	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# For testing purposes show these videos
#
#	cv2.imshow("Thresh", thresh)
#	cv2.imshow("Frame Delta", frameDelta)


# cleanup the cam and close any open windows
video.release()
cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()
'''
for c in cnts:
	# if the contour is too small, ignore it
	if cv2.contourArea(c) < 3000:  #cv2.contourArea(c) < args['min_area']
		continue

	text = "Occupied1"
'''
