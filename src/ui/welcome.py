from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from auth import Auth
from db import Database
from ui.main import MainScreen
from ui.ui_welcome import Ui_WelcomeWindow


class WelcomeScreen(QMainWindow):
    def __init__(self, parent: QMainWindow = None) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_WelcomeWindow()
        parent.ui.setupUi(parent)

        parent.ui.label_signup_msg.setText("")
        parent.ui.label_login_msg.setText("")

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

    def signup(self, parent) -> None:
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
                parent.ui.label_signup_msg.setText(
                    "Signup successful, please login with your new account.")
            case 1:
                parent.ui.label_signup_msg.setText("Missing credentials!")
            case 2:
                parent.ui.label_signup_msg.setText("Passwords do not match!")
            case 3:
                parent.ui.label_signup_msg.setText("Username already exists!")

    def login(self, parent) -> None:
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

    def login_username_listener(self, text) -> str:
        self.login_username = text

    def login_password_listener(self, text) -> str:
        self.login_password = text

    def signup_username_listener(self, text) -> str:
        self.signup_username = text

    def signup_password_listener(self, text) -> str:
        self.signup_password = text

    def signup_confirm_password_listener(self, text) -> str:
        self.signup_confirm_password = text
