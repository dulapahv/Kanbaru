import os
from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QKeyEvent
from PySide6.QtWidgets import (QInputDialog, QLineEdit, QMainWindow,
                               QMessageBox, QPushButton)


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


def dialog_factory(parent: QMainWindow, function: Callable, title: str, msg: str, yes_no: bool = True, btn_color: str = "#6badee") -> bool:
    """Creates a dialog box with a title, message, and two buttons.

    Parameters
    ----------
    parent : QMainWindow
        The parent window of the dialog box.
    function : Callable
        The function to be called when the user clicks the "Yes" button.
    title : str
        The title of the dialog box.
    msg : str
        The message of the dialog box.

    Returns
    -------
    bool
        True if the user clicks the "Yes" button, False otherwise.
    """
    dialog = QMessageBox()
    dialog.setWindowTitle(title)
    dialog.setText(msg)
    font = setup_font_db("TorusPro.ttf")
    dialog.setFont(font[0])
    if yes_no:
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttons = dialog.findChildren(QPushButton)
        for button in buttons:
            if dialog.buttonRole(button) == QMessageBox.YesRole:
                button.setObjectName("yesButton")
            elif dialog.buttonRole(button) == QMessageBox.NoRole:
                button.setObjectName("noButton")
            button.setFont(font[0])
        dialog.setStyleSheet(
            f"""
            QLabel {{
                color: #ffffff;
                font-size: 15px;
                padding: 10px 18px 5px 0px;
            }}
            QPushButton {{
                color: #ffffff;
                font-size: 15px;
                width: 80%;
                height: 25%;
                border-radius: 5px;
            }}
            QPushButton#yesButton {{
                background-color: {btn_color};
            }}
            QPushButton#noButton {{
                background-color: #7f8ca6;
            }}
            QPushButton#yesButton:hover {{
                background-color: {modify_hex_color(btn_color, -30)};
            }}
            QPushButton#noButton:hover {{
                background-color: {modify_hex_color("#7f8ca6", -30)};
            }}
            QPushButton:focus {{
                border-color: #000000;
                border-width: 1px;
                border-style: solid;
            }}
            QMessageBox {{
                background-color: #454c5a;
            }}
            """
        )
        buttons[1].setFocus()
    else:
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.setStyleSheet(
            f"""
            QLabel {{
                color: #ffffff;
                font-size: 15px;
                padding: 10px 18px 5px 0px;
            }}
            QPushButton {{
                background-color: {btn_color};
                color: #ffffff;
                border-radius: 5px;
                width: 80%; height: 25%
            }}
            QMessageBox {{
                background-color: #454c5a;
            }}
            """
        )
    if dialog.exec() == QMessageBox.Yes:
        if function is not None:
            function(parent)
        return True
    return False


def input_dialog_factory(title: str, msg: str, default: str = "", btn_color: str = "#6badee") -> str:
    """Creates an input dialog box with a title, message, and an input field.

    Parameters
    ----------
    parent : QMainWindow
        The parent window of the dialog box.
    title : str
        The title of the dialog box.
    msg : str
        The message of the dialog box.
    default : str, optional
        The default text in the input field, by default ""

    Returns
    -------
    str
        The text in the input field.
    """
    dialog = QInputDialog()
    font = setup_font_db("TorusPro.ttf")
    dialog.setFont(font[0])
    dialog.setStyleSheet(
        """
        QLabel {
            color: #ffffff;
            font-size: 14px;
        }
        QLineEdit {
            color: #ffffff;
            font-size: 14px;
            background-color: #454c5a;
            border: 1px solid #ffffff;
            border-radius: 5px;
        }
        QLineEdit:focus {
            border: 1px solid #000000;
        }
        """
    )
    text, ok = dialog.getText(None, title, msg, QLineEdit.Normal, default)
    if ok:
        return text
    return None


def keyPressEvent(event: QKeyEvent, parent: QMainWindow = None, function: Callable = None) -> Callable:
    """This function is used to call a function when the enter key is pressed

    Parameters
    ----------
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
