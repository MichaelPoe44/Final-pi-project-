import cv2
import os

# Function to capture and save multiple images of the face
def capture_images(name, num_images=5):
    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize the video capture object to access the webcam (0 indicates the default camera)
    cap = cv2.VideoCapture(0)

    # Create a directory to store the captured images if it doesn't exist
    if not os.path.exists('captured_images'):
        os.makedirs('captured_images')

    # Counter for the number of captured images
    count = 0

    # Continuously capture frames from the webcam
    while count < num_images:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Check if any faces are detected
        if len(faces) > 0:
            # Loop through the detected faces
            for (x, y, w, h) in faces:
                # Draw a rectangle around the detected face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the frame with rectangles around the detected faces
            cv2.imshow('Capture Images', frame)

            # Check for the 'c' key press to capture an image
            key = cv2.waitKey(0)
            if key == ord('c'):
                # Save the detected face as an image
                face_image = gray_frame[y:y+h, x:x+w]
                image_path = f'captured_images/{name}_{count}.jpg'
                cv2.imwrite(image_path, face_image)

                # Increment the image counter
                count += 1

                # Display a message indicating the number of images captured
                print(f'Captured image {count}/{num_images}')

            # Check for the 'q' key press to exit the loop
            elif key == ord('q'):
                break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Function for facial recognition
def recognize_face():
    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load captured images for recognition
    captured_images = []
    for file in os.listdir('captured_images'):
        if file.endswith('.jpg'):
            image_path = os.path.join('captured_images', file)
            captured_images.append((image_path, cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)))

    # Initialize the video capture object to access the webcam (0 indicates the default camera)
    cap = cv2.VideoCapture(0)

    # Continuously capture frames from the webcam
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Loop through the detected faces
        for (x, y, w, h) in faces:
            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Compare the detected face with captured images for recognition
            for image_path, captured_image in captured_images:
                match_result = cv2.matchTemplate(gray_frame[y:y+h, x:x+w], captured_image, cv2.TM_CCOEFF_NORMED)
                similarity_score = match_result[0][0]

                # If similarity score is above a threshold, recognize the person
                if similarity_score > 0.8:  # Adjust the threshold as needed
                    cv2.putText(frame, "Recognized: " + os.path.splitext(os.path.basename(image_path))[0], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    break

        # Display the frame with rectangles around the detected faces
        cv2.imshow('Face Recognition', frame)

        # Check for the 'q' key press to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Face Recognition', cv2.WND_PROP_VISIBLE) < 1:
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    mode = 'r'  # Start in recognition mode
    while True:
        if mode == 'r':
            recognize_face()
        elif mode == 'c':
            name = input("Enter the name to be stored as: ")
            capture_images(name, num_images=5)
            mode = 'r'  # Switch back to recognition mode

        # Check for the 'q' key press to exit the loop
        key = cv2.waitKey(0)
        if key == ord('q'):
            break
        elif key == ord('c'):
            mode = 'c'  # Switch to capture mode

if __name__ == "__main__":
    main()
