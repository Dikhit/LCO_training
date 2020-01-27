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


obj = employee_data_management()
obj.register_user(["Dikhit Kumar Bhuyan", "dikhitbhuyan@gmail.com", "kaku0001"])
obj.register_user(["kashmiri Moni Mahanta Bhuyan", "kmonimahanta@gmail.com", "heythere"])
