# from PySide6.QtCore import QCoreApplication, QSize, Qt
# from PySide6.QtGui import QCursor, QFont
# from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QFrame,
#                                QLabel, QListWidget, QListWidgetItem,
#                                QMainWindow, QPushButton, QSizePolicy,
#                                QSpacerItem, QVBoxLayout, QWidget)
from typing import Callable

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from db import Database
from kanbaru_objects import Board, Card, List
from ui.app_settings import AppSettings
from ui.board_settings import BoardSettings
from ui.card_description import CardDescription
from ui.ui_main import Ui_MainWindow
from utils import setupFontDB


class MainScreen(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_MainWindow()
        parent.ui.setupUi(parent)

        title = "12345678901234567890123456789012345678901234567890"
        parent.ui.label_board.setText(title[:40] + (title[40:] and '...'))

        boards = Database.getInstance().boards

        for board in boards:
            qpushbutton = self.boardFactory(parent, board, "TorusPro.ttf")
            parent.ui.verticalLayout_4.addWidget(qpushbutton)

        parent.ui.vertSpacer_scrollAreaContent = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        parent.ui.verticalLayout_4.addItem(
            parent.ui.vertSpacer_scrollAreaContent)

        self.addListButton(parent, "TorusPro.ttf")

        parent.ui.btn_app_settings.clicked.connect(
            lambda: self.showAppSettings(parent))
        parent.ui.btn_board_settings.clicked.connect(
            lambda: self.showBoardSettings(parent))
        parent.ui.btn_add_board.clicked.connect(
            lambda: self.addBoard(parent))

        parent.ui.btn_app_settings.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent, self.showAppSettings(parent))
        parent.ui.btn_board_settings.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent, self.showBoardSettings(parent))
        parent.ui.btn_add_board.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent, self.addBoard(parent))

        self.setupFont(parent, "TorusPro.ttf")

    # connect drag and drop to move card between List
    

    def boardFactory(self, parent: Ui_MainWindow, board: Board, font: str) -> QPushButton:
        """Creates a board widget.

        Parameters
        ----------
        parent : QMainWindow
            The parent window.
        board : Board
            The board object.
        font : str
            The font to use.

        Returns
        -------
        QPushButton
            The board widget.
        """
        parent.ui.btn_board = QPushButton(
            parent.ui.scrollAreaContent_panel_left)
        parent.ui.btn_board.setObjectName(u"btn_board")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            parent.ui.btn_board.sizePolicy().hasHeightForWidth())
        parent.ui.btn_board.setSizePolicy(sizePolicy)
        parent.ui.btn_board.setMinimumSize(QSize(0, 40))
        parent.ui.btn_board.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_board.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_board.setStyleSheet(u"QPushButton {background-color: #6badee; color: #ffffff; border-radius: 5px}\n"
                                          "QPushButton:hover {background-color: #7e828c;}\n"
                                          "QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        parent.ui.btn_board.setText(
            board.title[:12] + (board.title[12:] and '...'))
        fontDB = setupFontDB(font)[0]
        parent.ui.btn_board.setFont(QFont(fontDB, 12))

        for list in board.lists:
            qwidget = self.listFactory(parent, list, font)
            parent.ui.horizontalLayout_5.addWidget(qwidget)

        return parent.ui.btn_board

    def listFactory(self, parent: Ui_MainWindow, list: List, font: str) -> QWidget:
        """Creates a list widget.

        Parameters
        ----------
        parent : QMainWindow
            The parent window.
        list : List
            The list object.
        font : str
            The font to use.

        Returns
        -------
        QWidget
            The list widget.
        """
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
        parent.ui.widget = QWidget(parent.ui.list)
        parent.ui.widget.setObjectName(u"widget_list_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            parent.ui.widget.sizePolicy().hasHeightForWidth())
        parent.ui.widget.setSizePolicy(sizePolicy3)
        parent.ui.widget.setStyleSheet(u"background-color: #ebecf0;\n"
                                       "border-radius: 10px;")
        parent.ui.verticalLayout_2 = QVBoxLayout(parent.ui.widget)
        parent.ui.verticalLayout_2.setObjectName(u"verticalLayout_11")
        parent.ui.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        parent.ui.label_list = QLabel(parent.ui.widget)
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

        parent.ui.verticalLayout_2.addWidget(parent.ui.label_list)

        parent.ui.listWidget = QListWidget(parent.ui.widget)

        parent.ui.listWidget.setObjectName(u"listWidget_list_1")
        sizePolicy2.setHeightForWidth(
            parent.ui.listWidget.sizePolicy().hasHeightForWidth())
        parent.ui.listWidget.setSizePolicy(sizePolicy2)
        parent.ui.listWidget.setMaximumSize(QSize(250, 16777215))
        parent.ui.listWidget.setFocusPolicy(Qt.TabFocus)
        parent.ui.listWidget.setAcceptDrops(True)
        parent.ui.listWidget.setStyleSheet(u"QListWidget {background-color: #ebecf0; border-radius: 10px;}\n"
                                           "QListWidget::item {height: 40px; padding: 0px 8px 0px 8px}\n"
                                           "QListWidget::item {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255)); color: #000000; border-radius: 5px}\n"
                                           "QListWidget::item:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(226, 228, 233, 255), stop:1 rgba(226, 228, 233, 255)); color: #000000}\n"
                                           "QListWidget::item:selected {background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
                                           "QListWidget::item:focus {background-color: qlineargradient(spread:pad, x1:0"
                                           ", y1:0.5, x2:0.95, y2:0.5, stop:0 rgba(251, 217, 69, 255), stop:0.0338983 rgba(251, 217, 69, 255), stop:0.039548 rgba(204, 204, 204, 255), stop:1 rgba(204, 204, 204, 255)); color: #000000}\n"
                                           "QScrollBar:vertical {width: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}\n"
                                           "QScrollBar:horizontal {height: 10px; margin: 0px 0px 0px 0px; background-color: #acb2bf}")
        parent.ui.listWidget.setFrameShape(QFrame.NoFrame)
        parent.ui.listWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustIgnored)
        parent.ui.listWidget.setAutoScroll(True)
        parent.ui.listWidget.setDragEnabled(True)
        parent.ui.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        parent.ui.listWidget.setDefaultDropAction(Qt.MoveAction)
        parent.ui.listWidget.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        parent.ui.listWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        parent.ui.listWidget.setHorizontalScrollMode(
            QAbstractItemView.ScrollPerPixel)
        parent.ui.listWidget.setProperty("isWrapping", False)
        parent.ui.listWidget.setSpacing(5)
        parent.ui.listWidget.setUniformItemSizes(True)
        parent.ui.listWidget.setWordWrap(True)
        parent.ui.listWidget.setSelectionRectVisible(True)

        parent.ui.verticalLayout_2.addWidget(parent.ui.listWidget)

        parent.ui.widget_add_card = QWidget(parent.ui.widget)
        parent.ui.widget_add_card.setObjectName(u"widget_add_card")
        sizePolicy1.setHeightForWidth(
            parent.ui.widget_add_card.sizePolicy().hasHeightForWidth())
        parent.ui.widget_add_card.setSizePolicy(sizePolicy1)
        parent.ui.verticalLayout_3 = QVBoxLayout(parent.ui.widget_add_card)
        parent.ui.verticalLayout_3.setObjectName(u"verticalLayout_6")
        parent.ui.verticalLayout_3.setContentsMargins(6, 0, 6, 6)
        parent.ui.btn_add_card = QPushButton(parent.ui.widget_add_card)
        parent.ui.btn_add_card.setObjectName(u"btn_add_card_list_1")
        parent.ui.btn_add_card.setMinimumSize(QSize(0, 25))
        parent.ui.btn_add_card.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_add_card.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_add_card.setStyleSheet(u"QPushButton {background-color: #ebecf0; color: #6a758b; border-radius: 5px}\n"
                                             "QPushButton:hover {background-color: #dadbe2; color: #505b76}\n"
                                             "QPushButton:focus {border-color: #000000; border-width: 1.5px; border-style: solid;}")

        parent.ui.verticalLayout_3.addWidget(parent.ui.btn_add_card)

        parent.ui.verticalLayout_2.addWidget(parent.ui.widget_add_card)

        parent.ui.verticalLayout_1.addWidget(parent.ui.widget)

        parent.ui.label_list.setText(
            QCoreApplication.translate("MainWindow", list.title[:25] + (list.title[25:] and '...'), None))

        parent.ui.listWidget.setSortingEnabled(False)

        parent.ui.btn_add_card.setText(
            QCoreApplication.translate("MainWindow", u"+ Add a card", None))

        fontDB = setupFontDB(font)
        parent.ui.label_list.setFont(QFont(fontDB[0], 12, QFont.Bold))
        parent.ui.btn_add_card.setFont(QFont(fontDB[0], 12))

        for card in list.cards:
            qlistwidgetitem = self.cardFactory(parent, card, font)
            parent.ui.listWidget.addItem(qlistwidgetitem)
            parent.ui.listWidget.clicked.connect(
                lambda: self.showCardDescription(parent, card))
        return parent.ui.list

    def cardFactory(self, parent: Ui_MainWindow, card: Card, font: str) -> QListWidgetItem:
        """Create a card item

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        card : Card
            The card to create
        font : str
            The font to use

        Returns
        -------
        QListWidgetItem
            The card item
        """
        qlistwidgetitem = QListWidgetItem(parent.ui.listWidget)
        qlistwidgetitem.setFlags(
            Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        qlistwidgetitem = parent.ui.listWidget.item(0)
        qlistwidgetitem.setText(
            QCoreApplication.translate("MainWindow", card.title[:24] + (card.title[24:] and '...'), None))
        fontDB = setupFontDB(font)[0]
        qlistwidgetitem.setFont(QFont(fontDB, 12))
        return qlistwidgetitem

    def addListButton(self, parent: Ui_MainWindow, font: str) -> None:
        """Add a button to add a new list

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        font : str
            The font to use
        """
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

        fontDB = setupFontDB(font)[0]
        parent.ui.btn_add_list.setFont(QFont(fontDB, 12))

    def showAppSettings(self, parent: Ui_MainWindow) -> None:
        self.appSettings = AppSettings(parent)
        self.appSettings.setWindowModality(Qt.ApplicationModal)
        self.appSettings.show()

    def showBoardSettings(self, parent: Ui_MainWindow) -> None:
        self.boardSettings = BoardSettings()
        self.boardSettings.setWindowModality(Qt.ApplicationModal)
        self.boardSettings.show()

    def showCardDescription(self, parent: Ui_MainWindow, card: Card) -> None:
        self.cardDescription = CardDescription(card)
        self.cardDescription.setWindowModality(Qt.ApplicationModal)
        self.cardDescription.show()

    def addBoard(self, parent: Ui_MainWindow) -> None:
        ...

    def setupFont(self, parent: Ui_MainWindow, font: str | list[str]) -> None:
        toruspro = setupFontDB(font)[0]
        parent.ui.label_logo.setFont(QFont(toruspro, 36))
        parent.ui.label_board.setFont(QFont(toruspro, 28))
        parent.ui.btn_add_board.setFont(QFont(toruspro, 12))
        parent.ui.btn_board_settings.setFont(QFont(toruspro, 12))
        parent.ui.btn_app_settings.setFont(QFont(toruspro, 12))

    def keyPressEvent(self, event: QKeyEvent, parent: Ui_MainWindow = None, function: Callable = None) -> None | Callable:
        """This function is used to call a function when the enter key is pressed

        Parameters
        ----------
        event : QKeyEvent
            The key event
        function : Callable
            The function to call
        parent : Ui_MainWindow, optional
            The parent window, by default None
        """
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if not function:
                return None
            if not parent:
                return function()
            return function(parent)
