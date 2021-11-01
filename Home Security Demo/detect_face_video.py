
#neccesary imports
import cv2
import os


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (205, 0, 255), 5)
        print("Person seen in room, setting of alarm.")
        os.system("start alarm.mp3")

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    key_press = cv2.waitKey(30) & 0xff
    if key_press == 27:
        break
        
# Release the VideoCapture object
cap.release()