import cv2 as cv

# Open the video file
cap = cv.VideoCapture("video3.mp4")

# Loop through each frame in the video
while True:
    _, frame1 = cap.read()  # Read the first frame
    _, frame2 = cap.read()  # Read the second frame

    # Resize both frames to a fixed size for better performance
    resize1 = cv.resize(frame1, (780, 480))
    resize2 = cv.resize(frame2, (780, 480))

    # Calculate the absolute difference between the two frames
    frame_abs = cv.absdiff(resize1, resize2)

    # Convert the difference image to grayscale
    frame_gray = cv.cvtColor(frame_abs, cv.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    GaussianBlur = cv.GaussianBlur(frame_gray, (3, 3), 2)

    # Apply thresholding to get a binary image
    _, threshold = cv.threshold(GaussianBlur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Find contours (shapes/objects) in the thresholded image
    find_contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Loop through all found contours
    for contours in find_contours:
        # If the contour area is larger than 50, consider it as movement
        if cv.contourArea(contours) > 50:
            # Get the bounding box around the moving object
            (x, y, w, h) = cv.boundingRect(contours)
            # Draw a rectangle around the moving object
            cv.rectangle(resize1, (x, y), (x + w, y + h), (255, 50, 255), 2)

    # Show the blurred image (mask) to see the difference
    cv.imshow("mask: ", GaussianBlur)

    # Show the resized image with rectangles drawn around moving objects
    cv.imshow("resize: ", resize1)

    # Wait for the ESC key to exit the loop
    key_exit = cv.waitKey(5) & 0XFF
    if key_exit == 27:
        break

# Close all OpenCV windows and release the video capture object
cv.destroyAllWindows()
cap.release()