import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("1.jpg", 1)
image = np.zeros((512,512))
img = cv2.line(image, (255,0), (255,100), (0,200,150), 10)
img = cv2.arrowedLine(img, (0,0), (200,100), (100,100,150), 10)
img = cv2.rectangle(img, (300,100), (400,190), (0,0,200), 5)
img = cv2.circle(img, (200,300), 50, (100,100,100), -1)

cv2.imshow("img", img) 

cv2.waitKey(5000)
cv2.destroyAllWindows()
