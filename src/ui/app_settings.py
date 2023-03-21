from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from kanbaru_objects import Card, Board, List
from ui.ui_app_settings import Ui_SettingsWindow


class AppSettings(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_SettingsWindow = Ui_SettingsWindow()
        self.ui.setupUi(self)