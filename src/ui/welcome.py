from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow

from auth import Auth
from db import Database
from ui.main import MainScreen
from ui.ui_welcome import Ui_WelcomeWindow
from utils import setupFontDB


class WelcomeScreen(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        parent.ui: Ui_WelcomeWindow = Ui_WelcomeWindow()
        parent.ui.setupUi(parent)

        self.setupFont(parent, "TorusPro.ttf")

        parent.ui.label_login_msg.setText("")
        parent.ui.label_signup_msg.setText("")

        self.login_username: str = ""
        self.login_password: str = ""
        self.signup_username: str = ""
        self.signup_password: str = ""
        self.signup_confirm_password: str = ""
        parent.ui.lineEdit_login_username.textChanged.connect(
            self.login_username_listener)
        parent.ui.lineEdit_login_password.textChanged.connect(
            self.login_password_listener)
        parent.ui.lineEdit_signup_username.textChanged.connect(
            self.signup_username_listener)
        parent.ui.lineEdit_signup_password.textChanged.connect(
            self.signup_password_listener)
        parent.ui.lineEdit_signup_confirm_password.textChanged.connect(
            self.signup_confirm_password_listener)

        parent.ui.btn_login.clicked.connect(lambda: self.login(parent))
        parent.ui.btn_signup.clicked.connect(lambda: self.signup(parent))

    def signup(self, parent: Ui_WelcomeWindow) -> None:
        """Signs up a user.
        Status codes:
            - 0: Signup successful
            - 1: Missing credentials
            - 2: Passwords do not match
            - 3: Username already exists
        If the status code is 0, the user will be redirected to the main screen.

        Parameters
        ----------
        parent : QMainWindow
            The parent window.
        """
        if len(self.signup_username) >= 128:
            parent.ui.label_signup_msg.setText(
                "Username must not exceed 128 characters!")
        if len(self.signup_password) >= 128:
            parent.ui.label_signup_msg.setText(
                "Password must not exceed 128 characters!")
        status = Auth.signup(self.signup_username, self.signup_password,
                             self.signup_confirm_password)
        match (status):
            case 0:
                Database.getInstance().username = self.signup_username
                Database.getInstance().password = self.signup_password
                Database.getInstance().write()
                Database.getInstance().pushToFirebase(self.signup_username)
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
        If the status code is 0, the user will be redirected to the main screen.

        Parameters
        ----------
        parent : QMainWindow
            The parent window.
        """
        if len(self.login_username) >= 128:
            parent.ui.label_login_msg.setText(
                "Username must not exceed 128 characters!")
        if len(self.login_password) >= 128:
            parent.ui.label_login_msg.setText(
                "Password must not exceed 128 characters!")
        status = Auth.login(self.login_username, self.login_password)

        match (status):
            case 0:
                Database.getInstance().pullFromFirebase(self.login_username)
                MainScreen(parent)
            case 1:
                parent.ui.label_login_msg.setText("Missing credentials!")
            case 2:
                parent.ui.label_login_msg.setText("Invalid credentials!")

    def setupFont(self, parent: Ui_WelcomeWindow, font: str | list[str]) -> None:
        fontDB = setupFontDB(font)
        parent.ui.label_logo.setFont(QFont(fontDB[0], 36))
        parent.ui.label_login.setFont(QFont(fontDB[0], 13, QFont.Bold))
        parent.ui.label_signup.setFont(QFont(fontDB[0], 13, QFont.Bold))
        parent.ui.lineEdit_login_username.setFont(QFont(fontDB[0], 12))
        parent.ui.lineEdit_login_password.setFont(QFont(fontDB[0], 12))
        parent.ui.lineEdit_signup_username.setFont(QFont(fontDB[0], 12))
        parent.ui.lineEdit_signup_password.setFont(QFont(fontDB[0], 12))
        parent.ui.lineEdit_signup_confirm_password.setFont(
            QFont(fontDB[0], 12))
        parent.ui.label_login_msg.setFont(QFont(fontDB[0], 11, QFont.Bold))
        parent.ui.label_signup_msg.setFont(QFont(fontDB[0], 11, QFont.Bold))
        parent.ui.btn_login.setFont(QFont(fontDB[0], 12, QFont.Bold))
        parent.ui.btn_signup.setFont(QFont(fontDB[0], 12, QFont.Bold))

    def login_username_listener(self, text: str) -> None:
        """Listens for changes in the login username field."""
        self.login_username = text

    def login_password_listener(self, text: str) -> None:
        """Listens for changes in the login password field."""
        self.login_password = text

    def signup_username_listener(self, text: str) -> None:
        """Listens for changes in the signup username field."""
        self.signup_username = text

    def signup_password_listener(self, text: str) -> None:
        """Listens for changes in the signup password field."""
        self.signup_password = text

    def signup_confirm_password_listener(self, text: str) -> None:
        """Listens for changes in the signup confirm password field."""
        self.signup_confirm_password = text
