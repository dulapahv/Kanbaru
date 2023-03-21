import logging

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from db import Database
from kanbaru_objects import Board, Card, List
from ui.ui_app_settings import Ui_SettingsWindow
from utils import dialogFactory


class AppSettings(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_SettingsWindow = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)

        self.ui.btn_delete_board.clicked.connect(
            lambda: dialogFactory(None, self.deleteBoard, "Delete Board Confirmation", "Are you sure you want to delete this board?\nThis action cannot be undone."))

        self.ui.btn_logout.clicked.connect(
            lambda: dialogFactory(parent, self.logout, "Logout Confirmation", "Are you sure you want to logout?"))

        self.ui.btn_delete_account.clicked.connect(
            lambda: dialogFactory(parent, self.deleteAccount, "Delete Account Confirmation", "Are you sure you want to delete your account?\nThis action cannot be undone."))

    def dialogFactory(self, parent: QMainWindow, function: callable, title: str, msg: str) -> None:
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        dialog.setWindowTitle(title)
        dialog.setText(msg)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if dialog.exec() == QMessageBox.Yes:
            function(parent)

    def deleteBoard(self):
        ...

    def logout(self, parent: QMainWindow):
        Database.getInstance().logout()
        logging.info("Going to welcome screen...")
        self.close()
        from ui.welcome import WelcomeScreen
        WelcomeScreen(parent)

    def deleteAccount(self, parent: QMainWindow):
        Database.getInstance().deleteAccount()
        logging.info("Going to welcome screen...")
        self.close()
        from ui.welcome import WelcomeScreen
        WelcomeScreen(parent)
