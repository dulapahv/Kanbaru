from typing import List

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


class Panel:
    def __init__(self, title: str = "New Panel", card_lists=[]) -> None:
        self.__title = title
        self.__card_lists = card_lists

    @property
    def title(self) -> str:
        return self.__title

    @property
    def cards(self) -> List[Card]:
        return self.__card_lists

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @cards.setter
    def cards(self, card: Card) -> None:
        if card in self.__cards:
            raise ValueError("Card already exists in panel.")
        self.__cards.append(card)

    def __eq__(self, panel):
        return self.__title == panel.title and self.__cards == panel.cards

    def __str__(self):
        return self.__title


class Board:
    def __init__(self, title: str = "New Board", color="Light blue", panels_lists=[]):
        self.__title = title
        self.__color = color
        self.__panels_lists = panels_lists

    @property
    def title(self) -> str:
        return self.__title

    @property
    def color(self) -> str:
        return self.__color

    @property
    def panels(self) -> List[Panel]:
        return self.__panels_lists

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    @panels.setter
    def panels(self, panel: Panel) -> None:
        if panel in self.__panels:
            raise ValueError("Panel already exists in board.")
        self.__panels.append(panel)

    def __eq__(self, board):
        return self.__title == board.title and self.__color == board.color and self.__panels == board.panels

    def __str__(self):
        return self.__title
