import logging

import ui.ui_welcome
from db import Database


class Auth:
    @staticmethod
    def login():
        logging.debug("login")

    @staticmethod
    def signup():
        logging.debug("signup")

    @staticmethod
    def verifyCredentials(username: str, password: str) -> bool:
        logging.debug("verifyCredentials")
        
