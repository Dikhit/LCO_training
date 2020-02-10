import cv2
import numpy as np

points = []

def mouse_callback(event, x_co, y_co, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x_co, y_co)
        cv2.circle(img, (x_co,y_co), 3, (0,0,255), -1)
        points.append((x_co,y_co))
        if len(points) >=2:
            cv2.arrowedLine(img, points[-1], points[-2], (255,200,10), 3)
        cv2.imshow("image", img)
        
img = np.zeros((512,512,3),  np.uint8)
cv2.putText(img, "click to draw a lines", (10,30), font, 1, (0,255,255), 2 , cv2.LINE_AA)

cv2.imshow("image", img)
cv2.setMouseCallback('image', mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
