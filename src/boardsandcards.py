from enum import Enum
import random

class Color(Enum):
    LIGHTBLUE = "#6badee"
    ROSE = "#fb568a"
    GOLD = "#fbd945"
    GREEN = "#99c37b"
    LAVENDER = "#c577dc"
    TEAL = "#5eb5c1"


class Board:
    def __init__(self, id: int = random.randint(0, 1000000), color: Color = Color.LIGHTBLUE, title: str = "New Board"):
        self.__title = title
        self.__id = id
        self.__color = color
        self.__member = []

    def get_title(self):
        return self.__title

    def get_id(self):
        return self.__id
    
    def get_color(self):
        return self.__color
    
    def get_member(self):
        return self.__member
    
    def set_title(self, title):
        self.__title = title
    
    def set_color(self, color):
        if color in Color:
            self.__color = color
        else:
            raise ValueError("Invalid color. We only support the following colors: " + str(Color))

    def add_member(self, member):
        self.__member.append(member)

    def remove_member(self, member):
        self.__member.remove(member)

    def __str__(self):
        return str(self.__id)


#access card through board?
#TODO: figure out the datetime system for Qt
class Card:
    def __init__(self, title: str = "New Card", date, time, color: Color = Color.LIGHTBLUE, description):
        self.__title = title
        self.__description = description
        self.__color = color
        self.__date = date
        self.__time = time

    def get_title(self):
        return self.__title
    
    def get_description(self):
        return self.__description
    
    def get_color(self):
        return self.__color
    
    def get_date(self):
        return self.__date
    
    def get_time(self):
        return self.__time
    
    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description
    
    def set_color(self, color):
        if color in Color:
            self.__color = color
        else:
            raise ValueError("Invalid color. We only support the following colors: " + str(Color))
    

    #polymorphism to support multiple param types?
    def set_date(self, date):
        self.__date = date

    def set_time(self, time):
        self.__time = time

    