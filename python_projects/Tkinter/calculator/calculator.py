root = Tk()
root.title("Simple Calculator")
root.geometry("430x330+40+40")
          
def button_controller(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))
    pass

def button_clear():
    entry.delete(0, END)
    pass

def button_add():
    global operator
    operator = "add"
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0,END)
    pass

def button_sub():
    global operator
    operator = "sub"
    first_number = entry.get()
    f_num = int(first_number)
    entry.delete(0,END)
    pass

def button_mult():
    global operator
    operator = "mult"
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0,END)
    pass

def button_div():
    global operator
    operator = "div"
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0,END)
    pass
    
def button_equal():
    second_number = entry.get()
    entry.delete(0,END)
    if operator == "add":
        entry.insert(0,f_num + int(second_number))
    elif operator == "sub":
        entry.insert(0,f_num - int(second_number))
    elif operator == "mult":
        entry.insert(0,f_num * int(second_number))
    elif operator == "div":
        entry.insert(0,f_num / int(second_number))
    
entry = Entry(root, width="50", borderwidth='5')
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


button_one = Button(root, text = "1", padx=40, pady=20, command = lambda : button_controller(1))
button_two = Button(root, text = "2", padx=40, pady=20, command = lambda : button_controller(2))
button_three = Button(root, text = "3", padx=40, pady=20, command = lambda : button_controller(3))
button_four = Button(root, text = "4", padx=40, pady=20, command = lambda : button_controller(4))
button_five = Button(root, text = "5", padx=40, pady=20, command = lambda : button_controller(5))
button_six = Button(root, text = "6", padx=40, pady=20, command = lambda : button_controller(6))
button_seven = Button(root, text = "7", padx=40, pady=20, command = lambda : button_controller(7))
button_eigth = Button(root, text = "8", padx=40, pady=20, command = lambda : button_controller(8))
button_nine = Button(root, text = "9", padx=40, pady=20, command = lambda : button_controller(9))
button_zero = Button(root, text = "0", padx=40, pady=20, command = lambda : button_controller(0))


add_button = Button(root, text = "+", padx=40, pady=20, command=lambda : button_add())
sub_button = Button(root, text = "-", padx=40, pady=20, command=lambda : button_sub())
multi_button = Button(root, text = "*", padx=40, pady=20, command=lambda : button_mult())
div_button = Button(root, text = "/", padx=40, pady=20, command=lambda : button_div())
equal_button = Button(root, text = "=", padx=40, pady=20, command=lambda : button_equal())
all_clear_button = Button(root, text = "C", padx=40, pady=20, command = lambda : button_clear())

button_one.grid(row=3,column = 0)
button_two.grid(row=3,column = 1)
button_three.grid(row=3,column = 2)
sub_button.grid(row=3, column = 3)

button_four.grid(row=2,column = 0)
button_five.grid(row=2,column = 1)
button_six.grid(row=2,column = 2)
add_button.grid(row=2, column = 3)

button_seven.grid(row=1,column = 0)
button_eigth.grid(row=1,column = 1)
button_nine.grid(row=1,column = 2)
all_clear_button.grid(row=1, column = 3)

button_zero.grid(row=4, column =0)
equal_button.grid(row=4, column = 1)
div_button.grid(row=4, column = 2)
multi_button.grid(row=4, column =3)
root.mainloop()