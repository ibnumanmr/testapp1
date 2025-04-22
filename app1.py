import cv2  # Importing the OpenCV library for computer vision tasks
import streamlit as st  # Importing Streamlit for building interactive web applications
import numpy as np  # Importing NumPy for numerical computing
from PIL import Image  # Importing the Python Imaging Library for image processing


# Streamlit UI
st.title("Face Detection")
st.subheader("Either Open Camera And Detect Faces Or Upload An Image And Detect Faces ")

# Button to start face detection in live camera stream
if st.button("Open Camera"):
    # Open the default camera (0) for capturing video
    cap = cv2.VideoCapture(0)

   
    while True:
        # Capture frame-by-frame
        ret, img = cap.read()

        # Convert the captured frame to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame with face detection
        cv2.imshow('Face', img)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera capture
    cap.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()


