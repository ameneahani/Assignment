# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(503, 318)
        MainWindow.setStyleSheet(u"QLineEdit {\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"border-radius: 20px;\n"
"background-color: #73C2FB;\n"
"color: black;\n"
"border: 2px solid rgba(0, 0, 0, 60);\n"
"padding: 15px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_guess = QLineEdit(self.centralwidget)
        self.txt_guess.setObjectName(u"txt_guess")
        self.txt_guess.setGeometry(QRect(130, 200, 141, 51))
        self.txt_guess.setStyleSheet(u"QLineEdit {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: #73C2FB;\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")
        self.btn_guess = QPushButton(self.centralwidget)
        self.btn_guess.setObjectName(u"btn_guess")
        self.btn_guess.setGeometry(QRect(280, 200, 81, 51))
        self.btn_guess.setStyleSheet(u"QPushButton {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                      stop:0 #FFFF00, stop:0.5 white);\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")
        self.lbl_instruction = QLabel(self.centralwidget)
        self.lbl_instruction.setObjectName(u"lbl_instruction")
        self.lbl_instruction.setGeometry(QRect(30, 140, 431, 51))
        self.lbl_instruction.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color:#FFFFE0 ;\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 60);\n"
"    padding: 15px;\n"
"}")
        self.lbl_title = QLabel(self.centralwidget)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setGeometry(QRect(90, 10, 321, 51))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet(u"color:#73C2FB;")
        self.btn_restart = QPushButton(self.centralwidget)
        self.btn_restart.setObjectName(u"btn_restart")
        self.btn_restart.setGeometry(QRect(310, 80, 121, 51))
        self.btn_restart.setStyleSheet(u"QPushButton {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                      stop:0 #73C2FB, stop:1 white);\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")
        self.txt_min_num = QLineEdit(self.centralwidget)
        self.txt_min_num.setObjectName(u"txt_min_num")
        self.txt_min_num.setGeometry(QRect(60, 80, 111, 51))
        self.txt_min_num.setStyleSheet(u"QLineEdit {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: #73C2FB;\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")
        self.txt_max_num = QLineEdit(self.centralwidget)
        self.txt_max_num.setObjectName(u"txt_max_num")
        self.txt_max_num.setGeometry(QRect(180, 80, 121, 51))
        self.txt_max_num.setStyleSheet(u"QLineEdit {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: #73C2FB;\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 503, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_guess.setText(QCoreApplication.translate("MainWindow", u"Guess", None))
        self.lbl_instruction.setText("")
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"Guess Number Game", None))
        self.btn_restart.setText(QCoreApplication.translate("MainWindow", u"New Target", None))
        self.txt_min_num.setText(QCoreApplication.translate("MainWindow", u"         1", None))
        self.txt_max_num.setText(QCoreApplication.translate("MainWindow", u"      100", None))
    # retranslateUi

