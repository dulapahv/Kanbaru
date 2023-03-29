import logging
from typing import Callable, List

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from db import Database
from kanbaru_objects import Board
from ui.ui_app_settings import Ui_SettingsWindow
from utils import dialog_factory, setup_font_db


class AppSettings(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_SettingsWindow = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.ui.btn_delete.clicked.connect(
            lambda: dialog_factory(None, self.delete, "Delete Board",
                                   "Are you sure you want to delete selected board?\nThis action cannot be undone."))
        self.ui.btn_rename.clicked.connect(self.rename)
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_logout.clicked.connect(
            lambda: dialog_factory(parent, self.logout, "Logout", "Are you sure you want to logout?"))
        self.ui.btn_delete_account.clicked.connect(
            lambda: dialog_factory(parent, self.delete_account, "Delete Account",
                                   "Are you sure you want to delete your account?\nThis action cannot be undone."))

        self.ui.btn_delete.keyPressEvent = lambda event: self.keyPressEvent(
            event, dialog_factory(None, self.delete, "Delete Board",
                                  "Are you sure you want to delete selected board?\nThis action cannot be undone."))
        self.ui.btn_rename.keyPressEvent = lambda event: self.keyPressEvent(
            event, function=self.rename)
        self.ui.btn_cancel.keyPressEvent = lambda event: self.keyPressEvent(
            event, function=self.close)
        self.ui.btn_save.keyPressEvent = lambda event: self.keyPressEvent(
            event, function=self.save)
        self.ui.btn_logout.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent,
            dialog_factory(parent, self.logout, "Logout", "Are you sure you want to logout?"))
        self.ui.btn_delete_account.keyPressEvent = lambda event: self.keyPressEvent(
            event, parent, dialog_factory(parent, self.delete_account, "Delete Account",
                                          "Are you sure you want to delete your account?\nThis action cannot be undone."))

        self.setup_font()

    @staticmethod
    def dialog_factory(parent: QMainWindow, function: Callable, title: str, msg: str) -> None:
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setWindowTitle(title)
        dialog.setText(msg)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if dialog.exec() == QMessageBox.Yes:
            function(parent)

    def delete(self) -> None:
        ...

    def rename(self) -> None:
        ...

    def save(self) -> None:
        ...

    @property
    def board_all(self) -> List[Board]:
        ...

    @board_all.setter
    def board_all(self, board: Board | List[Board]) -> None:
        ...

    def logout(self, parent: QMainWindow):
        Database.get_instance().logout()
        logging.info("Going to welcome screen...")
        self.close()
        from ui.welcome import WelcomeScreen
        WelcomeScreen(parent)

    def delete_account(self, parent: QMainWindow):
        Database.get_instance().delete_account()
        logging.info("Going to welcome screen...")
        self.close()
        from ui.welcome import WelcomeScreen
        WelcomeScreen(parent)

    def setup_font(self) -> None:
        toruspro = setup_font_db("TorusPro.ttf")[0]
        self.ui.label_app_settings.setFont(QFont(toruspro, 28))
        self.ui.label_manage_board.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_account.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_board_desc.setFont(QFont(toruspro, 11))
        self.ui.btn_delete.setFont(QFont(toruspro, 12))
        self.ui.btn_rename.setFont(QFont(toruspro, 12))
        self.ui.btn_logout.setFont(QFont(toruspro, 12))
        self.ui.btn_delete_account.setFont(QFont(toruspro, 12))
        self.ui.btn_cancel.setFont(QFont(toruspro, 12))
        self.ui.btn_save.setFont(QFont(toruspro, 12))

    def keyPressEvent(self, event: QKeyEvent, parent: Ui_SettingsWindow = None,
                      function: Callable = None) -> None | Callable:
        """This function is used to call a function when the enter key is pressed

        Parameters
        ----------
        event : QKeyEvent
            The key event
        function : Callable
            The function to call
        parent : Ui_SettingsWindow, optional
            The parent window, by default None
        """
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if not function:
                return None
            if not parent:
                return function()
            return function(parent)
