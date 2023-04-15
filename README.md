# Face Detection App (real-time)

**What is this?**

- Test repo for python app for face detection
- Libraries used: 
	- [DeepFace](https://github.com/serengil/deepface) by Sefik Ilkin Serengil
	- [MTCNN](https://pypi.org/project/mtcnn/)
	- [OpenCV-Python](https://pypi.org/project/opencv-python/)
	- [TensorFlow](https://pypi.org/project/tensorflow/)
	- [MediaPipe](https://github.com/google/mediapipe)

**Note: create a virtual environment first, then install requirements:**
- `python -m venv ./venv`
- `pip install -r requirements.txt`

### DeepFace
To run, use `app-df.py`.
- Uses **VGG-Face** face detection model as default model.
	- Installs them on code run at `C:\Users\<userfolder>\.deepface\weights`
	- Database (db) folder is used for [One-Shot Learning](https://serokell.io/blog/nn-and-one-shot-learning). multiple faces/expressions can be used as a baseline to compare to our model used.
		- It compares input img from video camera to our base pics in the db, with the help of our model

<<<<<<< HEAD
### OpenCV - Bounding Box
=======
### OpenCV-Python
>>>>>>> 8df22256e59437f7f775983aa949adf55d5a8402
To run, use `app-cv.py`.
- Simple face detection using [Haar Cascade Classifier](https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d).
- Outputs face recognition bounding box, along with x, y coordinates of bounding box.


### OpenCV - Face Landmarks
To run, use `app-cv-2.py`.
- Simple face detection same as `app-cv`, but with facial landmarks.
- Outputs face recognition bounding box, and points for facial landmarks.

### MediaPipe
To run, use `app-mp-land.py`.
- Simple face detection with face mesh.
- Outputs face recognition face mesh.