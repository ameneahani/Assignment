import time
import cv2
import numpy as np
import random
import threading

lock = threading.Lock()

# مختصات زنده‌ی هر برف
snowflakes = []

def falling_snow(img_row, img_col, snow_row, snow_col):
    global snowflakes
    radius = 2
    while snow_row < img_row - radius:
        snow_row += random.randint(2, 5)
        snow_col += random.randint(-1, 1)  # کمی حرکت افقی مثل باد
        snow_col = max(0, min(img_col - 1, snow_col))

        # به‌روزرسانی موقعیت دونه برف
        with lock:
            snowflakes.append((snow_row, snow_col, radius))
        time.sleep(0.03)
        # حذف برف قبلی (یعنی پاک‌کردن رد)
        with lock:
            if snowflakes:
                snowflakes.pop(0)

def display_snow(img):
    global snowflakes
    frame = img.copy()
    while True:
        with lock:
            frame[:] = img.copy()
            for (r, c, radius) in snowflakes:
                cv2.circle(frame, (c, r), radius, 255, -1)
        cv2.imshow("", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.02)


# --- بارگذاری تصویر ---
img = cv2.imread("winter1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
row, col = img.shape

# --- ترد نمایش ---
threading.Thread(target=display_snow, args=(img,), daemon=True).start()

# --- ایجاد برف‌ها ---
for _ in range(50):
    snow_row = random.randint(0, row // 3)
    snow_col = random.randint(0, col - 4)
    t = threading.Thread(target=falling_snow, args=(row, col, snow_row, snow_col), daemon=True)
    t.start()
    time.sleep(0.1)

cv2.waitKey(0)
# cv2.destroyAllWindows()
