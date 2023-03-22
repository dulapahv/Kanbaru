# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'board_settings.ui'
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
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
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
        self.label_board_desc = QLabel(self.centralwidget)
        self.label_board_desc.setObjectName(u"label_board_desc")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_board_desc.sizePolicy().hasHeightForWidth())
        self.label_board_desc.setSizePolicy(sizePolicy)
        self.label_board_desc.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(28)
        self.label_board_desc.setFont(font)
        self.label_board_desc.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(107, 173, 238, 255), stop:1 rgba(69, 76, 90, 255));\n"
"color: #ffffff;\n"
"padding: 0px 0px 0px 10px;")
        self.label_board_desc.setMargin(10)

        self.verticalLayout_3.addWidget(self.label_board_desc)

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
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title = QLabel(self.widget1)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: #282c33;")
        self.label_title.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_title)

        self.lineEdit_title = QLineEdit(self.widget1)
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

        self.label_color = QLabel(self.widget1)
        self.label_color.setObjectName(u"label_color")
        self.label_color.setFont(font1)
        self.label_color.setStyleSheet(u"color: #282c33;")
        self.label_color.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_color)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_color_1 = QRadioButton(self.widget1)
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
        self.btn_color_1.setChecked(True)

        self.verticalLayout_6.addWidget(self.btn_color_1)

        self.btn_color_2 = QRadioButton(self.widget1)
        self.btn_color_2.setObjectName(u"btn_color_2")
        self.btn_color_2.setMinimumSize(QSize(120, 40))
        self.btn_color_2.setFont(font3)
        self.btn_color_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_2.setFocusPolicy(Qt.TabFocus)
        self.btn_color_2.setStyleSheet(u"QRadioButton {background-color: #fb568a; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_6.addWidget(self.btn_color_2)

        self.btn_color_3 = QRadioButton(self.widget1)
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
        self.btn_color_4 = QRadioButton(self.widget1)
        self.btn_color_4.setObjectName(u"btn_color_4")
        self.btn_color_4.setMinimumSize(QSize(120, 40))
        self.btn_color_4.setFont(font3)
        self.btn_color_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_4.setFocusPolicy(Qt.TabFocus)
        self.btn_color_4.setStyleSheet(u"QRadioButton {background-color: #99c37b; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_5.addWidget(self.btn_color_4)

        self.btn_color_5 = QRadioButton(self.widget1)
        self.btn_color_5.setObjectName(u"btn_color_5")
        self.btn_color_5.setMinimumSize(QSize(120, 40))
        self.btn_color_5.setFont(font3)
        self.btn_color_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_color_5.setFocusPolicy(Qt.TabFocus)
        self.btn_color_5.setStyleSheet(u"QRadioButton {background-color: #c577dc; color: #ffffff; padding: 0px 5px 0px 5px;}\n"
"QRadioButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid; padding: 0px 3px 0px 3px;}")

        self.verticalLayout_5.addWidget(self.btn_color_5)

        self.btn_color_6 = QRadioButton(self.widget1)
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

        self.label_manage_list = QLabel(self.widget1)
        self.label_manage_list.setObjectName(u"label_manage_list")
        self.label_manage_list.setFont(font1)
        self.label_manage_list.setStyleSheet(u"color: #282c33;")
        self.label_manage_list.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_manage_list)

        self.label_manage_list_desc = QLabel(self.widget1)
        self.label_manage_list_desc.setObjectName(u"label_manage_list_desc")
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(11)
        self.label_manage_list_desc.setFont(font4)
        self.label_manage_list_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_manage_list_desc)

        self.listWidget_manage_list = QListWidget(self.widget1)
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
        self.btn_delete = QPushButton(self.widget1)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy1)
        self.btn_delete.setMinimumSize(QSize(140, 30))
        self.btn_delete.setFont(font3)
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setFocusPolicy(Qt.TabFocus)
        self.btn_delete.setStyleSheet(u"QPushButton {background-color: #d63a3e; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #9e2a2a;}\n"
"QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        self.horizontalLayout_5.addWidget(self.btn_delete)

        self.btn_rename = QPushButton(self.widget1)
        self.btn_rename.setObjectName(u"btn_rename")
        sizePolicy1.setHeightForWidth(self.btn_rename.sizePolicy().hasHeightForWidth())
        self.btn_rename.setSizePolicy(sizePolicy1)
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


        self.verticalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.widget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
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
        QWidget.setTabOrder(self.btn_rename, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.btn_save)

        self.retranslateUi(BoardWindow)

        QMetaObject.connectSlotsByName(BoardWindow)
    # setupUi

    def retranslateUi(self, BoardWindow):
        BoardWindow.setWindowTitle(QCoreApplication.translate("BoardWindow", u"Board Settings", None))
        self.label_board_desc.setText(QCoreApplication.translate("BoardWindow", u"Board Settings", None))
        self.label_title.setText(QCoreApplication.translate("BoardWindow", u"Title", None))
        self.lineEdit_title.setText("")
        self.lineEdit_title.setPlaceholderText(QCoreApplication.translate("BoardWindow", u"Add a board title...", None))
        self.label_color.setText(QCoreApplication.translate("BoardWindow", u"Color", None))
        self.btn_color_1.setText(QCoreApplication.translate("BoardWindow", u"Light blue", None))
        self.btn_color_2.setText(QCoreApplication.translate("BoardWindow", u"Rose", None))
        self.btn_color_3.setText(QCoreApplication.translate("BoardWindow", u"Gold", None))
        self.btn_color_4.setText(QCoreApplication.translate("BoardWindow", u"Green", None))
        self.btn_color_5.setText(QCoreApplication.translate("BoardWindow", u"Lavender", None))
        self.btn_color_6.setText(QCoreApplication.translate("BoardWindow", u"Teal", None))
        self.label_manage_list.setText(QCoreApplication.translate("BoardWindow", u"Manage List", None))
        self.label_manage_list_desc.setText(QCoreApplication.translate("BoardWindow", u"Drag to rearrange. Select and press Delete/Rename to update.", None))

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
        self.btn_cancel.setText(QCoreApplication.translate("BoardWindow", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("BoardWindow", u"Save", None))
    # retranslateUi

