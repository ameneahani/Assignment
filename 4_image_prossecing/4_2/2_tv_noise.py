import cv2
import numpy as np
import imageio

IMG = []
while True:
    img = np.random.random((250, 350))* 255
    img = np.array(img, dtype=np.uint8)
    IMG.append(img)
    cv2.imshow("", img)
    if cv2.waitKey(100) & 0XFF == ord('q'):
        break

imageio.mimsave("output.gif", IMG)