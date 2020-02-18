from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.title("Image Viewer App")
root.geometry("400x400+40+40")

def browse_file():
    top = Toplevel()
    top.title("Browse File")
    top.filename = filedialog.askopenfilename(initialdir="C:\\Users\\Katlic", title="Select a file", filetypes = ( ("all files", "*.*"), ("jpg files", "*.jpg")  ))
    
    file_saver = Label(top, text = top.filename)
    file_saver.pack()
    global img
    img = ImageTk.PhotoImage(Image.open(top.filename))
    img_label = Label(top,image = img)
    img_label.pack()
button = ttk.Button(root, text = "Browse", command = browse_file)
button.pack()



root.mainloop()