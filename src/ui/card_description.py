from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from kanbaru_objects import Card, Board, List
from ui.ui_card_description import Ui_CardWindow


class CardDescription(QMainWindow):
    def __init__(self, card: Card) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_CardWindow = Ui_CardWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_title.setText(card.title)
        self.ui.calendarWidget.setSelectedDate(
            QDate.fromString("06-03-2023", "dd-MM-yyyy"))
        self.ui.timeEdit.setTime(QTime.fromString(card.time, "hh:mm"))
        self.ui.textEdit_description.setText(card.description)
