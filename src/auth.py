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
          - If the user is logged in, return 0
          - If the user is not logged in, return 1
        """
        try:
            auth.sign_in_with_email_and_password(email, password)
            return 0
        except:
            return 1

    @staticmethod
    def signup(email: str, password: str) -> int:
        """Signs the user up.
          - If the user is signed up, return 0
          - If the user is not signed up, return 1
        """
        try:
            auth.create_user_with_email_and_password(email, password)
            return 0
        except:
            return 1

    @staticmethod
    def verify_credentials(email: str, password: str) -> int:
        """Verifies the user's credentials.
          - If the credentials are correct, return 0
          - If the credentials are incorrect, return 1
        """
        try:
            auth.sign_in_with_email_and_password(email, password)
            return 0
        except:
            return 1
