import cv2
import numpy as np
import matplotlib.pyplot as plt



capture = cv2.VideoCapture(0)

video_saver = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', video_saver, 20.0, (640,480))
while True:
    ret, frame =  capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    
    cv2.imshow('Normal Frame', frame)
    cv2.imshow('Gray Frame ', gray)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(0xFF)
        break
        
capture.release()
out.release()
cv2.destroyAllWindows()  