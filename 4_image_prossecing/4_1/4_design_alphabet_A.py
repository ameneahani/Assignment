import numpy as np
import cv2

height, width = 400, 300
img = np.ones((height, width, 3),dtype= np.uint8) *255

block_h , block_w = 20, 20
block = np.zeros((block_h, block_w, 3), dtype= np.uint8)

A_pattern = [[0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1]]

x_start = 100
y_start = 135

for i in range(len(A_pattern)):
    for j in range(len(A_pattern[0])):
        if A_pattern[i][j] == 1:
            y = i*block_h + y_start
            x = j*block_w + x_start
            img[y:y+block_h, x:x+block_w] = block

cv2.imshow("", img)
cv2.waitKey()

