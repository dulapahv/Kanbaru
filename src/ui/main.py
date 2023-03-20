from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from auth import Auth
from db import Database
from ui.ui_main import Ui_MainWindow
from utils import setupFontDB

# from PySide6.QtCore import (QObject)
# from PySide6.QtGui import (QFont, QFontDatabase)
# from PySide6.QtWidgets import (QApplication, QMainWindow)


class MainScreen(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_MainWindow()
        parent.ui.setupUi(parent)

        boards = Database.getInstance().boards

        for board in boards:
            for list in board.lists:
                self.listFactory(parent, list)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        parent.ui.list_add = QWidget(parent.ui.scrollAreaContent_panel_right)
        parent.ui.list_add.setObjectName(u"list_add")
        sizePolicy.setHeightForWidth(
            parent.ui.list_add.sizePolicy().hasHeightForWidth())
        parent.ui.list_add.setSizePolicy(sizePolicy)
        parent.ui.list_add.setMinimumSize(QSize(250, 0))
        parent.ui.verticalLayout_9 = QVBoxLayout(parent.ui.list_add)
        parent.ui.verticalLayout_9.setSpacing(0)
        parent.ui.verticalLayout_9.setObjectName(u"verticalLayout_9")
        parent.ui.verticalLayout_9.setContentsMargins(0, 0, 6, 0)
        parent.ui.btn_add_list = QPushButton(parent.ui.list_add)
        parent.ui.btn_add_list.setObjectName(u"btn_add_list")
        parent.ui.btn_add_list.setMinimumSize(QSize(0, 30))
        parent.ui.btn_add_list.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_add_list.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_add_list.setStyleSheet(u"QPushButton {background-color: #acb2bf; color: #ffffff; border-radius: 5px}\n"
                                             "QPushButton:hover {background-color: #7e828c;}\n"
                                             "QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        parent.ui.verticalLayout_9.addWidget(parent.ui.btn_add_list)

        parent.ui.vertSpacer_list_add = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        parent.ui.verticalLayout_9.addItem(parent.ui.vertSpacer_list_add)
        parent.ui.btn_add_list.setText(
            QCoreApplication.translate("MainWindow", u"+ Add a list", None))

        parent.ui.scrollAreaContent_panel_right.layout().addWidget(parent.ui.list_add)
        parent.ui.horzSpacer_panel_right = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        parent.ui.horizontalLayout_5.addItem(parent.ui.horzSpacer_panel_right)

        # self.setupFont(parent, "TorusPro.ttf")

    def listFactory(self, parent: Ui_MainWindow, board: dict) -> QWidget:
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        parent.ui.list = QWidget(parent.ui.scrollAreaContent_panel_right)
        parent.ui.list.setObjectName(u"list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            parent.ui.list.sizePolicy().hasHeightForWidth())
        parent.ui.list.setSizePolicy(sizePolicy2)
        parent.ui.list.setMinimumSize(QSize(250, 0))
        parent.ui.list.setStyleSheet(u"")
        parent.ui.verticalLayout_1 = QVBoxLayout(parent.ui.list)
        parent.ui.verticalLayout_1.setSpacing(0)
        parent.ui.verticalLayout_1.setObjectName(u"verticalLayout_1")
        parent.ui.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        parent.ui.widget_list_1 = QWidget(parent.ui.list)
        parent.ui.widget_list_1.setObjectName(u"widget_list_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            parent.ui.widget_list_1.sizePolicy().hasHeightForWidth())
        parent.ui.widget_list_1.setSizePolicy(sizePolicy3)
        parent.ui.widget_list_1.setStyleSheet(u"background-color: #ebecf0;\n"
                                              "border-radius: 10px;")
        parent.ui.verticalLayout_11 = QVBoxLayout(parent.ui.widget_list_1)
        parent.ui.verticalLayout_11.setObjectName(u"verticalLayout_11")
        parent.ui.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        parent.ui.label_list = QLabel(parent.ui.widget_list_1)
        parent.ui.label_list.setObjectName(u"label_list")
        sizePolicy1.setHeightForWidth(
            parent.ui.label_list.sizePolicy().hasHeightForWidth())
        parent.ui.label_list.setSizePolicy(sizePolicy1)
        parent.ui.label_list.setMinimumSize(QSize(0, 30))
        parent.ui.label_list.setStyleSheet(u"color: #282c33;\n"
                                             "background-color: #ebecf0;\n"
                                             "border-radius: 5px;\n"
                                             "padding: 5px 0px 0px 5px;")
        parent.ui.label_list.setMargin(0)

        parent.ui.verticalLayout_11.addWidget(parent.ui.label_list)

        parent.ui.listWidget_list_1 = QListWidget(parent.ui.widget_list_1)
        __qlistwidgetitem = QListWidgetItem(parent.ui.listWidget_list_1)
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable |
                                   Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

        parent.ui.listWidget_list_1.setObjectName(u"listWidget_list_1")
        sizePolicy2.setHeightForWidth(
            parent.ui.listWidget_list_1.sizePolicy().hasHeightForWidth())
        parent.ui.listWidget_list_1.setSizePolicy(sizePolicy2)
        parent.ui.listWidget_list_1.setMaximumSize(QSize(250, 16777215))
        parent.ui.listWidget_list_1.setFocusPolicy(Qt.TabFocus)
        parent.ui.listWidget_list_1.setAcceptDrops(True)
        parent.ui.listWidget_list_1.setStyleSheet(u"QListWidget {background-color: #ebecf0; border-radius: 10px;}\n"
                                                  "QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
                                                  "QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
                                                  "QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(226, 228, 233, 255), stop:1 rgba(226, 228, 233, 255)); color: #000000}\n"
                                                  "QListWidget::item:selected {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
                                                  "QListWidget::item:focus {background-color: qlineargradient(spread:pad, x1:0"
                                                  ", y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
                                                  "QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
                                                  "QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        parent.ui.listWidget_list_1.setFrameShape(QFrame.NoFrame)
        parent.ui.listWidget_list_1.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustIgnored)
        parent.ui.listWidget_list_1.setAutoScroll(True)
        parent.ui.listWidget_list_1.setDragEnabled(True)
        parent.ui.listWidget_list_1.setDragDropMode(QAbstractItemView.DragDrop)
        parent.ui.listWidget_list_1.setDefaultDropAction(Qt.MoveAction)
        parent.ui.listWidget_list_1.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        parent.ui.listWidget_list_1.setVerticalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        parent.ui.listWidget_list_1.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        parent.ui.listWidget_list_1.setProperty("isWrapping", False)
        parent.ui.listWidget_list_1.setSpacing(5)
        parent.ui.listWidget_list_1.setUniformItemSizes(True)
        parent.ui.listWidget_list_1.setWordWrap(True)
        parent.ui.listWidget_list_1.setSelectionRectVisible(True)

        parent.ui.verticalLayout_11.addWidget(parent.ui.listWidget_list_1)

        parent.ui.widget_add_card = QWidget(parent.ui.widget_list_1)
        parent.ui.widget_add_card.setObjectName(u"widget_add_card")
        sizePolicy1.setHeightForWidth(
            parent.ui.widget_add_card.sizePolicy().hasHeightForWidth())
        parent.ui.widget_add_card.setSizePolicy(sizePolicy1)
        parent.ui.verticalLayout_6 = QVBoxLayout(parent.ui.widget_add_card)
        parent.ui.verticalLayout_6.setObjectName(u"verticalLayout_6")
        parent.ui.verticalLayout_6.setContentsMargins(6, 0, 6, 6)
        parent.ui.btn_add_card_list_1 = QPushButton(parent.ui.widget_add_card)
        parent.ui.btn_add_card_list_1.setObjectName(u"btn_add_card_list_1")
        parent.ui.btn_add_card_list_1.setMinimumSize(QSize(0, 25))
        parent.ui.btn_add_card_list_1.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_add_card_list_1.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_add_card_list_1.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
                                                    "QPushButton:hover {background-color: #dadbe2; color: #505b76}\n"
                                                    "QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        parent.ui.verticalLayout_6.addWidget(parent.ui.btn_add_card_list_1)

        parent.ui.verticalLayout_11.addWidget(parent.ui.widget_add_card)

        parent.ui.verticalLayout_1.addWidget(parent.ui.widget_list_1)

        parent.ui.horizontalLayout_5.addWidget(parent.ui.list)

        parent.ui.label_list.setText(
            QCoreApplication.translate("MainWindow", u"To Do", None))

        __sortingEnabled = parent.ui.listWidget_list_1.isSortingEnabled()
        parent.ui.listWidget_list_1.setSortingEnabled(False)
        ___qlistwidgetitem = parent.ui.listWidget_list_1.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"Test1", None))

        parent.ui.btn_add_card_list_1.setText(
            QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        return parent.ui.list

    def setupFont(self, parent: Ui_MainWindow, font: str | list[str]) -> None:
        fontDB = setupFontDB(font)
        parent.ui.label_logo.setFont(QFont(fontDB[0], 36))
        parent.ui.label_board.setFont(QFont(fontDB[0], 28))
        parent.ui.label_list.setFont(QFont(fontDB[0], 12, QFont.Bold))
        parent.ui.btn_add_card_list_1.setFont(QFont(fontDB[0], 12))
        parent.ui.btn_add_list.setFont(QFont(fontDB[0], 12))
