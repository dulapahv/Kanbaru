from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from kanbaru_objects import Card, Board, List
from ui.ui_board_settings import Ui_BoardWindow
from utils import dialogFactory


class BoardSettings(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_BoardWindow = Ui_BoardWindow()
        self.ui.setupUi(self)

        self.ui.btn_delete_list.clicked.connect(
            lambda: dialogFactory(None, self.deleteList, "Delete List Confirmation", "Are you sure you want to delete this list?\nThis action cannot be undone."))

        self.ui.btn_cancel.clicked.connect(self.close)

    def deleteList(self):
        ...
