import cv2 as cv
import pyttsx3
import time

faces = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(0)
text = False
while True:
    read, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    mask = faces.detectMultiScale(frame_gray, 1.3, 5)
    if read:
        for (x, y, w, h) in mask:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 1)
            text = True
            font = cv.FONT_HERSHEY_PLAIN
            cv.putText(frame, "face detected", (30, 70), font, 1, (255, 0, 255), 1)
        cv.imshow("face", frame)
        key_exit = cv.waitKey(5) & 0xFF
        if key_exit == 27:
            print(read)
            break
    time.sleep(3)
    read = False
    if not read:
        cap.release()
        print(read)
        break
if text:
    sound = pyttsx3.init()
    sound.setProperty("rr", 115)
    sound.say("face detected")
    sound.runAndWait()
else:
    sound = pyttsx3.init()
    sound.setProperty("rr", 115)
    sound.say("the face was not recognized")
    sound.runAndWait()
cap.release()
cv.destroyAllWindows()
