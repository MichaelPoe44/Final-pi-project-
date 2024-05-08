import cv2
import os
from Server_sender import *
import requests
from time import time

face_not_found=True
# Load the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Path to the directory containing target face images
target_faces_dir = 'target_faces'

# Load all target face images from the directory
target_faces = []
for filename in os.listdir(target_faces_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        target_face_path = os.path.join(target_faces_dir, filename)
        target_face = cv2.imread(target_face_path, cv2.IMREAD_GRAYSCALE)
        target_faces.append(target_face)

# Initialize the video capture object to access the webcam (0 for default camera)
cap = cv2.VideoCapture(0)

#def face_detected():
    #global face_not_found
    #face_not_found = False
    #Condition_met()
    #sleep(3)
    
# Continuously capture frames from the webcam
while face_not_found:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply histogram equalization for contrast enhancement
    gray_frame_equalized = cv2.equalizeHist(gray_frame)

    # Apply Gaussian blur for noise reduction
    gray_frame_blur = cv2.GaussianBlur(gray_frame_equalized, (5, 5), 0)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame_blur, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if any faces are detected
    if len(faces) == 0:
        print("No faces detected")
    else:
        print(f"{len(faces)} face(s) detected")

        # Loop through the detected faces
        for (x, y, w, h) in faces:
            # Extract the region of interest (ROI) containing the face
            face_roi = gray_frame_equalized[y:y+h, x:x+w]

            # Resize the ROI to match each target face size
            for target_face in target_faces:
                face_roi_resized = cv2.resize(face_roi, (target_face.shape[1], target_face.shape[0]))

                # Comparing the faces after resize
                match_result = cv2.matchTemplate(face_roi_resized, target_face, cv2.TM_CCOEFF_NORMED)

                # Print match score
                print("Match score:", match_result)

                # Adjusting the threshold for template matching
                threshold = 0.3  # Set your desired threshold

                # If face matches target face, simulate unlock
                if match_result >= threshold:
                    print("Detected the target face - Unlocking the lock")
                    #face_detected()
                    face_not_found = False
                    Condition_met()
                    time_now = time()
                    print(time_now)
                    break
                    # Simulating not unlocking box
                else:
                    print("Detected a face but not the target face")

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display frame with rectangles around detected faces
    cv2.imshow('Face Recognition', frame)
    
    # Kill the program if 'q' is pressed or window is closed
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Face Recognition', cv2.WND_PROP_VISIBLE) < 1:
        break
cap.release()
cv2.destroyAllWindows()

time_after = time()
while 10 > (time_after-time_now):
    time_after = time()
if 10 < (time_after-time_now) and not face_not_found:
    Condition_met()



print("yes")
# Release the video capture object and close all OpenCV windows

