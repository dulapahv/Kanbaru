import logging
import os
import sys

try:
    from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

    from auth import Auth
    from db import Database
    from ui.main import MainScreen
    from ui.welcome import WelcomeScreen
    from utils import getCurrentDirectory
except ModuleNotFoundError:
    from tkinter import messagebox, Tk
    root = Tk()
    root.withdraw()
    response = messagebox.askyesno("Error: Module Not Found",
        "Required modules not found. Would you like to install them now?\n\nRequired modules: PySide6, firebase-admin")

    if response:
        try:
            import pip
            pip.main(["install", "-r", "requirements.txt"])
        except ModuleNotFoundError:
            print("pip not found. Installing pip rn. Risky move, but I'll do it for you.\n btw why dont you have pip installed yet?")
            import ensurepip
            ensurepip.bootstrap()
            pip.main(["install", "-r", "requirements.txt"])
        finally:
            from PySide6.QtWidgets import (QApplication, QMainWindow,
                                           QMessageBox)

            from auth import Auth
            from db import Database
            from ui.main import MainScreen
            from ui.welcome import WelcomeScreen
            from utils import getCurrentDirectory
    else:
        sys.exit(1)


class Kanbaru(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        # Get current directory
        self.path = getCurrentDirectory()

        # Set up event logger
        self.initEventLogger(os.path.join(
            self.path, "event.log"), "%(asctime)s - %(levelname)s - %(message)s", debug=True, stdout=True)

        logging.info("Starting Kanbaru...")
        logging.info(f'Current directory: "{self.path}"')

        # Initialize local database
        self.initializeLocalDatabase()

        # Initialize Firebase database
        self.initializeFirebaseDatabase(Database.getInstance(), os.path.join(
            self.path, "resources", "kanbaru-credentials.json"))
        self.showMainScreen()
        # Check if user is logged in, if not, prompt login
        # if self.checkCredentials():
        #     Database.getInstance().pullFromFirebase(Database.getInstance().username)
        #     self.showMainScreen()
        # else:
        #     self.showWelcomeScreen()

    def initEventLogger(self, path: str, fmt: str, debug: bool = False, stdout: bool = False) -> None:
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
        if stdout:
            logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

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
        return Auth.verifyCredentials(Database.getInstance().username, Database.getInstance().password)

    def showWelcomeScreen(self):
        """Shows the welcome screen."""
        logging.info("Going to welcome screen...")
        WelcomeScreen(self)

    def showMainScreen(self):
        """Shows the main screen."""
        logging.info("Going to main screen...")
        MainScreen(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Kanbaru()
    window.show()
    sys.exit(app.exec())
