# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_description.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 615)
        MainWindow.setStyleSheet(u"background-color: #454c5a;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.35, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(107, 173, 238, 255), stop:1 rgba(69, 76, 90, 255));\n"
"color: #ffffff;")
        self.label_3.setMargin(10)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #ffffff")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(14)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"QLineEdit {background-color: #ebecf0; color: #000000; border-radius: 5px}")

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #ffffff")

        self.verticalLayout_4.addWidget(self.label_5)

        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        self.calendarWidget.setFont(font3)
        self.calendarWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.calendarWidget.setStyleSheet(u"background-color: rgb(107, 173, 238);")
        self.calendarWidget.setGridVisible(False)

        self.verticalLayout_4.addWidget(self.calendarWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #ffffff")

        self.verticalLayout_2.addWidget(self.label_4)

        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(16)
        self.timeEdit.setFont(font4)
        self.timeEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.timeEdit.setStyleSheet(u"QTimeEdit {background-color: #6badee; color: #ffffff; border-radius: 5px}")
        self.timeEdit.setTimeSpec(Qt.LocalTime)

        self.verticalLayout_2.addWidget(self.timeEdit)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: #ffffff")

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(120, 40))
        self.radioButton_2.setFont(font3)
        self.radioButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_2.setStyleSheet(u"background-color: #6badee;\n"
"color: #ffffff;\n"
"padding: 0px 5px 0px 5px;")

        self.verticalLayout_6.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(120, 40))
        self.radioButton_3.setFont(font3)
        self.radioButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_3.setStyleSheet(u"background-color: #fb568a;\n"
"color: #ffffff;\n"
"padding: 0px 5px 0px 5px;")

        self.verticalLayout_6.addWidget(self.radioButton_3)

        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setMinimumSize(QSize(120, 40))
        self.radioButton_5.setFont(font3)
        self.radioButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_5.setStyleSheet(u"background-color: #fbd945;\n"
"color: #ffffff;\n"
"padding: 0px 5px 0px 5px;")

        self.verticalLayout_6.addWidget(self.radioButton_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(120, 40))
        self.radioButton.setFont(font3)
        self.radioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton.setStyleSheet(u"background-color: #99c37b;\n"
"color: #ffffff;\n"
"padding: 0px 5px 0px 5px;")

        self.verticalLayout_5.addWidget(self.radioButton)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMinimumSize(QSize(120, 40))
        self.radioButton_4.setFont(font3)
        self.radioButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_4.setStyleSheet(u"background-color: #c577dc;\n"
"color: #ffffff;\n"
"padding: 0px 5px 0px 5px;")

        self.verticalLayout_5.addWidget(self.radioButton_4)

        self.radioButton_6 = QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setMinimumSize(QSize(120, 40))
        self.radioButton_6.setFont(font3)
        self.radioButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_6.setStyleSheet(u"background-color: #5eb5c1;\n"
"color: #ffffff;\n"
"padding: 0px 5px 0px 5px;")

        self.verticalLayout_5.addWidget(self.radioButton_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: #ffffff")

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(0, 20))
        self.horizontalSlider.setFont(font3)
        self.horizontalSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #ffffff")

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        font5 = QFont()
        font5.setFamilies([u"Torus Pro"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.textEdit.setFont(font5)
        self.textEdit.setStyleSheet(u"QTextEdit {background-color: #ebecf0; color: #000000; border-radius: 5px}")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(100, 50))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(100, 50))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #5487bb;}")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit, self.calendarWidget)
        QWidget.setTabOrder(self.calendarWidget, self.timeEdit)
        QWidget.setTabOrder(self.timeEdit, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Card Description", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Card Description", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Test Title", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Light blue", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Rose", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Gold", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Lavender", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Teal", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Progress (0%)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Torus Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Test Desc</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

