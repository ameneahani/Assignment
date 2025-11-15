import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("todolist.db")
        self.my_cursor = self.con.cursor()

    def get_tasks(self):
        quary = "SELECT *FROM tasks"
        self.my_cursor.execute(quary)
        res = self.my_cursor.fetchall()
        return res

    def delete_task(self, task_id):
        quary = f"DELETE FROM tasks WHERE id = '{task_id}'"
        self.my_cursor.execute(quary)
        self.con.commit()

    def add_task(self, new_title, new_description, new_time):
        quary = f"INSERT INTO tasks(title, description, time) VALUES('{new_title}', '{new_description}', '{new_time}')"
        self.my_cursor.execute(quary)
        self.con.commit()

    def edit_task(self):
        quary = f"UPDATE SET ... INTO ..."
        self.my_cursor.execute(quary)
        self.con.commit()

    def is_done(self, status, task_id):
        quary = f"UPDATE tasks SET is_done = '{status}' WHERE id = '{task_id}'"
        self.my_cursor.execute(quary)
        self.con.commit()
