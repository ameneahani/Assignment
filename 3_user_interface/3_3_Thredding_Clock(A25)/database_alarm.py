import sqlite3

class DatabaseAlarm:
    def __init__(self):
        self.con = sqlite3.connect("alarm.db")
        self.my_cursor = self.con.cursor()

    def get(self):
        quary = "SELECT * FROM alarms"
        self.my_cursor.execute(quary)
        res = self.my_cursor.fetchall()
        return res

    def delete(self, alarm_id):
        quary = f"DELETE FROM alarms WHERE id = '{alarm_id}'"
        self.my_cursor.execute(quary)
        self.con.commit()

    def edit(self, alarm_id, time):
        quary = f"UPDATE alarms set time='{time}' WHERE id = '{alarm_id}'"
        self.my_cursor.execute(quary)
        self.con.commit()

    def add(self, time):
        quary = f"INSERT INTO alarms(time) VALUES( '{time}')"
        self.my_cursor.execute(quary)
        self.con.commit()


# d = Database()
# d.add_alarm( 11)
# d.get_alarms()
# # d.delete_alarm(2)
# d.edit_alarm(4, 12)


