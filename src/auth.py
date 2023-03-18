import logging

import ui.ui_welcome
from db import Database
from firebase_admin import db


class Auth:
    @staticmethod
    def login():
        logging.debug("login")

    @staticmethod
    def signup():
        logging.debug("signup")

    @staticmethod
    def verifyCredentials(username: str, password: str) -> bool:
        if username == None:
            username = Database.getInstance().getUsername()
        if password == None:
            password = Database.getInstance().getPassword()
        ref = db.reference(username).get()
        if ref == None or password != ref["_Database__password"]:
            logging.warning("Invalid credentials!")
            return False
        logging.info("Credentials verified")
        return True
