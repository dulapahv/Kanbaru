import json
import logging
import os

import firebase_admin
from firebase_admin import credentials, db

from kanbaru_objects import Board, List, Card


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
    """

    _instance: "Database" = None

    def __init__(self: "Database") -> None:
        self._db_path = None
        assert Database._instance is None, "Database class is a singleton class!"
        Database._instance = self

        self.__username: str = ""
        self.__password: str = ""
        self.__data: list[dict] = [vars(Board())]

    @staticmethod
    def get_instance() -> "Database":
        """Static method to return the instance of the database class.

        Returns
        -------
        _instance : Database
            The instance of the database class.
        """
        if Database._instance is None:
            Database()
        return Database._instance

    def get_path(self: "Database") -> str:
        """Returns the path of the database file.

        Returns
        -------
        db_path : str
            The path of the database file.
        """
        return self._db_path

    def set_path(self: "Database", path: str) -> None:
        """Sets the path of the database file.

        Parameters
        ----------
        path : str
            The path of the database file.
        """
        if not path:
            logging.warning("Database path is empty!")
            return None
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
        The database file is a JSON file.
        """
        try:
            if not os.path.exists(self._db_path):
                os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
            with open(self._db_path, "w") as f:
                json.dump(vars(self.get_instance()), f, indent=4)
            logging.info("Database file created")
        except Exception as e:
            logging.warning(
                "Failed to create/access database file! The application will now exit.", exc_info=True)
            raise Exception(
                "Failed to create/access database file! The application will now exit.")
        self.get_instance().read()

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
                self.__username = self.__data["_Database__username"]
                self.__password = self.__data["_Database__password"]
                logging.info("Database read from the database file")
        except FileNotFoundError:
            logging.warning(
                "Database file not found! Creating new database...", exc_info=True)
            self.create()
        except Exception as e:
            logging.warning(
                "Failed to read data from database! Creating new database...", exc_info=True)
            self.create()

    @staticmethod
    def init_firebase(cred_path: str) -> None:
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
        if not cred_path:
            logging.warning(
                "Cannot initialize Firebase: credential path is empty")
            return None
        logging.info("Initializing Firebase...")
        cred = credentials.Certificate(cred_path)
        try:
            firebase_admin.initialize_app(
                cred, {'databaseURL': 'https://kanbaru-42069-default-rtdb.asia-southeast1.firebasedatabase.app/'})
            logging.info("Firebase credentials initialized")
        except Exception as e:
            logging.warning(
                "Failed to initialize Firebase!", exc_info=True)

    def pull_from_firebase(self: "Database", username: str) -> None:
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
        if not username:
            logging.warning(
                "Cannot pull database to Firebase: username is empty")
            return None
        logging.info("Pulling database from Firebase...")
        ref = db.reference(username)
        try:
            self.__data = ref.get()
            self.username = self.__data["_Database__username"]
            self.password = self.__data["_Database__password"]
            logging.info("Database pulled from Firebase")
            Database.write(self)
        except Exception as e:
            logging.warning(
                "Failed to pull database from Firebase!", exc_info=True)

    def push_to_firebase(self: "Database", username: str) -> None:
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
        if not username:
            logging.warning(
                "Cannot push database to Firebase: username is empty")
            return None
        ref = db.reference(username)
        try:
            Database.read(self)
            logging.info("Uploading database to Firebase...")
            ref.set(self.__data)
            logging.info("Database uploaded to Firebase")
        except Exception as e:
            logging.warning(
                "Failed to upload database to Firebase!", exc_info=True)

    @property
    def username(self: "Database") -> str:
        """Returns the username of the user.

        Returns
        -------
        username : str
            The username of the user.
        """
        return self.__username

    @property
    def password(self: "Database") -> str:
        """Returns the password of the user.

        Returns
        -------
        password : str
            The password of the user.
        """
        return self.__password

    @username.setter
    def username(self: "Database", username: str) -> None:
        """Sets the username of the user.

        Parameters
        ----------
        username : str
            The username of the user.
        """
        self.__username = username
        self.__data["_Database__username"] = username

    @password.setter
    def password(self: "Database", password: str) -> None:
        """Sets the password of the user.

        Parameters
        ----------
        password : str
            The password of the user.
        """
        self.__password = password
        self.__data["_Database__password"] = password

    @property
    def boards(self: "Database") -> list[Board | list[List | list[Card]]]:
        """Returns the list of boards containing its attributes and list of
        Lists containing its attributes and list of Cards containing its
        attributes.

        Returns
        -------
        boards : list[Board | list[List | list[Card]]]
            The list of boards containing its attributes and list of Lists
            containing its attributes and list of Cards containing its
            attributes.

        Notes
        -----
        I know this is a very ugly function, but this is the only way I can
        think of. I'm open to suggestions.
        """
        try:
            board_lists = self.__data['_Database__data']
        except KeyError:
            board_lists = []
        boards = []
        for board_item in board_lists:
            try:
                list_data = board_item['_Board__lists']
            except KeyError:
                list_data = []
            lists = []
            for list_item in list_data:
                try:
                    card_data = list_item['_List__cards']
                except KeyError:
                    card_data = []
                cards = []
                for card_item in card_data:
                    card = Card(title=card_item['_Card__title'],
                                description=card_item['_Card__description'],
                                date=card_item['_Card__date'],
                                time=card_item['_Card__time'])
                    cards.append(card)
                list_obj = List(title=list_item['_List__title'],
                                cards=cards)
                lists.append(list_obj)
            board = Board(title=board_item['_Board__title'],
                          color=board_item['_Board__color'],
                          lists=lists)
            boards.append(board)

        return boards

    @boards.setter
    def boards(self: "Database", boards: list[Board]) -> None:
        """Sets the list of boards.

        Parameters
        ----------
        boards : list
            The list of boards.
        """
        self.__data["_Board__title"] = boards

    def update_card(self: "Database", card_old: Card, card_new: Card) -> None:
        """Update card info in database.

        Parameters
        ----------
        card_old : Card
            The old card to be updated.
        card_new : Card
            The new card to be updated to.
        """
        for index_b, board in enumerate(self.boards):
            for index_l, list in enumerate(board.lists):
                for index_c, card in enumerate(list.cards):
                    if card == card_old:
                        self.data["_Database__data"][index_b]["_Board__lists"][index_l]["_List__cards"][index_c][
                            "_Card__title"] = card_new.title
                        self.data["_Database__data"][index_b]["_Board__lists"][index_l][
                            "_List__cards"][index_c]["_Card__description"] = card_new.description
                        self.data["_Database__data"][index_b]["_Board__lists"][index_l]["_List__cards"][index_c][
                            "_Card__date"] = card_new.date
                        self.data["_Database__data"][index_b]["_Board__lists"][index_l]["_List__cards"][index_c][
                            "_Card__time"] = card_new.time
                        Database.write(self)
                        return None

    @property
    def data(self: "Database") -> list[dict]:
        """Returns the data of the database.

        Returns
        -------
        data : list[dict]
            The data of the database.
        """
        return self.__data

    @data.setter
    def data(self: "Database", data: list[dict]) -> None:
        """Sets the data of the database.

        Parameters
        ----------
        data : list[dict]
            The data of the database.
        """
        self.__data = data

    def logout(self: "Database") -> None:
        """Logs the user out of the application.

        Raises
        ------
        Exception
            If the database cannot be written to the database file, an exception will be raised.
        """
        logging.info("Logging out...")
        self.username: str = ""
        self.password: str = ""
        self.__data: list[dict] = [vars(Board())]
        try:
            Database.create(self)
            logging.info("Logged out")
        except Exception as e:
            logging.warning("Failed to log out!", exc_info=True)

    def delete_account(self: "Database") -> None:
        """Deletes the user's account.

        Raises
        ------
        Exception
            If the database cannot be deleted from the database file, an exception will be raised.
        """
        logging.info("Deleting account...")
        try:
            if self.username == "":
                raise Exception("Illegal attempt to delete account!")
            ref = db.reference(self.username)
            if ref is None:
                raise Exception("User does not exist!")
            ref.delete()
            self.logout()
            logging.info("Account deleted")
        except Exception as e:
            logging.warning("Failed to delete account!", exc_info=True)

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
