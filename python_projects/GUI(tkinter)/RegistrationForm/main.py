from modules import *

# Window setup
Window = Tk()
Window.title("Registration App")
Window.geometry("500x500+40+40")

########################## Functions ###########################

def log_in():
    prog_lang = var_c1
    prog_lang = var_c2
    users = [first_name.get(), last_name.get(), dob.get(), prog_lang, var.get() ]
    print(users)



###################### Window #########################

# logo = ImageTk.PhotoImage(Image.open("images.png"))
# logo_label = Label(Window, image = logo)
# logo_label.pack()

fn = StringVar()
ln = StringVar()
date = StringVar()
var_c1 = "Java Script"
var_c2 = "Python"

heading = Label(Window, text="Registration Form", relief ="solid", font=("arial", 19, "bold"))
heading.place(x=140, y=23)


first_name_label = Label(Window, text="First Name : ")
first_name_label.place(x=80, y=130)
first_name = Entry(Window, text = fn, width = 40)
first_name.place(x=160,y=130)

last_name_label = Label(Window, text="Last Name : ")
last_name_label.place(x=80, y=170)
last_name = Entry(Window, text = ln, width = 40)
last_name.place(x=160,y=170)

country_label = Label(Window, text="Country : ")
country_label.place(x=80, y=220)
# country_name = Entry(Window, text = cn, width = 30)
# country_name.place(x=160,y=220)

var = StringVar()
country_list = ["India", "Nepal", "China", "Bangladesh", "Pakistan","Bhutan"]
droplist = OptionMenu(Window, var, *country_list)
var.set("Select Country")
droplist.config(width = 33)
droplist.place(x=160,y=220)


dob_label = Label(Window, text="Date of Birth : ")
dob_label.place(x=80, y=270)
dob = Entry(Window, text = date, width = 40)
dob.place(x=160,y=270)

prog_lang_label = Label(Window, text="prog lang : ")
prog_lang_label.place(x=80, y=320)
# prog_lang = Entry(Window, text = date, width = 40)
# prog_lang.place(x=160,y=320)
check_box = Checkbutton(Window, text="JS", variable = var_c1)
check_box.place(x=160,y=320)
check_box = Checkbutton(Window, text="Python", variable = var_c2)
check_box.place(x=230,y=320)


login_button = Button(Window, text = "Log In", width=12, bg="brown", fg="white", command=log_in)
login_button.place(x=150, y=380)

login_button = Button(Window, text = "Quit", width=12, bg="brown", fg="white", command=print)
login_button.place(x=280, y=380)

Window.mainloop()