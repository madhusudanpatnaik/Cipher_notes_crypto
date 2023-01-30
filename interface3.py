from asyncio import sleep
import cv2
import threading
import subprocess as sp
def camera():
    # Get a reference to webcam
    cap = cv2.VideoCapture(0)
    
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    while True:
    
        ret, frame = cap.read(0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
    
        count = 0
    
        # Draw a rectangle around the facesqq
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            count += 1
    
        # Display count
        cv2.putText(frame, str(count), (70, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
        cv2.imshow('Video Face Detection', frame)
    
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # When everything is done, release the capture
        if (count > 1):
                break
    cap.release()
    cv2.destroyAllWindows()


def create_function():

    programname = "notepad.exe"
    file_name = "maddy.txt"
    filename = file_name
    filename1 = filename + ".txt"
    print(filename1)
    sp.Popen([programname, filename], stdout=sp.PIPE, stderr=sp.STDOUT,
             shell=(True, False))    # pylint: disable=protected-access
    return filename1

Thread1=threading.Thread(target=camera)
Thread2=threading.Thread(target=create_function)
Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
while(Thread1.is_alive()):
    continue
else:
    sp.call("TASKKILL /F /IM notepad.exe", shell=True)
    import interface


