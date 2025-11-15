# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTimeEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 361)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 0, 391, 291))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lbl_worldclock = QLabel(self.tab)
        self.lbl_worldclock.setObjectName(u"lbl_worldclock")
        self.lbl_worldclock.setGeometry(QRect(170, 75, 151, 51))
        font = QFont()
        font.setFamilies([u"Seven Segment"])
        font.setPointSize(14)
        self.lbl_worldclock.setFont(font)
        self.cb_worldclock = QComboBox(self.tab)
        self.cb_worldclock.addItem("")
        self.cb_worldclock.setObjectName(u"cb_worldclock")
        self.cb_worldclock.setGeometry(QRect(60, 80, 81, 34))
        font1 = QFont()
        font1.setPointSize(14)
        self.cb_worldclock.setFont(font1)
        self.cb_worldclock.setEditable(False)
        self.cb_worldclock.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.btn_add_alarm = QPushButton(self.tab_3)
        self.btn_add_alarm.setObjectName(u"btn_add_alarm")
        self.btn_add_alarm.setGeometry(QRect(290, 40, 51, 41))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Text Semibold"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.btn_add_alarm.setFont(font2)
        self.timeedit_alarm = QTimeEdit(self.tab_3)
        self.timeedit_alarm.setObjectName(u"timeedit_alarm")
        self.timeedit_alarm.setGeometry(QRect(40, 40, 201, 41))
        self.timeedit_alarm.setFont(font)
        self.widget_alarm_area = QWidget(self.tab_3)
        self.widget_alarm_area.setObjectName(u"widget_alarm_area")
        self.widget_alarm_area.setGeometry(QRect(0, 90, 391, 171))
        self.gridLayout = QGridLayout(self.widget_alarm_area)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gl_alarm = QGridLayout()
        self.gl_alarm.setObjectName(u"gl_alarm")

        self.gridLayout.addLayout(self.gl_alarm, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lbl_stopwatch = QLineEdit(self.tab_4)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(130, 50, 141, 51))
        font3 = QFont()
        font3.setFamilies([u"Seven Segment"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setKerning(True)
        self.lbl_stopwatch.setFont(font3)
        self.lbl_stopwatch.setStyleSheet(u"color:rgb(255, 85, 0)")
        self.lbl_stopwatch.setFrame(True)
        self.lbl_stopwatch.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lbl_stopwatch.setCursorPosition(5)
        self.lbl_stopwatch.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_stopwatch.setDragEnabled(False)
        self.lbl_stopwatch.setReadOnly(True)
        self.btn_start_stopwatch = QPushButton(self.tab_4)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(80, 140, 75, 24))
        self.btn_stop_stopwatch = QPushButton(self.tab_4)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(160, 140, 75, 24))
        self.btn_reset_stopwatch = QPushButton(self.tab_4)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(240, 140, 75, 24))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.btn_start_timer = QPushButton(self.tab_2)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(70, 150, 75, 24))
        self.btn_stop_timer = QPushButton(self.tab_2)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(154, 150, 75, 24))
        self.tb_hour_timer = QLineEdit(self.tab_2)
        self.tb_hour_timer.setObjectName(u"tb_hour_timer")
        self.tb_hour_timer.setGeometry(QRect(100, 60, 51, 51))
        font4 = QFont()
        font4.setFamilies([u"Seven Segment"])
        font4.setPointSize(20)
        self.tb_hour_timer.setFont(font4)
        self.tb_hour_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb_second_timer = QLineEdit(self.tab_2)
        self.tb_second_timer.setObjectName(u"tb_second_timer")
        self.tb_second_timer.setGeometry(QRect(220, 60, 51, 51))
        self.tb_second_timer.setFont(font4)
        self.tb_second_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb_minute_timer = QLineEdit(self.tab_2)
        self.tb_minute_timer.setObjectName(u"tb_minute_timer")
        self.tb_minute_timer.setGeometry(QRect(160, 60, 51, 51))
        self.tb_minute_timer.setFont(font4)
        self.tb_minute_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_reset_timer = QPushButton(self.tab_2)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(240, 150, 75, 24))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 538, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_worldclock.setText("")
        self.cb_worldclock.setItemText(0, "")

        self.cb_worldclock.setCurrentText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Word Clock", None))
        self.btn_add_alarm.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tb_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tb_second_timer.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.tb_minute_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

