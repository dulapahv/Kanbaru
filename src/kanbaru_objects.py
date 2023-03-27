# from enum import Enum


# class Color(Enum):
#     LIGHTBLUE = "#6badee"
#     ROSE = "#fb568a"
#     GOLD = "#fbd945"
#     GREEN = "#99c37b"
#     LAVENDER = "#c577dc"
#     TEAL = "#5eb5c1"

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

    @cards.deleter
    def cards(self, card: Card) -> None:
        if card not in self.__cards:
            raise ValueError("Card does not exist in list.")
        self.__cards.remove(card)

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
        # if color in Color:
        #     self.__color = color
        # else:
        #     raise ValueError(
        #         "Invalid color. We only support the following colors: " + str(Color))
        self.__color = color

    @lists.setter
    def lists(self, list: List) -> None:
        if list in self.__lists:
            raise ValueError("List already exists in board.")
        self.__lists.append(list)

    @lists.deleter
    def lists(self, list: List) -> None:
        if list not in self.__lists:
            raise ValueError("List does not exist in board.")
        self.__lists.remove(list)

    def __str__(self):
        return self.__title
