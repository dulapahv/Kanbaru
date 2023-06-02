# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'board_settings_bkp.ui'
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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_BoardWindow(object):
    def setupUi(self, BoardWindow):
        if not BoardWindow.objectName():
            BoardWindow.setObjectName(u"BoardWindow")
        BoardWindow.resize(576, 678)
        icon = QIcon()
        icon.addFile(u":/img/resources/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        BoardWindow.setWindowIcon(icon)
        BoardWindow.setStyleSheet(u"background-color: #454c5a;")
        BoardWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(BoardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(107, 173, 238, 255), stop:1 rgba(69, 76, 90, 255));\n"
"color: #ffffff;\n"
"padding: 0px 0px 0px 10px;")
        self.label_3.setMargin(10)

        self.verticalLayout_3.addWidget(self.label_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(390, 0))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"background-color: #f4f5f7;\n"
"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(self.widget1)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
"QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 516, 871))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #282c33;")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.lineEdit_title = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(12)
        self.lineEdit_title.setFont(font2)
        self.lineEdit_title.setStyleSheet(u"QLineEdit {background-color: #ebecf0; color: #282c33; border-radius: 5px; padding: 0px 8px 0px 8px}\n"
"QLineEdit:focus {background-color: #ffffff; border-color: #6badee; border-width: 1.5px; border-style: solid;; padding: 0px 6px 0px 6px}")

        self.verticalLayout_2.addWidget(self.lineEdit_title)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: #282c33;")
        self.label_7.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_color_1 = QRadioButton(self.scrollAreaWidgetContents)
        self.btn_color_1.setObjectName(u"btn_color_1")
        self.btn_color_1.setMinimumSize(QSize(120, 40))
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        self.btn_color_1.setFont(font3)
        self.btn_color_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_1.setFocusPolicy(Qt.TabFocus)
        self.btn_color_1.setStyleSheet(u"QRadioButton {background-color: #6badee; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_6.addWidget(self.btn_color_1)

        self.btn_color_2 = QRadioButton(self.scrollAreaWidgetContents)
        self.btn_color_2.setObjectName(u"btn_color_2")
        self.btn_color_2.setMinimumSize(QSize(120, 40))
        self.btn_color_2.setFont(font3)
        self.btn_color_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_2.setFocusPolicy(Qt.TabFocus)
        self.btn_color_2.setStyleSheet(u"QRadioButton {background-color: #fb568a; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_6.addWidget(self.btn_color_2)

        self.btn_color_3 = QRadioButton(self.scrollAreaWidgetContents)
        self.btn_color_3.setObjectName(u"btn_color_3")
        self.btn_color_3.setMinimumSize(QSize(120, 40))
        self.btn_color_3.setFont(font3)
        self.btn_color_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_3.setFocusPolicy(Qt.TabFocus)
        self.btn_color_3.setStyleSheet(u"QRadioButton {background-color: #fbd945; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_6.addWidget(self.btn_color_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_color_4 = QRadioButton(self.scrollAreaWidgetContents)
        self.btn_color_4.setObjectName(u"btn_color_4")
        self.btn_color_4.setMinimumSize(QSize(120, 40))
        self.btn_color_4.setFont(font3)
        self.btn_color_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_4.setFocusPolicy(Qt.TabFocus)
        self.btn_color_4.setStyleSheet(u"QRadioButton {background-color: #99c37b; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_5.addWidget(self.btn_color_4)

        self.btn_color_5 = QRadioButton(self.scrollAreaWidgetContents)
        self.btn_color_5.setObjectName(u"btn_color_5")
        self.btn_color_5.setMinimumSize(QSize(120, 40))
        self.btn_color_5.setFont(font3)
        self.btn_color_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_5.setFocusPolicy(Qt.TabFocus)
        self.btn_color_5.setStyleSheet(u"QRadioButton {background-color: #c577dc; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_5.addWidget(self.btn_color_5)

        self.btn_color_6 = QRadioButton(self.scrollAreaWidgetContents)
        self.btn_color_6.setObjectName(u"btn_color_6")
        self.btn_color_6.setMinimumSize(QSize(120, 40))
        self.btn_color_6.setFont(font3)
        self.btn_color_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_6.setFocusPolicy(Qt.TabFocus)
        self.btn_color_6.setStyleSheet(u"QRadioButton {background-color: #5eb5c1; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_5.addWidget(self.btn_color_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: #282c33;")
        self.label_8.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(11)
        self.label_2.setFont(font4)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.listWidget_manage_list = QListWidget(self.scrollAreaWidgetContents)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_manage_list)
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_manage_list)
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_manage_list)
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_manage_list.setObjectName(u"listWidget_manage_list")
        font5 = QFont()
        font5.setFamilies([u"Torus Pro"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.listWidget_manage_list.setFont(font5)
        self.listWidget_manage_list.setFocusPolicy(Qt.TabFocus)
        self.listWidget_manage_list.setStyleSheet(u"QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
"QListWidget::item {background-color: #ffffff; color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: #e2e4e9; color: #000000}\n"
"QListWidget::item:selected {background-color: #cccccc; color: #000000}\n"
"QListWidget::item:focus {background-color: #cccccc; color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_manage_list.setFrameShape(QFrame.NoFrame)
        self.listWidget_manage_list.setDragEnabled(True)
        self.listWidget_manage_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget_manage_list.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_manage_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_manage_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_manage_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_manage_list.setProperty("isWrapping", False)
        self.listWidget_manage_list.setSpacing(5)
        self.listWidget_manage_list.setUniformItemSizes(True)
        self.listWidget_manage_list.setWordWrap(True)
        self.listWidget_manage_list.setSelectionRectVisible(True)

        self.verticalLayout_2.addWidget(self.listWidget_manage_list)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_delete = QPushButton(self.scrollAreaWidgetContents)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy2)
        self.btn_delete.setMinimumSize(QSize(140, 30))
        self.btn_delete.setFont(font3)
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setFocusPolicy(Qt.TabFocus)
        self.btn_delete.setStyleSheet(u"QPushButton {background-color: #d63a3e; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #9e2a2a;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_5.addWidget(self.btn_delete)

        self.btn_rename = QPushButton(self.scrollAreaWidgetContents)
        self.btn_rename.setObjectName(u"btn_rename")
        sizePolicy2.setHeightForWidth(self.btn_rename.sizePolicy().hasHeightForWidth())
        self.btn_rename.setSizePolicy(sizePolicy2)
        self.btn_rename.setMinimumSize(QSize(140, 30))
        self.btn_rename.setFont(font3)
        self.btn_rename.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rename.setFocusPolicy(Qt.TabFocus)
        self.btn_rename.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #5487bb;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_5.addWidget(self.btn_rename)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: #282c33;")
        self.label_9.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.listWidget_manage_member = QListWidget(self.scrollAreaWidgetContents)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_manage_member)
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_manage_member)
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_manage_member)
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_manage_member.setObjectName(u"listWidget_manage_member")
        self.listWidget_manage_member.setFont(font5)
        self.listWidget_manage_member.setFocusPolicy(Qt.TabFocus)
        self.listWidget_manage_member.setStyleSheet(u"QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
"QListWidget::item {background-color: #ffffff; color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: #e2e4e9; color: #000000}\n"
"QListWidget::item:selected {background-color: #cccccc; color: #000000}\n"
"QListWidget::item:focus {background-color: #cccccc; color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_manage_member.setFrameShape(QFrame.NoFrame)
        self.listWidget_manage_member.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget_manage_member.setProperty("showDropIndicator", False)
        self.listWidget_manage_member.setDragEnabled(False)
        self.listWidget_manage_member.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_manage_member.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_manage_member.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_manage_member.setProperty("isWrapping", False)
        self.listWidget_manage_member.setSpacing(5)
        self.listWidget_manage_member.setUniformItemSizes(True)
        self.listWidget_manage_member.setWordWrap(True)
        self.listWidget_manage_member.setSelectionRectVisible(True)
        self.listWidget_manage_member.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.listWidget_manage_member)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_member = QPushButton(self.scrollAreaWidgetContents)
        self.btn_add_member.setObjectName(u"btn_add_member")
        sizePolicy2.setHeightForWidth(self.btn_add_member.sizePolicy().hasHeightForWidth())
        self.btn_add_member.setSizePolicy(sizePolicy2)
        self.btn_add_member.setMinimumSize(QSize(150, 30))
        self.btn_add_member.setFont(font3)
        self.btn_add_member.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_member.setFocusPolicy(Qt.TabFocus)
        self.btn_add_member.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #5487bb;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_2.addWidget(self.btn_add_member)

        self.btn_delete_member = QPushButton(self.scrollAreaWidgetContents)
        self.btn_delete_member.setObjectName(u"btn_delete_member")
        sizePolicy2.setHeightForWidth(self.btn_delete_member.sizePolicy().hasHeightForWidth())
        self.btn_delete_member.setSizePolicy(sizePolicy2)
        self.btn_delete_member.setMinimumSize(QSize(170, 30))
        self.btn_delete_member.setFont(font3)
        self.btn_delete_member.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_member.setFocusPolicy(Qt.TabFocus)
        self.btn_delete_member.setStyleSheet(u"QPushButton {background-color: #d63a3e; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #9e2a2a;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_2.addWidget(self.btn_delete_member)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.widget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy2.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy2)
        self.btn_cancel.setMinimumSize(QSize(100, 30))
        self.btn_cancel.setFont(font3)
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancel.setFocusPolicy(Qt.TabFocus)
        self.btn_cancel.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(self.widget1)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy2.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy2)
        self.btn_save.setMinimumSize(QSize(100, 30))
        self.btn_save.setFont(font3)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setFocusPolicy(Qt.TabFocus)
        self.btn_save.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #5487bb;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.widget1)


        self.verticalLayout_3.addWidget(self.widget)

        BoardWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_title, self.btn_color_1)
        QWidget.setTabOrder(self.btn_color_1, self.btn_color_2)
        QWidget.setTabOrder(self.btn_color_2, self.btn_color_3)
        QWidget.setTabOrder(self.btn_color_3, self.btn_color_4)
        QWidget.setTabOrder(self.btn_color_4, self.btn_color_5)
        QWidget.setTabOrder(self.btn_color_5, self.btn_color_6)
        QWidget.setTabOrder(self.btn_color_6, self.listWidget_manage_list)
        QWidget.setTabOrder(self.listWidget_manage_list, self.btn_delete)
        QWidget.setTabOrder(self.btn_delete, self.btn_rename)
        QWidget.setTabOrder(self.btn_rename, self.listWidget_manage_member)
        QWidget.setTabOrder(self.listWidget_manage_member, self.btn_add_member)
        QWidget.setTabOrder(self.btn_add_member, self.btn_delete_member)
        QWidget.setTabOrder(self.btn_delete_member, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.btn_save)
        QWidget.setTabOrder(self.btn_save, self.scrollArea)

        self.retranslateUi(BoardWindow)

        QMetaObject.connectSlotsByName(BoardWindow)
    # setupUi

    def retranslateUi(self, BoardWindow):
        BoardWindow.setWindowTitle(QCoreApplication.translate("BoardWindow", u"Board Settings", None))
        self.label_3.setText(QCoreApplication.translate("BoardWindow", u"Board Settings", None))
        self.label.setText(QCoreApplication.translate("BoardWindow", u"Title", None))
        self.lineEdit_title.setText("")
        self.lineEdit_title.setPlaceholderText(QCoreApplication.translate("BoardWindow", u"Add a board title...", None))
        self.label_7.setText(QCoreApplication.translate("BoardWindow", u"Color", None))
        self.btn_color_1.setText(QCoreApplication.translate("BoardWindow", u"Light blue", None))
        self.btn_color_2.setText(QCoreApplication.translate("BoardWindow", u"Rose", None))
        self.btn_color_3.setText(QCoreApplication.translate("BoardWindow", u"Gold", None))
        self.btn_color_4.setText(QCoreApplication.translate("BoardWindow", u"Green", None))
        self.btn_color_5.setText(QCoreApplication.translate("BoardWindow", u"Lavender", None))
        self.btn_color_6.setText(QCoreApplication.translate("BoardWindow", u"Teal", None))
        self.label_8.setText(QCoreApplication.translate("BoardWindow", u"Manage Panel", None))
        self.label_2.setText(QCoreApplication.translate("BoardWindow", u"Drag to rearrange. Select and press Delete/Rename to update.", None))

        __sortingEnabled = self.listWidget_manage_list.isSortingEnabled()
        self.listWidget_manage_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_manage_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("BoardWindow", u"To Do", None));
        ___qlistwidgetitem1 = self.listWidget_manage_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("BoardWindow", u"Doing", None));
        ___qlistwidgetitem2 = self.listWidget_manage_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("BoardWindow", u"Done", None));
        self.listWidget_manage_list.setSortingEnabled(__sortingEnabled)

        self.btn_delete.setText(QCoreApplication.translate("BoardWindow", u"Delete List", None))
        self.btn_rename.setText(QCoreApplication.translate("BoardWindow", u"Rename List", None))
        self.label_9.setText(QCoreApplication.translate("BoardWindow", u"Manage Member", None))
        self.label_4.setText(QCoreApplication.translate("BoardWindow", u"Member can have access to this board. Select and press Delete Member to remove access.", None))

        __sortingEnabled1 = self.listWidget_manage_member.isSortingEnabled()
        self.listWidget_manage_member.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget_manage_member.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("BoardWindow", u"beam", None));
        ___qlistwidgetitem4 = self.listWidget_manage_member.item(1)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("BoardWindow", u"illya", None));
        ___qlistwidgetitem5 = self.listWidget_manage_member.item(2)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("BoardWindow", u"spiral", None));
        self.listWidget_manage_member.setSortingEnabled(__sortingEnabled1)

        self.btn_add_member.setText(QCoreApplication.translate("BoardWindow", u"Add Member", None))
        self.btn_delete_member.setText(QCoreApplication.translate("BoardWindow", u"Delete Member", None))
        self.btn_cancel.setText(QCoreApplication.translate("BoardWindow", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("BoardWindow", u"Save", None))
    # retranslateUi

