import logging

from firebase_admin import db

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
        """Verifies credentials from the database file.

        Parameters
        ----------
        username : str
            The username of the user.
        password : str
            The password of the user.

        Returns
        -------
        valid : bool
            True if the credentials are valid, False otherwise.
        """
        logging.info("Verifying credentials...")
        if not username or not password:
            logging.warning("Empty credentials!")
            return False
        ref = db.reference(username).get()
        if ref == None or password != ref["_Database__password"]:
            logging.warning("Invalid credentials!")
            return False
        logging.info("Credentials verified")
        return True
