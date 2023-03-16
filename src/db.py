import json
import logging
import os


class Database:
    """
    Singleton class for database.

    Attributes
    -------
    _instance : Database
        The instance of the database class.
    _data : dict
        The data stored in the database.

    Methods
    -------
    getInstance() -> Database
        Returns the instance of the database class.
    getDBPath() -> str
        Returns the path of the database file.
    setDBPath(path: str) -> None
        Sets the path of the database file.
    createDBFile() -> None
        Creates a new database file. If the directory does not exist, it will be created.
    write() -> None
        Writes data from the database instance to the database file.
    read() -> None
        Reads data from the database file and stores it in the database instance.
    """

    _instance = None
    _data = {}

    def __init__(self) -> None:
        if Database._instance is not None:
            logging.warning("Database class is a singleton class!")
        else:
            Database._instance = self

    @staticmethod
    def getInstance() -> "Database":
        """Returns the instance of the database class.

        Returns
        -------
        _instance : Database
            The instance of the database class.
        """
        if Database._instance is None:
            Database()
        return Database._instance

    def getDBPath(self) -> str:
        """Returns the path of the database file.

        Returns
        -------
        db_path : str
            The path of the database file.
        """
        return self.db_path

    def setDBPath(self, path: str) -> None:
        """Sets the path of the database file.

        Parameters
        ----------
        path : str
            The path of the database file.
        """
        self.db_path = path

    def createDBFile(self) -> None:
        """Creates a new database file. If the directory does not exist, it will be created.

        Raises
        ------
        Exception
            If the database file cannot be created, an exception will be raised.

        Notes
        -----
        The database file is a JSON file.
        """
        try:
            if not os.path.exists(self.db_path):
                os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, "w") as f:
                json.dump({}, f)
            logging.info("Database file created successfully")
        except Exception as e:
            logging.warning(
                "Failed to create database file! The application will now exit.", exc_info=True)
            raise Exception(
                "Failed to create database file! The application will now exit.")

    def write(self) -> None:
        """Writes data from the database instance to the database file.

        Raises
        ------
        FileNotFoundError
            If the database file cannot be found, a FileNotFoundError will be raised.
        Exception
            If the database file cannot be written to, an exception will be raised.
        """
        try:
            with open(self.db_path, "w") as f:
                json.dump(self._data, f)
        except FileNotFoundError:
            logging.warning(
                "Database file not found! Creating new database...", exc_info=True)
            self.createDBFile()
        except Exception as e:
            logging.warning(
                "Failed to write data to database! Creating new database...", exc_info=True)
            self.createDBFile()

    def read(self) -> None:
        """Reads data from the database file and stores it in the database instance.

        Raises
        ------
        FileNotFoundError
            If the database file cannot be found, a FileNotFoundError will be raised.
        Exception
            If the database file cannot be read from, an exception will be raised.
        """
        try:
            with open(self.db_path, "r") as f:
                self._data = json.load(f)
        except FileNotFoundError:
            logging.warning(
                "Database file not found! Creating new database...", exc_info=True)
            self.createDBFile()
        except Exception as e:
            logging.warning(
                "Failed to read data from database! Creating new database...", exc_info=True)
            self.createDBFile()
