import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
# from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                        [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                        [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                        [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]
        self.random_numbers = []
        self.btn_empty = []
        for i in range(4):
            for j in range(4):
                r = random.randint(1, 16)
                while r in self.random_numbers:
                    r = random.randint(1, 16)
                if r == 16:
                    self.buttons[i][j].setVisible(False)
                    self.buttons[i][j].setText("16")
                    self.btn_empty = [i, j]
                else:
                    self.buttons[i][j].setText(str(r))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                self.random_numbers.append(r)

    def play(self, i, j):

        if (i == self.btn_empty[0] and abs(j - self.btn_empty[1]) ==  1) or\
              (j == self.btn_empty[1] and abs(i - self.btn_empty[0]) == 1):
            self.buttons[self.btn_empty[0]][self.btn_empty[1]].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")

            self.buttons[self.btn_empty[0]][self.btn_empty[1]].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.btn_empty[0] = i
            self.btn_empty[1] = j

        if self.ckeck_win() == True :
            msg_box = QMessageBox()
            msg_box.setText("🎉 Congratulation you win 🎉")
            msg_box.exec()

    def ckeck_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if self.buttons[i][j].text() != str(index):
                    index += 1
                    return False
        else:
            return True


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()


app.exec()


