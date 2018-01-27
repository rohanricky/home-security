import cv2

img1 = cv2.imread('donga.jpg')
img2 = cv2.imread('donga1.jpg')
print(img1.shape)
print(img2.shape)
height , width , layers =  img1.shape
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video = cv2.VideoWriter('video.avi',fourcc,20.0,(height*2,width*2),True)

video.write(img1)
video.write(img2)

cv2.destroyAllWindows()
video.release()
