from multiprocessing import Process, Queue
from PIL import Image
import cv2
import numpy as np

def image_display(taskqueue):
#   cv2.namedWindow ('image_display', cv2.CV_WINDOW_AUTOSIZE)
   while True:

      image = taskqueue.get()              # Added
      if image is None:  break             # Added
      cv2.imshow ('image_display', image)  # Added
      cv2.waitKey(10)                      # Added
      continue                             # Added

      if taskqueue.get()==None:
         continue
      else:
         image = taskqueue.get()
         im = Image.fromstring(image['mode'], image['size'], image['pixels'])
         num_im = np.asarray(im)
         cv2.imshow ('image_display', num_im)


if __name__ == '__main__':
   taskqueue = Queue()
   vidFile = cv2.VideoCapture(0)
   p = Process(target=image_display, args=(taskqueue,))
   p.start()
   while True:
      flag, image=vidFile.read()

      taskqueue.put(image)  # Added
      import time           # Added
      time.sleep(0.010)     # Added
      continue              # Added

      if flag == 0:
         break
      im = Image.fromarray(image)
      im_dict = {
      'pixels': im.tostring(),
      'size': im.size,
      'mode': im.mode,
      }
      taskqueue.put(im_dict)

taskqueue.put(None)
p.join()
cv.DestroyAllWindows()
