# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_settings.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(576, 678)
        MainWindow.setStyleSheet(u"background-color: #454c5a;")
        self.centralwidget = QWidget(MainWindow)
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
"padding: 0px 0px 0px 10px;")
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
        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: #282c33;")
        self.label_8.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_manage_baoard_info = QLabel(self.widget1)
        self.label_manage_baoard_info.setObjectName(u"label_manage_baoard_info")
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(11)
        self.label_manage_baoard_info.setFont(font2)
        self.label_manage_baoard_info.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_manage_baoard_info)

        self.listWidget = QListWidget(self.widget1)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget.setObjectName(u"listWidget")
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.listWidget.setFont(font3)
        self.listWidget.setFocusPolicy(Qt.TabFocus)
        self.listWidget.setStyleSheet(u"QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
"QListWidget::item {background-color: #ffffff; color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: #e2e4e9; color: #000000}\n"
"QListWidget::item:selected {background-color: #cccccc; color: #000000}\n"
"QListWidget::item:focus {background-color: #cccccc; color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setSpacing(5)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(True)

        self.verticalLayout_2.addWidget(self.listWidget)

        self.btn_delete_board = QPushButton(self.widget1)
        self.btn_delete_board.setObjectName(u"btn_delete_board")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_delete_board.sizePolicy().hasHeightForWidth())
        self.btn_delete_board.setSizePolicy(sizePolicy1)
        self.btn_delete_board.setMinimumSize(QSize(150, 30))
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(12)
        self.btn_delete_board.setFont(font4)
        self.btn_delete_board.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_board.setFocusPolicy(Qt.TabFocus)
        self.btn_delete_board.setStyleSheet(u"QPushButton {background-color: #d63a3e; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #9e2a2a;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_2.addWidget(self.btn_delete_board)

        self.line_1 = QFrame(self.widget1)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setStyleSheet(u"background-color: #9096a6;")
        self.line_1.setFrameShadow(QFrame.Plain)
        self.line_1.setLineWidth(0)
        self.line_1.setMidLineWidth(0)
        self.line_1.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_1)

        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: #282c33;")
        self.label_9.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_logout = QPushButton(self.widget1)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(100, 30))
        self.btn_logout.setFont(font4)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setFocusPolicy(Qt.TabFocus)
        self.btn_logout.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_2.addWidget(self.btn_logout)

        self.btn_change_passwd = QPushButton(self.widget1)
        self.btn_change_passwd.setObjectName(u"btn_change_passwd")
        sizePolicy1.setHeightForWidth(self.btn_change_passwd.sizePolicy().hasHeightForWidth())
        self.btn_change_passwd.setSizePolicy(sizePolicy1)
        self.btn_change_passwd.setMinimumSize(QSize(180, 30))
        self.btn_change_passwd.setFont(font4)
        self.btn_change_passwd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_change_passwd.setFocusPolicy(Qt.TabFocus)
        self.btn_change_passwd.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_2.addWidget(self.btn_change_passwd)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_delete_account = QPushButton(self.widget1)
        self.btn_delete_account.setObjectName(u"btn_delete_account")
        sizePolicy1.setHeightForWidth(self.btn_delete_account.sizePolicy().hasHeightForWidth())
        self.btn_delete_account.setSizePolicy(sizePolicy1)
        self.btn_delete_account.setMinimumSize(QSize(150, 30))
        self.btn_delete_account.setFont(font4)
        self.btn_delete_account.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_account.setFocusPolicy(Qt.TabFocus)
        self.btn_delete_account.setStyleSheet(u"QPushButton {border-color: #d63a3e; border-width: 1.5px; border-style: solid; color: #282c33; border-radius: 5px}\n"
"QPushButton:hover {background-color: #d63a3e; color: #ffffff;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; background-color: #d63a3e; color: #ffffff;}")

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
        self.btn_cancel.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(self.widget1)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        self.btn_save.setMinimumSize(QSize(100, 30))
        self.btn_save.setFont(font4)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setFocusPolicy(Qt.TabFocus)
        self.btn_save.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #5487bb;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.widget1)


        self.verticalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.listWidget, self.btn_delete_board)
        QWidget.setTabOrder(self.btn_delete_board, self.btn_logout)
        QWidget.setTabOrder(self.btn_logout, self.btn_change_passwd)
        QWidget.setTabOrder(self.btn_change_passwd, self.btn_delete_account)
        QWidget.setTabOrder(self.btn_delete_account, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.btn_save)
        QWidget.setTabOrder(self.btn_save, self.widget1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"App Settings", None))
        self.label_app_settings.setText(QCoreApplication.translate("MainWindow", u"App Settings", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Manage Board", None))
        self.label_manage_baoard_info.setText(QCoreApplication.translate("MainWindow", u"Drag to rearrange. Select and press Delete Board to delete it.", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Board 1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Board 2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Board 3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Board 4", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Board 5", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Board 5", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Board 5", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.btn_delete_board.setText(QCoreApplication.translate("MainWindow", u"Delete Board", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Manage Account", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btn_change_passwd.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.btn_delete_account.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

