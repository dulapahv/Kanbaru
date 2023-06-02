from kanbaru_objects import Board, Card, Color, Panel
import logging
import os
import sys
import pickle
from typing import Dict, List


class Table:
    """
    Singleton class for table. This class is used to store, retrieve, and
    manipulate data from the local table.

    Use `Table.get_instance()` to get the instance of the table class.
    """

    _instance: "Table" = None

    def __init__(self: "Table") -> None:
        assert Table._instance is None, \
            "Table class is a singleton class!"
        Table._instance = self

        self._tb_path: str = ""
        self.__data: List[Dict] = [vars(Board())]

    @staticmethod
    def get_instance() -> "Table":
        """Static method to return the instance of the table class.

        Returns
        -------
        _instance : Table
            The instance of the table class.
        """
        if Table._instance is None:
            Table()
        return Table._instance

    def get_path(self: "Table") -> str:
        """Returns the path of the table file.

        Returns
        -------
        tb_path : str
            The path of the table file.
        """
        return self._tb_path

    def set_path(self: "Table", path: str) -> None:
        """Sets the path of the table file.

        Parameters
        ----------
        path : str
            The path of the table file.
        """
        if not path:
            logging.warning("Table path is empty!")
            return None
        self._tb_path = path

    def create(self: "Table") -> None:
        """Creates a new table file at the path specified in self.tb_path.
        If the directory does not exist, it will be created.

        Raises
        ------
        Exception
            If the table file cannot be created,
            an exception will be raised.

        Notes
        -----
        The table file is a JSON file.
        """
        try:
            os.makedirs(os.path.dirname(self._tb_path), exist_ok=True)
            with open(self._tb_path, "wb") as f:
                pickle.dump(self.__data, f)
            logging.info("Table file created")
        except Exception as e:
            logging.warning(
                "Failed to create/access table file! "
                "The application will now exit.", exc_info=True)
            raise Exception(
                "Failed to create/access table file! "
                "The application will now exit.", sys.exit(1))
        self.get_instance().read()

    def write(self: "Table") -> None:
        """Writes data from the table instance to the table file.
        If exceptions are raised, a new table file will be created.

        Raises
        ------
        FileNotFoundError
            If the table file cannot be found, a FileNotFoundError will be
            raised and a new table file will be created.
        Exception
            If the table file cannot be written to, an exception will be
            raised and a new table file will be created.
        """
        try:
            with open(self._tb_path, "wb") as f:
                pickle.dump(self.__data, f)
                logging.info("Table written to the table file")
        except FileNotFoundError:
            logging.warning(
                "Table file not found! "
                "Creating new table...", exc_info=True)
            self.create()
        except Exception as e:
            logging.warning(
                "Failed to create/access table file! "
                "The application will now exit.", exc_info=True)
            raise Exception(
                "Failed to create/access table file! "
                "The application will now exit.", sys.exit(1))

    def read(self: "Table") -> None:
        """Reads data from the table file and stores it in the table
        instance. If exceptions are raised, a new table file will be
        created.

        Raises
        ------
        FileNotFoundError
            If the table file cannot be found, a FileNotFoundError will be
            raised and a new table file will be created.
        Exception
            If the table file cannot be read from, an exception will be
            raised and a new table file will be created.
        """
        logging.info("Reading table file...")
        try:
            with open(self._tb_path, "rb") as f:
                self.__data = pickle.load(f)
        except FileNotFoundError:
            logging.warning(
                "Table file not found! "
                "Creating new table...", exc_info=True)
            self.create()
        except Exception as e:
            logging.warning(
                "Failed to read data from table! "
                "Creating new table...", exc_info=True)
            self.create()
        logging.info(
            f"Loaded {len(self.boards)} "
            f"board{'s' if len(self.boards) > 1 else ''}")
        for board in self.boards:
            logging.info(
                f'+--"{board.title}" [{len(board.panels)} '
                f'panel{"s" if len(board.panels) > 1 else ""}]')
            for panel in board.panels:
                logging.info(
                    f'|   +--"{panel.title}" [{len(panel.cards)} '
                    f'card{"s" if len(panel.cards) > 1 else ""}]')
                for card in panel.cards:
                    logging.info(f'|   |   +--"{card.title}"')
        logging.info("Table read from the table file")

    @property
    def boards(self: "Table") -> List[Board]:
        """Returns a list of boards containing their attributes and a list of
        panels containing their attributes and a list of cards containing their
        attributes.

        Returns
        -------
        boards : List[Board]
            A list of boards containing their attributes and a list of panels
            containing their attributes and a list of cards containing their
            attributes.
        """
        boards = []
        board_lists = self.__data

        for board_item in board_lists:
            panel_data = board_item.get('_Board__panels_lists', [])
            panels = []

            for panel_item in panel_data:
                card_data = panel_item.get('_Board__panels', [])
                cards = []

                for card_item in card_data:
                    card = Card(
                        title=card_item.get('_Card__title', ''),
                        description=card_item.get('_Card__description', ''),
                        date=card_item.get('_Card__date', ''),
                        time=card_item.get('_Card__time', '')
                    )
                    cards.append(card)

                panel_obj = Panel(
                    title=panel_item.get('_Panel__title', ''),
                    card_lists=cards
                )
                panels.append(panel_obj)

            board = Board(
                title=board_item.get('_Board__title', ''),
                color=board_item.get('_Board__color', ''),
                panels_lists=panels
            )
            boards.append(board)
        return boards

    @boards.setter
    def boards(self: "Table", boards: List[Board]) -> None:
        """Sets the list of boards.

        Parameters
        ----------
        boards : List[Board]
            The list of boards.
        """
        self.__data["_Board__title"] = boards

    def update_card(self: "Table", card_old: Card, card_new: Card) -> None:
        """Update card info in table.

        Parameters
        ----------
        card_old : Card
            The old card to be updated.
        card_new : Card
            The new card to be updated to.
        """
        for index_b, board in enumerate(self.boards):
            for index_p, panel in enumerate(board.panels):
                for index_c, card in enumerate(panel.cards):
                    if card == card_old:
                        card_dict = self.data[index_b].get(
                            "_Board__panels_lists")[index_p].get(
                                "_Board__panels")[index_c]
                        card_dict["_Card__title"] = card_new.title
                        card_dict["_Card__description"] = card_new.description
                        card_dict["_Card__date"] = card_new.date
                        card_dict["_Card__time"] = card_new.time
                        Table.write(self)
                        logging.info("Card updated:")
                        logging.info(
                            f"{card_old} -> title='{card_new.title}', "
                            f"date='{card_new.date}', "
                            f"time='{card_new.time}', "
                            f"description='{card_new.description}'")
                        return None

    def update_panel(self: "Table", panel_old: Panel,
                     panel_new: Panel) -> None:
        """Update panel info in table

        Parameters
        ----------
        panel_old : Panel
            The old panel to be updated.
        panel_new : Panel
            The new panel to be updated to.
        """
        for index_b, board in enumerate(self.boards):
            for index_p, panel in enumerate(board.panels):
                if panel == panel_old:
                    panel_dict = self.data[index_b].get(
                        "_Board__panels_lists")[index_p]
                    panel_dict["_Panel__title"] = panel_new.title
                    Table.write(self)
                    logging.info("Panel updated:")
                    cards = [
                        card.title for card in panel_new.cards if hasattr(
                            panel_new, 'cards')
                    ] if hasattr(panel_new, 'cards') else []
                    logging.info(
                        f"{panel_old} -> title='{panel_new.title}', "
                        f"cards={cards}")
                    return None

    def update_board(self: "Table", board_old: Board,
                     board_new: Board) -> None:
        """Update board info in table.

        Parameters
        ----------
        board_old : Board
            The old board to be updated.
        board_new : Board
            The new board to be updated to.
        """
        for index_b, board in enumerate(self.boards):
            if board == board_old:
                board_dict = self.data[index_b]
                board_dict["_Board__title"] = board_new.title
                board_dict["_Board__color"] = Color(board_new.color).name
                logging.info("Board updated:")
                logging.info(
                    f"{board_old} -> title='{board_new.title}', "
                    f"color='{Color(board_new.color).name}'")
                Table.write(self)
                return None

    def update_panel_order(self: "Table", board: Board,
                           new_panel_list: List[Panel]) -> None:
        """Update the order of panels in a board.

        Parameters
        ----------
        board : Board
            The board to be updated.
        new_panel_list : List[Panel]
            The new list of panels to be updated to.
        """
        old_panel_list = board.panels
        for index_b, board_ in enumerate(self.boards):
            if board_ == board:
                board_dict = self.data[index_b]
                board_dict["_Board__panels_lists"] = [
                    {
                        "_Panel__title": panel.title,
                        "_Board__panels": [
                            {
                                "_Card__title": card.title,
                                "_Card__description": card.description,
                                "_Card__date": card.date,
                                "_Card__time": card.time
                            }
                            for card in panel.cards
                        ]
                    }
                    for panel in new_panel_list
                ]
                logging.info("Panel order updated:")
                logging.info(
                    f"{[panel.title for panel in old_panel_list]} -> "
                    f"{[panel.title for panel in new_panel_list]}")
                Table.write(self)
                return None

    def update_board_order(self: "Table",
                           new_board_list: List[Board]) -> None:
        """Update the order of boards.

        Parameters
        ----------
        new_board_list : List[Board]
            The new list of boards to be updated to.
        """
        old_board_list = self.boards
        self.data = [
            {
                "_Board__title": board.title,
                "_Board__color": Color(board.color).name,
                "_Board__panels_lists": [
                    {
                        "_Panel__title": panel.title,
                        "_Board__panels": [
                            {
                                "_Card__title": card.title,
                                "_Card__description": card.description,
                                "_Card__date": card.date,
                                "_Card__time": card.time
                            }
                            for card in panel.cards
                        ]
                    }
                    for panel in board.panels
                ]
            }
            for board in new_board_list
        ]
        logging.info("Board order updated:")
        logging.info(
            f"{[board.title for board in old_board_list]} -> "
            f"{[board.title for board in new_board_list]}")
        Table.write(self)
        return None

    def delete_card(self: "Table", card_delete: Card) -> None:
        """Delete card from table.

        Parameters
        ----------
        card_delete : Card
            The card to be deleted.
        """
        for index_b, board in enumerate(self.boards):
            for index_p, panel in enumerate(board.panels):
                for index_c, card in enumerate(panel.cards):
                    if card == card_delete:
                        del self.data[index_b].get(
                            "_Board__panels_lists")[index_p].get(
                                "_Board__panels")[index_c]
                        Table.write(self)
                        logging.info(f'Card "{card.title}" deleted')
                        return None

    def delete_panel(self: "Table", panel_delete: Panel) -> None:
        """Delete panel from table.

        Parameters
        ----------
        panel_delete : Panel
            The panel to be deleted.
        """
        for index_b, board in enumerate(self.boards):
            for index_p, panel in enumerate(board.panels):
                if panel == panel_delete:
                    del self.data[index_b].get(
                        "_Board__panels_lists")[index_p]
                    Table.write(self)
                    logging.info(f'Panel "{panel.title}" deleted')
                    return None

    def delete_board(self: "Table", board_delete: Board) -> None:
        """Delete board from table.

        Parameters
        ----------
        board_delete : Board
            The board to be deleted.
        """
        for index_b, board in enumerate(self.boards):
            if board == board_delete:
                del self.data[index_b]
                Table.write(self)
                logging.info(f'Board "{board.title}" deleted')
                return None

    def change_board_color(self: "Table", board: Board,
                           color: Color) -> None:
        """Change the color of a board.

        Parameters
        ----------
        board : Board
            The board to change the color of.
        color : Color
            The new color of the board.
        """
        for index_b, board in enumerate(self.boards):
            if board == board:
                self.data.get(
                    "_Table__data")[index_b]["_Board__color"] = Color(
                    color).name
                Table.write(self)
                return None

    @property
    def data(self: "Table") -> List[Dict]:
        """Returns the data of the table.

        Returns
        -------
        data : List[Dict]
            The data of the table.
        """
        return self.__data

    @data.setter
    def data(self: "Table", data: List[Dict]) -> None:
        """Sets the data of the table.

        Parameters
        ----------
        data : List[Dict]
            The data of the table.
        """
        self.__data = data

    def __str__(self: "Table") -> str:
        """Returns the table instance as a stringified dictionary.

        Returns
        -------
        str
            The table instance as a stringified dictionary.

        Notes
        -----
        This method is used for debugging purposes.
        """
        logging.debug("Table printed")
        return str(self.__data)
