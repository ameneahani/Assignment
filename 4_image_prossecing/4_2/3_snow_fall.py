import time
import imageio
import cv2
import random
import threading

lock = threading.Lock()
IMG = []
snowflakes = []
radius_snow = 1
running = True
def falling_snow(img_row, snow_row, snow_col):
    global running
    while snow_row < img_row-4 and running==True:
        snow_row += 3
        with lock:
            snowflakes.append((snow_row, snow_col))
        time.sleep(0.08)
        with lock:
            if snowflakes:
                snowflakes.pop(0)
        
    
def display_snow(img):
    global running, IMG
    global snowflakes, radius_snow

    while running:
        frame[:] = img.copy()
        for r,c in snowflakes:
            cv2.circle(frame, (c,r), radius_snow, 215, -1)
        
        cv2.imshow("", frame)
        IMG.append(frame.copy())
        if cv2.waitKey(1) & 0XFF == ord('q'):
            running = False
            break
        time.sleep(0.01)

img = cv2.imread("winter2.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
frame = img.copy()
row, col = img.shape

threading.Thread(target=display_snow, args=(img,)).start()

while running:
    for _ in range(10):
        snow_row = random.randint(0, 20)
        snow_col = random.randint(0, col-4)
        
        t1 = threading.Thread(target=falling_snow, args=[row, snow_row,snow_col])
        t1.start()
    if cv2.waitKey(25) & 0XFF == ord('q'):
        running = False
        break
    time.sleep(0.03)
imageio.mimsave("winter.gif", IMG)
        