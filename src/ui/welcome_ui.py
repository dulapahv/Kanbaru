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
import resources_rc

class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        if not WelcomeWindow.objectName():
            WelcomeWindow.setObjectName(u"WelcomeWindow")
        WelcomeWindow.resize(1024, 678)
        icon = QIcon()
        icon.addFile(u":/img/resources/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        WelcomeWindow.setWindowIcon(icon)
        WelcomeWindow.setStyleSheet(u"background-color: #454c5a;")
        WelcomeWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(WelcomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-image: url(:/img/resources/img/bg.png);\n"
"background-position: left center;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background: none;")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.widget1 = QWidget(self.widget_4)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"background: none;\n"
"background-color: #f4f5f7;\n"
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

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(250, 50))
        self.label.setPixmap(QPixmap(u":/img/resources/img/kanbaru.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.widget_2 = QWidget(self.widget1)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_login = QLabel(self.widget_2)
        self.label_login.setObjectName(u"label_login")
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(13)
        font.setBold(True)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet(u"color: #282c33;")
        self.label_login.setAlignment(Qt.AlignCenter)
        self.label_login.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_login)

        self.lineEdit_login_username = QLineEdit(self.widget_2)
        self.lineEdit_login_username.setObjectName(u"lineEdit_login_username")
        self.lineEdit_login_username.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Manrope Medium"])
        font1.setPointSize(12)
        self.lineEdit_login_username.setFont(font1)
        self.lineEdit_login_username.setStyleSheet(u"QLineEdit {\n"
"	border-color: #dfe1e6;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"	color: #282c33;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	padding: 0 0 0 8px\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: #6badee;\n"
"}\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: #454c5a;\n"
"border: none;\n"
"padding: 5px;\n"
"margin: 0px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit QMenu::item:selected {\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}\n"
"")
        self.lineEdit_login_username.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.lineEdit_login_username)

        self.lineEdit_login_password = QLineEdit(self.widget_2)
        self.lineEdit_login_password.setObjectName(u"lineEdit_login_password")
        self.lineEdit_login_password.setMinimumSize(QSize(0, 40))
        self.lineEdit_login_password.setFont(font1)
        self.lineEdit_login_password.setStyleSheet(u"QLineEdit {\n"
"	border-color: #dfe1e6;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"	color: #282c33;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	padding: 0 0 0 8px\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: #6badee;\n"
"}\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: #454c5a;\n"
"border: none;\n"
"padding: 5px;\n"
"margin: 0px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit QMenu::item:selected {\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}\n"
"")
        self.lineEdit_login_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_login_password.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.lineEdit_login_password)

        self.label_login_msg = QLabel(self.widget_2)
        self.label_login_msg.setObjectName(u"label_login_msg")
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_login_msg.setFont(font2)
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
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.btn_login.setFont(font3)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setFocusPolicy(Qt.TabFocus)
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	background-color: #5dac48;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #64bd53;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")

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
        self.label_signup = QLabel(self.widget_3)
        self.label_signup.setObjectName(u"label_signup")
        self.label_signup.setFont(font)
        self.label_signup.setStyleSheet(u"color: #282c33;")
        self.label_signup.setAlignment(Qt.AlignCenter)
        self.label_signup.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_signup)

        self.lineEdit_signup_username = QLineEdit(self.widget_3)
        self.lineEdit_signup_username.setObjectName(u"lineEdit_signup_username")
        self.lineEdit_signup_username.setMinimumSize(QSize(0, 40))
        self.lineEdit_signup_username.setFont(font1)
        self.lineEdit_signup_username.setStyleSheet(u"QLineEdit {\n"
"	border-color: #dfe1e6;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"	color: #282c33;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	padding: 0 0 0 8px\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: #6badee;\n"
"}\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: #454c5a;\n"
"border: none;\n"
"padding: 5px;\n"
"margin: 0px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit QMenu::item:selected {\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}\n"
"")
        self.lineEdit_signup_username.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_signup_username)

        self.lineEdit_signup_password = QLineEdit(self.widget_3)
        self.lineEdit_signup_password.setObjectName(u"lineEdit_signup_password")
        self.lineEdit_signup_password.setMinimumSize(QSize(0, 40))
        self.lineEdit_signup_password.setFont(font1)
        self.lineEdit_signup_password.setStyleSheet(u"QLineEdit {\n"
"	border-color: #dfe1e6;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"	color: #282c33;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	padding: 0 0 0 8px\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: #6badee;\n"
"}\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: #454c5a;\n"
"border: none;\n"
"padding: 5px;\n"
"margin: 0px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit QMenu::item:selected {\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}\n"
"")
        self.lineEdit_signup_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_signup_password.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_signup_password)

        self.lineEdit_signup_confirm_password = QLineEdit(self.widget_3)
        self.lineEdit_signup_confirm_password.setObjectName(u"lineEdit_signup_confirm_password")
        self.lineEdit_signup_confirm_password.setMinimumSize(QSize(0, 40))
        self.lineEdit_signup_confirm_password.setFont(font1)
        self.lineEdit_signup_confirm_password.setStyleSheet(u"QLineEdit {\n"
"	border-color: #dfe1e6;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"	color: #282c33;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	padding: 0 0 0 8px\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-color: #6badee;\n"
"}\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: #454c5a;\n"
"border: none;\n"
"padding: 5px;\n"
"margin: 0px;\n"
"font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit QMenu::item:selected {\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}\n"
"")
        self.lineEdit_signup_confirm_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_signup_confirm_password.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_signup_confirm_password)

        self.label_signup_msg = QLabel(self.widget_3)
        self.label_signup_msg.setObjectName(u"label_signup_msg")
        self.label_signup_msg.setFont(font2)
        self.label_signup_msg.setStyleSheet(u"color: #d63a3e;")
        self.label_signup_msg.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_signup_msg)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_signup = QPushButton(self.widget_3)
        self.btn_signup.setObjectName(u"btn_signup")
        sizePolicy.setHeightForWidth(self.btn_signup.sizePolicy().hasHeightForWidth())
        self.btn_signup.setSizePolicy(sizePolicy)
        self.btn_signup.setMinimumSize(QSize(120, 30))
        self.btn_signup.setFont(font3)
        self.btn_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_signup.setFocusPolicy(Qt.TabFocus)
        self.btn_signup.setStyleSheet(u"QPushButton {\n"
"	background-color: #5dac48;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #64bd53;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_signup)


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

        WelcomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomeWindow)

        QMetaObject.connectSlotsByName(WelcomeWindow)
    # setupUi

    def retranslateUi(self, WelcomeWindow):
        WelcomeWindow.setWindowTitle(QCoreApplication.translate("WelcomeWindow", u"Kanbaru", None))
        self.label.setText("")
        self.label_login.setText(QCoreApplication.translate("WelcomeWindow", u"Log in to Kanbaru", None))
        self.lineEdit_login_username.setPlaceholderText(QCoreApplication.translate("WelcomeWindow", u"Username", None))
        self.lineEdit_login_password.setPlaceholderText(QCoreApplication.translate("WelcomeWindow", u"Password", None))
        self.label_login_msg.setText(QCoreApplication.translate("WelcomeWindow", u"Incorrect username/password", None))
        self.btn_login.setText(QCoreApplication.translate("WelcomeWindow", u"Login", None))
        self.label_signup.setText(QCoreApplication.translate("WelcomeWindow", u"Sign up for an account", None))
        self.lineEdit_signup_username.setPlaceholderText(QCoreApplication.translate("WelcomeWindow", u"Username", None))
        self.lineEdit_signup_password.setPlaceholderText(QCoreApplication.translate("WelcomeWindow", u"Password", None))
        self.lineEdit_signup_confirm_password.setPlaceholderText(QCoreApplication.translate("WelcomeWindow", u"Confirm password", None))
        self.label_signup_msg.setText(QCoreApplication.translate("WelcomeWindow", u"Incorrect username/password", None))
        self.btn_signup.setText(QCoreApplication.translate("WelcomeWindow", u"Sign up", None))
    # retranslateUi

