class Card:
    def __init__(self, title: str = "New Card", date="", time="", description: str = "") -> None:
        self.__title = title
        self.__date = date
        self.__time = time
        self.__description = description

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def date(self) -> str:
        return self.__date

    @property
    def time(self) -> str:
        return self.__time

    @title.setter
    def title(self, title: str):
        self.__title = title

    @description.setter
    def description(self, description: str):
        self.__description = description

    @date.setter
    def date(self, date: str):
        self.__date = date

    @time.setter
    def time(self, time: str):
        self.__time = time

    def __eq__(self, card):
        return self.__title == card.title and self.__date == card.date and self.__time == card.time and self.__description == card.description

    def __str__(self):
        return self.__title


class List:
    def __init__(self, title: str = "New List", cards=[]) -> None:
        self.__title = title
        self.__cards = cards

    @property
    def title(self) -> str:
        return self.__title

    @property
    def cards(self) -> list[Card]:
        return self.__cards

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @cards.setter
    def cards(self, card: Card) -> None:
        if card in self.__cards:
            raise ValueError("Card already exists in list.")
        self.__cards.append(card)

    def __eq__(self, list):
        return self.__title == list.title and self.__cards == list.cards

    def __str__(self):
        return self.__title


class Board:
    def __init__(self, title: str = "New Board", color="", lists=[]):
        self.__title = title
        self.__color = color
        self.__lists = lists

    @property
    def title(self) -> str:
        return self.__title

    @property
    def color(self) -> str:
        return self.__color

    @property
    def lists(self) -> list[List]:
        return self.__lists

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    @lists.setter
    def lists(self, list: List) -> None:
        if list in self.__lists:
            raise ValueError("List already exists in board.")
        self.__lists.append(list)

    def __eq__(self, board):
        return self.__title == board.title and self.__color == board.color and self.__lists == board.lists

    def __str__(self):
        return self.__title
