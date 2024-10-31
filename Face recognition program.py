import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
while True:
    red, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(frame_gray, 1.1, 5)
    eye = eye_cascade.detectMultiScale(frame_gray, 1.1, 5)
    for (x, y, w, h) in face:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 4)
    for (x, y, w, h) in eye:
        cv.rectangle(frame, (x, y), (x + w, y + h), (147, 112, 219), 2)
    cv.imshow("frame", frame)
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break

cv.destroyAllWindows()
cap.release()
