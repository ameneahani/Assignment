import random
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbl_instruction.setText("    Please guess a number, enter it, and press Guess:")
        self.target()
        self.play()
        self.ui.btn_guess.clicked.connect(self.play)
        self.ui.btn_restart.clicked.connect(self.target)

    def target(self):
        self.min_num = int(self.ui.txt_min_num.text())
        self.max_num = int(self.ui.txt_max_num.text())
        self.cpu_num = random.randint(self.min_num, self.max_num)
        self.attempt = 0

    def play(self):
        
        if self.ui.txt_guess.text():
            self.input_num = int(self.ui.txt_guess.text())
            if self.input_num < self.cpu_num :
                self.ui.lbl_instruction.setText(f"My number is greater than {self.input_num}")
                self.attempt += 1
            elif self.input_num > self.cpu_num:
                self.ui.lbl_instruction.setText(f"My number is less than {self.input_num}")
                self.attempt += 1
            else:
                self.ui.lbl_instruction.setText(f"Well Done! It took you {self.attempt} attempts to guess this number.")

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()
app.exec()