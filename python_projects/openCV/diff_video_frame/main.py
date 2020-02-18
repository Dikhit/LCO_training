import cv2
path = "a.mp4"
capture = cv2.VideoCapture(path)

while True:
    _, frame = capture.read()
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    other = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
#     cv2.imshow("frame", frame)
    cv2.imshow("gray", gray_video)
    cv2.imshow("others", other)
    key = cv2.waitKey(1)
    if key == 27:
        break
        
capture.release()
cv2.destroyAllWindows()