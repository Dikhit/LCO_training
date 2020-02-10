from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import cv2
import time
import matplotlib.pyplot as plt

root =Tk()
root.geometry("400x400+40+40")
root.resizable(False, False)
root.title("Image Viewer App")

global img 
current_deg = 0

img = cv2.imread("1.jpg")
num_rows, num_cols = img.shape[:2]

def left_rotate(deg):
    global current_deg
    current_deg = current_deg - 10

    rot_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), current_deg, 1.0)
    img_rotation = cv2.warpAffine(img, rot_matrix, (num_cols, num_rows))
    
    cv2.imwrite("1.jpg", img_rotation)
    pass

def right_rotate(deg):
    global current_deg
    current_deg = current_deg + 10

    rot_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), current_deg, 1.0)
    img_rotation = cv2.warpAffine(img, rot_matrix, (num_cols, num_rows))
    
    cv2.imwrite("1.jpg", img_rotation)


my_img = ImageTk.PhotoImage(Image.open("1.jpg"))
# why we don't have to pass the root object in the image
lbl=Label(image=my_img)
lbl.pack()


left_rotation_button = ttk.Button(root, text = "-10deg", command=lambda : left_rotate(current_deg)).pack(side="left")
# current_degree = Label(root, text = current_deg).pack()
right_rotation_button = ttk.Button(root, text = "+10deg", command=lambda : right_rotate(current_deg)).pack(side="right")


root.mainloop()    