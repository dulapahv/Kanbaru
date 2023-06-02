# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_settings_bkp2.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(576, 678)
        icon = QIcon()
        icon.addFile(u":/img/resources/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingsWindow.setWindowIcon(icon)
        SettingsWindow.setStyleSheet(u"background-color: #454c5a;")
        SettingsWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_app_settings = QLabel(self.centralwidget)
        self.label_app_settings.setObjectName(u"label_app_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_app_settings.sizePolicy().hasHeightForWidth())
        self.label_app_settings.setSizePolicy(sizePolicy)
        self.label_app_settings.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(28)
        self.label_app_settings.setFont(font)
        self.label_app_settings.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(107, 173, 238, 255), stop:1 rgba(69, 76, 90, 255));\n"
"color: #ffffff;\n"
"padding: 0 0 0 10px;")
        self.label_app_settings.setMargin(10)

        self.verticalLayout_3.addWidget(self.label_app_settings)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setFocusPolicy(Qt.TabFocus)
        self.widget1.setStyleSheet(u"background-color: #f4f5f7;\n"
"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_manage_board = QLabel(self.widget1)
        self.label_manage_board.setObjectName(u"label_manage_board")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_manage_board.setFont(font1)
        self.label_manage_board.setStyleSheet(u"color: #282c33;")
        self.label_manage_board.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_manage_board)

        self.label_manage_board_desc = QLabel(self.widget1)
        self.label_manage_board_desc.setObjectName(u"label_manage_board_desc")
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(11)
        self.label_manage_board_desc.setFont(font2)
        self.label_manage_board_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_manage_board_desc)

        self.listWidget_manage_board = QListWidget(self.widget1)
        self.listWidget_manage_board.setObjectName(u"listWidget_manage_board")
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.listWidget_manage_board.setFont(font3)
        self.listWidget_manage_board.setFocusPolicy(Qt.TabFocus)
        self.listWidget_manage_board.setStyleSheet(u"QListWidget::item {\n"
"	height: 40px;\n"
"	padding: 0 8px 0 8px\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	background-color: #ffffff;\n"
"	color: #000000;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background-color: #e2e4e9;\n"
"	color: #000000\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background-color: #cccccc;\n"
"	color: #000000\n"
"}\n"
"\n"
"QListWidget::item:focus {\n"
"	background-color: #cccccc;\n"
"	color: #000000\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: #f4f5f7;\n"
"	width: 10px;\n"
"	margin: 1px 0 0 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #bfc0c5;\n"
"	min-height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #afb0b4;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"	background-color: #929497;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0"
                        ";\n"
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
"	background-color: #ebecf0;\n"
"	border: none;\n"
"	padding: 5px;\n"
"	margin: 0px;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QScrollBar QMenu::item {\n"
"	padding: 5px 13px 5px 13px;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QScrollBar QMenu::item:selected {\n"
"	border-radius: 5px;\n"
"	background-color: #acb2bf;\n"
"	color: #ffffff;\n"
"}\n"
"")
        self.listWidget_manage_board.setFrameShape(QFrame.NoFrame)
        self.listWidget_manage_board.setDragEnabled(True)
        self.listWidget_manage_board.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget_manage_board.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_manage_board.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_manage_board.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_manage_board.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_manage_board.setProperty("isWrapping", False)
        self.listWidget_manage_board.setSpacing(5)
        self.listWidget_manage_board.setUniformItemSizes(True)
        self.listWidget_manage_board.setWordWrap(True)
        self.listWidget_manage_board.setSelectionRectVisible(True)

        self.verticalLayout_2.addWidget(self.listWidget_manage_board)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_delete = QPushButton(self.widget1)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy1)
        self.btn_delete.setMinimumSize(QSize(150, 30))
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(12)
        self.btn_delete.setFont(font4)
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setFocusPolicy(Qt.TabFocus)
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
"	background-color: #d63a3e;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #9e2a2a;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_delete)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.line_1 = QFrame(self.widget1)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setStyleSheet(u"background-color: #9096a6;")
        self.line_1.setFrameShadow(QFrame.Plain)
        self.line_1.setLineWidth(0)
        self.line_1.setMidLineWidth(0)
        self.line_1.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_1)

        self.label_manage_account = QLabel(self.widget1)
        self.label_manage_account.setObjectName(u"label_manage_account")
        self.label_manage_account.setFont(font1)
        self.label_manage_account.setStyleSheet(u"color: #282c33;")
        self.label_manage_account.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_manage_account)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_logout = QPushButton(self.widget1)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(110, 30))
        self.btn_logout.setFont(font4)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setFocusPolicy(Qt.TabFocus)
        self.btn_logout.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u":/img/resources/img/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_logout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_delete_account = QPushButton(self.widget1)
        self.btn_delete_account.setObjectName(u"btn_delete_account")
        sizePolicy1.setHeightForWidth(self.btn_delete_account.sizePolicy().hasHeightForWidth())
        self.btn_delete_account.setSizePolicy(sizePolicy1)
        self.btn_delete_account.setMinimumSize(QSize(160, 30))
        self.btn_delete_account.setFont(font4)
        self.btn_delete_account.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_account.setFocusPolicy(Qt.TabFocus)
        self.btn_delete_account.setStyleSheet(u"QPushButton {\n"
"	border-color: #d63a3e;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"	color: #282c33;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #d63a3e;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"	background-color: #d63a3e;\n"
"	color: #ffffff;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/img/resources/img/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_account.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.btn_delete_account)

        self.line_2 = QFrame(self.widget1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: #9096a6;")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_about = QPushButton(self.widget1)
        self.btn_about.setObjectName(u"btn_about")
        sizePolicy1.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy1)
        self.btn_about.setMinimumSize(QSize(100, 30))
        self.btn_about.setFont(font4)
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_about.setFocusPolicy(Qt.TabFocus)
        self.btn_about.setStyleSheet(u"QPushButton {\n"
"	background-color: #6badee;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #5487bb;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_about)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.widget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)
        self.btn_cancel.setMinimumSize(QSize(100, 30))
        self.btn_cancel.setFont(font4)
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancel.setFocusPolicy(Qt.TabFocus)
        self.btn_cancel.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(self.widget1)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        self.btn_save.setMinimumSize(QSize(100, 30))
        self.btn_save.setFont(font4)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setFocusPolicy(Qt.TabFocus)
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"	background-color: #6badee;\n"
"	color: #ffffff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #5487bb;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border-color: #000000;\n"
"	border-width: 1.5px;\n"
"	border-style: solid;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.widget1)


        self.verticalLayout_3.addWidget(self.widget)

        SettingsWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.widget, self.listWidget_manage_board)
        QWidget.setTabOrder(self.listWidget_manage_board, self.btn_delete)
        QWidget.setTabOrder(self.btn_delete, self.btn_logout)
        QWidget.setTabOrder(self.btn_logout, self.btn_delete_account)
        QWidget.setTabOrder(self.btn_delete_account, self.btn_about)
        QWidget.setTabOrder(self.btn_about, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.btn_save)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"App Settings", None))
        self.label_app_settings.setText(QCoreApplication.translate("SettingsWindow", u"App Settings", None))
        self.label_manage_board.setText(QCoreApplication.translate("SettingsWindow", u"Manage Board", None))
        self.label_manage_board_desc.setText(QCoreApplication.translate("SettingsWindow", u"Drag to rearrange. Select and press Delete to delete.\n"
"You can select multiple boards at the same time.", None))
        self.btn_delete.setText(QCoreApplication.translate("SettingsWindow", u"Delete Board", None))
        self.label_manage_account.setText(QCoreApplication.translate("SettingsWindow", u"Manage Account", None))
        self.btn_logout.setText(QCoreApplication.translate("SettingsWindow", u"Logout", None))
        self.btn_delete_account.setText(QCoreApplication.translate("SettingsWindow", u"Delete Account", None))
        self.btn_about.setText(QCoreApplication.translate("SettingsWindow", u"About", None))
        self.btn_cancel.setText(QCoreApplication.translate("SettingsWindow", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("SettingsWindow", u"Save", None))
    # retranslateUi

