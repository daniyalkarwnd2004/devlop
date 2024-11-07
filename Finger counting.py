import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
# This program is for counting the fingers of 1 hand
# Note that in some cases this program does not count the thumb
# Note: This program has its own algorithm
"""
    Be sure to read the above tips before using
"""
cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
while True:
    read, frame = cap.read()
    hand, frames = detector.findHands(frame)
    if hand:
        hand1 = hand[0]
        im_list = hand1["lmList"]
        font = cv.FONT_HERSHEY_TRIPLEX
        if (im_list[4][1] < im_list[3][1] and im_list[8][1] < im_list[6][1]
            and im_list[12][1] < im_list[16][1] < im_list[14][1] and im_list[20][1] < im_list[18][1]):
            cv.putText(frame, "5", (30, 70), font, 3, (116, 255, 255), 3)
        elif (im_list[8][1] < im_list[6][1] and im_list[12][1] < im_list[16][1] < im_list[14][1] and im_list[20][1] < im_list[18][1])\
            or (im_list[4][1] < im_list[3][1] and im_list[8][1] < im_list[6][1] and im_list[12][1] < im_list[16][1] < im_list[14][1])\
            or (im_list[4][1] < im_list[3][1] and im_list[12][1] < im_list[10][1] and im_list[16][1] < im_list[14][1] and im_list[20][1] < im_list[18][1])\
            or (im_list[4][1] < im_list[3][1] and im_list[8][1] < im_list[6][1] and im_list[16][1] < im_list[14][1] and im_list[20][1] < im_list[18][1])\
            or (im_list[4][1] < im_list[3][1] and im_list[8][1] < im_list[6][1] and im_list[12][1] < im_list[10][1] and im_list[20][1] < im_list[18][1])\
            or (im_list[4][1] < im_list[3][1] and im_list[8][1] < im_list[6][1] and im_list[12][1] < im_list[10][1] and im_list[16][1] < im_list[14][1]):
            cv.putText(frame, "4", (30, 70), font, 3, (116, 200, 200), 3)
        elif (im_list[8][1] < im_list[6][1] and im_list[12][1] < im_list[10][1] and im_list[16][1] < im_list[14][1]) or\
           (im_list[12][1] < im_list[10][1] and im_list[16][1] < im_list[14][1] and im_list[20][1] < im_list[18][1]) or\
           (im_list[16][1] < im_list[14][1] and im_list[20][1] < im_list[18][1] and im_list[8][1] < im_list[6][1]) or \
           (im_list[8][1] < im_list[6][1] and im_list[12][1] < im_list[10][1] and im_list[20][1] < im_list[18][1]):
            cv.putText(frame, "3", (30, 70), font, 3, (116, 200, 200), 3)
        elif (im_list[8][1] < im_list[6][1] and im_list[12][1] < im_list[10][1]) or (im_list[12][1] < im_list[10][1] and
            im_list[16][1] < im_list[14][1]) or (im_list[16][1] < im_list[14][1] and im_list[20][1] < im_list[18][1])\
            or (im_list[12][1] < im_list[10][1] and im_list[20][1] < im_list[18][1]) or (im_list[8][1] < im_list[6][1]
            and im_list[20][1] < im_list[18][1]) or (im_list[8][1] < im_list[6][1] and im_list[16][1] < im_list[14][1]):
            cv.putText(frame, "2", (30, 70), font, 3, (116, 200, 200), 3)
        elif im_list[8][1] < im_list[6][1] or im_list[12][1] < im_list[10][1] or im_list[16][1] < im_list[14][1] \
                or im_list[20][1] < im_list[18][1]:
            cv.putText(frame, "1", (30, 70), font, 3, (116, 200, 200), 3)
    cv.imshow("frame", frame)
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break
cv.destroyAllWindows()
cap.release()

