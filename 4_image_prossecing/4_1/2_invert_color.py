import cv2

img_1 = cv2.imread("img1.jpg")
img_2 = cv2.imread("img2.jpg")

def invert_color(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i:i+1, j:j+1] = 255 - img[i:i+1, j:j+1]

invert_color(img_1)
invert_color(img_2)

cv2.imshow("", img_1)
cv2.waitKey()
cv2.imshow("", img_2)
cv2.waitKey()


