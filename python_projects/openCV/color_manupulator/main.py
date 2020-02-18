import cv2
img = cv2.imread("1.jpg")
b,g,r = cv2.split(img)

img = cv2.merge((g,r,b))
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()