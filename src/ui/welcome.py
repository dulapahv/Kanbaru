from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow

from db import Database
from ui.main import MainScreen
from ui.welcome_ui import Ui_WelcomeWindow
from utils import keyPressEvent, setup_font_db


class WelcomeScreen(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_WelcomeWindow()
        parent.ui.setupUi(parent)

        self.setup_font(parent)

        parent.ui.label_login_msg.setText("")
        parent.ui.label_signup_msg.setText("")

        self.login_username: str = ""
        self.login_password: str = ""
        self.signup_username: str = ""
        self.signup_password: str = ""
        self.signup_confirm_password: str = ""
        parent.ui.lineEdit_login_username.textChanged.connect(
            lambda text: self.login_username_listener(text, parent))
        parent.ui.lineEdit_login_password.textChanged.connect(
            lambda text: self.login_password_listener(text, parent))
        parent.ui.lineEdit_signup_username.textChanged.connect(
            lambda text: self.signup_username_listener(text, parent))
        parent.ui.lineEdit_signup_password.textChanged.connect(
            lambda text: self.signup_password_listener(text, parent))
        parent.ui.lineEdit_signup_confirm_password.textChanged.connect(
            lambda text: self.signup_confirm_password_listener(text, parent))

        parent.ui.btn_login.clicked.connect(lambda: self.login(parent))
        parent.ui.btn_signup.clicked.connect(lambda: self.signup(parent))

        parent.ui.btn_login.keyPressEvent = lambda event: keyPressEvent(
            event, parent, self.login)
        parent.ui.btn_signup.keyPressEvent = lambda event: keyPressEvent(
            event, parent, self.signup)

    def signup(self, parent: Ui_WelcomeWindow) -> None:
        """Signs up a user.
        Status codes:
            - 0: Signup successful
            - 1: Missing credentials
            - 2: Passwords do not match
            - 3: Username already exists
        If the status code is 0, the user will be redirected to the main
        screen.

        Parameters
        ----------
        parent : QMainWindow
            The parent window.
        """
        if len(self.signup_username) >= 128:
            parent.ui.label_signup_msg.setText(
                "Username must not exceed 128 characters!")
            return None
        if len(self.signup_password) >= 128:
            parent.ui.label_signup_msg.setText(
                "Password must not exceed 128 characters!")
            return None
        if len(self.signup_password) < 6:
            parent.ui.label_signup_msg.setText(
                "Password must be at least 6 characters long!")
            return None
        if self.signup_password != self.signup_confirm_password:
            parent.ui.label_signup_msg.setText("Passwords do not match!")
            return None
        status = Auth.signup(self.signup_username, self.signup_password)
        match status:
            case 0:
                Database.get_instance().username = self.signup_username
                Database.get_instance().password = self.signup_password
                Database.get_instance().write()
                Database.get_instance().push_to_firebase(self.signup_username)
                MainScreen(parent)
            case 1:
                parent.ui.label_signup_msg.setText("Missing credentials!")
            case 2:
                parent.ui.label_signup_msg.setText("Passwords do not match!")
            case 3:
                parent.ui.label_signup_msg.setText("Username already exists!")

    def login(self, parent: Ui_WelcomeWindow) -> None:
        """Logs in a user.
        Status codes:
            - 0: Login successful
            - 1: Missing credentials
            - 2: Invalid credentials
        If the status code is 0, the user will be redirected to the main
        screen.

        Parameters
        ----------
        parent : QMainWindow
            The parent window.
        """
        if len(self.login_username) >= 128:
            parent.ui.label_login_msg.setText(
                "Username must not exceed 128 characters!")
            return None
        if len(self.login_password) >= 128:
            parent.ui.label_login_msg.setText(
                "Password must not exceed 128 characters!")
            return None
        status = Auth.login(self.login_username, self.login_password)
        match status:
            case 0:
                Database.get_instance().pull_from_firebase(self.login_username)
                MainScreen(parent)
            case 1:
                parent.ui.label_login_msg.setText("Missing credentials!")
            case 2:
                parent.ui.label_login_msg.setText("Invalid credentials!")

    @staticmethod
    def setup_font(parent: Ui_WelcomeWindow) -> None:
        notosans = setup_font_db("NotoSans.ttf")[0]
        toruspro = setup_font_db("TorusPro.ttf")[0]
        parent.ui.label_login.setFont(QFont(toruspro, 13, QFont.Bold))
        parent.ui.label_signup.setFont(QFont(toruspro, 13, QFont.Bold))
        parent.ui.lineEdit_login_username.setFont(QFont(notosans, 12))
        parent.ui.lineEdit_login_password.setFont(QFont(notosans, 12))
        parent.ui.lineEdit_signup_username.setFont(QFont(notosans, 12))
        parent.ui.lineEdit_signup_password.setFont(QFont(notosans, 12))
        parent.ui.lineEdit_signup_confirm_password.setFont(
            QFont(notosans, 12))
        parent.ui.label_login_msg.setFont(QFont(notosans, 11, QFont.Bold))
        parent.ui.label_signup_msg.setFont(QFont(notosans, 11, QFont.Bold))
        parent.ui.btn_login.setFont(QFont(toruspro, 12, QFont.Bold))
        parent.ui.btn_signup.setFont(QFont(toruspro, 12, QFont.Bold))

    def login_username_listener(self, text: str,
                                parent: Ui_WelcomeWindow) -> None:
        """Listens for changes in the login username field."""
        self.login_username = text
        if not parent.ui.label_login_msg.text() == "":
            parent.ui.label_login_msg.setText("")

    def login_password_listener(self, text: str,
                                parent: Ui_WelcomeWindow) -> None:
        """Listens for changes in the login password field."""
        self.login_password = text
        if not parent.ui.label_login_msg.text() == "":
            parent.ui.label_login_msg.setText("")

    def signup_username_listener(self, text: str,
                                 parent: Ui_WelcomeWindow) -> None:
        """Listens for changes in the signup username field."""
        self.signup_username = text
        if not parent.ui.label_signup_msg.text() == "":
            parent.ui.label_signup_msg.setText("")

    def signup_password_listener(self, text: str,
                                 parent: Ui_WelcomeWindow) -> None:
        """Listens for changes in the signup password field."""
        self.signup_password = text
        if not parent.ui.label_signup_msg.text() == "":
            parent.ui.label_signup_msg.setText("")

    def signup_confirm_password_listener(self, text: str,
                                         parent: Ui_WelcomeWindow) -> None:
        """Listens for changes in the signup confirm password field."""
        self.signup_confirm_password = text
        if not parent.ui.label_signup_msg.text() == "":
            parent.ui.label_signup_msg.setText("")
