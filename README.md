# Face Detection App

**What is this?**

- Test repo for python app for face detection
- Libraries used: 
	- [DeepFace](https://github.com/serengil/deepface) by Sefik Ilkin Serengil
	- [MTCNN](https://pypi.org/project/mtcnn/)
	- [OpenCV-Python](https://pypi.org/project/opencv-python/)
	- [TensorFlow](https://pypi.org/project/tensorflow/)

**Note: create a virtual environment first, then install requirements:**
- `python -m venv ./venv`
- `pip install -r requirements.txt`

### DeepFace
To run, use `app-df.py`.
- Uses **VGG-Face** face detection model as default model.
	- installs them on code run at `C:\Users\<userfolder>\.deepface\weights`
	- database (db) folder is used for [One-Shot Learning](https://serokell.io/blog/nn-and-one-shot-learning). multiple faces/expressions can be used as a baseline to compare to our model used.
		- it compares input img from video camera to our base pics in the db, with the help of our model

### DeepFace
To run, use `app-cv.py`.
- Simple face detection using [Haar Cascade Classifier](https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d).
- Outputs face recognition bounding box, along with x, y coordinates of bounding box.
