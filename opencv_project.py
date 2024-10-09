import cv2 as cv
import numpy as np
# Image processing program
# This program checks the packages and confirms them if they are square and undamaged


def open_cv():
    img = cv.imread("regtangle.jpg", 0)
    img2 = cv.cornerHarris(img, 3, 9, 0.04)
    corner = cv.dilate(img2, None)
    img[corner > 0.01 * corner.max()] = 255
    threshold = 0.01 * corner.max()
    corner_points = np.argwhere(corner > threshold)
    num_corners = len(corner_points)
    if num_corners == 136:
        print("yes closed is True")
    else:
        print("yes closed is False")
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

open_cv()