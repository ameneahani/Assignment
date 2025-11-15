# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(506, 492)
        self.menu_open_file = QAction(MainWindow)
        self.menu_open_file.setObjectName(u"menu_open_file")
        self.menu_About = QAction(MainWindow)
        self.menu_About.setObjectName(u"menu_About")
        self.menu_Help = QAction(MainWindow)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menu_Exit = QAction(MainWindow)
        self.menu_Exit.setObjectName(u"menu_Exit")
        self.menu_new_puzzle = QAction(MainWindow)
        self.menu_new_puzzle.setObjectName(u"menu_new_puzzle")
        self.menu_solve_puzzle = QAction(MainWindow)
        self.menu_solve_puzzle.setObjectName(u"menu_solve_puzzle")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 481, 441))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 506, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menunew = QMenu(self.menuGame)
        self.menunew.setObjectName(u"menunew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menuGame.addAction(self.menunew.menuAction())
        self.menuGame.addAction(self.menu_open_file)
        self.menuGame.addAction(self.menu_About)
        self.menuGame.addAction(self.menu_Help)
        self.menuGame.addAction(self.menu_Exit)
        self.menunew.addAction(self.menu_new_puzzle)
        self.menunew.addAction(self.menu_solve_puzzle)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_open_file.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.menu_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_Help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_new_puzzle.setText(QCoreApplication.translate("MainWindow", u"New Puzzle", None))
        self.menu_solve_puzzle.setText(QCoreApplication.translate("MainWindow", u"Solve Puzzle", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menunew.setTitle(QCoreApplication.translate("MainWindow", u"New...", None))
    # retranslateUi

