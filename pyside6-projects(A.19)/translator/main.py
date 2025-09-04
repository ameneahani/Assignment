import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.f = open("database.txt")
        self.words = self.f.read().split("\n")
        self.f.close()
        self.word_bank = []
        for i in range(0,len(self.words),2):
                word = {"eng":self.words[i], "fa":self.words[i+1]}
                self.word_bank.append(word)
        self.ui.btn_translate.clicked.connect(self.translate)
        self.ui.btn_change_lang.clicked.connect(self.change_lang)

    def translate(self):
        translated_text = []
        
        input_words = (self.ui.text_input.toPlainText()).split(" ")
        if self.ui.lbl_lang_1.text() == "English":
            for word in input_words:
                for w in self.word_bank:
                    if word == w['eng']:
                        res_word = w['fa']
                        break
                else:
                    res_word = word
                translated_text.append(res_word)
        elif self.ui.lbl_lang_1.text() == "Persian":
            for word in input_words:
                for w in self.word_bank:
                    if word == w['fa']:
                        res_word = w['eng']
                        break
                else:
                    res_word = word
                translated_text.append(res_word)
        
        
        self.ui.text_result.setText(" ".join (translated_text))
        

    def change_lang(self):
        if self.ui.lbl_lang_1.text() == "English":
            self.ui.lbl_lang_1.setText("Persian")
            self.ui.lbl_lang_2.setText("English")
        else:
            self.ui.lbl_lang_1.setText("English")
            self.ui.lbl_lang_2.setText("Persian")
            print(self.ui.lbl_lang_1.text())

            

                  

        




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
