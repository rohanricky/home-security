import cv2
import numpy as np
import imutils
import os

images = [n for n in os.listdir('shit/hand/') if n[-4:]=='.jpg']
index=0
print(images)


def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    print(image)
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

while(1):
    print(images[index])
    x=cv2.imread('shit/hand/'+images[index],0)
#    cv2.imshow('hi',x)
    cv2.imwrite('shit/'+str(index)+'.jpg',rotate_bound(x,90))
    index+=1
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break         # wait for ESC key to exit

cv2.destroyAllWindows()
