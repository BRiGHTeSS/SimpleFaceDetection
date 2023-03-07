"""
This is simple FACE DETECTION by using images
How it's works? -> So u just put a relative path into img variable
https://www.geeksforgeeks.org/face-detection-using-cascade-classifier-using-opencv-python
"""

# import Open-CV to access function to create face detection
import cv2

# Create variable that stored a photo (photo path)
photo = "mygang7.png" # change photo in this line

# Load the Cascade (import file)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # use algorithms haarcascade to create face detection
# Learning more about haarcascade -> https://www.geeksforgeeks.org/face-detection-using-cascade-classifier-using-opencv-python

# Read the photo varible (photo path)
img = cv2.imread(photo)

# Convert image into grey color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert color of photo to grey 
# Pictures with lots of colors It is a very detailed photo that makes detection more difficult and that why people use grey color

# Detected faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5) # (color (gray is better), scaleFactor, minNeighbors)
#scaleFactor = Parameter specifying how much the image size is reduced at each image scale
#minNeighbors = Parameter specifying how many neighbors each candidate rectangle should have to retain it

# Draw rectangle around the face ()
for (x, y, w, h) in faces: # w = weight, h = height
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 174, 0), 1) # draw a rectangle a photo | .rectangle(image, start_point, end_point, color, thickness)
# Read more about 5 arguments -> https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method

# Display the output (Show result)
cv2.imshow("img", img) # display an image to specified window (make another window)
cv2.waitKey() # press any key to exit the window
#.waitkey() = OpenCV allows users to display a window for given milliseconds or until any key is pressed