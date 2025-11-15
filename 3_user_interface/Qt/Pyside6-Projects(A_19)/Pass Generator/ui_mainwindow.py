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
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 333)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#73C2FB;")

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(19)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(60, -1, 31, -1)
        self.lbl_standard = QLabel(self.widget)
        self.lbl_standard.setObjectName(u"lbl_standard")
        self.lbl_standard.setStyleSheet(u"QLabel {\n"
"    font-size: 12px;\n"
"    border-radius: 20px;\n"
"    background-color: #73C2FB;\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")

        self.horizontalLayout.addWidget(self.lbl_standard)

        self.btn_standard = QPushButton(self.widget)
        self.btn_standard.setObjectName(u"btn_standard")
        self.btn_standard.setStyleSheet(u"QPushButton {\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                      stop:0 #73C2FB, stop:1 white);\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_standard)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(60, -1, 31, -1)
        self.lbl_strong_pass = QLabel(self.widget_2)
        self.lbl_strong_pass.setObjectName(u"lbl_strong_pass")
        self.lbl_strong_pass.setStyleSheet(u"QLabel {\n"
"    font-size: 12px;\n"
"\n"
"    border-radius: 20px;\n"
"    background-color: #73C2FB;\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lbl_strong_pass)

        self.btn_strong_pass = QPushButton(self.widget_2)
        self.btn_strong_pass.setObjectName(u"btn_strong_pass")
        self.btn_strong_pass.setStyleSheet(u"QPushButton {\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                      stop:0 #73C2FB, stop:1 white);\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_strong_pass)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(34)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(60, -1, 31, -1)
        self.lbl_super_pass = QLabel(self.widget_3)
        self.lbl_super_pass.setObjectName(u"lbl_super_pass")
        self.lbl_super_pass.setStyleSheet(u"QLabel {\n"
"    font-size: 12px;\n"
"\n"
"    border-radius: 20px;\n"
"    background-color: #73C2FB;\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lbl_super_pass)

        self.btn_super_pass = QPushButton(self.widget_3)
        self.btn_super_pass.setObjectName(u"btn_super_pass")
        self.btn_super_pass.setStyleSheet(u"QPushButton {\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                      stop:0 #73C2FB, stop:1 white);\n"
"    color: black;\n"
"    border: 2px solid rgba(0, 0, 0, 100);\n"
"    padding: 15px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_super_pass)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 442, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"         Password Generator", None))
        self.lbl_standard.setText("")
        self.btn_standard.setText(QCoreApplication.translate("MainWindow", u"Standard strenth password", None))
        self.lbl_strong_pass.setText("")
        self.btn_strong_pass.setText(QCoreApplication.translate("MainWindow", u"Extra Strong Password", None))
        self.lbl_super_pass.setText("")
        self.btn_super_pass.setText(QCoreApplication.translate("MainWindow", u"Super Strong Password", None))
    # retranslateUi

