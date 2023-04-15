import cv2

# Load the face detector and landmark detector models
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel("lbfmodel.yaml")

# Start the video capture device
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using the face detector
    faces = face_detector.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    if len(faces):
        # Detect facial landmarks using the landmark detector
        _, landmarks = landmark_detector.fit(gray, faces)

        # Loop over the detected faces and landmarks and draw them on the image
        for face, landmark in zip(faces, landmarks):
            for x, y in landmark[0]:
                cv2.circle(frame, (int(x), int(y)), 2, (255, 0, 255), -1)
            cv2.rectangle(
                frame,
                (face[0], face[1]),
                (face[0] + face[2], face[1] + face[3]),
                (0, 255, 0),
                2,
            )

    # Display the image with facial landmarks
    cv2.imshow("Facial Landmarks", frame)

    # Exit the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
