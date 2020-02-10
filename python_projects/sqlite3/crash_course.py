from back_end import DatabaseManagement
import sys
import tabulate as tb

def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT ::\n\n")
    db_obj = DatabaseManagement()

    print("*"*40)
    print("\n")
    print("\n ::User Manual :: \n")
    print("-"*40)
    print("\n\n")

    print("\nPress 1. Insert a New Course...")
    print("\nPress 2. View All Courses...")
    print("\nPress 3. Delete any Course (NEED ID OF THAT COURSE)...")
    print("\nPress 4. Search any Course (NEED ID OF THAT COURSE)...")
    print("\n")
    print("*"*40)

    choice = int(input("\nEnter your Choice : "))

    if choice == 1:
        name = input("\nEnter the course name : ")
        description = input("\nEnter the course description : ")
        price = input("\nEnter the course price : ")
        is_private = input("\nThe Course is private or not (1/0) : ")
        
        data = [name, description, price, is_private]
        if db_obj.insert_data(data):
            print("\n Course was inserted Successfully")
        else:
            print("Oopps, Something went wrong!")
        
    elif choice == 2:
        print("\n:: Course List :: \n")

        all_courses = db_obj.fetch_data()
        headers = ["Sl No", "Course Name", "Course Desc", "Price", "availability"]
        print(tb.tabulate(all_courses, headers=headers, tablefmt="grid"))

    elif choice == 3:
        course_id = int(input("Enter the course id : "))
        if db_obj.delete_course(id):
            print("Course was deleted")
        else:
            print("Oops! Something went wrong")

    elif choice == 4:
        course_id = int(input("Enter the course id : "))
        course_details = db_obj.search_data(course_id)
        headers = ["Sl No", "Course Name", "Course Desc", "Price", "availability"]
        print(tb.tabulate(course_details, headers=headers, tablefmt="grid"))
    else:
        sys.exit(0)





if __name__ == '__main__':
    main()