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
        self.widget1.setStyleSheet(u"background-color: #f4f5f7;\n"
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
        self.label_8.setWordWrap(True)

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
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_login_username = QLineEdit(self.widget_2)
        self.lineEdit_login_username.setObjectName(u"lineEdit_login_username")
        self.lineEdit_login_username.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(12)
        self.lineEdit_login_username.setFont(font2)
        self.lineEdit_login_username.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #282c33; border-radius: 5px; background-color: #ffffff; padding: 0px 0px 0px 8px}\n"
"QLineEdit:focus {border-color: #6badee;}")
        self.lineEdit_login_username.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.lineEdit_login_username)

        self.lineEdit_2_login_passwd = QLineEdit(self.widget_2)
        self.lineEdit_2_login_passwd.setObjectName(u"lineEdit_2_login_passwd")
        self.lineEdit_2_login_passwd.setMinimumSize(QSize(0, 40))
        self.lineEdit_2_login_passwd.setFont(font2)
        self.lineEdit_2_login_passwd.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #282c33; border-radius: 5px; background-color: #ffffff; padding: 0px 0px 0px 8px}\n"
"QLineEdit:focus {border-color: #6badee;}")
        self.lineEdit_2_login_passwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_2_login_passwd.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.lineEdit_2_login_passwd)

        self.label_login_msg = QLabel(self.widget_2)
        self.label_login_msg.setObjectName(u"label_login_msg")
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_login_msg.setFont(font3)
        self.label_login_msg.setStyleSheet(u"color: #d63a3e;")
        self.label_login_msg.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_login_msg)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_login = QPushButton(self.widget_2)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(120, 30))
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.btn_login.setFont(font4)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {background-color: #5dac48; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #64bd53;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_login)


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
        self.label_3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_3)

        self.lineEdit_sign_up_username = QLineEdit(self.widget_3)
        self.lineEdit_sign_up_username.setObjectName(u"lineEdit_sign_up_username")
        self.lineEdit_sign_up_username.setMinimumSize(QSize(0, 40))
        self.lineEdit_sign_up_username.setFont(font2)
        self.lineEdit_sign_up_username.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #282c33; border-radius: 5px; background-color: #ffffff; padding: 0px 0px 0px 8px}\n"
"QLineEdit:focus {border-color: #6badee;}")
        self.lineEdit_sign_up_username.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_sign_up_username)

        self.lineEdit_sign_up_passwd = QLineEdit(self.widget_3)
        self.lineEdit_sign_up_passwd.setObjectName(u"lineEdit_sign_up_passwd")
        self.lineEdit_sign_up_passwd.setMinimumSize(QSize(0, 40))
        self.lineEdit_sign_up_passwd.setFont(font2)
        self.lineEdit_sign_up_passwd.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #282c33; border-radius: 5px; background-color: #ffffff; padding: 0px 0px 0px 8px}\n"
"QLineEdit:focus {border-color: #6badee;}")
        self.lineEdit_sign_up_passwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_sign_up_passwd.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_sign_up_passwd)

        self.lineEdit_sign_up_con_passwd = QLineEdit(self.widget_3)
        self.lineEdit_sign_up_con_passwd.setObjectName(u"lineEdit_sign_up_con_passwd")
        self.lineEdit_sign_up_con_passwd.setMinimumSize(QSize(0, 40))
        self.lineEdit_sign_up_con_passwd.setFont(font2)
        self.lineEdit_sign_up_con_passwd.setStyleSheet(u"QLineEdit {border-color: #dfe1e6; border-width: 1.5px; border-style: solid; color: #282c33; border-radius: 5px; background-color: #ffffff; padding: 0px 0px 0px 8px}\n"
"QLineEdit:focus {border-color: #6badee;}")
        self.lineEdit_sign_up_con_passwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_sign_up_con_passwd.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_sign_up_con_passwd)

        self.label_sign_up_msg = QLabel(self.widget_3)
        self.label_sign_up_msg.setObjectName(u"label_sign_up_msg")
        self.label_sign_up_msg.setFont(font3)
        self.label_sign_up_msg.setStyleSheet(u"color: #d63a3e;")
        self.label_sign_up_msg.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_sign_up_msg)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_sign_up = QPushButton(self.widget_3)
        self.btn_sign_up.setObjectName(u"btn_sign_up")
        sizePolicy.setHeightForWidth(self.btn_sign_up.sizePolicy().hasHeightForWidth())
        self.btn_sign_up.setSizePolicy(sizePolicy)
        self.btn_sign_up.setMinimumSize(QSize(120, 30))
        self.btn_sign_up.setFont(font4)
        self.btn_sign_up.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sign_up.setStyleSheet(u"QPushButton {background-color: #5dac48; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #64bd53;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_4.addWidget(self.btn_sign_up)


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
        self.lineEdit_login_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2_login_passwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_login_msg.setText(QCoreApplication.translate("MainWindow", u"Incorrect username/password", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sign up for an account", None))
        self.lineEdit_sign_up_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_sign_up_passwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_sign_up_con_passwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.label_sign_up_msg.setText(QCoreApplication.translate("MainWindow", u"Incorrect username/password", None))
        self.btn_sign_up.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
    # retranslateUi

