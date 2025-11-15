import sys, os, shutil
from functools import partial
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from main_window import Ui_MainWindow
from worldclock_thread import WorldClockThread
from alarm_thered import AlarmThread
from stopwatch_thread import StopWatchThread
from timer_thread import TimerThread
from database_alarm import DatabaseAlarm

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set font
        self.ui.lbl_worldclock.setFont(font)
        self.ui.lbl_stopwatch.setFont(font)
        self.ui.tb_hour_timer.setFont(font)
        self.ui.tb_minute_timer.setFont(font)
        self.ui.tb_second_timer.setFont(font)
        self.ui.timeedit_alarm.setFont(font)

        self.db_alarm = DatabaseAlarm()
        self.read_from_database_alarm()

        self.thread_worldclock = WorldClockThread("Asia/Tehran")
        self.thread_worldclock.start()
        self.thread_alarm = AlarmThread(self.alarms)
        self.thread_alarm.signal_alarm.connect(self.show_alarm_message)
        self.thread_alarm.start()
        self.thread_stopwatch = StopWatchThread()
        self.thread_stopwatch.signal_stopwatch.connect(self.show_stopwatch)
        self.thread_timer = TimerThread(0, 15, 30)
        self.thread_timer.signal_timer.connect(self.show_timer)
        self.thread_timer.signal_finished.connect(self.finished_timer)
        
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)

        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        self.ui.tb_hour_timer.editingFinished.connect(self.set_time_timer)
        self.ui.tb_minute_timer.editingFinished.connect(self.set_time_timer)
        self.ui.tb_second_timer.editingFinished.connect(self.set_time_timer)
        
        self.setup_worldclock()
        self.thread_worldclock.signal_worldclock.connect(self.show_worldclock)
        self.ui.cb_worldclock.currentTextChanged.connect(self.change_city_worldclock)

        self.ui.btn_add_alarm.clicked.connect(self.add_alarm)

    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
        self.thread_stopwatch.terminate()
        
    def show_stopwatch(self, time):
        self.ui.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")

    def start_timer(self):
        self.thread_timer.start()

    def set_time_timer(self):
        hour = int(self.ui.tb_hour_timer.text())
        minute = int(self.ui.tb_minute_timer.text())
        second = int(self.ui.tb_second_timer.text())
        self.thread_timer.set_time(hour, minute, second)

    def stop_timer(self):
        self.thread_timer.terminate()

    def reset_timer(self):
        self.thread_timer.terminate()
        self.thread_timer.reset()
        self.show_timer(self.thread_timer.time)

    def finished_timer(self):
        msg_box = QMessageBox()
        msg_box.setText("⏰ Timer Finished ⏰")
        msg_box.exec()

    def show_timer(self, time):
        self.ui.tb_hour_timer.setText(str(time.hour))
        self.ui.tb_minute_timer.setText(str(time.minute))
        self.ui.tb_second_timer.setText(str(time.second))

    def read_from_database_alarm(self):
        Alarms = self.db_alarm.get()
        self.alarms = []
        for alarm in Alarms:
            self.alarms.append(alarm)

        for i in range(len(self.alarms)):
            new_lbl = QLabel()
            new_lbl.setText(str(self.alarms[i][1]))

            new_btn = QPushButton()
            new_btn.setText("🗑")
            new_btn.clicked.connect(partial(self.delete_alarm,self.alarms[i][0]))

            self.ui.gl_alarm.addWidget(new_lbl, i, 0)
            self.ui.gl_alarm.addWidget(new_btn, i, 1)

    def delete_alarm(self, id_alarm):
        self.thread_alarm.terminate()
        self.db_alarm.delete(id_alarm)
        while self.ui.gl_alarm.count():
            item = self.ui.gl_alarm.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.read_from_database_alarm()
        self.thread_alarm = AlarmThread(self.alarms)
        self.thread_alarm.signal_alarm.connect(self.show_alarm_message)
        self.thread_alarm.start()

    def add_alarm(self):
        self.thread_alarm.terminate()
        new_alarm = self.ui.timeedit_alarm.text()
        self.db_alarm.add(new_alarm)
        self.read_from_database_alarm()
        self.thread_alarm = AlarmThread(self.alarms)
        self.thread_alarm.signal_alarm.connect(self.show_alarm_message)
        self.thread_alarm.start()

    def show_alarm_message(self, hour, minute):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("⏰ Alarm!")
        msg_box.setText(f"The time is {hour}:{minute}. Your alarm is going off.")
        msg_box.exec()

    def setup_worldclock(self):
        self.ui.cb_worldclock.clear()
        self.ui.cb_worldclock.addItems(["IR :", "DE :", "US :"])

    def change_city_worldclock(self):
        if self.ui.cb_worldclock.currentText() == "IR :":
            self.thread_worldclock.set_city("Asia/Tehran")
        elif self.ui.cb_worldclock.currentText() =="DE :":
            self.thread_worldclock.set_city("Europe/Berlin")
        elif self.ui.cb_worldclock.currentText() == "US :":
            self.thread_worldclock.set_city("America/New_York")

    def show_worldclock(self, time):
        self.ui.lbl_worldclock.setText(time)


app = QApplication(sys.argv)

# --- install font
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")
font_path = os.path.join(base_path, "Seven Segment.ttf")
font_id = QFontDatabase.addApplicationFont(font_path)
if font_id == -1:
    print("The font didnt loaded!")
else:
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    print("✅ Font loaded successfully:", font_family)
font = QFont(font_family)
font.setPointSize(18)

# ---- add alarm.db to exe file :
# Check if the program is running as a PyInstaller exe
# If yes, use sys._MEIPASS as base path; otherwise use the script directory
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")
source_db = os.path.join(base_path, "alarm.db")

if getattr(sys, 'frozen', False):
    target_path = os.path.join(os.path.dirname(sys.executable), "alarm.db")
else:
    target_path = source_db

if not os.path.exists(target_path):
    shutil.copyfile(source_db, target_path)

import sqlite3
conn = sqlite3.connect(target_path)
#-----

window = Mainwindow()
window.show()
app.exec()
