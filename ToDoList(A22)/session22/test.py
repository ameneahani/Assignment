import sqlite3

con = sqlite3.connect("todolist.db")
my_cursor = con.cursor()
quary_INSERT = "INSERT INTO tasks(id, title, description, is_done) VALUES(19, 'python','bargozari dar githab',0)"
quary_SELECT = "SELECT *FROM tasks"
quary_IF = "SELECT *FROM tasks WHERE id = 19"
quary_UPDATE = "UPDATE tasks SET is_done = 1 WHERE id = 19"
quary_DELET = "DELETE FROM tasks WHERE id = 19"
res = my_cursor.execute(quary_DELET)
# a = res.fetchall()
# print(a)
con.commit()
