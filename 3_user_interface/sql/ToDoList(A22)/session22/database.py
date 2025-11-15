import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("todolist.db")
        self.cursor = self.con.cursor()


    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    def add_new_task(self, new_title, new_description):
        try:
            quary = f"INSERT INTO tasks(title, description) VALUES('{new_title}', '{new_description}')"
            self.cursor.execute(quary)
            self.con.commit()
            return True
        except Exception as e:
            print("DB Error :" ,e)
            return False
        
    def remove_task(self):
        quary = "DELETE FROM ..."

    def task_don(self):
        quary = "UPDATE ... SET is_done = 1 WHERE ..."


        