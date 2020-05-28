import cv2
import numpy
import io
import time

def show_webcam():
    
    #Load face cascade into memory for use
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Set video source to webcam
    video_capture = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()  # Read one frame from source
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # detectMultiScale detects faces
        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.5,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        
        
        # Loop over rectangles which it thinks found a facee
        for (x, y, w, h) in faces:
            # Use returned values to draw a rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Function return x,y location and size of rectangle
            
        
        # This is the frame name
        #cv2.imshow('FaceDetection', frame)
        
        #if str(len(faces)) > str(0):
            #If found
            #cv2.imwrite('found_face1.jpg', frame)
        
        k = cv2.waitKey(30) & 0xff
        img_counter = 1
        
        #ESC Pressed
        if k == 27:
            break

        #SPACE Pressed
        elif k == 32:
            # When space pressed save the current frame as image with counter at the end of its name
            img_name = "facedetect_webcam_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter +=1
            continue
        
        
        img = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.1)

    # When everything is done, release the capture

    video_capture.release()
    cv2.destroyAllWindows()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    