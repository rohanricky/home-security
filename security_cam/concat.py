'''
combines all the video files into a single file
'''

import cv2
import os
import sys

sys.path.append('/home/rohan/github/home')
videofiles = [n for n in os.listdir('/home/rohan/github/home/videos/') if n[-4:]=='.avi']
print(videofiles)
videofiles=sorted(videofiles, key=lambda item: item.partition('.')[0])

print(videofiles)
video_index = 0
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

out = cv2.VideoWriter("video.avi",fourcc,30, (500,375),True)

def concat():
    global video_index,fourcc,out,videofiles
    for singleVideo in videofiles:
        cap = cv2.VideoCapture(singleVideo)
        width, height = cap.get(3), cap.get(4)
        print(width, height)
        ret, frame = cap.read()
        if frame is None:
            print("end of video " + str(video_index) + " .. next one now")
        out.write(frame)

    # cap = cv2.VideoCapture(videofiles[0])
    # while(1):
    #     ret, frame = cap.read()
    #     if frame is None:
    #         print("end of video " + str(video_index) + " .. next one now")
    #         video_index += 1
    #         if video_index >= len(videofiles):
    #             break
    #         cap = cv2.VideoCapture(videofiles[ video_index ])
    #         ret, frame = cap.read()
    #     out.write(frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

#out.release()
cv2.destroyAllWindows()

if __name__=='__main__':
    concat()
