import cv2
from multiprocessing import Process
from send_email import email
from face import face

def process(frame,count=0):
    cv2.imwrite('donga.jpg',frame)
    if face('donga.jpg') == 1:
        print("Good")
    else:
        email('donga.jpg')
