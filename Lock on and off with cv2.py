# Import necessary libraries
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import ctypes
import pyttsx3
import time
import os

# Initialize video capture and hand detector
cap = cv.VideoCapture(0)  # Start webcam
detect = HandDetector(detectionCon=0.5, maxHands=1)  # Initialize hand detector
text = "The distance between the fingers is short, the screen is locked"  # Text when fingers are close
text_lock = "The system is locked"  # Text when system is locked
sound = pyttsx3.init()  # Initialize text-to-speech engine
sound.setProperty("rpr", 0)  # Set speech rate
text_number = 0  # Flag to track text announcement
number = 0  # Counter for actions
locke = False  # Lock state flag

try:
    # Start an infinite loop to continuously read frames from the camera
    while True:

        read, frame = cap.read()  # Capture frame from webcam
        frame = cv.flip(frame, 1)  # Flip the frame horizontally for mirror effect
        head, frames = detect.findHands(frame)  # Detect hands in the frame
        if head:
            head1 = head[0]  # Get the first detected hand
            lm_list = head1["lmList"]  # Get list of hand landmarks

            # Calculate distance between specific finger landmarks
            length, info, _ = detect.findDistance(lm_list[4][:-1], lm_list[20][:-1])
            length2, info2, _ = detect.findDistance(lm_list[4][:-1], lm_list[16][:-1])

            # Shutdown the system if distance between thumb and index finger is very small
            if length2 <= 30:
                sound.say("The system shuts down")
                sound.runAndWait()  # Announce shutdown
                time.sleep(2)  # Wait for 2 seconds
                os.system(r"C:\Windows\System32\shutdown.exe /s /t 1")  # Shutdown command
                break  # Exit the loop

            # Lock the system when thumb and little finger are close
            if 80 >= length >= 25:
                font = cv.FONT_HERSHEY_PLAIN  # Define font style
                cv.putText(frame, text, (10, 70), font, 1, (255, 0, 255), 1)  # Display text
                if text_number == 0:
                    time.sleep(0.5)  # Wait for 0.5 seconds before announcing
                    sound.say(text)  # Announce the text
                    sound.runAndWait()
                    text_number += 1  # Mark the text as announced
                else:
                    sound.say("")  # Clear the previous text if already announced

            # Lock the system if thumb and index finger are very close
            elif length <= 24 and not locke:
                font = cv.FONT_ITALIC  # Set different font for lock message
                cv.putText(frame, text_lock, (30, 70), font, 2, (180, 199, 210), 2)  # Display lock text
                time.sleep(3)  # Wait for 3 seconds before locking
                sound.say(text_lock)  # Announce system lock
                sound.runAndWait()
                ctypes.windll.user32.LockWorkStation()  # Lock the workstation
                locke = True  # Update lock state
                time.sleep(1)  # Wait for 1 second before proceeding

            # Open password entry page when hand distance is large enough
            elif length >= 150 and locke:
                sound.say(
                    "Hello, I have a Lenovo laptop. If you want to enter the system, please pay attention to the description.")
                sound.runAndWait()
                time.sleep(2)
                sound.say(
                    "Due to security issues, the password entry page will open and enter your password manually. Thank you.")
                sound.runAndWait()
                time.sleep(1)

                # Simulate pressing the Enter key to open the password page
                ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
                ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
                number += 1
                ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
                ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
                number += 1
                time.sleep(5)  # Wait for 5 seconds before continuing
                break  # Exit the loop

        # Display the frame in the OpenCV window
        cv.imshow("video: ", frame)

        # Exit the loop if the 'Esc' key is pressed
        key_exit = cv.waitKey(5) & 0xFF
        if key_exit == 27:
            break

    # Announce system login if two "Enter" presses were detected
    if number == 2:
        sound.say("Welcome to the system")
        sound.runAndWait()

    # Clean up and release resources
    cv.destroyAllWindows()
    cap.release()
except Exception as error:
    print(f"error: {error}")  # Print error message if an exception occurs