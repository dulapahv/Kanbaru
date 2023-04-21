import logging
import os
import sys
from tkinter import Tk, messagebox

if sys.version_info < (3, 10):
    print("Python 3.10 or higher is required to run Kanbaru. Please consider upgrading.")

try:
    from PySide6.QtWidgets import QApplication, QMainWindow
    from auth import Auth
    from db import Database
    from ui.main import MainScreen
    from ui.welcome import WelcomeScreen
    from utils import get_current_directory
except ModuleNotFoundError:
    logging.warning("Required modules not found. Prompting user to install...")
    root = Tk()
    root.withdraw()
    response = messagebox.askyesno(
        "Error: Module Not Found",
        "Required modules not found. Would you like to install them now?\n\n"
        "Required modules: PySide6, firebase-admin"
    )

    if response:
        path = os.path.dirname(os.path.abspath(__file__))
        try:
            import pip
            pip.main(
                ["install", "-r", f"{os.path.join(path, 'requirements.txt')}"]
            )
        except ModuleNotFoundError:
            logging.warning(
                "pip not found. Installing pip now. This is a risky move. "
                "btw why don't you have pip installed yet?"
            )
            import ensurepip
            ensurepip.bootstrap()
            pip.main(["install", "-r", "requirements.txt"])
        finally:
            from PySide6.QtWidgets import QApplication, QMainWindow

            from auth import Auth
            from db import Database
            from ui.main import MainScreen
            from ui.welcome import WelcomeScreen
            from utils import get_current_directory
    else:
        sys.exit(1)


class Kanbaru(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        # Get current directory
        self.db_path = None
        self.path = get_current_directory()

        # Set up event logger
        self.init_event_logger(
            os.path.join(self.path, "event.log"),
            "%(asctime)s - %(levelname)s - %(message)s",
            debug=True,
            stdout=True,
        )

        logging.info("Starting Kanbaru...")
        logging.info(f'Current directory: "{self.path}"')

        # Initialize local database
        self.initialize_local_database()

        # Initialize Firebase database
        self.initialize_firebase_database(
            Database.get_instance(),
            os.path.join(self.path, "resources", "kanbaru-credentials.json"),
        )

        # self.show_main_screen()
        # Check if user is logged in, if not, prompt login
        if self.check_credentials():
            Database.get_instance().pull_from_firebase(Database.get_instance().username)
            self.show_main_screen()
        else:
            self.show_welcome_screen()

    @staticmethod
    def init_event_logger(path: str, fmt: str, debug: bool = False,
                          stdout: bool = False) -> None:
        """Initializes the event logger.
        - Set the path of the event log file
        - Set the format of the event log file
        - Set the debug level of the event log file
        - Set up the event logger
        """
        logging.basicConfig(
            filename=path,
            filemode="w",
            format=fmt,
            datefmt="%d-%b-%y %H:%M:%S",
            level=logging.DEBUG if debug else logging.INFO,
        )
        if stdout:
            logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    def initialize_local_database(self) -> None:
        """Initializes the database instance.
        - Determine database path
        - Create database instance
        - Set database path
        - Read database file
        """
        if sys.platform == "win32":
            logging.info("Windows OS detected")
            self.db_path = os.path.join(
                os.path.expanduser(
                    "~"), "Documents", "Kanbaru", "Database.json"
            )
        else:
            logging.info("Unix OS detected")
            self.db_path = os.path.join(
                os.path.expanduser("~"), "Kanbaru", "Database.json"
            )
        db = Database.get_instance()
        db.set_path(self.db_path)
        db.read()
        logging.info(f'Database path: "{db.get_path()}"')
        logging.info("Database instance initialized and read successfully")

    @staticmethod
    def initialize_firebase_database(
        db_instance: Database, cred_path: str
    ) -> None:
        """Initializes the Firebase database instance.
        - Set database instance
        - Set credential path
        - Set up Firebase database
        """
        db_instance.init_firebase(cred_path)
        logging.info("Firebase database initialized and connected")

    @staticmethod
    def check_credentials() -> bool:
        """Checks credentials from the database file.
            - Get username and password from database file
            - If username or password is empty, return False
            - If credentials are invalid, return False
        """
        return Auth.verify_credentials(
            Database.get_instance().username, Database.get_instance().password
        )

    def show_welcome_screen(self):
        """Shows the welcome screen."""
        logging.info("Going to welcome screen...")
        WelcomeScreen(self)

    def show_main_screen(self):
        """Shows the main screen."""
        logging.info("Going to main screen...")
        MainScreen(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Kanbaru()
    window.show()
    sys.exit(app.exec())
