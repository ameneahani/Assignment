import cv2

img = cv2.imread("batman.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
col, row = img.shape
print(row, col)
_, img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY_INV)
cv2.putText(img, "BATMAN", (350, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.5, 255, 3)
cv2.imshow("", img)
cv2.waitKey()


