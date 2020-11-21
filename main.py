import cv2
import numpy as np
import pyautogui

cam = cv2.VideoCapture(0)
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
prev_y = 0
forward_y = 0

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low_blue, high_blue)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:   
        area = cv2.contourArea(c)
        if area > 300:
            # img = cv2.drawContours(frame, contours, -1, (0,255,0), 3)    for normal view of boundary
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,   y), (x+w, y+h), (0, 255, 0), 2)
            if y < forward_y:
                pyautogui.press('space')
                print("left")      
            forward_y = y       

        else:
            # img = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y > prev_y:
                pyautogui.press('up')                      
                print("hey")
            prev_y = y
                

        

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
