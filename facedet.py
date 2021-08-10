import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier(
    "./haarcascades/haarcascade_frontalface_default.xml"
)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        img = cv2.resize(frame, (640, 320))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.4, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(
                img,
                (x, y), (x + w, y + h),
                (255, 0, 0), 2
            )


    cv2.imshow('faces detected', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
