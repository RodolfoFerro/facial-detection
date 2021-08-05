import numpy as np
import imutils
import cv2

# Load Haar cascade files:
path_cascade = "./haarcascades/"
face_cascade = cv2.CascadeClassifier(
    path_cascade + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    path_cascade + 'haarcascade_mcs_eyepair_big.xml')

# Load video capture:
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame:
    ret, img = cap.read()
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create multiscale classifier:
    faces = face_cascade.detectMultiScale(gray, 1.8, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
