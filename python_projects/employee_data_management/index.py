class employee_data_management():
    def __init__(self):
        self.database = "auth_data.txt"
        try:
            self.file =  open(self.database, "a+") 
        except:
            print("Something went wrong!!")
        pass


    def register_user(self, user_data):
        try:
            with open(self.database, 'a+') as file:
                for info in user_data:
                    file.write(info + "\n")
            
                file.write('\n\n')
                print("User Successfully Created!!")
        except:
            return False


    def view_all_users(self):
        user_data = ""
        all_user_list = []
        try:
            with open(self.database, "r+") as file:
                user_data = file.read() 

            single_user_chunk = user_data.split('\n\n\n')
            del single_user_chunk[len(single_user_chunk) - 1]

            for item in single_user_chunk:    
                single_chunk = item.split('\n')
                all_user_list.append((single_chunk[0],single_chunk[1],single_chunk[2]))
            
            return all_user_list
        
        except :
            print("close")
            return False
    def update_data(self,email="example@emaple.com"):
        if not email == "example@emaple.com":
            all_users = self.read_data()
            for items in all_users:
                if items[1] == email:
                    print("\n\nyour name is : ", items[0])
                    print("your email is : ", items[1])
                    print("your password is : ", items[2])
                    ans = input("\nWhat you want to change (name/email/password) : " )
                    
                    if ans == "name":
                        name = input("\nEnter your name : ")
                        old_name = items[0]
                        if len(name) > 0:
                            items[0] = name
                            with open(self.database,'r') as file:
                                filedata = file.read()
                            filedata = filedata.replace(old_name,items[0])
                            with open(self.database,'w') as file:
                                file.write(filedata)
                            print("your name is successfully changed")
                        else:
                            return "Wrong Input"
                             
                    
                    elif ans == "email":
                        email = input("\nEnter your email : ")
                        old_email = items[1]
                        if len(email) > 0:
                            items[1] = email
                            with open(self.database,'r') as file:
                                filedata = file.read()
                            filedata = filedata.replace(old_email,items[1])
                            with open(self.database,'w') as file:
                                file.write(filedata)

                            print("your email is successfully changed") 
                        else:
                            return "Wrong Input"

                    elif ans == "password":
                        password = input("\nEnter your password : ")
                        old_password = items[2]
                        if len(password) > 0:
                            items[2] = password
                            with open(self.database,'r') as file:
                                filedata = file.read()
                            filedata = filedata.replace(old_password,items[1])
                            with open(self.database,'w') as file:
                                file.write(filedata)
                            print("your password is successfully changed")
                        else:
                            return "Wrong Input"
            return all_users
        return "Wrong Input"
    
    def search_user(self, serial_num = -1):
        if not serial_num == -1:
            all_users = self.read_data()
            return all_users[serial_num - 1]


obj = employee_data_management()
obj.register_user(["Dikhit Kumar Bhuyan", "dikhitbhuyan@gmail.com", "kaku0001"])
obj.register_user(["kashmiri Moni Mahanta Bhuyan", "kmonimahanta@gmail.com", "heythere"])
