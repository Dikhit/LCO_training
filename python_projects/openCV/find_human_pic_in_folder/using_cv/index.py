import os
import matplotlib.pyplot as plt
import cv2
import numpy


def load_images(floder_path):
    images = []
    for filename in os.listdir(floder_path):
        img = cv2.imread(os.path.join(floder_path,filename))
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # detector = cv2.CascadeClassifier(path)
            # faces = detector.detectMultiScale(gray,1.3,5)
            images.append(gray)
    return images



path = 'C:\\Users\\Katlic\\Documents\\LCO_Bootcamp\\LCO_class_assign_prac\\PracticeFolder'
list_of_images = load_images(path)
print("num of human pics in the folder : ", len(list_of_images))
