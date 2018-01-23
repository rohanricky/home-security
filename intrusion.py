
import argparse
import datetime
import imutils
import time
import cv2
from multiprocessing import Process,Queue
from send_email import email
from face import face
from process import process
import pyautogui

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# Webcam
cam = cv2.VideoCapture(0)

# initialize the first frame in the video stream
firstFrame = None
count=0
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	(grabbed, frame) = cam.read()
	text = "Unoccupied"

	# if the frame could not be grabbed, then we have reached the end
	# of the video
	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
#	pyautogui.confirm('Shall I confirm?')
	thresh = cv2.dilate(thresh, None, iterations=2)
	_, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue

		text = "Occupied"
	if text=="Occupied":
		p=Process(target=process,args=(frame,))
		p.start()
		p.join()
#	process(text,frame)

	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# For testing purposes show these videos
	Process(cv2.imshow("Security Feed", frame)).start()
#	cv2.imshow("Thresh", thresh)
#	cv2.imshow("Frame Delta", frameDelta)

	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

# cleanup the cam and close any open windows
cam.release()
cv2.destroyAllWindows()
