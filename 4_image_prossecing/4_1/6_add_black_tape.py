import cv2
import numpy as np

my_img = cv2.imread("old_woman.jpg")

def put_deth_symbol(img):
    img_height, img_width = img.shape[0], img.shape[1]
    stripe_width = 1
    block = np.zeros((stripe_width, stripe_width, 3), dtype= np.uint8)

    x_start = img_width//8
    for i in range((img_width//(8*stripe_width))):
        for j in range(20):
            x = x_start - i* stripe_width 
            y =  i* stripe_width + j* stripe_width
            
            img[y:y+ stripe_width, x:x+ stripe_width] = block
            img[x:x+ stripe_width, y:y+ stripe_width] = block

put_deth_symbol(my_img)
cv2.imshow("", my_img)
cv2.waitKey()

