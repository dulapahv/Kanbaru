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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"background-color: #454c5a;")
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
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.widget_7.setStyleSheet(u"background-color: #282c34;")
        self.verticalLayout_2 = QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Torus Pro"])
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: #282c34;\n"
"color: #FFFFFF;")
        self.label_5.setMargin(10)

        self.verticalLayout_2.addWidget(self.label_5)

        self.pushButton_2 = QPushButton(self.widget_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(14)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.horizontalLayout_4.addWidget(self.widget_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: #343943;\n"
"color: #FFFFFF;")
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(280, 500))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-162, 0, 1040, 500))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(8, 0, 0, 8)
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(250, 0))
        self.widget_3.setStyleSheet(u"background-color: #343943;\n"
"border-radius: 10px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;")
        self.label_2.setMargin(10)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.listWidget_3 = QListWidget(self.widget_3)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setFont(font1)
        self.listWidget_3.setStyleSheet(u"QListWidget::item {height: 50px}\n"
"QListWidget::item {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: #5487bb; color: #ffffff}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #343943}")
        self.listWidget_3.setFrameShape(QFrame.NoFrame)
        self.listWidget_3.setAutoScroll(True)
        self.listWidget_3.setDragEnabled(True)
        self.listWidget_3.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_3.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_3.setSpacing(5)

        self.verticalLayout_3.addWidget(self.listWidget_3)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(250, 0))
        self.widget_5.setStyleSheet(u"background-color: #343943;\n"
"border-radius: 10px;")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 50))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;")
        self.label_4.setMargin(10)

        self.verticalLayout_7.addWidget(self.label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.listWidget_5 = QListWidget(self.widget_5)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setFont(font1)
        self.listWidget_5.setStyleSheet(u"QListWidget::item {height: 50px}\n"
"QListWidget::item {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: #5487bb; color: #ffffff}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #343943}")
        self.listWidget_5.setFrameShape(QFrame.NoFrame)
        self.listWidget_5.setAutoScroll(True)
        self.listWidget_5.setDragEnabled(True)
        self.listWidget_5.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_5.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_5.setAlternatingRowColors(False)
        self.listWidget_5.setSpacing(5)

        self.verticalLayout_7.addWidget(self.listWidget_5)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.pushButton_6 = QPushButton(self.widget_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 25))
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_7.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.widget_5, 0, 2, 1, 1)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMinimumSize(QSize(250, 0))
        self.verticalLayout_9 = QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 6, 0)
        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_9.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget_6, 0, 3, 1, 1)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(250, 0))
        self.widget_4.setStyleSheet(u"background-color: #343943;\n"
"border-radius: 10px;")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;")
        self.label_3.setMargin(10)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.listWidget_4 = QListWidget(self.widget_4)
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setFont(font1)
        self.listWidget_4.setStyleSheet(u"QListWidget::item {height: 50px}\n"
"QListWidget::item {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: #5487bb; color: #ffffff}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #343943}")
        self.listWidget_4.setFrameShape(QFrame.NoFrame)
        self.listWidget_4.setAutoScroll(True)
        self.listWidget_4.setDragEnabled(True)
        self.listWidget_4.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_4.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_4.setSpacing(5)

        self.verticalLayout_5.addWidget(self.listWidget_4)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.pushButton_5 = QPushButton(self.widget_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 25))
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_5.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.widget_4, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kanbaru", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kan\n"
"baru", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Board 1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Board 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Board 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Not Done", None))

        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_3.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Test1", None));
        ___qlistwidgetitem1 = self.listWidget_3.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Test2", None));
        ___qlistwidgetitem2 = self.listWidget_3.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Test3", None));
        ___qlistwidgetitem3 = self.listWidget_3.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget_3.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget_3.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget_3.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget_3.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem8 = self.listWidget_3.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem9 = self.listWidget_3.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem10 = self.listWidget_3.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem11 = self.listWidget_3.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled)

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Done", None))

        __sortingEnabled1 = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        ___qlistwidgetitem12 = self.listWidget_5.item(0)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Test7", None));
        ___qlistwidgetitem13 = self.listWidget_5.item(1)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Test8", None));
        ___qlistwidgetitem14 = self.listWidget_5.item(2)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Test9", None));
        self.listWidget_5.setSortingEnabled(__sortingEnabled1)

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+ Add more list", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Doing", None))

        __sortingEnabled2 = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        ___qlistwidgetitem15 = self.listWidget_4.item(0)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Test4", None));
        ___qlistwidgetitem16 = self.listWidget_4.item(1)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Test5", None));
        ___qlistwidgetitem17 = self.listWidget_4.item(2)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Test6", None));
        self.listWidget_4.setSortingEnabled(__sortingEnabled2)

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
    # retranslateUi

