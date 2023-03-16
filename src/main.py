import os
import sys
import logging
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
# from PySide6.QtCore import (QObject)
# from PySide6.QtGui import (QFont, QFontDatabase)
# from PySide6.QtWidgets import (QApplication, QMainWindow)
# from ui.ui_main import Ui_MainWindow
from ui.ui_welcome import Ui_WelcomeWindow
from auth import Auth
from db import Database


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        # Determine current directory and get a path. If it's in the not in the src folder, go into src
        self.path = os.path.dirname(os.path.abspath(__file__))
        if os.path.basename(self.path) != "src":
            self.path = os.path.join(self.path, "src")

        # Set up logging
        logging.basicConfig(filename=f'{os.path.join(self.path,"eventlog.log")}', filemode='w',
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.DEBUG)

        logging.info("Starting Kanbaru")
        logging.info(f'Current directory: "{self.path}"')

        # Determine database path. Set self.db_path to Documents in windows, and home in Unix
        if sys.platform == "win32":
            logging.info("Windows OS detected")
            self.db_path = os.path.join(os.path.expanduser(
                "~"), "Documents", "Kanbaru", "Database.json")
        else:
            logging.info("Unix OS detected")
            self.db_path = os.path.expanduser(
                "~", "Kanbaru", "Database.json")

        # Set up database
        db = Database.getInstance()
        db.setDBPath(self.db_path)
        db.read()
        logging.info("Database instance initialized successfully")
        logging.info(f'Database path: "{db.getDBPath()}"')

        # Setup WelcomeWindow
        self.ui_welcome = Ui_WelcomeWindow()
        self.ui_welcome.setupUi(self)

        self.ui_welcome.btn_login.clicked.connect(lambda: Auth.login())

        # # Set up font
        # fontPath = "./resources/font/TorusPro-Regular.ttf"
        # if not os.path.exists(fontPath):
        #     fontPath = "./src/resources/font/TorusPro-Regular.ttf"
        # fontDatabase = QFontDatabase.addApplicationFont(fontPath)
        # if fontDatabase < 0:
        #     raise Exception(f'Font not found at path "{fontPath}"! Exiting...')

        # # Add font to font database
        # fontFamilies = QFontDatabase.applicationFontFamilies(fontDatabase)

        # # Set up UI
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

        # # Set font for all widgets
        # for obj in self.findChildren(QObject):
        #     if hasattr(obj, "setFont"):
        #         obj.setFont(QFont(fontFamilies[0], 12))
        # self.ui.label_list_1.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        # self.ui.label_list_2.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        # self.ui.label_list_3.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        # self.ui.label_logo.setFont(QFont(fontFamilies[0], 36))
        # self.ui.label_board.setFont(QFont(fontFamilies[0], 28))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
