from modules import *


root = Tk()
root.geometry("400x400+40+40")
root.title("Employee Management System")

# Database connections
global db_connection
try:
    db_connection = lite.connect("address.db")

    with db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""CREATE TABLE IF NOT EXISTS address(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                pincode INTEGER
            )""")
except Exception:
    print("Something went wrong !")
    
    
def insert_data(user):
    try:
        with db_connection:
            db_cursor = db_connection.cursor()
            db_cursor.execute(
                """INSERT INTO address(
                    first_name, last_name, address, city, state, pincode
                ) VALUES (?,?,?,?,?,?)""", user
            )
        return True
    except Exception:
        return False



def fetch_data():
    try:
        with db_connection:
            db_cursor = db_connection.cursor()
            sql_command = "select * from address"
            db_cursor.execute(sql_command)
            return db_cursor.fetchall()
    except Exception:
        return False
    
    
def search_data(id):
    id = int(id)
    try:
        with db_connection:
            db_cursor = db_connection.cursor()
            sql_command = "select * from address where id = ?"
            db_cursor.execute(sql_command, [id])
            return db_cursor.fetchall()
    except Exception:
        return False
################ front end part ##################

# functions
def submit():
    user = [first_name.get(), last_name.get(), address.get(), city.get(), state.get(), pincode.get()]
    print(user)
    if insert_data(user):
        print("Data Successfully saved")
        label_some= Label(root, text = "data Submitted")
        label_some.grid(row = 14, column=0, columnspan=4)
    else:
        print("something went wrong here!!")
        
    
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    pincode.delete(0,END)
    
def show_data():
    all_users = fetch_data()
    headers = ["First Name", "Last Name", "Address", "City", "State", "Pincode"]
    print(tb.tabulate(all_users, headers = headers, tablefmt="grid"))
    
        
# Entry point
first_name = Entry(root, width = 30)
first_name.grid(row=0, column = 1, padx = 20)

last_name = Entry(root, width = 30)
last_name.grid(row=1, column = 1, padx = 20)

address = Entry(root, width = 30)
address.grid(row=2, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row=3, column = 1, padx = 20)

state = Entry(root, width = 30)
state.grid(row=4, column = 1, padx = 20)

pincode = Entry(root, width = 30)
pincode.grid(row=5, column = 1, padx = 20)



# label point

first_name_label = Label(root, text = "first name : ")
first_name_label.grid(row=0, column=0)

last_name_label = Label(root, text = "last name : ")
last_name_label.grid(row=1, column=0)

address_label = Label(root, text = "Address : ")
address_label.grid(row=2, column=0)

city_label = Label(root, text = "City : ")
city_label.grid(row=3, column=0)

state_name_label = Label(root, text = "State : ") 
state_name_label.grid(row=4, column=0)

pincode_label = Label(root, text = "pincode : ")
pincode_label.grid(row=5, column=0)

# Submit Button
submit_button = ttk.Button(root, text = "Submit", command = submit)
submit_button.grid(row = 7, column = 0, columnspan = 4, padx=10, pady=10)


show_button = ttk.Button(root, text = "fetch data", command = show_data)
show_button.grid(row = 8, column = 0, columnspan = 4, padx=10, pady=10)



root.mainloop()