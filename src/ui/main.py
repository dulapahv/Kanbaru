from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.ui_main import Ui_MainWindow


class MainScreen(QMainWindow):
    def __init__(self, parent: QMainWindow = None) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_MainWindow()
        parent.ui.setupUi(parent)
