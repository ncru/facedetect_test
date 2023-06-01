import cv2
import numpy as np

# Open the camera and set the resolution
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get the depth information from the frame
    depth = np.abs(cv2.Laplacian(gray, cv2.CV_64F))

    # Normalize the depth values between 0 and 255
    depth = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the depth map to grayscale
    depth = np.uint8(depth)

    # Display the grayscale depth map
    cv2.imshow("Depth Map", depth)

    # Exit the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
