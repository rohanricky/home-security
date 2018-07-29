import cv2

def Camera():
	cam = cv2.VideoCapture(0)
	grabbed, frame = cam.read()
	return frame

while(1):
	Camera()
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break