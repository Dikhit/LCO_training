class my_file_database(object):
    def __init__(self):
        self.database = "database.txt"
        try:
            self.file = open(self.database,'a')
        except:
            print("Error in creating the file ...")
    def insert_data(self,single_user_details):
        try:
            with open(self.database,'a') as f:
                f.write(single_user_details[0] + "\n")
                f.write(single_user_details[1] + "\n")
                f.write(single_user_details[2])
                f.write("\n\n\n")
            return True
        except:
            return False
    
    def read_data(self):
        data = ""
        final_user_list = []
        with open(self.database) as f:
            data = f.read()
            single_user_details_list = data.split('\n\n\n')
            for items in single_user_details_list[:-1]:
                single_users = items.split('\n')
                print(len(single_users))
                for i in range(0,len(single_users) - 1):
                    final_user_list.append([
                        single_users[i]
                    ])
        return final_user_list

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
    
    def delete_user(self,email):
        with open(self.database, 'r+') as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != email:
                    f.write(i)
            f.truncate()         

    def delete_one_information(self,email):
        with open(self.database,'r') as file:
            all_users = file.read()
            for items in all_users:
                if items[1] == email:
                    print("\n\nyour name is : ", items[0])
                    print("your email is : ", items[1])
                    print("your password is : ", items[2])
                    
                    name = items[0]
                    email = items[1]
                    password = items[2]

                    with open(self.database,'r') as file:
                        filedata = file.read()
                    filedata = filedata.replace(name,'\t')
                    filedata = filedata.replace(email,'\t')
                    filedata = filedata.replace(password,'\t')
                    with open(self.database,'w') as file:
                        file.write(filedata)
                    print("your name is successfully changed")
                else:
                    return "Wrong Input"