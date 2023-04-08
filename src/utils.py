import os
from typing import Callable, Type

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QKeyEvent
from PySide6.QtWidgets import QMainWindow


def overrides(interface_class: Type) -> Callable[[Callable], Callable]:
    """This function is used to override a method in a class.

    Parameters
    ----------
    interface_class : Type
        The class to override the method in.

    Returns
    -------
    overrider : Callable[[Callable], Callable]
        The overrider function.
    """
    def overrider(method: Callable) -> Callable:
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


def hex_to_rgba(hex_color: str) -> str:
    """Converts a hex color to a rgba color.

    Parameters
    ----------
    hex_color : str
        The hex color to be converted.

    Returns
    -------
    rgba_color : str
        The rgba color.
    """
    return hex_color.replace('rgb', 'rgba').replace(')', ', 255)')


def modify_hex_color(hex_color: str, modifier: int = 30) -> str:
    """Lightens a hex color by a specified amount.
    - Converts hex color to RGB
    - Calculates new RGB values for lighter shade
    - Converts back to hex color code

    Parameters
    ----------
    hex_color : str
        The hex color to be lightened.
    modifier : int, optional
        The amount to lighten the color by, by default 30

    Returns
    -------
    light_hex_color : str
        The lightened hex color.
    """
    red = int(hex_color[1:3], 16)
    green = int(hex_color[3:5], 16)
    blue = int(hex_color[5:], 16)

    light_red = min(int(red + modifier), 255)
    light_green = min(int(green + modifier), 255)
    light_blue = min(int(blue + modifier), 255)

    light_hex_color = '#' + \
        format(light_red, '02x') + format(light_green,
                                          '02x') + format(light_blue, '02x')

    return light_hex_color


def get_current_directory() -> str:
    """Returns the current directory of the application. If the current
    directory is not the src directory, it will be appended to the path.

    Returns
    -------
    path : str
        The current directory of the application.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(path) != "src":
        path = os.path.join(path, "src")
    return path


def setup_font_db(font: str) -> QFontDatabase:
    """Sets up the font database for the application.

    Parameters
    ----------
    font : str
        The name of the font to be added to the database.

    Returns
    -------
    font_database : QFontDatabase
        The font database for the application.
    """
    path = get_current_directory()
    font_path = os.path.dirname(path)
    font_path = os.path.join(path, "resources", "font", font)
    font_database = QFontDatabase.addApplicationFont(font_path)
    if font_database < 0:
        raise Exception(
            f'Font not found at path "{font_path}"! Exiting...')
    return QFontDatabase.applicationFontFamilies(font_database)


def keyPressEvent(event: QKeyEvent, parent: QMainWindow = None, function: Callable = None) -> Callable:
    """This function is used to call a function when the enter key is pressed

    Parameters
    ----------
    parent
    event : QKeyEvent
        The key event
    function : Callable
        The function to call
    """
    if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
        if not function:
            return None
        if not parent:
            return function()
        return function(parent)
