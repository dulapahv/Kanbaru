# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 678)
        MainWindow.setStyleSheet(u"background-color: #454c5a;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.widget1 = QWidget(self.widget_4)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"background-color: #ebecf0;\n"
"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 0, 30, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(36)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: #282c33;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.widget_2 = QWidget(self.widget1)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #282c33;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(12)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #000000; border-radius: 5px; background-color: #ffffff; padding: 0px 8px 0px 8px}")
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #000000; border-radius: 5px; background-color: #ffffff; padding: 0px 8px 0px 8px}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: #d63a3e;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(120, 30))
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {background-color: #5dac48; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #64bd53;}")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.line_2 = QFrame(self.widget1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: #9096a6;")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_2)

        self.widget_3 = QWidget(self.widget1)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #282c33;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #000000; border-radius: 5px; background-color: #ffffff; padding: 0px 8px 0px 8px}")
        self.lineEdit_4.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #000000; border-radius: 5px; background-color: #ffffff; padding: 0px 8px 0px 8px}")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_3)

        self.lineEdit_5 = QLineEdit(self.widget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 40))
        self.lineEdit_5.setFont(font2)
        self.lineEdit_5.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #000000; border-radius: 5px; background-color: #ffffff; padding: 0px 8px 0px 8px}")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.lineEdit_5.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_5)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: #d63a3e;")

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_5 = QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(120, 30))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton {background-color: #5dac48; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #64bd53;}")

        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalSpacer_5 = QSpacerItem(300, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addWidget(self.widget1)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kanbaru", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Log in to Kanbaru", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Incorrect username/password", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sign up for an account", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Incorrect username/password", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
    # retranslateUi

