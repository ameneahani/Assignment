import numpy as np
import cv2

height ,width = 255, 255
img = np.ones((height, width, 3), dtype= np.uint8)

for i in range(0, 255):
    img[i] = img[i] * (254-i)

cv2.imshow("", img)
cv2.waitKey()
