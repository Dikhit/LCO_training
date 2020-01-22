from back_end import my_file_database


def main():
    db = my_file_database()

    print("1. Insert Data \n2. View Data \n3. Update User data \n4. Search Data \n5. Delete My Account")
    input_choice = input("\n\nEnter your choice : ")

    if input_choice == "1":
        name = input("Enter your name : ")
        email = input("Enter your email :")
        password = input("Enter your password : ")
        data = [name,email,password]
        if db.insert_data(data):
            print("your information added")
        elif not db.insert_data(data):
            print("Sorry, try again")

    elif input_choice == "2":
        all_users = db.read_data()
        for index,items in enumerate(all_users):
            print("\nUser Number : ", index + 1)
            print("User name : ",items[0])
            print("User Email : ",items[1])
            print('\n')

    elif input_choice == "3":
        email = input("\nEnter your email : ")
        data = db.update_data(email)

        if not data == "Wrong Input":
            for index,items in enumerate(data):
                if items[1] == email:
                    print("\n\nUser Number : ", index + 1)
                    print("User name : ",items[0])
                    print("User Email : ",items[1])
                    print("User password : ", items[2])
                    print('\n')
        else:
            print(data)

    elif input_choice == "4":
        sl = input("\nEnter the serial number : ")
        data = db.search_user(int(sl))
        print("\n\nHey ",data[0])
        print("your email is : ", data[1])
        print("password is :", data[2])

    elif input_choice == "5":
        id = input("Enter your ID : ")
        db.delete_user(id)

if __name__ == "__main__":
    main()