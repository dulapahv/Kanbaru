# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_bkp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 678)
        icon = QIcon()
        icon.addFile(u":/img/resources/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #454c5a;")
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
        self.panel_left.setMinimumSize(QSize(150, 0))
        self.panel_left.setMaximumSize(QSize(144, 16777215))
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

        self.verticalLayout_2.addWidget(self.label_logo)

        self.scrollArea_panel_left = QScrollArea(self.panel_left)
        self.scrollArea_panel_left.setObjectName(u"scrollArea_panel_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_panel_left.sizePolicy().hasHeightForWidth())
        self.scrollArea_panel_left.setSizePolicy(sizePolicy1)
        self.scrollArea_panel_left.setStyleSheet(u"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #343943}")
        self.scrollArea_panel_left.setFrameShape(QFrame.NoFrame)
        self.scrollArea_panel_left.setWidgetResizable(True)
        self.scrollAreaContent_panel_left = QWidget()
        self.scrollAreaContent_panel_left.setObjectName(u"scrollAreaContent_panel_left")
        self.scrollAreaContent_panel_left.setGeometry(QRect(0, 0, 134, 417))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaContent_panel_left)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.btn_board_1 = QPushButton(self.scrollAreaContent_panel_left)
        self.btn_board_1.setObjectName(u"btn_board_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_board_1.sizePolicy().hasHeightForWidth())
        self.btn_board_1.setSizePolicy(sizePolicy2)
        self.btn_board_1.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(12)
        self.btn_board_1.setFont(font1)
        self.btn_board_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_1.setFocusPolicy(Qt.TabFocus)
        self.btn_board_1.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_4.addWidget(self.btn_board_1)

        self.btn_board_2 = QPushButton(self.scrollAreaContent_panel_left)
        self.btn_board_2.setObjectName(u"btn_board_2")
        self.btn_board_2.setMinimumSize(QSize(0, 40))
        self.btn_board_2.setFont(font1)
        self.btn_board_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_2.setFocusPolicy(Qt.TabFocus)
        self.btn_board_2.setStyleSheet(u"QPushButton {background-color: #fb568a; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_4.addWidget(self.btn_board_2)

        self.btn_board_3 = QPushButton(self.scrollAreaContent_panel_left)
        self.btn_board_3.setObjectName(u"btn_board_3")
        self.btn_board_3.setMinimumSize(QSize(0, 40))
        self.btn_board_3.setFont(font1)
        self.btn_board_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_3.setFocusPolicy(Qt.TabFocus)
        self.btn_board_3.setStyleSheet(u"QPushButton {background-color: #fbd945; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_4.addWidget(self.btn_board_3)

        self.btn_board_4 = QPushButton(self.scrollAreaContent_panel_left)
        self.btn_board_4.setObjectName(u"btn_board_4")
        self.btn_board_4.setMinimumSize(QSize(0, 40))
        self.btn_board_4.setFont(font1)
        self.btn_board_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_4.setFocusPolicy(Qt.TabFocus)
        self.btn_board_4.setStyleSheet(u"QPushButton {background-color: #99c37b; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_4.addWidget(self.btn_board_4)

        self.btn_board_5 = QPushButton(self.scrollAreaContent_panel_left)
        self.btn_board_5.setObjectName(u"btn_board_5")
        self.btn_board_5.setMinimumSize(QSize(0, 40))
        self.btn_board_5.setFont(font1)
        self.btn_board_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_5.setFocusPolicy(Qt.TabFocus)
        self.btn_board_5.setStyleSheet(u"QPushButton {background-color: #c577dc; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_4.addWidget(self.btn_board_5)

        self.btn_board_6 = QPushButton(self.scrollAreaContent_panel_left)
        self.btn_board_6.setObjectName(u"btn_board_6")
        self.btn_board_6.setMinimumSize(QSize(0, 40))
        self.btn_board_6.setFont(font1)
        self.btn_board_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_6.setFocusPolicy(Qt.TabFocus)
        self.btn_board_6.setStyleSheet(u"QPushButton {background-color: #5eb5c1; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_4.addWidget(self.btn_board_6)

        self.btn_board_7 = QPushButton(self.scrollAreaContent_panel_left)
        self.btn_board_7.setObjectName(u"btn_board_7")
        self.btn_board_7.setMinimumSize(QSize(0, 40))
        self.btn_board_7.setFont(font1)
        self.btn_board_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_board_7.setFocusPolicy(Qt.TabFocus)
        self.btn_board_7.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_4.addWidget(self.btn_board_7)

        self.vertSpacer_scrollAreaContent = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.vertSpacer_scrollAreaContent)

        self.scrollArea_panel_left.setWidget(self.scrollAreaContent_panel_left)

        self.verticalLayout_2.addWidget(self.scrollArea_panel_left)

        self.btn_add_board = QPushButton(self.panel_left)
        self.btn_add_board.setObjectName(u"btn_add_board")
        self.btn_add_board.setMinimumSize(QSize(0, 30))
        self.btn_add_board.setFont(font1)
        self.btn_add_board.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_board.setFocusPolicy(Qt.TabFocus)
        self.btn_add_board.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")
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
        self.btn_board_settings.setStyleSheet(u"QPushButton {background-color: #7f8ca6; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #576073;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")
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
        self.btn_app_settings.setStyleSheet(u"QPushButton {background-color: #7f8ca6; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #576073;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")
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
        self.scrollArea_panel_right.setStyleSheet(u"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
"QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.scrollArea_panel_right.setFrameShape(QFrame.NoFrame)
        self.scrollArea_panel_right.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_panel_right.setWidgetResizable(True)
        self.scrollAreaContent_panel_right = QWidget()
        self.scrollAreaContent_panel_right.setObjectName(u"scrollAreaContent_panel_right")
        self.scrollAreaContent_panel_right.setGeometry(QRect(0, 0, 1032, 579))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaContent_panel_right)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 0, 0, 8)
        self.list_1 = QWidget(self.scrollAreaContent_panel_right)
        self.list_1.setObjectName(u"list_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.list_1.sizePolicy().hasHeightForWidth())
        self.list_1.setSizePolicy(sizePolicy4)
        self.list_1.setMinimumSize(QSize(250, 0))
        self.list_1.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.list_1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_list_1 = QWidget(self.list_1)
        self.widget_list_1.setObjectName(u"widget_list_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_list_1.sizePolicy().hasHeightForWidth())
        self.widget_list_1.setSizePolicy(sizePolicy5)
        self.widget_list_1.setStyleSheet(u"background-color: #ebecf0;\n"
"border-radius: 10px;")
        self.verticalLayout_11 = QVBoxLayout(self.widget_list_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_list_1 = QLabel(self.widget_list_1)
        self.label_list_1.setObjectName(u"label_list_1")
        sizePolicy2.setHeightForWidth(self.label_list_1.sizePolicy().hasHeightForWidth())
        self.label_list_1.setSizePolicy(sizePolicy2)
        self.label_list_1.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_list_1.setFont(font3)
        self.label_list_1.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;\n"
"padding: 5px 0px 0px 5px;")
        self.label_list_1.setMargin(0)

        self.verticalLayout_11.addWidget(self.label_list_1)

        self.listWidget_list_1 = QListWidget(self.widget_list_1)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem11 = QListWidgetItem(self.listWidget_list_1)
        __qlistwidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_list_1.setObjectName(u"listWidget_list_1")
        sizePolicy4.setHeightForWidth(self.listWidget_list_1.sizePolicy().hasHeightForWidth())
        self.listWidget_list_1.setSizePolicy(sizePolicy4)
        self.listWidget_list_1.setMaximumSize(QSize(250, 16777215))
        self.listWidget_list_1.setFont(font1)
        self.listWidget_list_1.setFocusPolicy(Qt.TabFocus)
        self.listWidget_list_1.setAcceptDrops(True)
        self.listWidget_list_1.setStyleSheet(u"QListWidget {background-color: #ebecf0; border-radius: 10px;}\n"
"QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
"QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(226, 228, 233, 255), stop:1 rgba(226, 228, 233, 255)); color: #000000}\n"
"QListWidget::item:selected {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
"QListWidget::item:focus {background-color: qlineargradient(spread:pad, x1:0"
                        ", y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
"QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_list_1.setFrameShape(QFrame.NoFrame)
        self.listWidget_list_1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget_list_1.setAutoScroll(True)
        self.listWidget_list_1.setDragEnabled(True)
        self.listWidget_list_1.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_list_1.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_list_1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_list_1.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_list_1.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_list_1.setProperty("isWrapping", False)
        self.listWidget_list_1.setSpacing(5)
        self.listWidget_list_1.setUniformItemSizes(True)
        self.listWidget_list_1.setWordWrap(True)
        self.listWidget_list_1.setSelectionRectVisible(True)

        self.verticalLayout_11.addWidget(self.listWidget_list_1)

        self.widget_add_card = QWidget(self.widget_list_1)
        self.widget_add_card.setObjectName(u"widget_add_card")
        sizePolicy2.setHeightForWidth(self.widget_add_card.sizePolicy().hasHeightForWidth())
        self.widget_add_card.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.widget_add_card)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 0, 6, 6)
        self.btn_add_card_list_1 = QPushButton(self.widget_add_card)
        self.btn_add_card_list_1.setObjectName(u"btn_add_card_list_1")
        self.btn_add_card_list_1.setMinimumSize(QSize(0, 25))
        self.btn_add_card_list_1.setFont(font1)
        self.btn_add_card_list_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_card_list_1.setFocusPolicy(Qt.TabFocus)
        self.btn_add_card_list_1.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
"QPushButton:hover {background-color: #dadbe2; color: #505b76}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_6.addWidget(self.btn_add_card_list_1)


        self.verticalLayout_11.addWidget(self.widget_add_card)


        self.verticalLayout_3.addWidget(self.widget_list_1)


        self.horizontalLayout_5.addWidget(self.list_1)

        self.list_2 = QWidget(self.scrollAreaContent_panel_right)
        self.list_2.setObjectName(u"list_2")
        sizePolicy4.setHeightForWidth(self.list_2.sizePolicy().hasHeightForWidth())
        self.list_2.setSizePolicy(sizePolicy4)
        self.list_2.setMinimumSize(QSize(250, 0))
        self.list_2.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.list_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_list_2 = QWidget(self.list_2)
        self.widget_list_2.setObjectName(u"widget_list_2")
        sizePolicy5.setHeightForWidth(self.widget_list_2.sizePolicy().hasHeightForWidth())
        self.widget_list_2.setSizePolicy(sizePolicy5)
        self.widget_list_2.setStyleSheet(u"background-color: #ebecf0;\n"
"border-radius: 10px;")
        self.verticalLayout_12 = QVBoxLayout(self.widget_list_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_list_2 = QLabel(self.widget_list_2)
        self.label_list_2.setObjectName(u"label_list_2")
        sizePolicy2.setHeightForWidth(self.label_list_2.sizePolicy().hasHeightForWidth())
        self.label_list_2.setSizePolicy(sizePolicy2)
        self.label_list_2.setMinimumSize(QSize(0, 30))
        self.label_list_2.setFont(font3)
        self.label_list_2.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;\n"
"padding: 5px 0px 0px 5px;")
        self.label_list_2.setMargin(0)

        self.verticalLayout_12.addWidget(self.label_list_2)

        self.listWidget_list_2 = QListWidget(self.widget_list_2)
        __qlistwidgetitem12 = QListWidgetItem(self.listWidget_list_2)
        __qlistwidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem13 = QListWidgetItem(self.listWidget_list_2)
        __qlistwidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem14 = QListWidgetItem(self.listWidget_list_2)
        __qlistwidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_list_2.setObjectName(u"listWidget_list_2")
        sizePolicy4.setHeightForWidth(self.listWidget_list_2.sizePolicy().hasHeightForWidth())
        self.listWidget_list_2.setSizePolicy(sizePolicy4)
        self.listWidget_list_2.setMaximumSize(QSize(250, 16777215))
        self.listWidget_list_2.setFont(font1)
        self.listWidget_list_2.setFocusPolicy(Qt.TabFocus)
        self.listWidget_list_2.setAcceptDrops(True)
        self.listWidget_list_2.setStyleSheet(u"QListWidget {background-color: #ebecf0; border-radius: 10px;}\n"
"QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
"QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(226, 228, 233, 255), stop:1 rgba(226, 228, 233, 255)); color: #000000}\n"
"QListWidget::item:selected {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
"QListWidget::item:focus {background-color: qlineargradient(spread:pad, x1:0"
                        ", y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
"QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_list_2.setFrameShape(QFrame.NoFrame)
        self.listWidget_list_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget_list_2.setAutoScroll(True)
        self.listWidget_list_2.setDragEnabled(True)
        self.listWidget_list_2.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_list_2.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_list_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_list_2.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_list_2.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_list_2.setProperty("isWrapping", False)
        self.listWidget_list_2.setSpacing(5)
        self.listWidget_list_2.setUniformItemSizes(True)
        self.listWidget_list_2.setWordWrap(True)
        self.listWidget_list_2.setSelectionRectVisible(True)

        self.verticalLayout_12.addWidget(self.listWidget_list_2)

        self.widget_9 = QWidget(self.widget_list_2)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 0, 6, 6)
        self.btn_add_card_list_2 = QPushButton(self.widget_9)
        self.btn_add_card_list_2.setObjectName(u"btn_add_card_list_2")
        self.btn_add_card_list_2.setMinimumSize(QSize(0, 25))
        self.btn_add_card_list_2.setFont(font1)
        self.btn_add_card_list_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_card_list_2.setFocusPolicy(Qt.TabFocus)
        self.btn_add_card_list_2.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
"QPushButton:hover {background-color: #dadbe2; color: #505b76}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_7.addWidget(self.btn_add_card_list_2)


        self.verticalLayout_12.addWidget(self.widget_9)


        self.verticalLayout_5.addWidget(self.widget_list_2)


        self.horizontalLayout_5.addWidget(self.list_2)

        self.list_3 = QWidget(self.scrollAreaContent_panel_right)
        self.list_3.setObjectName(u"list_3")
        sizePolicy4.setHeightForWidth(self.list_3.sizePolicy().hasHeightForWidth())
        self.list_3.setSizePolicy(sizePolicy4)
        self.list_3.setMinimumSize(QSize(250, 0))
        self.list_3.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.list_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_list_3 = QWidget(self.list_3)
        self.widget_list_3.setObjectName(u"widget_list_3")
        sizePolicy5.setHeightForWidth(self.widget_list_3.sizePolicy().hasHeightForWidth())
        self.widget_list_3.setSizePolicy(sizePolicy5)
        self.widget_list_3.setStyleSheet(u"background-color: #ebecf0;\n"
"border-radius: 10px;")
        self.verticalLayout_13 = QVBoxLayout(self.widget_list_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_list_3 = QLabel(self.widget_list_3)
        self.label_list_3.setObjectName(u"label_list_3")
        sizePolicy2.setHeightForWidth(self.label_list_3.sizePolicy().hasHeightForWidth())
        self.label_list_3.setSizePolicy(sizePolicy2)
        self.label_list_3.setMinimumSize(QSize(0, 30))
        self.label_list_3.setFont(font3)
        self.label_list_3.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;\n"
"padding: 5px 0px 0px 5px;")
        self.label_list_3.setMargin(0)

        self.verticalLayout_13.addWidget(self.label_list_3)

        self.listWidget_list_3 = QListWidget(self.widget_list_3)
        __qlistwidgetitem15 = QListWidgetItem(self.listWidget_list_3)
        __qlistwidgetitem15.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem16 = QListWidgetItem(self.listWidget_list_3)
        __qlistwidgetitem16.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem17 = QListWidgetItem(self.listWidget_list_3)
        __qlistwidgetitem17.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_list_3.setObjectName(u"listWidget_list_3")
        sizePolicy4.setHeightForWidth(self.listWidget_list_3.sizePolicy().hasHeightForWidth())
        self.listWidget_list_3.setSizePolicy(sizePolicy4)
        self.listWidget_list_3.setMaximumSize(QSize(250, 16777215))
        self.listWidget_list_3.setFont(font1)
        self.listWidget_list_3.setFocusPolicy(Qt.TabFocus)
        self.listWidget_list_3.setAcceptDrops(True)
        self.listWidget_list_3.setStyleSheet(u"QListWidget {background-color: #ebecf0; border-radius: 10px;}\n"
"QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
"QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(226, 228, 233, 255), stop:1 rgba(226, 228, 233, 255)); color: #000000}\n"
"QListWidget::item:selected {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
"QListWidget::item:focus {background-color: qlineargradient(spread:pad, x1:0"
                        ", y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
"QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_list_3.setFrameShape(QFrame.NoFrame)
        self.listWidget_list_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget_list_3.setAutoScroll(True)
        self.listWidget_list_3.setDragEnabled(True)
        self.listWidget_list_3.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_list_3.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_list_3.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_list_3.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_list_3.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_list_3.setProperty("isWrapping", False)
        self.listWidget_list_3.setSpacing(5)
        self.listWidget_list_3.setUniformItemSizes(True)
        self.listWidget_list_3.setWordWrap(True)
        self.listWidget_list_3.setSelectionRectVisible(True)

        self.verticalLayout_13.addWidget(self.listWidget_list_3)

        self.widget_10 = QWidget(self.widget_list_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy2.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.widget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 0, 6, 6)
        self.btn_add_card_list_3 = QPushButton(self.widget_10)
        self.btn_add_card_list_3.setObjectName(u"btn_add_card_list_3")
        self.btn_add_card_list_3.setMinimumSize(QSize(0, 25))
        self.btn_add_card_list_3.setFont(font1)
        self.btn_add_card_list_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_card_list_3.setFocusPolicy(Qt.TabFocus)
        self.btn_add_card_list_3.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
"QPushButton:hover {background-color: #dadbe2; color: #505b76}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_10.addWidget(self.btn_add_card_list_3)


        self.verticalLayout_13.addWidget(self.widget_10)


        self.verticalLayout_8.addWidget(self.widget_list_3)


        self.horizontalLayout_5.addWidget(self.list_3)

        self.list_add = QWidget(self.scrollAreaContent_panel_right)
        self.list_add.setObjectName(u"list_add")
        sizePolicy.setHeightForWidth(self.list_add.sizePolicy().hasHeightForWidth())
        self.list_add.setSizePolicy(sizePolicy)
        self.list_add.setMinimumSize(QSize(250, 0))
        self.verticalLayout_9 = QVBoxLayout(self.list_add)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 6, 0)
        self.btn_add_list = QPushButton(self.list_add)
        self.btn_add_list.setObjectName(u"btn_add_list")
        self.btn_add_list.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.btn_add_list.setFont(font4)
        self.btn_add_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_list.setFocusPolicy(Qt.TabFocus)
        self.btn_add_list.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.verticalLayout_9.addWidget(self.btn_add_list)

        self.vertSpacer_list_add = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.vertSpacer_list_add)


        self.horizontalLayout_5.addWidget(self.list_add)

        self.horzSpacer_panel_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horzSpacer_panel_right)

        self.scrollArea_panel_right.setWidget(self.scrollAreaContent_panel_right)

        self.horizontalLayout_2.addWidget(self.scrollArea_panel_right)


        self.panel_right.addWidget(self.widget_panel_right)


        self.horizontalLayout_4.addLayout(self.panel_right)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_add_list, self.btn_add_board)
        QWidget.setTabOrder(self.btn_add_board, self.btn_board_settings)
        QWidget.setTabOrder(self.btn_board_settings, self.btn_app_settings)
        QWidget.setTabOrder(self.btn_app_settings, self.btn_board_1)
        QWidget.setTabOrder(self.btn_board_1, self.btn_board_2)
        QWidget.setTabOrder(self.btn_board_2, self.btn_board_3)
        QWidget.setTabOrder(self.btn_board_3, self.btn_board_4)
        QWidget.setTabOrder(self.btn_board_4, self.btn_board_5)
        QWidget.setTabOrder(self.btn_board_5, self.btn_board_6)
        QWidget.setTabOrder(self.btn_board_6, self.btn_board_7)
        QWidget.setTabOrder(self.btn_board_7, self.listWidget_list_1)
        QWidget.setTabOrder(self.listWidget_list_1, self.listWidget_list_2)
        QWidget.setTabOrder(self.listWidget_list_2, self.listWidget_list_3)
        QWidget.setTabOrder(self.listWidget_list_3, self.btn_add_card_list_1)
        QWidget.setTabOrder(self.btn_add_card_list_1, self.btn_add_card_list_2)
        QWidget.setTabOrder(self.btn_add_card_list_2, self.btn_add_card_list_3)
        QWidget.setTabOrder(self.btn_add_card_list_3, self.scrollArea_panel_left)
        QWidget.setTabOrder(self.scrollArea_panel_left, self.scrollArea_panel_right)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kanbaru", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"Kan\n"
"baru", None))
        self.btn_board_1.setText(QCoreApplication.translate("MainWindow", u"Board 1", None))
        self.btn_board_2.setText(QCoreApplication.translate("MainWindow", u"Board 2", None))
        self.btn_board_3.setText(QCoreApplication.translate("MainWindow", u"Board 3", None))
        self.btn_board_4.setText(QCoreApplication.translate("MainWindow", u"Board 4", None))
        self.btn_board_5.setText(QCoreApplication.translate("MainWindow", u"Board 5", None))
        self.btn_board_6.setText(QCoreApplication.translate("MainWindow", u"Board 6", None))
        self.btn_board_7.setText(QCoreApplication.translate("MainWindow", u"Board 7", None))
        self.btn_add_board.setText(QCoreApplication.translate("MainWindow", u" Add a board", None))
        self.btn_board_settings.setText(QCoreApplication.translate("MainWindow", u"Manage Board", None))
        self.btn_app_settings.setText(QCoreApplication.translate("MainWindow", u" App Settings", None))
        self.label_board.setText(QCoreApplication.translate("MainWindow", u"Board 1", None))
        self.label_list_1.setText(QCoreApplication.translate("MainWindow", u"To Do", None))

        __sortingEnabled = self.listWidget_list_1.isSortingEnabled()
        self.listWidget_list_1.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_list_1.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Test1", None));
        ___qlistwidgetitem1 = self.listWidget_list_1.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Test2", None));
        ___qlistwidgetitem2 = self.listWidget_list_1.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Test3", None));
        ___qlistwidgetitem3 = self.listWidget_list_1.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget_list_1.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget_list_1.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget_list_1.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget_list_1.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem8 = self.listWidget_list_1.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem9 = self.listWidget_list_1.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem10 = self.listWidget_list_1.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem11 = self.listWidget_list_1.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_list_1.setSortingEnabled(__sortingEnabled)

        self.btn_add_card_list_1.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.label_list_2.setText(QCoreApplication.translate("MainWindow", u"Doing", None))

        __sortingEnabled1 = self.listWidget_list_2.isSortingEnabled()
        self.listWidget_list_2.setSortingEnabled(False)
        ___qlistwidgetitem12 = self.listWidget_list_2.item(0)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Test1", None));
        ___qlistwidgetitem13 = self.listWidget_list_2.item(1)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Test2", None));
        ___qlistwidgetitem14 = self.listWidget_list_2.item(2)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Test3", None));
        self.listWidget_list_2.setSortingEnabled(__sortingEnabled1)

        self.btn_add_card_list_2.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.label_list_3.setText(QCoreApplication.translate("MainWindow", u"Done", None))

        __sortingEnabled2 = self.listWidget_list_3.isSortingEnabled()
        self.listWidget_list_3.setSortingEnabled(False)
        ___qlistwidgetitem15 = self.listWidget_list_3.item(0)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Test1", None));
        ___qlistwidgetitem16 = self.listWidget_list_3.item(1)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Test2", None));
        ___qlistwidgetitem17 = self.listWidget_list_3.item(2)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Test3", None));
        self.listWidget_list_3.setSortingEnabled(__sortingEnabled2)

        self.btn_add_card_list_3.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.btn_add_list.setText(QCoreApplication.translate("MainWindow", u"+ Add a list", None))
    # retranslateUi

