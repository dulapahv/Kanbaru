from typing import Callable

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from kanbaru_objects import List
from ui.ui_board_settings import Ui_BoardWindow
from utils import dialog_factory, setup_font_db


class BoardSettings(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.title_txt = None
        self.ui: Ui_BoardWindow = Ui_BoardWindow()
        self.ui.setupUi(self)

        self.ui.btn_delete.clicked.connect(
            lambda: dialog_factory(None, self.delete, "Delete List Confirmation",
                                   "Are you sure you want to delete selected list?\nThis action cannot be undone."))
        self.ui.btn_rename.clicked.connect(self.rename)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_cancel.clicked.connect(self.close)

        self.ui.btn_delete.keyPressEvent = lambda event: self.keyPressEvent(
            event, self.delete)
        self.ui.btn_rename.keyPressEvent = lambda event: self.keyPressEvent(
            event, self.rename)
        self.ui.btn_save.keyPressEvent = lambda event: self.keyPressEvent(
            event, self.save)
        self.ui.btn_cancel.keyPressEvent = lambda event: self.keyPressEvent(
            event, self.close)

        self.setup_font()

    def delete(self) -> None:
        ...

    def rename(self) -> None:
        ...

    def save(self) -> None:
        ...

    @property
    def title(self) -> str:
        return self.title_txt

    @property
    def color(self) -> str:
        if self.ui.btn_color_1.isChecked():
            return "Light blue"
        if self.ui.btn_color_2.isChecked():
            return "Rose"
        if self.ui.btn_color_3.isChecked():
            return "Gold"
        if self.ui.btn_color_4.isChecked():
            return "Green"
        if self.ui.btn_color_5.isChecked():
            return "Lavender"
        if self.ui.btn_color_6.isChecked():
            return "Teal"

    @property
    def list_all(self) -> list[List]:
        ...

    @title.setter
    def title(self, text: str) -> None:
        self.ui.lineEdit_title.setText(text)

    @color.setter
    def color(self, color: str) -> None:
        if color == "Light blue":
            self.ui.btn_color_1.setChecked(True)
        elif color == "Rose":
            self.ui.btn_color_2.setChecked(True)
        elif color == "Gold":
            self.ui.btn_color_3.setChecked(True)
        elif color == "Green":
            self.ui.btn_color_4.setChecked(True)
        elif color == "Lavender":
            self.ui.btn_color_5.setChecked(True)
        elif color == "Teal":
            self.ui.btn_color_6.setChecked(True)

    @list_all.setter
    def list_all(self, lists: list[List]) -> None:
        ...

    def title_listener(self, text: str) -> None:
        self.title_txt = text

    def setup_font(self) -> None:
        notosans = setup_font_db("NotoSans.ttf")[0]
        toruspro = setup_font_db("TorusPro.ttf")[0]
        self.ui.label_board_desc.setFont(QFont(toruspro, 28))
        self.ui.label_title.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_color.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_list.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_list_desc.setFont(QFont(toruspro, 11))
        self.ui.lineEdit_title.setFont(QFont(notosans, 12))
        self.ui.btn_color_1.setFont(QFont(toruspro, 12))
        self.ui.btn_color_2.setFont(QFont(toruspro, 12))
        self.ui.btn_color_3.setFont(QFont(toruspro, 12))
        self.ui.btn_color_4.setFont(QFont(toruspro, 12))
        self.ui.btn_color_5.setFont(QFont(toruspro, 12))
        self.ui.btn_color_6.setFont(QFont(toruspro, 12))
        self.ui.listWidget_manage_list.setFont(QFont(toruspro, 12))
        self.ui.btn_delete.setFont(QFont(toruspro, 12))
        self.ui.btn_rename.setFont(QFont(toruspro, 12))
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
