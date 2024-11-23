import cv2 as cv
import datetime

# Initialize the webcam capture
cap = cv.VideoCapture(0)

# Create a background subtractor to detect moving objects
create_background = cv.createBackgroundSubtractorMOG2(history=50, varThreshold=30, detectShadows=True)

while True:
    # Read a frame from the webcam
    _, frame = cap.read()

    # Apply the background subtractor to get the foreground mask
    mask = create_background.apply(frame)

    # Apply a median blur to the mask to reduce noise
    mask = cv.medianBlur(mask, 5)

    # Find contours of the moving objects in the mask
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Skip small contours (noise)
        if cv.contourArea(contour) < 800:
            continue

        # Get the bounding rectangle for each moving object
        x, y, w, h = cv.boundingRect(contour)

        # Print "moved" when a moving object is detected
        print("moved")

        # Write the coordinates and the timestamp of the detected movement to a file
        with open("x y w h.txt", "a", encoding="utf-8") as file:
            # Format the data as (x, y, x + w, y + h) and the current timestamp
            file.write(f"{x, y, x + w, y + h}\t{datetime.datetime.now()}\n")
            file.flush()

        # Draw a rectangle around the detected moving object
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 1)

    # Display the frame with the rectangle(s) around moving objects
    cv.imshow("frame", frame)

    # Check if the user pressed the "Esc" key to exit
    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:  # 27 is the ASCII code for the "Esc" key
        break

# Release resources and close any OpenCV windows
cv.destroyAllWindows()
cap.release()