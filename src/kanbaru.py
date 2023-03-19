import logging
import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from auth import Auth
from db import Database
# from PySide6.QtCore import (QObject)
# from PySide6.QtGui import (QFont, QFontDatabase)
# from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui.ui_main import Ui_MainWindow
from ui.ui_welcome import Ui_WelcomeWindow


class Kanbaru(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        # Get current directory
        self.path = self.getCurrentDirectory()

        # Set up event logger
        self.initEventLogger(os.path.join(
            self.path, "event.log"), "%(asctime)s - %(levelname)s - %(message)s", debug=True)

        logging.info("Starting Kanbaru...")
        logging.info(f'Current directory: "{self.path}"')

        # Initialize local database
        self.initializeLocalDatabase()

        # Initialize Firebase database
        self.initializeFirebaseDatabase(Database.getInstance(), os.path.join(
            self.path, "resources", "kanbaru-credentials.json"))

        # Check if user is logged in, if not, prompt login
        if self.checkCredentials():
            Database.getInstance().pullFromFirebase(Database.getInstance().getUsername())
            self.showMainScreen()
        else:
            self.showWelcomeScreen()

    def initEventLogger(self, path: str, fmt: str, debug: bool = False) -> None:
        """Initializes the event logger.
          - Set the path of the event log file
          - Set the format of the event log file
          - Set the debug level of the event log file
          - Set up the event logger
        """
        logging.basicConfig(filename=path,
                            filemode='w',
                            format=fmt,
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.DEBUG if debug else logging.INFO)

    def getCurrentDirectory(self) -> str:
        """Returns the current directory of the application. If the current
        directory is not the src directory, it will be appended to the path.

        Returns
        -------
        path : str
            The current directory of the application.
        """
        self.path = os.path.dirname(os.path.abspath(__file__))
        if os.path.basename(self.path) != "src":
            self.path = os.path.join(self.path, "src")
        return self.path

    def initializeLocalDatabase(self) -> None:
        """Initializes the database instance.
          - Determine database path
          - Create database instance
          - Set database path
          - Read database file
        """
        if sys.platform == "win32":
            logging.info("Windows OS detected")
            self.db_path = os.path.join(os.path.expanduser(
                "~"), "Documents", "Kanbaru", "Database.json")
        else:
            logging.info("Unix OS detected")
            self.db_path = os.path.join(os.path.expanduser(
                "~"), "Kanbaru", "Database.json")
        db = Database.getInstance()
        db.setPath(self.db_path)
        db.read()
        logging.info(f'Database path: "{db.getPath()}"')
        logging.info("Database instance initialized and read successfully")

    def initializeFirebaseDatabase(self, db_instance: Database, cred_path: str) -> None:
        """Initializes the Firebase database instance.
          - Set database instance
          - Set credential path
          - Set up Firebase database
        """
        db_instance.initFirebase(cred_path)
        logging.info("Firebase database initialized and connected")

    def checkCredentials(self) -> bool:
        """Checks credentials from the database file.
            - Get username and password from database file
            - If username or password is empty, return False
            - If credentials are invalid, return False
        """
        return Auth.verifyCredentials(Database.getInstance().getUsername(), Database.getInstance().getPassword())

    def showWelcomeScreen(self):
        logging.info("Going to welcome screen...")
        self.ui_welcome = Ui_WelcomeWindow()
        self.ui_welcome.setupUi(self)

        self.ui_welcome.btn_login.clicked.connect(lambda: Auth.login())

    def showMainScreen(self):
        logging.info("Going to main screen...")
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

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
    window = Kanbaru()
    window.show()
    sys.exit(app.exec())
