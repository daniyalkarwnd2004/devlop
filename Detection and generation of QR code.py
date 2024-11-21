import cv2 as cv
import qrcode as QR
import pyttsx3
import time
import os

# Initialize text-to-speech engine and ask the user for their choice
time.sleep(1)
sound = pyttsx3.init()
sound.say("Do you want to recognize QR code or make QR code?")
time.sleep(1)
sound.say("Number one is QR code detection and number two is QR code generation")
sound.runAndWait()

# Get user input to choose between QR code detection or generation
number = int(input("Enter your number: "))

if number == 1:
    try:
        # Start capturing video from the webcam
        cap = cv.VideoCapture(0)
        while True:
            # Read frames from the webcam
            _, frame = cap.read()

            # Initialize QRCodeDetector for detecting QR codes
            detector = cv.QRCodeDetector()
            value, box, _ = detector.detectAndDecode(frame)  # Decode the QR code

            if box is not None:
                # If a QR code is detected, draw a rectangle around it
                box = box[0]
                x_min = int(min(point[0] for point in box))
                y_min = int(min(point[1] for point in box))
                x_max = int(max(point[0] for point in box))
                y_max = int(max(point[1] for point in box))
                cv.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 1)
                print(value)  # Print the decoded value
            else:
                pass

            # Display the video with QR detection
            cv.imshow("QRcode: ", frame)

            # Exit the loop if the user presses the 'ESC' key
            key_exit = cv.waitKey(5) & 0xFF
            if key_exit == 27:
                break

        # Release resources and close all OpenCV windows
        cv.destroyAllWindows()
        cap.release()

    except Exception as Error:
        # Handle any errors during the QR code detection process
        print(Error)

elif number == 2:
    try:
        # Ask the user to enter the text for QR code generation
        sound.say("Please enter the text you want to be included in the QR code")
        sound.runAndWait()
        time.sleep(0.5)
        text = input("Enter the text: ")

        # Generate a QR code with the input text
        generation_QRcode = QR.make(text)

        # Ask the user for the save location and file name
        time.sleep(0.5)
        sound.say("Please enter an address to store the QR code and then specify the name and format")
        sound.runAndWait()
        address_saves = input("Enter the address: ")

        # Check if the directory is valid
        if not os.path.isdir(os.path.dirname(address_saves)):
            sound.say("Please enter a valid directory")
            sound.runAndWait()
        else:
            # Save the QR code to the specified location
            generation_QRcode.save(fr'{address_saves}')

    except Exception as Error:
        # Handle any errors during the QR code generation process
        print("ERROR", Error)

else:
    # Handle invalid input for the choice
    raise "Error :)"
