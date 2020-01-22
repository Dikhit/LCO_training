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
                final_user_list.append([
                    single_users[0],
                    single_users[1],
                    single_users[2],
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
                    ans = input("What you want to change :(name/email/password)")
                    if ans == "name":
                        name = input("\nEnter your name : ")
                        old_name = items[0]
                        if len(name) > 0:
                            items[0] = name
                            f = open(self.database,'r+')
                            for line in f:
                                f.write(line.replace(old_name,name))
                            print("your name is successfully changed") 
                    elif ans == "email":
                        email = input("\nEnter your email : ")
                        old_email = items[1]
                        if len(email) > 0:
                            items[1] = email
                            f = open(self.database,'r+')
                            f = open(self.database,'r+')
                            for line in f:
                                f.write(line.replace(old_email,name))
                            print("your email is successfully changed") 
                    elif ans == "password":
                        password = input("\nEnter your password : ")
                        old_password = items[2]
                        if len(password) > 0:
                            items[2] = password
                            f = open(self.database,'r+')
                            f = open(self.database,'r+')
                            for line in f:
                                f.write(line.replace(old_password,name))
                            print("your password is successfully changed")
            print(all_users)
            return all_users
        return False
    
    def search_user(self, serial_num = -1):
        if not serial_num == -1:
            all_users = self.read_data()
            return all_users[serial_num - 1]

