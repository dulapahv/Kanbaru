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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 678)
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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QSize(150, 0))
        self.widget_7.setMaximumSize(QSize(144, 16777215))
        self.widget_7.setStyleSheet(u"background-color: #282c34;")
        self.verticalLayout_2 = QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 0, 8, 8)
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

        self.scrollArea_2 = QScrollArea(self.widget_7)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setStyleSheet(u"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #343943}")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 134, 417))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Torus Pro"])
        font1.setPointSize(12)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {background-color: #fb568a; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton {background-color: #fbd945; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_4.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 40))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton {background-color: #99c37b; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_4.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 40))
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton {background-color: #c577dc; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 40))
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton {background-color: #5eb5c1; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 40))
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_4.addWidget(self.pushButton_12)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_11)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.pushButton_13 = QPushButton(self.widget_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 30))
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_2.addWidget(self.pushButton_13)

        self.pushButton_15 = QPushButton(self.widget_7)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 30))
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton {background-color: #7f8ca6; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #576073;}")

        self.verticalLayout_2.addWidget(self.pushButton_15)

        self.pushButton_7 = QPushButton(self.widget_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton {background-color: #7f8ca6; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #576073;}")

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.horizontalLayout_4.addWidget(self.widget_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        font2 = QFont()
        font2.setFamilies([u"Torus Pro"])
        font2.setPointSize(28)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(107, 173, 238, 255), stop:1 rgba(69, 76, 90, 255));\n"
"color: #FFFFFF;")
        self.label.setMargin(10)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1032, 579))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 0, 0, 8)
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setMinimumSize(QSize(250, 0))
        self.widget_3.setStyleSheet(u"background-color: #ebecf0;\n"
"border-radius: 10px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Torus Pro"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;\n"
"padding: 5px 0px 0px 5px;")
        self.label_2.setMargin(0)

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
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.listWidget_3.sizePolicy().hasHeightForWidth())
        self.listWidget_3.setSizePolicy(sizePolicy5)
        self.listWidget_3.setMaximumSize(QSize(250, 16777215))
        self.listWidget_3.setFont(font1)
        self.listWidget_3.setStyleSheet(u"QListWidget::item {height: 40px; padding: 0px 0px 0px 8px}\n"
"QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(244, 245, 247, 255), stop:1 rgba(244, 245, 247, 255)); color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_3.setFrameShape(QFrame.NoFrame)
        self.listWidget_3.setAutoScroll(True)
        self.listWidget_3.setDragEnabled(True)
        self.listWidget_3.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_3.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_3.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_3.setSpacing(5)
        self.listWidget_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.listWidget_3)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.pushButton_4 = QPushButton(self.widget_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 25))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
"QPushButton:hover {background-color: #dadbe2; color: #505b76}")

        self.verticalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.widget_8)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy4.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy4)
        self.widget_4.setMinimumSize(QSize(250, 0))
        self.widget_4.setStyleSheet(u"background-color: #ebecf0;\n"
"border-radius: 10px;")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;\n"
"padding: 5px 0px 0px 5px;")
        self.label_3.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.listWidget_4 = QListWidget(self.widget_4)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_4.setObjectName(u"listWidget_4")
        sizePolicy5.setHeightForWidth(self.listWidget_4.sizePolicy().hasHeightForWidth())
        self.listWidget_4.setSizePolicy(sizePolicy5)
        self.listWidget_4.setMaximumSize(QSize(250, 16777215))
        self.listWidget_4.setFont(font1)
        self.listWidget_4.setStyleSheet(u"QListWidget::item {height: 40px; padding: 0px 0px 0px 8px}\n"
"QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(244, 245, 247, 255), stop:1 rgba(244, 245, 247, 255)); color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_4.setFrameShape(QFrame.NoFrame)
        self.listWidget_4.setAutoScroll(True)
        self.listWidget_4.setDragEnabled(True)
        self.listWidget_4.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_4.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_4.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_4.setSpacing(5)
        self.listWidget_4.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.listWidget_4)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.pushButton_5 = QPushButton(self.widget_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 25))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
"QPushButton:hover {background-color: #dadbe2; color: #505b76}")

        self.verticalLayout_7.addWidget(self.pushButton_5)


        self.verticalLayout_5.addWidget(self.widget_9)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.widget_5.setMinimumSize(QSize(250, 0))
        self.widget_5.setStyleSheet(u"background-color: #ebecf0;\n"
"border-radius: 10px;")
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: #282c33;\n"
"background-color: #ebecf0;\n"
"border-radius: 5px;\n"
"padding: 5px 0px 0px 5px;")
        self.label_4.setMargin(0)

        self.verticalLayout_8.addWidget(self.label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.listWidget_5 = QListWidget(self.widget_5)
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_5.setObjectName(u"listWidget_5")
        sizePolicy5.setHeightForWidth(self.listWidget_5.sizePolicy().hasHeightForWidth())
        self.listWidget_5.setSizePolicy(sizePolicy5)
        self.listWidget_5.setMaximumSize(QSize(250, 16777215))
        self.listWidget_5.setFont(font1)
        self.listWidget_5.setStyleSheet(u"QListWidget::item {height: 40px; padding: 0px 0px 0px 8px}\n"
"QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
"QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(244, 245, 247, 255), stop:1 rgba(244, 245, 247, 255)); color: #000000}\n"
"QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        self.listWidget_5.setFrameShape(QFrame.NoFrame)
        self.listWidget_5.setAutoScroll(True)
        self.listWidget_5.setDragEnabled(True)
        self.listWidget_5.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_5.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_5.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_5.setSpacing(5)
        self.listWidget_5.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.listWidget_5)

        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_10 = QVBoxLayout(self.widget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.pushButton_6 = QPushButton(self.widget_10)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 25))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
"QPushButton:hover {background-color: #dadbe2; color: #505b76}")

        self.verticalLayout_10.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.widget_10)


        self.horizontalLayout_5.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QSize(250, 0))
        self.verticalLayout_9 = QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 6, 0)
        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Torus Pro"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
"QPushButton:hover {background-color: #7e828c;}")

        self.verticalLayout_9.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addWidget(self.widget_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pushButton, self.listWidget_3)
        QWidget.setTabOrder(self.listWidget_3, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_7)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kanbaru", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kan\n"
"baru", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Board 1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Board 2", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Board 3", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Board 4", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Board 5", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Board 5", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Board 5", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"+ Add a board", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Board Settings", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"App Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Board 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To Do", None))

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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Doing", None))

        __sortingEnabled1 = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        ___qlistwidgetitem12 = self.listWidget_4.item(0)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Test11", None));
        ___qlistwidgetitem13 = self.listWidget_4.item(1)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Test22", None));
        ___qlistwidgetitem14 = self.listWidget_4.item(2)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Test33", None));
        self.listWidget_4.setSortingEnabled(__sortingEnabled1)

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Done", None))

        __sortingEnabled2 = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        ___qlistwidgetitem15 = self.listWidget_5.item(0)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Test111", None));
        ___qlistwidgetitem16 = self.listWidget_5.item(1)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Test222", None));
        ___qlistwidgetitem17 = self.listWidget_5.item(2)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Test333", None));
        self.listWidget_5.setSortingEnabled(__sortingEnabled2)

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+ Add a list", None))
    # retranslateUi

