import cv2 as cv

image_bgr = cv.imread("rgb.jpg")
image_hsv = cv.cvtColor(image_bgr, cv.COLOR_BGR2HSV)
image_gray = cv.cvtColor(image_bgr, cv.COLOR_BGR2GRAY)
blue, green, red = cv.split(image_bgr)
cv.imshow("color image", image_bgr)
cv.imshow("color hsv", image_hsv)
cv.imshow("color gray", image_gray)
cv.imshow("color blue", blue)
cv.imshow("color green", green)
cv.imshow("color red", red)
cv.waitKey(0)
cv.destroyAllWindows()

