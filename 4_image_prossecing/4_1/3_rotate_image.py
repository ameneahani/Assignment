import cv2

img_3 = cv2.imread("3.jpg")

def rotate(img):
    height = img.shape[0]
    for i in range(0, height//2, 1):
        for j in range(img.shape[1]):
            a = img[height-1-i, j].copy()
            img[height-1-i, j] = img[i, j]
            img[i, j] = a

rotate(img_3)
cv2.imshow("", img_3)
cv2.waitKey()

