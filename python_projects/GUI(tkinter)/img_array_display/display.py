from modules import *


root = Tk()
root.title("Image Viewer App")


def back(img_number):
    global img_label
    global button_forward
    global button_back
    
    img_label.grid_forget()
    img_label = Label(image = img_list[img_number-1])
    img_label.grid(row = 0, column = 0, columnspan = 3)
    
    if img_number + 1 <= 5:
        right_button = ttk.Button(root, text = ">>", command = lambda : forward(img_number+1)).grid(row = 1, column = 2)
        if img_number == 1:
            left_button = ttk.Button(root, text = "<<", command = lambda : back(1)).grid(row = 1, column = 0)
        else:
            left_button = ttk.Button(root, text = "<<", command = lambda : back(img_number-1)).grid(row = 1, column = 0)
    else:
        right_button = ttk.Button(root, text = ">>", command = lambda : forward(1)).grid(row = 1, column = 2)

def forward(img_number):
    global img_label
    global button_forward
    global button_back
    
    img_label.grid_forget()
    img_label = Label(image = img_list[img_number-1])
    img_label.grid(row = 0, column = 0, columnspan = 3)
    
    if img_number + 1 <= 5:
        right_button = ttk.Button(root, text = ">>", command = lambda : forward(img_number+1)).grid(row = 1, column = 2)
        if img_number == 1:
            left_button = ttk.Button(root, text = "<<", command = lambda : back(1)).grid(row = 1, column = 0)
        else:
            left_button = ttk.Button(root, text = "<<", command = lambda : back(img_number-1)).grid(row = 1, column = 0)
    else:
        right_button = ttk.Button(root, text = ">>", command = lambda : forward(1)).grid(row = 1, column = 2)

    
img_1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))


img_list = [img_1,img_2, img_3, img_4, img_5]

img_label = Label(image = img_1, height = 550, width = 600)
img_label.grid(row = 0, column = 0, columnspan = 3)




left_button = ttk.Button(root, text = "<<", command = lambda : back(1)).grid(row = 1, column = 0)
right_button = ttk.Button(root, text = ">>", command = lambda : forward(2)).grid(row = 1, column = 2)

root.mainloop()