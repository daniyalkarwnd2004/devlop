import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
while True:
    red, frame = cap.read()
    head, frames = detector.findHands(frame)
    if head:
        head1 = head[0]
        im_list = head1["lmList"]
        length, info, _ = detector.findDistance(im_list[4][:-1], im_list[8][:-1], frame)
        print("length:", str(length))
    cv.imshow("frame", frame)
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break

cv.destroyAllWindows()
cap.release()
