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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(486, 443)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(66)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(80, -1, 96, -1)
        self.lbl_lang_1 = QLabel(self.widget)
        self.lbl_lang_1.setObjectName(u"lbl_lang_1")
        font = QFont()
        font.setPointSize(11)
        self.lbl_lang_1.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_lang_1)

        self.btn_change_lang = QPushButton(self.widget)
        self.btn_change_lang.setObjectName(u"btn_change_lang")
        font1 = QFont()
        font1.setPointSize(18)
        self.btn_change_lang.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_change_lang)

        self.lbl_lang_2 = QLabel(self.widget)
        self.lbl_lang_2.setObjectName(u"lbl_lang_2")
        self.lbl_lang_2.setFont(font)
        self.lbl_lang_2.setMidLineWidth(0)

        self.horizontalLayout.addWidget(self.lbl_lang_2)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.text_input = QTextEdit(self.widget_2)
        self.text_input.setObjectName(u"text_input")
        self.text_input.setGeometry(QRect(5, 0, 222, 210))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_input.sizePolicy().hasHeightForWidth())
        self.text_input.setSizePolicy(sizePolicy)
        self.text_result = QLabel(self.widget_2)
        self.text_result.setObjectName(u"text_result")
        self.text_result.setGeometry(QRect(242, 0, 220, 210))
        sizePolicy.setHeightForWidth(self.text_result.sizePolicy().hasHeightForWidth())
        self.text_result.setSizePolicy(sizePolicy)
        self.text_result.setStyleSheet(u"background-color: white;")

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.btn_translate = QPushButton(self.widget_3)
        self.btn_translate.setObjectName(u"btn_translate")
        self.btn_translate.setGeometry(QRect(160, 40, 153, 24))

        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 486, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_lang_1.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.btn_change_lang.setText(QCoreApplication.translate("MainWindow", u"\u21c4", None))
        self.lbl_lang_2.setText(QCoreApplication.translate("MainWindow", u"persian", None))
        self.text_result.setText("")
        self.btn_translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
    # retranslateUi

