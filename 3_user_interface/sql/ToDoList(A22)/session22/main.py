import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QLabel, QCheckBox
from PySide6.QtCore import Qt
from main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_task)

    def new_task(self):
        new_title = self.ui.tb_new_task_title.text()
        new_description = self.ui.tb_new_task_description.toPlainText()
        feedback = self.db.add_new_task(new_title, new_description)
        if feedback == True:
            self.read_from_database()
            self.ui.tb_new_task_title.setText("")
            self.ui.tb_new_task_description.setText("")

        else:
            msg_box = QMessageBox()
            msg_box.setText("there is a problem")
            msg_box.exec_()
    
    def read_from_database(self):
        tasks = self.db.get_tasks()
        # print(tasks)
        for i in range(len(tasks)):
            new_cb = QCheckBox()
            new_lb = QLabel()
            new_btn = QPushButton()
            new_btn.setText("❌")
            new_lb.setText(tasks[i][1])
            
            self.ui.gl_tasks.addWidget(new_cb, i, 0)
            self.ui.gl_tasks.addWidget(new_lb, i, 1)
            self.ui.gl_tasks.addWidget(new_btn, i, 2)
            



if __name__=="__main__":
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()

    app.exec()