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
        logging.info("Logging in...")
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
        logging.info("Signing up...")
        if not username or not password or not confirm_password:
            logging.warning("Missing credentials!")
            return 1
        if password != confirm_password:
            logging.warning("Passwords do not match!")
            return 2
        try:
            ref = db.reference(username).get()
        except Exception as e:
            logging.warning(
                f"Error while checking if username exists! Retrying...", exc_info=True)
            try:
                ref = db.reference(username).get()
            except Exception as e:
                raise Exception(
                    f"Could not verify credentials! Please check your internet connection or try again later.\n{e}")
        if ref is not None:
            logging.warning("Username already exists!")
            return 3
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
        try:
            ref = db.reference(username).get()
        except:
            logging.warning(
                f"Error while verifying credentials! Retrying...", exc_info=True)
            try:
                ref = db.reference(username).get()
            except Exception as e:
                raise Exception(
                    f"Could not verify credentials! Please check your internet connection or try again later.\n{e}")
        finally:
            ref = db.reference(username).get()
        if ref is None or password != ref["_Database__password"]:
            logging.warning("Invalid credentials!")
            return False
        logging.info("Credentials verified")
        return True
