import cv2 as cv


cap = cv.VideoCapture(0)
sample = cv.CascadeClassifier("haarcascade_smile.xml")
while True:
    red, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    smiles = sample.detectMultiScale(frame_gray, 1.8, 20)
    for (x, y, w, h) in smiles:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 3)
    cv.imshow("frame", frame)
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break

cv.destroyAllWindows()
cap.release()
