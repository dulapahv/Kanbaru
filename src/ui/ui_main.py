# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1042, 768)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #fde6d4;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1302, 749))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label_5.setFont(font1)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"background-color: rgb(231, 147, 147);")
        self.label_5.setMargin(12)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(20)
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy2)
        self.scrollArea_2.setMinimumSize(QSize(250, 0))
        self.scrollArea_2.setAcceptDrops(True)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 248, 624))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(242, 187, 187);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_3)

        self.scrollArea_4 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy2.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy2)
        self.scrollArea_4.setMinimumSize(QSize(250, 0))
        self.scrollArea_4.setAcceptDrops(True)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 248, 624))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_29 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(0, 50))
        self.pushButton_29.setFont(font3)
        self.pushButton_29.setStyleSheet(u"background-color: rgb(242, 187, 187);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.pushButton_29, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_3.addWidget(self.scrollArea_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2)

        self.scrollArea_3 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy2.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy2)
        self.scrollArea_3.setMinimumSize(QSize(250, 0))
        self.scrollArea_3.setAcceptDrops(True)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 248, 624))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 50))
        self.pushButton_19.setFont(font3)
        self.pushButton_19.setStyleSheet(u"background-color: rgb(242, 187, 187);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_19, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_4)

        self.scrollArea_5 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy2.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy2)
        self.scrollArea_5.setMinimumSize(QSize(250, 0))
        self.scrollArea_5.setAcceptDrops(True)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 248, 624))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_39 = QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(0, 50))
        self.pushButton_39.setFont(font3)
        self.pushButton_39.setStyleSheet(u"background-color: rgb(242, 187, 187);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.pushButton_39, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_4.addWidget(self.scrollArea_5)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_8)

        self.scrollArea_8 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        sizePolicy2.setHeightForWidth(self.scrollArea_8.sizePolicy().hasHeightForWidth())
        self.scrollArea_8.setSizePolicy(sizePolicy2)
        self.scrollArea_8.setMinimumSize(QSize(250, 0))
        self.scrollArea_8.setAcceptDrops(True)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 248, 622))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_42 = QPushButton(self.scrollAreaWidgetContents_8)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(0, 50))
        self.pushButton_42.setFont(font3)
        self.pushButton_42.setStyleSheet(u"background-color: rgb(242, 187, 187);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.pushButton_42, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_8.addWidget(self.scrollArea_8)


        self.horizontalLayout.addLayout(self.verticalLayout_8)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kanbaru", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kanbaru", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"To Do", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Doing", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.label_4.setText("")
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"+ Add another list", None))
        self.label_8.setText("")
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"+ Add another list", None))
    # retranslateUi

