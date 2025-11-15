import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main_window.ui")
class Tic_Toc_Toe:
    def __init__(self):
        self.game_mode = ["tow_player", "vs_cpu"]
        self.flag_win = False
        self.player = 1
        self.player_sign = ["X","O"]
        self.player1_score = 0
        self.player2_score = 0
        self.tie = 0
        self.buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
                        [main_window.btn_4, main_window.btn_5, main_window.btn_6],
                        [main_window.btn_7, main_window.btn_8, main_window.btn_9]]
        self.tow_player()
        main_window.new_game.clicked.connect(self.new_game)
        main_window.about.clicked.connect(self.about)

    def make_move(self, i, j):
        style_x = "font-size: 40pt; font-weight: bold; color: #40E0D0;"
        style_o = "font-size: 40pt; font-weight: bold; color: orange;"
        if self.player == 1 and self.buttons[i][j].text() == '':
            self.buttons[i][j].setText(self.player_sign[0])
            self.buttons[i][j].setStyleSheet(style_x)
            self.player = 2
            if main_window.vs_cpu.isChecked() and self.flag_win == False:
                self.play_vs_cpu()
        elif self.player == 2 and self.buttons[i][j].text() == '':
            self.buttons[i][j].setText(self.player_sign[1])
            self.buttons[i][j].setStyleSheet(style_o)
            self.player = 1
        
        self.check_game()

    def tow_player(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(partial(self.make_move,i,j))
    
    def win(self, player):
        self.flag_win = True
        if player == "player 1":
            self.player1_score += 1
            main_window.player1_score.setText(f"you :\n {self.player1_score}")
        elif player == "player 2":
            self.player2_score += 1
            main_window.cpu.setText(f"player2 :\n {self.player2_score}")
        msg_box = QMessageBox( text=f"🎉 Congratulations, {player}! You win! 🎉")
        msg_box.exec()
        self.reset_game()

    def reset_game(self):
        self.player = 1
        self.flag_win = False
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText('')
        return
    def new_game(self):
        self.reset_game()
        self.player1_score = 0
        self.player2_score = 0
        self.tie = 0
        main_window.player1_score.setText(f"You(X) :\n {self.player1_score}")
        main_window.cpu.setText(f"Player2(O) :\n {self.player2_score}")
        main_window.tie.setText(f" Ties : \n {self.tie}")

    def about(self):
        msg_box = QMessageBox.about(main_window, "About" ,
                    "✨ Tic Tac Toe ✨\n\n"
                    "Developed by [Amene Ahani]\n"
                    "Version: 1.0\n"
                    "Play against your friend or CPU and have fun! 🎉" )
                
    def play_vs_cpu(self):
        empty_cells = [(i,j) for i in range(3) for j in range(3) if self.buttons[i][j].text() == ""]
        if empty_cells:
            rand_i , rand_j = random.choice(empty_cells)
            self.make_move(rand_i, rand_j)

    def check_game(self):
        for sign in self.player_sign:
            if sign == "X":
                player = "player 1"
            else:
                player = "player 2"
            for i in range(3):
                if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() == sign:
                    self.win(player)
                    return
                elif self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() == sign:
                    self.win(player)
                    return
            if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() == sign:
                    self.win(player)
                    return
            elif self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() == sign:
                    self.win(player)
                    return
        all_filled = True
        for i in range (3):# check for equal mod
            for button in self.buttons[i]: 
                if  button.text() == "":
                    all_filled = False
                    break
        if all_filled and self.flag_win == False:
            msg_box = QMessageBox( text="😅 It's a draw! Nobody wins.")
            self.tie += 1
            main_window.tie.setText(f" Ties : \n {self.tie}")
            msg_box.exec()
            self.reset_game()

game = Tic_Toc_Toe()
main_window.show()
app.exec()


