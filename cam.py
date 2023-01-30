import pathlib
import cv2
def start_webcam(model_gender, window_size, window_name='live', update_time=50):
cv2.namedWindow(window_name, WINDOW_NORMAL)
if window_size:
    width, height = window_size
    cv2.resizeWindow(window_name, width, height)

video_feed = cv2.VideoCapture(0)
video_feed.set(3, width)
video_feed.set(4, height)
read_value, webcam_image = video_feed.read()


delay = 0
init = True
while read_value:
    read_value, webcam_image = video_feed.read()
    webcam_image=cv2.flip(webcam_image,1,0)
    faces = face_cascade.detectMultiScale(webcam_image)
    for normalized_face, (x, y, w, h) in find_faces(webcam_image):
      if init or delay == 0:
        init = False
        gender_prediction = model_gender.predict(normalized_face)
      if (gender_prediction[0] == 0):
          cv2.rectangle(webcam_image, (x,y), (x+w, y+h), (0,0,255), 2)
          cv2.putText(webcam_image, 'female', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
      else:
          cv2.rectangle(webcam_image, (x,y), (x+w, y+h), (255,0,0), 2)
          cv2.putText(webcam_image, 'male', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)

    delay += 1
    delay %= 20

    cv2.putText(webcam_image, "Number of faces detected: " + str(len(faces)), (0,webcam_image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.7,  (255,255,255), 1)
    cv2.imshow(window_name, webcam_image)
    key = cv2.waitKey(update_time)
    if key == ESC:
        break

cv2.destroyWindow(window_name)
