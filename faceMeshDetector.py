import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv.VideoCapture(0)
detector = FaceDetector()
mesh_face = FaceMeshDetector(maxFaces=1)
while True:
    read, frame = cap.read()
    frames, box = detector.findFaces(frame)
    mesh = mesh_face.findFaceMesh(frame)
    if box:
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(frame, "The face was detected", (30, 30), font, 1, (255, 0, 255), 1)
    cv.imshow("frame", frame)
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break
cv.destroyAllWindows()
cap.release()
