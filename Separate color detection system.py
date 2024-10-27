import cv2 as cv
import numpy as np


def blue():
    cap = cv.VideoCapture(0)
    while True:
        rad, frame = cap.read()
        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([116, 255, 255])
        mask = cv.inRange(frame_hsv, lower_blue, upper_blue)
        cv.imshow("blue", mask)
        cv.imshow("frame", frame)
        key_exit = cv.waitKey(5) & 0xFF
        if key_exit == 27:
            break
    cv.destroyAllWindows()
    cap.release()


def red():
    cap = cv.VideoCapture(0)
    while True:
        rad, frame = cap.read()
        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_red = np.array([0, 110, 110])
        upper_red = np.array([6, 255, 255])
        mask = cv.inRange(frame_hsv, lower_red, upper_red)
        cv.imshow("blue", mask)
        cv.imshow("frame", frame)
        key_exit = cv.waitKey(5) & 0xFF
        if key_exit == 27:
            break
    cv.destroyAllWindows()
    cap.release()


def green():
    cap = cv.VideoCapture(0)
    while True:
        rad, frame = cap.read()
        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_green = np.array([35, 100, 100])
        upper_green = np.array([85, 255, 255])
        mask = cv.inRange(frame_hsv, lower_green, upper_green)
        cv.imshow("blue", mask)
        cv.imshow("frame", frame)
        key_exit = cv.waitKey(5) & 0xFF
        if key_exit == 27:
            break
    cv.destroyAllWindows()
    cap.release()

blue()
red()
green()