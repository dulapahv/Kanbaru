import logging

from firebase_admin import db


class Auth:
    @staticmethod
    def login(username: str, password: str) -> int:
        """Static method to log in a user.
        Status codes:
            - 0: Login successful
            - 1: Missing credentials
            - 2: Invalid credentials

        Parameters
        ----------
        username : str
            The username of the user.
        password : str
            The password of the user.

        Returns
        -------
        status : int
            Status code of the login process.
        """
        logging.debug("Logging in...")
        if not username or not password:
            logging.warning("Missing credentials!")
            return 1
        if not Auth.verifyCredentials(username, password):
            return 2
        logging.info(f"Logged in: {username}")
        return 0

    @staticmethod
    def signup(username: str, password: str, confirm_password: str) -> int:
        """Static method to sign up a user.
        Status codes:
            - 0: Signup successful
            - 1: Missing credentials
            - 2: Passwords do not match
            - 3: Username already exists

        Parameters
        ----------
        username : str
            The username of the user.
        password : str
            The password of the user.
        confirm_password : str
            The password of the user, to be confirmed.

        Returns
        -------
        status : int
            Status code of the signup process.
        """
        logging.debug("Signing up...")
        if not username or not password or not confirm_password:
            logging.warning("Missing credentials!")
            return 1
        if password != confirm_password:
            logging.warning("Passwords do not match!")
            return 2
        ref = db.reference(username).get()
        if ref is not None:
            logging.warning("Username already exists!")
            return 3
        db.reference(username).set({"_Database__password": password})
        logging.info(f"New user created: {username}")
        return 0

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
        if ref is None or password != ref["_Database__password"]:
            logging.warning("Invalid credentials!")
            return False
        logging.info("Credentials verified")
        return True
