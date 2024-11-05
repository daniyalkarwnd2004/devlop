import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
# This program calculates the distance between index fingers and returns its value in centimeters
cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)
while True:
    r, frame = cap.read()
    hand, frames = detector.findHands(frame)
    if hand:
        hane1 = hand[0]
        hane2 = hand[-1]
        im_list1 = hane1["lmList"]
        im_list2 = hane2["lmList"]
        length, info, _ = detector.findDistance(im_list1[8][:-1], im_list2[8][:-1], frame)
        if 0.0 <= length <= 30.0:
            fonts = cv.FONT_HERSHEY_PLAIN
            cv.putText(frame, f"There is no distance length: {round(length / 10, 5)}", (10, 50), fonts, 1, (100, 150, 20), 1)
        elif 31.0 <= length <= 250:
            fonts = cv.FONT_HERSHEY_PLAIN
            cv.putText(frame, f"There distance is short length: {round(length / 10, 5)}", (10, 50), fonts, 1, (100, 150, 20), 1)
        elif length >= 251:
            fonts = cv.FONT_HERSHEY_PLAIN
            cv.putText(frame, f"There distance increased length: {round(length / 10, 5)}", (10, 50), fonts, 1, (100, 150, 20), 1)
    cv.imshow("frame: ", frames)
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break
cv.destroyAllWindows()
cap.release()
