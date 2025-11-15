import sys
import random
from functools import partial
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow
from sudoku import *

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("""
                            QMainWindow {
                            background-color: #3e2723; 
                             }
                             """)
        
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        self.ui.menu_new_puzzle.triggered.connect(self.new_game)
        self.ui.menu_solve_puzzle.triggered.connect(self.solve_puzzle)
        self.ui.menu_open_file.triggered.connect(self.open_file)
        self.ui.menu_About.triggered.connect(self.about)
        self.ui.menu_Help.triggered.connect(self.help)
        self.ui.menu_Exit.triggered.connect(self.exit)
        self.new_game()
        
    def new_game(self):
        self.puzzle = Sudoku(3, 3, seed= random.randint(1, 1000)).difficulty(0.4)
        
        for i in range(9):
            for j in range(9):
                new_cell = self.make_cell(i, j)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                if self.puzzle.board[i][j] != None:
                    new_cell.setText(str(self.puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                else:
                    new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

    def solve_puzzle(self):
        solution = self.puzzle.solve()
        for i in range(9):
            for j in range(9):
                new_cell = self.make_cell(i, j)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.setText(str(solution.board[i][j]))
                new_cell.setReadOnly(True)

    def open_file(self):
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        try:
            file_path = QFileDialog.getOpenFileName(self, "Open file ...")
            if not file_path[0]:
                return
            
            f = open(file_path[0], 'r')
            try:
                big_str1 = f.read().split("\n")
            finally:
                f.close()
            big_str = []
            for row in big_str1:
                cell = row.split()
                big_str.append(cell)
            
            if len(big_str) != 9 or any(len(r) != 9 for r in big_str):
                QMessageBox(self).critical(self, "Error", "File format invalid")
                return
                
            for i in range(9):
                for j in range(9):
                    new_cell = self.make_cell(i, j)
                    self.ui.grid_layout.addWidget(new_cell, i, j)
                    if i < len(big_str) and j < len(big_str[i]) and big_str[i][j] != "0":
                        new_cell.setText(str(big_str[i][j]))
                        new_cell.setReadOnly(True)
                    else:
                        new_cell.textChanged.connect(partial(self.validation, i, j))
                    self.line_edits[i][j] = new_cell
        except Exception as e:
            QMessageBox(self).critical(self, "Error", "Failed to load data file.")
            print("open_file error:", e)

    def about(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("About Sudoko")
        msg_box.setText("Sudoku Python Game\n"
                        "Version 1.0\n"
                        "Developed with ❤️ using PySide6\n" 
                        "Copyright © 2025 Amene.\n"
                        "All rights reserved.")
        msg_box.exec()

    def help(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("How to Play Sudoku 🧩")
        msg_box.setText(
        "🔢 Sudoku Rules:\n"
        "• Fill a 9×9 grid so that every row, column,\n"
        "  and each 3×3 block contains all digits 1 to 9.\n\n"
        "💡 Playing Tips:\n"
        "• Use logic, not guessing.\n"
        "• Eliminate impossible numbers in each cell.\n"
        "• Focus on rows, columns & blocks to narrow down.\n\n"
        "Enjoy solving and challenge your brain! ✅"
        )
        msg_box.exec()

    def exit(self):
        exit(0)

    def make_cell(self, i, j):
        new_cell = QLineEdit()
        new_cell.setProperty("invalid", False)
        #-------------------------------------- style for Qlinedite
        new_cell.setFixedSize(45, 45)
        style = """
            QLineEdit {
                background-color: #5d4037;
                color: white;
                border: 2px solid #3e2723;
                border-radius: 8px;
                font-size: 20px;
                qproperty-alignment: 'AlignCenter';
        """
        # شرط‌ها برای مرزبندی بلوک‌ها
        if j % 3 == 0:
            style += "border-left: 3px solid black;"
        if i % 3 == 0:
            style += "border-top: 3px solid black;"
        if j == 8:
            style += "border-right: 3px solid black;"
        if i == 8:
            style += "border-bottom: 3px solid black;"
        style += "}"  # بستن استایل
        new_cell.setStyleSheet(style)
        #--------------------------------------------------------
        new_cell.focusInEvent = lambda event, x=i, y=j: (QLineEdit.focusInEvent(new_cell, event), self.highlight_cells(x, y))
        return new_cell

    def validation(self, i, j, text):
        if text not in ["1","2","3","4","5","6","7","8","9"]:
            self.line_edits[i][j].setText("")
        if self.check() is False:
            self.line_edits[i][j].setProperty("invalid", True)
            self.line_edits[i][j].setStyleSheet("""
                QLineEdit {
                    background-color: #c62828; /* قرمز */
                    color: white;
                    border: 2px solid #b71c1c;
                    border-radius: 12px;
                    font-size: 20px;
                    qproperty-alignment: 'AlignCenter';
                }
            """)
        else:
            self.line_edits[i][j].setProperty("invalid", False)
            self.line_edits[i][j].setStyleSheet("""
                QLineEdit {
                    background-color: #5d4037;
                    color: white;
                    border: 2px solid #3e2723;
                    border-radius: 12px;
                    font-size: 20px;
                    qproperty-alignment: 'AlignCenter';
                }
            """)

    def check(self):
        for i in range(9):
            for t in range(9):
                for j in range(t+1, 9):
                    if self.line_edits[i][j].text() != "" and self.line_edits[i][t].text() == self.line_edits[i][j].text():
                        return False

        for i in range(9):
            for t in range(9):
                for j in range(t+1, 9):
                    if self.line_edits[t][i].text() == self.line_edits[j][i].text() and self.line_edits[j][i].text() != "":
                        return False
                    
        for t in range(0, 9, 3):
            for i in range(0, 9, 3):
                cells = []
                for r in range(t, t+3):
                    for c in range(i, i+3):
                        if self.line_edits[r][c].text() != "":
                            cells.append(self.line_edits[r][c].text())
                if len(cells) != len(set(cells)):
                    return False
        self.check_win()
                
    def check_win(self):
        flag = True
        for cells in self.line_edits:
            for cell in cells:
                if cell.text() == "":
                    flag = False
                    break
                elif cell.property("invalid"):
                    flag = False
                    break
        if flag is True:
            msg_box = QMessageBox()
            msg_box.setText("Congratulations! 🎉 \n You solved the Sudoku! 🏆")
            msg_box.exec()

    def highlight_cells(self, row, col):
        for i in range(9):
            for j in range(9):
                cell = self.line_edits[i][j]
                if cell.property("invalid"):
                    continue
                bg_color = "#5d4037"
                # اگر در همان سطر، ستون یا بلوک باشد
                if i == row or j == col or (i//3 == row//3 and j//3 == col//3):
                    bg_color = "#7a6257"
                        
                # بازگشت استایل قبلی + تغییر رنگ
                style = f"""
                    QLineEdit {{
                        background-color: {bg_color};
                        color: white;
                        border: 2px solid #3e2723;
                        border-radius: 8px;
                        font-size: 20px;
                        qproperty-alignment: 'AlignCenter';
                    """
                # مرزبندی بلوک‌ها
                if j % 3 == 0:
                    style += "border-left: 3px solid black;"
                if i % 3 == 0:
                    style += "border-top: 3px solid black;"
                if j == 8:
                    style += "border-right: 3px solid black;"
                if i == 8:
                    style += "border-bottom: 3px solid black;"
                style += "}"
                cell.setStyleSheet(style)

app = QApplication(sys.argv)
win = Mainwindow()
win.show()
app.exec()


