import cv2
import numpy as np
height, width = 536, 536 
my_img = np.ones((height, width, 3), dtype= np.uint8)* 255

for i in range(0,8,2):
    for j in range(0,8,2):
        y = height //8
        x = width //8
        my_img[i*y:(i+1)*y, j*x:(j+1)*x ] = 0
        my_img[(i+1)*y:(i+2)*y, (j+1)*x:(j+2)*x ] = 0

cv2.imshow("", my_img)
cv2.waitKey()
print(my_img.shape)