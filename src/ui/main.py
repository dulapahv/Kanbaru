from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.ui_main import Ui_MainWindow

# from PySide6.QtCore import (QObject)
# from PySide6.QtGui import (QFont, QFontDatabase)
# from PySide6.QtWidgets import (QApplication, QMainWindow)


class MainScreen(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_MainWindow()
        parent.ui.setupUi(parent)
