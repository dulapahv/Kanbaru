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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 678)
        icon = QIcon()
        icon.addFile(u":/img/resources/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #454c5a;\n"
"color: rgb(255, 255, 255);\n"
"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #5487bb;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")
        MainWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.panel_left = QWidget(self.widget)
        self.panel_left.setObjectName(u"panel_left")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panel_left.sizePolicy().hasHeightForWidth())
        self.panel_left.setSizePolicy(sizePolicy)
        self.panel_left.setMinimumSize(QSize(160, 0))
        self.panel_left.setMaximumSize(QSize(160, 16777215))
        self.panel_left.setStyleSheet(u"background-color: #282c34;")
        self.verticalLayout_2 = QVBoxLayout(self.panel_left)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 0, 8, 8)
        self.label_logo = QLabel(self.panel_left)
        self.label_logo.setObjectName(u"label_logo")
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(36)
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet(u"background-color: #282c34;\n"
"color: #FFFFFF;")
        self.label_logo.setMargin(10)
        self.label_logo.setIndent(8)

        self.verticalLayout_2.addWidget(self.label_logo)

        self.scrollArea_panel_left = QScrollArea(self.panel_left)
        self.scrollArea_panel_left.setObjectName(u"scrollArea_panel_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_panel_left.sizePolicy().hasHeightForWidth())
        self.scrollArea_panel_left.setSizePolicy(sizePolicy1)
        self.scrollArea_panel_left.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: #282c34;\n"
"	width: 10px;\n"
"	margin: 1px 0 0 5px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #454c5a;\n"
"	min-height: 30px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #343a44;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"	background-color: #323741;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar QMenu {\n"
"	background-color: #454c5a;\n"
"	border: none;\n"
"	padding: 5px;\n"
"	margin: 0px;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QScrollBar QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"}\n"
"\n"
"QScrollBar QMenu::item:sel"
                        "ected {\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}")
        self.scrollArea_panel_left.setFrameShape(QFrame.NoFrame)
        self.scrollArea_panel_left.setWidgetResizable(True)
        self.scrollAreaContent_panel_left = QWidget()
        self.scrollAreaContent_panel_left.setObjectName(u"scrollAreaContent_panel_left")
        self.scrollAreaContent_panel_left.setGeometry(QRect(0, 0, 144, 417))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaContent_panel_left)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.scrollArea_panel_left.setWidget(self.scrollAreaContent_panel_left)

        self.verticalLayout_2.addWidget(self.scrollArea_panel_left)

        self.btn_add_board = QPushButton(self.panel_left)
        self.btn_add_board.setObjectName(u"btn_add_board")
        self.btn_add_board.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(12)
        self.btn_add_board.setFont(font1)
        self.btn_add_board.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_board.setFocusPolicy(Qt.TabFocus)
        self.btn_add_board.setStyleSheet(u"QPushButton {\n"
"	background-color: #acb2bf;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7e828c;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/img/resources/img/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_board.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.btn_add_board)

        self.btn_board_settings = QPushButton(self.panel_left)
        self.btn_board_settings.setObjectName(u"btn_board_settings")
        self.btn_board_settings.setMinimumSize(QSize(0, 30))
        self.btn_board_settings.setFont(font1)
        self.btn_board_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_settings.setFocusPolicy(Qt.TabFocus)
        self.btn_board_settings.setStyleSheet(u"QPushButton {\n"
"	background-color: #7f8ca6;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #576073;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/img/resources/img/settings_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_board_settings.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.btn_board_settings)

        self.btn_app_settings = QPushButton(self.panel_left)
        self.btn_app_settings.setObjectName(u"btn_app_settings")
        self.btn_app_settings.setMinimumSize(QSize(0, 30))
        self.btn_app_settings.setFont(font1)
        self.btn_app_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_app_settings.setFocusPolicy(Qt.TabFocus)
        self.btn_app_settings.setStyleSheet(u"QPushButton {\n"
"	background-color: #7f8ca6;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #576073;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/img/resources/img/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_app_settings.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.btn_app_settings)


        self.horizontalLayout_4.addWidget(self.panel_left)

        self.panel_right = QVBoxLayout()
        self.panel_right.setObjectName(u"panel_right")
        self.horzLayout_panel_right = QHBoxLayout()
        self.horzLayout_panel_right.setSpacing(0)
        self.horzLayout_panel_right.setObjectName(u"horzLayout_panel_right")
        self.label_board = QLabel(self.widget)
        self.label_board.setObjectName(u"label_board")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_board.sizePolicy().hasHeightForWidth())
        self.label_board.setSizePolicy(sizePolicy2)
        self.label_board.setMinimumSize(QSize(0, 70))
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(28)
        self.label_board.setFont(font2)
        self.label_board.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(107, 173, 238, 255), stop:1 rgba(69, 76, 90, 255));\n"
"color: #FFFFFF;")
        self.label_board.setMargin(10)

        self.horzLayout_panel_right.addWidget(self.label_board)


        self.panel_right.addLayout(self.horzLayout_panel_right)

        self.widget_panel_right = QWidget(self.widget)
        self.widget_panel_right.setObjectName(u"widget_panel_right")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_panel_right.sizePolicy().hasHeightForWidth())
        self.widget_panel_right.setSizePolicy(sizePolicy3)
        self.widget_panel_right.setMinimumSize(QSize(280, 500))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_panel_right)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.scrollArea_panel_right = QScrollArea(self.widget_panel_right)
        self.scrollArea_panel_right.setObjectName(u"scrollArea_panel_right")
        self.scrollArea_panel_right.setStyleSheet(u"QScrollBar:vertical {\n"
"	width: 10px;\n"
"	margin: 0 0 0 0;\n"
"	background-color: #acb2bf\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #454c5a;\n"
"	height: 10px;\n"
"	margin: 0 0 0 1px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: #76829b;\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #646e83;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"	background-color: #576072;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	height: 0;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar QMenu {\n"
"	background-color: #454c5a;\n"
"	border: none;\n"
"	padding: 5px;\n"
"	margin: 0px;\n"
"	font"
                        "-size: 13px;\n"
"}\n"
"\n"
"QScrollBar QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"}\n"
"\n"
"QScrollBar QMenu::item:selected {\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"}\n"
"")
        self.scrollArea_panel_right.setFrameShape(QFrame.NoFrame)
        self.scrollArea_panel_right.setWidgetResizable(True)
        self.scrollAreaContent_panel_right = QWidget()
        self.scrollAreaContent_panel_right.setObjectName(u"scrollAreaContent_panel_right")
        self.scrollAreaContent_panel_right.setGeometry(QRect(0, 0, 862, 589))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaContent_panel_right)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 0, 0, 8)
        self.scrollArea_panel_right.setWidget(self.scrollAreaContent_panel_right)

        self.horizontalLayout_2.addWidget(self.scrollArea_panel_right)


        self.panel_right.addWidget(self.widget_panel_right)


        self.horizontalLayout_4.addLayout(self.panel_right)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.scrollArea_panel_left, self.btn_add_board)
        QWidget.setTabOrder(self.btn_add_board, self.btn_board_settings)
        QWidget.setTabOrder(self.btn_board_settings, self.btn_app_settings)
        QWidget.setTabOrder(self.btn_app_settings, self.scrollArea_panel_right)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kanbaru", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"Kan\n"
"baru", None))
        self.btn_add_board.setText(QCoreApplication.translate("MainWindow", u" Add a board", None))
        self.btn_board_settings.setText(QCoreApplication.translate("MainWindow", u"Manage Board", None))
        self.btn_app_settings.setText(QCoreApplication.translate("MainWindow", u" App Settings", None))
        self.label_board.setText("")
    # retranslateUi

