import random
import string
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from sys import argv
from ui_mainwindow import Ui_MainWindow


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.password = []
        self.ui.btn_standard.clicked.connect(partial(self.make_password,"standard"))
        self.ui.btn_strong_pass.clicked.connect(partial(self.make_password,'Extra_strong'))
        self.ui.btn_super_pass.clicked.connect(partial(self.make_password,'super_strong'))



    def make_password(self, pass_type):
        self.password = []
        if pass_type == "standard":
            for i in range(8):
                letter = random.choice(string.ascii_letters)
                self.password.append(letter)
            self.ui.lbl_standard.setText("".join(self.password))
        elif pass_type == "Extra_strong":
            for i in range(12):
                letter = random.choice(string.ascii_letters)
                num = str(random.randint(0,9))
                self.password.append(random.choice([letter, num]))
            self.ui.lbl_strong_pass.setText("".join(self.password))
        elif pass_type == "super_strong":
            for i in range(12):
                letter = random.choice(string.ascii_letters)
                num = str(random.randint(0,9))
                character =random.choice(["!","@","#","$","%","&","*"])
                self.password.append(random.choice([num,letter,character]))
            self.ui.lbl_super_pass.setText("".join(self.password))
        






app = QApplication(argv)
window = Mainwindow()
window.show()
app.exec()
