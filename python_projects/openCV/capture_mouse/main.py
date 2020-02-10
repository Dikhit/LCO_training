import cv2
import numpy as np


def mouse_callback(event, x_co, y_co, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x_co, y_co)
        font = cv2.FONT_HERSHEY_SIMPLEX
        x_y = str(x_co) + "," + str(y_co)
        print(x_y)
        cv2.putText(img, x_y, (x_co,y_co), font, 0.8, (255,255,0), 2)
        cv2.imshow("image", img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(x_co, y_co)
        font = cv2.FONT_HERSHEY_SIMPLEX
        x_y = str(x_co) + "," + str(y_co)
        print(x_y)
        cv2.putText(img, x_y, (x_co,y_co), font, 1, (255,255,0), 2)
        cv2.imshow("image", img)
        
img = np.zeros((512,512,3), np.uint8)
cv2.imshow("image", img)
cv2.setMouseCallback('image', mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
