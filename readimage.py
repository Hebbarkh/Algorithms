import numpy as np
import cv2

img = cv2.imread('ubuntu.jpg',0)
#0 for gray scale image
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
