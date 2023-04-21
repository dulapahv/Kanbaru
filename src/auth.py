import logging

import pyrebase

config = {
    "apiKey": "AIzaSyBO6wkCcjnEfiXqfDGDvHriyw5p5trmmdk",
    "authDomain": "kanbaru-42069.firebaseapp.com",
    "databaseURL": "https://kanbaru-42069-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "kanbaru-42069",
    "storageBucket": "kanbaru-42069.appspot.com",
    "messagingSenderId": "750001844634",
    "appId": "1:750001844634:web:048364d270fbddea1d4a23",
    "measurementId": "G-MRP7PQ53QB"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


class Auth:
    @staticmethod
    def login(email: str, password: str) -> int:
        """Logs the user in.

        Parameters
        ----------
        email : str
            The user's email.
        password : str
            The user's password.

        Returns
        -------
        int
            0 if credentials are valid, 1 if credentials are missing, 2 if
            credentials are invalid.
        """
        if not email or not password:
            logging.info("Missing credentials!")
            return 1
        try:
            auth.sign_in_with_email_and_password(email, password)
            logging.info("Login successful!")
            return 0
        except:
            logging.info("Invalid credentials!")
            return 2

    @staticmethod
    def signup(email: str, password: str) -> int:
        """Signs the user up.

        Parameters
        ----------
        email : str
            The user's email.
        password : str
            The user's password.

        Returns
        -------
        int
            0 if signup is successful, 1 if credentials are missing, 2 if
            credentials are invalid.
        """
        if not email or not password:
            logging.info("Missing credentials!")
            return 1
        try:
            auth.create_user_with_email_and_password(email, password)
            logging.info("Signup successful!")
            return 0
        except Exception as err:
            print(err)
            logging.info("User already exists!")
            return 2

    @staticmethod
    def verify_credentials(email: str, password: str) -> bool:
        """Verifies the user's credentials.

        Parameters
        ----------
        email : str
            The user's email.
        password : str
            The user's password.

        Returns
        -------
        bool
            True if the credentials are valid, False otherwise.
        """
        try:
            auth.sign_in_with_email_and_password(email, password)
            logging.info("Credentials verified!")
            return True
        except:
            logging.info("Invalid credentials!")
            return False
