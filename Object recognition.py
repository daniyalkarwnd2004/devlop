import cv2 as cv
import numpy as np

img1 = cv.imread("beard.jpg", 0)
img2 = cv.imread("beard2.jpg", 0)
w, h = img2.shape
result = cv.matchTemplate(img1, img2, cv.TM_CCOEFF_NORMED)
threshold = 0.4
location = np.where(result >= threshold)
for point in zip(*location[::-1]):
    cv.rectangle(img1, point, (point[0] + h, point[1] + w), (255, 255, 0), 1)
cv.imshow("result", img1)
cv.waitKey(0)
cv.destroyAllWindows()
