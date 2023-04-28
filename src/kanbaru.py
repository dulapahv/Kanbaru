import logging
import os
import sys
from tkinter import Tk, messagebox

if sys.version_info < (3, 10):
    print("Python 3.10 or higher is required to run Kanbaru. Please consider upgrading.")
    sys.exit(1)

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

        # i dont care. im moving the timer here.
        from PySide6.QtCore import QTimer
        self.timer = QTimer(self)

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

        # straight to the main screen
        self.show_main_screen()
        self.init_mouse_tracking()

    def init_mouse_tracking(self):
        self.timer.timeout.connect(self.check_activity)
        self.setMouseTracking(True)
        self.uploaded = False

    def start_timer(self):
        self.timer.start(3000)

    #TODO: IT DOESNT PUSH TO FIREBASE NOR DETECT MOUSE MOVEMENT
    def check_activity(self):
        if not QApplication.mouseButtons() and not QApplication.keyboardModifiers():
            if not self.uploaded:
                Database.get_instance().push_to_firebase(Database.get_instance().username)
                logging.info("Pushed to Firebase")
                print("Incase it doesn't work, I'm pushing to firebase")
                self.uploaded = True
            self.start_timer()
    
    def mouseMoveEvent(self, event):
        self.start_timer()
        logging.info("Mouse moved")
        self.uploaded = False
    
    def keyPressEvent(self, event):
        self.start_timer()
        logging.info("Key pressed")
        self.uploaded = False


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
        username = Database.get_instance().username
        password = Database.get_instance().password
        return Auth.verify_credentials(username, password)

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
