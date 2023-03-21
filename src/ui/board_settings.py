from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from kanbaru_objects import Card, Board, List
from ui.ui_board_settings import Ui_BoardWindow


class BoardSettings(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_BoardWindow = Ui_BoardWindow()
        self.ui.setupUi(self)
