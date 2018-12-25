# OpenCV 7-day Challenge
Started to Learn OpenCV with Python
## Requirements:
1. OpenCv for Python
2. Imutils v0.5.2 - grab_contours() only works for v0.5.2... so make sure you have this version.
`pip install --upgrade imutils` can be used for the same.

## NOTE
I have made .ipnyb files so that one can see what is going on step by step. Change `image = cv2.imread("doc1.jpeg")` to  `image = cv2.imread(args["image"])` instead of image file name while exporting the ipnyb file to python file.


### For 001_Introduction.ipnyb
You will only need the file and image  - 'test.jpeg'.

### For 002_Counting_Objects.ipynb
Only 'tetris.png' is required.

### For 003_Mobile_Document_Scanner.ipynb
You will need a module called 'pyimagesearch' and 'doc1.jpeg'.
Unzip the 'pyimagesearch.zip' file and paste it in the same folder as your Python file.

### For 004_OMR_Scanner.ipynb
Only 'test_05.png' image is required for the same.

### For 005_Object_Tracking.py
A 'red_dot.png' file is given to test the tracker. The current tracker is made for detecting a red dot.. open the image in any other device or google for any red dot. The model shall work.

### For 006_Measuring_Size.py
You need to provide the width of leftmost object present in the image as reference. I used 'measure.jpeg' image to test the working. It has correctness upto 93-95%.

### For 007_Facial_Landmarks.py
You need to install dlib - Checkout here - https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
Also, you need a facial_landmarks_68 dataset. Download it from here : http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

I used it on an image child.jpg.. You can pass on any other image for testing.
