import cv2
import datetime

capture = cv2.VideoCapture(0)
while capture.isOpened():
    ret,frame = capture.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        text = "width " + str(width) + " height "+ str(height)
        date = str(datetime.datetime.now())
        cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2 , cv2.LINE_AA)
        cv2.putText(frame, "mainu-mon", (10,100), font, 1, (0,255,255), 2 , cv2.LINE_AA)
        cv2.putText(frame, date, (10,150), font, 1, (0,255,255), 2 , cv2.LINE_AA)


        cv2.imshow("webcam", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
            
        elif key == ord('s'):
            cv2.imwrite("screenshot.jpg", frame)
            
    else:
        break
        

capture.release()
cv2.destroyAllWindows()