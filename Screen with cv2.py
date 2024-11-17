import cv2 as cv
from cvzone.FaceMeshModule import FaceMeshDetector
import pyautogui
import time
import pyttsx3

# Initialize the video capture (webcam)
cap = cv.VideoCapture(0)

# Initialize the FaceMesh detector with a maximum of 1 face detection
detector = FaceMeshDetector(maxFaces=1)

# Wait for a few seconds to allow the webcam to initialize
time.sleep(3)

# Initialize text-to-speech engine
sound = pyttsx3.init()

# Text-to-speech instructions for the user
sound.say("Hello, welcome to the screen program through eyes")
sound.say("Please keep the distance so that the program works properly. Thank you for your cooperation")
sound.say("Please bring the webcam up to 38 cm")
sound.runAndWait()

while True:
    # Capture a frame from the webcam
    _, frame = cap.read()

    # Detect the face mesh (facial landmarks)
    frames, mesh = detector.findFaceMesh(frame)

    if mesh:
        # Extract facial landmarks from the first face detected
        face = mesh[0]

        # Get the coordinates of two specific landmarks on the face (159 and 145)
        x1, y1 = face[159]
        x2, y2 = face[145]

        # Calculate the distance between these two landmarks using the Euclidean distance formula
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        print(length)

        # If the distance between the two points is less than or equal to 13, take a screenshot
        if length <= 13:
            sound.say("The program took a screenshot")
            sound.runAndWait()
            time.sleep(1)

            # Take a screenshot and save it as "image.jpg"
            screenshot = pyautogui.screenshot()
            screenshot.save("image.jpg")
            screenshot.show()
            break  # Exit the loop after taking the screenshot

    # Display the webcam frame
    cv.imshow("frame", frame)

    # Check if the 'Esc' key (ASCII 27) is pressed to exit the loop
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break

# Close all OpenCV windows and release the webcam
cv.destroyAllWindows()
cap.release()