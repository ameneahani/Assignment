import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from database import Database
from main_window import Ui_MainWindow


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.db = Database()
        self.read_from_database()
    
        self.ui.btn_new_task.clicked.connect(self.new_task)

    


    def read_from_database(self):
        self.clear_layout()
        Tasks = self.db.get_tasks()
        tasks = []
        
        for task in Tasks:
            if task[3] == 1:
                tasks.append(task)
        for task in Tasks:
            if task[3] == 0:
                tasks.append(task)

        for i in range(len(tasks)):
            new_btn = QPushButton()
            new_btn.clicked.connect(partial(self.delete, id_task = tasks[i][0]))
            new_lb = QLabel()
            new_lb.mousePressEvent = lambda event, t=tasks[i][0]: self.show_detail(tasks, t)

            new_cb = QCheckBox()
            
            new_cb.setChecked(tasks[i][3] == 1) 
            new_cb.clicked.connect(partial(self.done, id_task = tasks[i][0], checkbox = new_cb))
            new_btn.setText("🗑")
            new_lb.setText(tasks[i][1])
            if tasks[i][4] == 1:
                new_lb.setStyleSheet("color : red; font-weight:bold")

            self.ui.gl_tasks.addWidget(new_btn, i, 0)
            self.ui.gl_tasks.addWidget(new_lb, i, 1)
            self.ui.gl_tasks.addWidget(new_cb, i, 2)

    def show_detail(self, tasks, task_id):
        for task in tasks:
            if task[0] == task_id:
                self.ui.tb_new_task_description.setText(task[2])
                self.ui.tb_new_task_title.setText(task[1])
                time_str = task[5]
                # print(time_str)
                hour = time_str.split(":")
                minute = hour[1].split(" ")
                time = QTime(int(hour[0]), int(minute[0]))          
                self.ui.timeEdit.setTime(time)
                break

    def delete(self, id_task):
        self.db.delete_task(id_task)
        while self.ui.gl_tasks.count():
            item = self.ui.gl_tasks.takeAt(0)   # از لایوت جدا کن
            widget = item.widget()
            if item.widget() is not None:    #بعضی وقت ها ویجت میتونه لابوت داخلی باشه اون وقت نان برمیگردونه
                widget.deleteLater()
        self.read_from_database()

    def clear_layout(self):
        while self.ui.gl_tasks.count():
            item = self.ui.gl_tasks.takeAt(0)   
            widget = item.widget()
            if item.widget() is not None:    
                widget.deleteLater()



    def new_task(self, id_task):
        new_title = self.ui.tb_new_task_title.text()
        new_description = self.ui.tb_new_task_description.toPlainText()
        new_time = self.ui.timeEdit.text()
        time = self.ui.timeEdit.time() # تایم رو به صورت شی ذخیره میکنه
        
        time_str = time.toString("HH:mm")
        if new_title != "":
            self.db.add_task(new_title, new_description, time_str)
        self.read_from_database()

        self.ui.tb_new_task_title.setText("")
        self.ui.tb_new_task_description.setText("")

    def done(self, id_task, checkbox):
        if checkbox.isChecked():
            status = 1 
        else:
            status = 0
        self.db.is_done(status, id_task)
        self.read_from_database()



app = QApplication()
win = Mainwindow()
win.show()
app.exec()