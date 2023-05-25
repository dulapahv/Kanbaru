from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import List


class Color(Enum):
    LIGHTBLUE = "#6badee"
    ROSE = "#fb568a"
    GOLD = "#f7c600"
    GREEN = "#99c37b"
    LAVENDER = "#c577dc"
    TEAL = "#5eb5c1"


class KanbaruObject(ABC):
    @property
    @abstractmethod
    def title(self) -> str:
        pass

    @title.setter
    @abstractmethod
    def title(self, title: str) -> None:
        pass

    def __eq__(self, other) -> bool:
        pass

    def __str__(self) -> str:
        pass


class Card(KanbaruObject):
    def __init__(self, title: str = "New Card", date: str = "", time: str = "",
                 description: str = "") -> None:
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
        if title is None:
            raise ValueError("Card title cannot be None.")
        self.__title = title

    @description.setter
    def description(self, description: str):
        if description is None:
            raise ValueError("Card description cannot be None.")
        self.__description = description

    @date.setter
    def date(self, date: str):
        if date is None:
            raise ValueError("Card date cannot be None.")
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Card date must follow format DD-MM-YYYY.")
        self.__date = date

    @time.setter
    def time(self, time: str):
        if time is None:
            raise ValueError("Card time cannot be None.")
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            raise ValueError("Card time must follow format HH:MM.")
        self.__time = time

    def __eq__(self, card):
        return (
            self.__title == card.title and
            self.__date == card.date and
            self.__time == card.time and
            self.__description == card.description
        )

    def __str__(self):
        return (
            f"{self.title=}, {self.date=}, {self.time=}, "
            f"{self.description=}".replace("self.", "")
        )


class Panel(KanbaruObject):
    def __init__(self, title: str = "New Panel",
                 card_lists: List[Card] = []) -> None:
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
        if title is None:
            raise ValueError("Panel title cannot be None.")
        self.__title = title

    @cards.setter
    def cards(self, card: Card) -> None:
        if card is None:
            raise ValueError("Card cannot be None.")
        for card in self.__card_lists:
            raise ValueError("Card already exists.")
        self.__card_lists.append(card)

    def __eq__(self, panel):
        return (
            self.__title == panel.title
            and self.__card_lists == panel.cards
        )

    def __str__(self):
        return (
            f"{self.title=}, "
            f"cards={[card.title for card in self.cards]}".replace("self.", "")
        )


class Board(KanbaruObject):
    def __init__(self, title: str = "New Board", color: str = "LIGHTBLUE",
                 panels_lists: List[Panel] = []):
        self.__title = title
        self.__panels_lists = panels_lists
        try:
            self.__color = color
            Color[self.__color].value
        except Exception as e:
            raise ValueError(
                "Board color must be one of the following: "
                "LIGHTBLUE, ROSE, GOLD, GREEN, LAVENDER, TEAL."
            )

    @property
    def title(self) -> str:
        return self.__title

    @property
    def color(self) -> str:
        return Color[self.__color].value

    @property
    def panels(self) -> List[Panel]:
        return self.__panels_lists

    @title.setter
    def title(self, title: str) -> None:
        if title is None:
            raise ValueError("Board title cannot be None.")
        self.__title = title

    @color.setter
    def color(self, color: str) -> None:
        if color in Color.value2member_map_:
            self.__color = color
        else:
            raise ValueError(
                "Board color must be one of the following: "
                "LIGHTBLUE, ROSE, GOLD, GREEN, LAVENDER, TEAL."
            )

    @panels.setter
    def panels(self, panel: Panel) -> None:
        if panel is None:
            raise ValueError("Panel cannot be None.")
        if panel in self.__panels_lists:
            raise ValueError("Panel already exists in board.")
        self.__panels_lists.append(panel)

    def __eq__(self, board):
        return (
            self.title == board.title and
            self.color == board.color and
            self.panels == board.panels
        )

    def __str__(self):
        return (
            f"{self.title=}, "
            f"color='{Color(self.color).name}'".replace("self.", "")
        )
