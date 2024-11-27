import cv2 as cv
import requests
import pyttsx3
import time
import datetime

from cvzone.HandTrackingModule import HandDetector

# Initialize video capture from the camera
cap = cv.VideoCapture(0)

# Create a hand detector object with a detection confidence of 0.5 and max number of hands set to 1
detector = HandDetector(detectionCon=0.5, maxHands=1)

# Wait for 1 second before starting
time.sleep(1)

# Initialize text-to-speech engine to provide voice feedback
sound = pyttsx3.init()

# Provide a welcome message using text-to-speech
sound.say("Hello, my friend, welcome to the online exchange. You can know the current price of dollars and gold"
          " using the distance between your fingers. Do you think this is not great? Now you can try it safely "
          "Thanks for your patience")
sound.runAndWait()

# Start the main loop to continuously capture frames and process them
while True:
    try:
        # Capture a frame from the camera
        _, frame = cap.read()

        # Use the hand detector to find hands in the frame
        hand, frames = detector.findHands(frame)

        if hand:
            # If a hand is detected, extract the first hand's landmark list
            hand1 = hand[0]
            lm_list1 = hand1["lmList"]

            # Calculate the distance between the thumb (index 4) and the index finger (index 8)
            length1, _, _ = detector.findDistance(lm_list1[4][:-1], lm_list1[8][:-1])

            # Calculate the distance between the thumb (index 4) and the middle finger (index 12)
            length2, _, _ = detector.findDistance(lm_list1[4][:-1], lm_list1[12][:-1])

            # If the distance between the thumb and index finger is less than 30, get the dollar price
            if length1 < 30:
                url = "https://api.exchangerate-api.com/v4/latest/USD"
                response = requests.get(url)
                if response.status_code == 200:
                    # If the request is successful, extract the data and print the dollar price
                    data = response.json()
                    price_dollar = data['rates']['IRR']
                    # Save the dollar price to a text file with a timestamp
                    with open("dollar.txt", "a", encoding="utf-8") as file:
                        file.write(f"price dollar: {price_dollar}\t{datetime.datetime.now()} \n")
                    print(f"dollar: {price_dollar}")
                else:
                    # If there's an error with the request, print an error message
                    print("ERROR")
                    raise "ERROR WARNING"

            # If the distance between the thumb and middle finger is less than 30, get the gold price
            elif length2 < 30:
                api_key = "TOKEN"  # Replace "TOKEN" with your actual API key
                url = f"https://www.goldapi.io/api/XAU/USD"
                headers = {
                    "x-api-key": api_key
                }
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    # If the request is successful, extract the gold price and print it
                    data = response.json()
                    price_gold = data['price']
                    # Save the gold price to a text file with a timestamp
                    with open("gold.txt", "a", encoding="utf-8") as file:
                        file.write(f"price gold: {price_gold}\t{datetime.datetime.now()} \n")
                    print(f"price gold: {price_gold}")
                else:
                    # If there's an error with the request, print an error message
                    print("ERROR")
                    raise "ERROR WARNING"

        # Display the camera feed in a window
        cv.imshow("frame: ", frame)

        # Wait for the 'Esc' key to exit the program
        key_exit = cv.waitKey(5) & 0xFF
        if key_exit == 27:
            break

    except Exception as error:
        # If an error occurs, print the error message
        print(error)
# Release the video capture object and close all OpenCV windows
cv.destroyAllWindows()
cap.release()