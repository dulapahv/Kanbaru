from typing import Callable

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from kanbaru_objects import Board, Card, List
from ui.ui_card_description import Ui_CardWindow
from utils import dialogFactory, setupFontDB


class CardDescription(QMainWindow):
    def __init__(self, card: Card) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_CardWindow = Ui_CardWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_title.textChanged.connect(self.title_listener)

        self.ui.btn_delete.clicked.connect(
            lambda: dialogFactory(None, self.delete, "Delete Card Confirmation", "Are you sure you want to delete this card?\nThis action cannot be undone."))
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save)

        self.ui.btn_delete.keyPressEvent = lambda event: self.keyPressEvent(
            event, self.delete)
        self.ui.btn_cancel.keyPressEvent = lambda event: self.keyPressEvent(
            event, self.close)
        self.ui.btn_save.keyPressEvent = lambda event: self.keyPressEvent(
            event, self.save)

        self.title = card.title
        self.date = card.date
        self.time = card.time
        self.description = card.description

        self.setupFont()

    def save(self) -> None:
        ...

    def delete(self) -> None:
        ...

    @property
    def title(self) -> str:
        return self.title_txt

    @property
    def date(self) -> str:
        return self.ui.calendarWidget.selectedDate().toString("dd-MM-yyyy")

    @property
    def time(self) -> str:
        return self.ui.timeEdit.time().toString("hh:mm")

    @property
    def description(self) -> str:
        return self.ui.textEdit_description.toPlainText()

    @title.setter
    def title(self, title: str) -> None:
        self.ui.lineEdit_title.setText(title)

    @date.setter
    def date(self, date: str) -> None:
        self.ui.calendarWidget.setSelectedDate(
            QDate.fromString(date, "dd-MM-yyyy"))

    @time.setter
    def time(self, time: str) -> None:
        self.ui.timeEdit.setTime(QTime.fromString(time, "hh:mm"))

    @description.setter
    def description(self, description: str) -> None:
        self.ui.textEdit_description.setText(description)

    def title_listener(self, text: str) -> None:
        self.title_txt = text

    def setupFont(self) -> None:
        notosans = setupFontDB("NotoSans.ttf")[0]
        toruspro = setupFontDB("TorusPro.ttf")[0]
        self.ui.label_card_desc.setFont(QFont(toruspro, 28))
        self.ui.label_title.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_date.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_time.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_description.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_card_info.setFont(QFont(toruspro, 11))
        self.ui.lineEdit_title.setFont(QFont(notosans, 12))
        self.ui.calendarWidget.setFont(QFont(notosans, 12))
        self.ui.timeEdit.setFont(QFont(notosans, 12))
        self.ui.textEdit_description.setFont(QFont(notosans, 12))
        self.ui.btn_delete.setFont(QFont(toruspro, 12))
        self.ui.btn_cancel.setFont(QFont(toruspro, 12))
        self.ui.btn_save.setFont(QFont(toruspro, 12))

    def keyPressEvent(self, event: QKeyEvent, function: Callable = None) -> None | Callable:
        """This function is used to call a function when the enter key is pressed

        Parameters
        ----------
        event : QKeyEvent
            The key event
        function : Callable
            The function to call
        """
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if not function:
                return function
            return function()
