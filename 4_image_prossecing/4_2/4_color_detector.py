import cv2
import numpy as np

cap = cv2.VideoCapture(0)
running = True
while running:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_row, frame_col = frame.shape
    gaussian = cv2.GaussianBlur(frame, (51,51), 0)
    y1, x1 = frame_row//2 - 50, frame_col//2 - 50
    y2, x2 = frame_row//2 +50, frame_col//2 + 50
    gaussian[y1:y2, x1:x2] = frame[y1:y2, x1:x2]
    cv2.rectangle(gaussian, (x1, y1), (x2, y2), 20,2)
    roi = gaussian[x1:x2, y1:y2]
    
    black_limit = 50
    white_limit = 140

    black_mask = (roi<=black_limit)
    gray_mask = (roi>black_limit) & (roi<white_limit)
    white_mask = (roi>=white_limit) & (roi<=255)
    black_pixel = np.sum(black_mask)
    gray_pixel = np.sum(gray_mask)
    white_pixel = np.sum(white_mask) 
    max_color = max(black_pixel, gray_pixel, white_pixel)
    if max_color == black_pixel:
        cv2.putText(gaussian, "Black", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 2)
    elif max_color == gray_pixel:
        cv2.putText(gaussian, "Gray", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 2)
    elif max_color == white_pixel:
        cv2.putText(gaussian, "White", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1,0 ,2)

    cv2.imshow("", gaussian)
    if cv2.waitKey(25) & 0XFF == ord('q') or running == False:
        break