import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
# from PySide6.QtCore import (QObject)
# from PySide6.QtGui import (QFont, QFontDatabase)
# from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up font
        fontPath = "./resources/font/TorusPro-Regular.ttf"
        if not os.path.exists(fontPath):
            fontPath = "./src/resources/font/TorusPro-Regular.ttf"
        fontDatabase = QFontDatabase.addApplicationFont(fontPath)
        if fontDatabase < 0:
            raise Exception(f'Font not found at path "{fontPath}"! Exiting...')

        # Add font to font database
        fontFamilies = QFontDatabase.applicationFontFamilies(fontDatabase)

        # Set up UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set font for all widgets
        for obj in self.findChildren(QObject):
            if hasattr(obj, "setFont"):
                obj.setFont(QFont(fontFamilies[0], 12))
        self.ui.label_list_1.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        self.ui.label_list_2.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        self.ui.label_list_3.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        self.ui.label_logo.setFont(QFont(fontFamilies[0], 36))
        self.ui.label_board.setFont(QFont(fontFamilies[0], 28))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
