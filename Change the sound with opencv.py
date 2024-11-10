import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import time

# Initialize the audio interface to control system volume
devices = AudioUtilities.GetSpeakers()  # Get the speakers device
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate the volume control interface
volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast the interface to the correct volume control pointer

# Set minimum and maximum volume levels
min_vol = 0.0  # Minimum volume
max_vol = 1.0  # Maximum volume

# Get the current volume level (as a scalar value between 0.0 and 1.0)
current_volume = volume.GetMasterVolumeLevelScalar()

# Initialize the hand detector from cvzone
detector = HandDetector(detectionCon=0.5, maxHands=1)  # Confidence threshold of 0.5, max one hand detection
cap = cv.VideoCapture(0)  # Open the webcam for capturing video

# Define the threshold for hand distance to trigger volume change
change_threshold = 100  # Distance threshold for volume change
volume_step = 0.05  # Step by which the volume will change (increase or decrease)

# Record the last time the volume changed to control the frequency of updates
last_change_time = time.time()

# Main loop to process each frame from the webcam
while True:
    read, frame = cap.read()  # Read a frame from the webcam
    hands, img = detector.findHands(frame)  # Detect hands in the frame using the hand detector

    if hands:  # If hands are detected
        hand1 = hands[0]  # Get the first detected hand
        lm_list = hand1["lmList"]  # Get the list of landmark positions of the hand

        # Extract the x and y coordinates of the thumb (index 4) and the index finger (index 8)
        x1, y1 = lm_list[4][0:2]  # Thumb (landmark 4)
        x2, y2 = lm_list[8][0:2]  # Index finger (landmark 8)

        # Calculate the distance between the thumb and index finger
        length, info, _ = detector.findDistance((x1, y1), (x2, y2), frame)

        # If enough time has passed since the last volume change (to prevent rapid changes)
        if time.time() - last_change_time > 0.2:  # 0.2 seconds interval between changes
            if length > change_threshold:  # If the distance is greater than the threshold, increase the volume
                current_volume += volume_step  # Increase the volume by the defined step
                if current_volume > max_vol:  # Ensure the volume does not exceed the maximum limit
                    current_volume = max_vol
                volume.SetMasterVolumeLevelScalar(current_volume, None)  # Set the new volume level
                font = cv.FONT_ITALIC  # Set font style for displaying volume on the frame
                cv.putText(frame, f"{current_volume:.2f}", (30, 70), font, 1, (0, 130, 165), 2)  # Display volume on the screen
                last_change_time = time.time()  # Update the last change time

            elif length < change_threshold:  # If the distance is smaller than the threshold, decrease the volume
                current_volume -= volume_step  # Decrease the volume by the defined step
                if current_volume < min_vol:  # Ensure the volume does not go below the minimum limit
                    current_volume = min_vol
                volume.SetMasterVolumeLevelScalar(current_volume, None)  # Set the new volume level
                font = cv.FONT_ITALIC  # Set font style for displaying volume on the frame
                cv.putText(frame, f"{current_volume:.2f}", (30, 70), font, 1, (0, 130, 165), 2)  # Display volume on the screen
                last_change_time = time.time()  # Update the last change time

    # Display the updated frame with volume information
    cv.imshow("Volume Control", frame)

    # Check if the user pressed the 'ESC' key to exit
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:  # 27 is the ASCII code for the 'ESC' key
        break  # Exit the loop if 'ESC' is pressed
# Release the webcam and close the OpenCV windows
cv.destroyAllWindows()
cap.release()