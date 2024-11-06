import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc

brightness = sbc.get_brightness()[0]
cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)
factor = 5
while True:
    r, frame = cap.read()
    head, frames = detector.findHands(frame)
    if head:
        head1 = head[0]
        im_list = head1["lmList"]
        length, info, _ = detector.findDistance(im_list[4][:-1], im_list[8][:-1], frame)
        if 20 <= length <= 100:
            brightness = min(100, brightness + 10)
            sbc.set_brightness(brightness)
        elif 101 <= length <= 200:
            brightness = max(0, brightness - 10)
            sbc.set_brightness(brightness)
        elif 201 <= length <= 300:
            brightness = max(0, brightness - 10)
            sbc.set_brightness(brightness)
    cv.imshow("frame", frame)
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break
cv.destroyAllWindows()
cap.release()

