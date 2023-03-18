import json
import logging
import os

import firebase_admin
from firebase_admin import credentials, db

from kanbaru_objects import Board, Card, List


class Database:
    """
    Singleton class for database.

    Attributes
    -------
    _instance : Database
        The instance of the database class.

    Methods
    -------
    getInstance() -> Database
        Returns the instance of the database class.
    getPath() -> str
        Returns the path of the database file.
    setPath(path: str) -> None
        Sets the path of the database file.
    create() -> None
        Creates a new database file. If the directory does not exist, it will be created.
    write() -> None
        Writes data from the database instance to the database file.
    read() -> None
        Reads data from the database file and stores it in the database instance.
    initFirebase(cred_path: str) -> None
        Initializes the Firebase database instance.
    pullFromFirebase(username: str) -> None
        Pulls the database of a user from Firebase then writes it to the
        database file.
    pushToFirebase(username: str) -> None
        Pushes the database of a user to Firebase.
    getUsername() -> str
        Returns the username of the user from the database file.
    getPassword() -> str
        Returns the password of the user from the database file.
    """

    _instance: "Database" = None

    def __init__(self: "Database") -> None:
        if Database._instance is not None:
            logging.warning("Database class is a singleton class!")
        else:
            Database._instance = self

            self.__username: str = ""
            self.__password: str = ""
            self.__data: str | Board[List[Card]] = vars(Board())

    @staticmethod
    def getInstance() -> "Database":
        """Static method to return the instance of the database class.

        Returns
        -------
        _instance : Database
            The instance of the database class.
        """
        if Database._instance is None:
            Database()
        return Database._instance

    def getPath(self: "Database") -> str:
        """Returns the path of the database file.

        Returns
        -------
        db_path : str
            The path of the database file.
        """
        return self._db_path

    def setPath(self: "Database", path: str) -> None:
        """Sets the path of the database file.

        Parameters
        ----------
        path : str
            The path of the database file.
        """
        self._db_path = path

    def create(self: "Database") -> None:
        """Creates a new database file at the path specified in self.db_path.
        If the directory does not exist, it will be created.

        Raises
        ------
        Exception
            If the database file cannot be created, an exception will be raised.

        Notes
        -----
        The database file is a JSON file with `{}` as the default content.
        """
        try:
            if not os.path.exists(self._db_path):
                os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
            with open(self._db_path, "w") as f:
                json.dump(vars(self.getInstance()), f, indent=4)
            logging.info("Database file created")
        except Exception as e:
            logging.warning(
                "Failed to create database file! The application will now exit.", exc_info=True)
            raise Exception(
                "Failed to create database file! The application will now exit.")
        self.getInstance().read()

    def write(self: "Database") -> None:
        """Writes data from the database instance to the database file.
        If exceptions are raised, a new database file will be created.

        Raises
        ------
        FileNotFoundError
            If the database file cannot be found, a FileNotFoundError will be raised
            and a new database file will be created.
        Exception
            If the database file cannot be written to, an exception will be raised
            and a new database file will be created.
        """
        try:
            with open(self._db_path, "w") as f:
                json.dump(self.__data, f, indent=4)
                logging.info("Database written to the database file")
        except FileNotFoundError:
            logging.warning(
                "Database file not found! Creating new database...", exc_info=True)
            self.create()
        except Exception as e:
            logging.warning(
                "Failed to write data to database! Creating new database...", exc_info=True)
            self.create()

    def read(self: "Database") -> None:
        """Reads data from the database file and stores it in the database instance.
        If exceptions are raised, a new database file will be created.

        Raises
        ------
        FileNotFoundError
            If the database file cannot be found, a FileNotFoundError will be raised
            and a new database file will be created.
        Exception
            If the database file cannot be read from, an exception will be raised.
            and a new database file will be created.
        """
        try:
            with open(self._db_path, "r") as f:
                self.__data = json.load(f)
                logging.info("Database read from the database file")
        except FileNotFoundError:
            logging.warning(
                "Database file not found! Creating new database...", exc_info=True)
            self.create()
        except Exception as e:
            logging.warning(
                "Failed to read data from database! Creating new database...", exc_info=True)
            self.create()

    def initFirebase(self: "Database", cred_path: str) -> None:
        """Initializes Firebase.

        Parameters
        ----------
        cred_path : str
            The path of the Firebase credentials file.

        Raises
        ------
        Exception
            If Firebase cannot be initialized, an exception will be raised.
        """
        cred = credentials.Certificate(cred_path)
        try:
            firebase_admin.initialize_app(
                cred, {'databaseURL': 'https://kanbaru-42069-default-rtdb.asia-southeast1.firebasedatabase.app/'})
            logging.info("Firebase credentials initialized")
        except Exception as e:
            logging.warning(
                "Failed to initialize Firebase!", exc_info=True)

    def pullFromFirebase(self: "Database", username: str) -> None:
        """Pulls the database of a user from Firebase then writes it to the
        database file.

        Parameters
        ----------
        username : str
            The username of the user whose database is to be pulled.

        Raises
        ------
        Exception
            If the database cannot be pulled from Firebase, an exception will
            be raised.
        """
        ref = db.reference(username)
        try:
            logging.info("Pulling database from Firebase...")
            self.__data = ref.get()
            logging.info("Database pulled from Firebase")
            Database.write(self)
        except Exception as e:
            logging.warning(
                "Failed to pull database from Firebase!", exc_info=True)

    def pushToFirebase(self: "Database", username: str) -> None:
        """Pushes the database of a user to Firebase.

        Parameters
        ----------
        username : str
            The username of the user whose database is to be pushed.

        Raises
        ------
        Exception
            If the database cannot be uploaded to Firebase, an exception will be raised.
        """
        ref = db.reference(username)
        try:
            Database.read(self)
            logging.info("Uploading database to Firebase...")
            ref.set(self.__data)
            logging.info("Database uploaded to Firebase")
        except Exception as e:
            logging.warning(
                "Failed to upload database to Firebase!", exc_info=True)

    def getUsername(self: "Database") -> str:
        """Returns the username of the user.

        Returns
        -------
        username : str
            The username of the user.
        """
        return self.__data["_Database__username"]

    def getPassword(self: "Database") -> str:
        """Returns the password of the user.

        Returns
        -------
        password : str
            The password of the user.
        """
        return self.__data["_Database__password"]

    def __str__(self: "Database") -> str:
        """Returns the database instance as a stringified dictionary.

        Returns
        -------
        str
            The database instance as a stringified dictionary.

        Notes
        -----
        This method is used for debugging purposes.
        """
        logging.debug("Database printed")
        return str(self.__data)
