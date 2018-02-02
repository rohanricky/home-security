import numpy as np
import cv2
import os

# this two lines are for loading the videos.
# in this case the video are named as: cut1.mp4, cut2.mp4, ..., cut15.mp4
videofiles = [n for n in os.listdir('shit/') if n[-4:]=='.avi']
videofiles=sorted(videofiles, key=lambda item: int(item.partition('.')[0]))
#videofiles = sorted(videofiles, key=lambda item: int( item.partition('.')[0]))
print(videofiles)
video_index = 0
cap = cv2.VideoCapture(videofiles[0])
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# video resolution: 1624x1234 px
out = cv2.VideoWriter("video.avi",fourcc,30, (500,375),True)

def concat():
    global video_index,fourcc,out,videofiles
    cap = cv2.VideoCapture(videofiles[0])
    while(1):
        ret, frame = cap.read()
        if frame is None:
            print("end of video " + str(video_index) + " .. next one now")
            video_index += 1
            if video_index >= len(videofiles):
                break
            cap = cv2.VideoCapture(videofiles[ video_index ])
            ret, frame = cap.read()
        cv2.imshow('frame',frame)
        out.write(frame)
        if cv2.waitKey(700) & 0xFF == ord('q'):
            break

out.release()
cv2.destroyAllWindows()

if __name__=='__main__':
    concat()
