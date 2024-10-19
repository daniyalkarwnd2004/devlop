import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread("xray2.jpg", 0)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img1)
histogram = cv.calcHist([cl1], [0], None, [256], [0, 256])
plt.subplot(121), plt.imshow(cl1, "gray")
plt.subplot(122), plt.plot(histogram)
plt.show()
