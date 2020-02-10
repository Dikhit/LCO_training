import sqlite3 as lite

class DatabaseManagement(object):
    def __init__(self):
        global db_connection
        try:
            db_connection = lite.connect('course.db')
            with db_connection:
                cursor = db_connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS course(
                    Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT,
                    description TEXT,
                    price TEXT,
                    is_private BOOLEAN NOT NULL DEFAULT 1
                    )""")
        except Exception:
            print("Something went wrong.. Unable to connect db")
    

    def insert_data(self, data):
        try:
            with db_connection:
                cursor = db_connection.cursor()
                cursor.execute(
                    """INSERT INTO course(
                        name, description, price, is_private
                    ) VALUES (?,?,?,?)""", data
                )
            return True
        except Exception:
            return False


    def fetch_data(self):
        try:
            with db_connection:
                cursor = db_connection.cursor()
                sql = "SELECT * FROM course"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception:
            return False


    def delete_course(self, id):
        try:
            with db_connection:
                cursor = db_connection.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cursor.execute(sql, [id])
            return True
        except Exception:
            return False

    def search_data(self, id):
        try:
            with db_connection:
                cursor = db_connection.cursor()
                sql = "SELECT * FROM course WHERE id = ?"
                cursor.execute(sql, [id])
                course_details = cursor.fetchall()
                return course_details
        except Exception:
            return False

        return False

