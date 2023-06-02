from typing import Callable, Type

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QLineEdit,
                               QMessageBox, QPushButton, QVBoxLayout)

from utils import get_current_directory, modify_hex_color, setup_font_db


def dialog_factory(parent: Type = None, function: Callable = None,
                   title: str = "", msg: str = "", yes_no: bool = True,
                   btn_color: str = "#6badee") -> bool | Callable:
    """This function is used to create a dialog box.
    If `yes_no` is True, the dialog box will have a "Yes" and "No" button.
    If `yes_no` is False, the dialog box will only have a "Close" button.

    Parameters
    ----------
    parent : Type
        The parent of the dialog box.
    function : Callable
        The function to call when the "Yes" button is clicked.
    title : str
        The title of the dialog box, by default "".
    msg : str
        The message to display in the dialog box, by default "".
    yes_no : bool
        Whether to display the "Yes" and "No" buttons, by default True.
    btn_color : str
        The color of the "Yes" button, by default "#6badee".

    Returns
    -------
    bool
        True if the user clicks the "Yes" button, False otherwise.
    Callable
        The function to call when the "Yes" button is clicked.
    """
    dialog = QMessageBox()
    icon = QIcon(f"{get_current_directory()}/resources/img/icon.png")
    dialog.setWindowIcon(icon)
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
                padding: 10px 18px 5px 0;
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
        buttons = dialog.findChildren(QPushButton)
        for button in buttons:
            button.setFont(QFont(font[0], 10))
        dialog.setStyleSheet(
            f"""
            QLabel {{
                color: #ffffff;
                font-size: 15px;
                padding: 10px 18px 5px 0;
            }}
            QPushButton {{
                background-color: {btn_color};
                color: #ffffff;
                border-radius: 5px;
                width: 80%; height: 25%
            }}
            QPushButton:hover {{
                background-color: {modify_hex_color(btn_color, -30)};
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
    if dialog.exec() == QMessageBox.Yes:
        if function is not None:
            function(parent)
        return True
    return False


def input_dialog_factory(title: str = "", msg: str = "", default: str = "",
                         btn_color: str = "#6badee") -> None | str:
    """This function is used to create an input dialog box.

    Parameters
    ----------
    title : str
        The title of the dialog box, by default "".
    msg : str
        The message to display in the dialog box, by default "".
    default : str
        The default text in the input field, by default "".
    btn_color : str
        The color of the "Ok" button, by default "#6badee".

    Returns
    -------
    None
        If the user clicks the "Cancel" button.
    str
        The text in the input field.
    """
    dialog = QDialog()
    icon = QIcon(f"{get_current_directory()}/resources/img/icon.png")
    dialog.setWindowIcon(icon)
    dialog.setWindowTitle(title)
    dialog.setFixedSize(dialog.size())
    dialog.setFixedSize(300, 100)
    layout = QVBoxLayout()
    label = QLabel(msg)
    line_edit = QLineEdit()
    line_edit.setText(default)
    buttons = QDialogButtonBox(
        QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, dialog)
    buttons.accepted.connect(dialog.accept)
    buttons.rejected.connect(dialog.reject)
    layout.addWidget(label)
    layout.addWidget(line_edit)
    layout.addWidget(buttons)
    dialog.setLayout(layout)
    font = setup_font_db("TorusPro.ttf")
    dialog.setFont(font[0])
    label.setFont(font[0])
    line_edit.setFont(QFont(font[0], 12))
    buttons.button(QDialogButtonBox.Ok).setObjectName("okButton")
    buttons.button(QDialogButtonBox.Cancel).setObjectName("cancelButton")
    for button in buttons.buttons():
        button.setFont(QFont(font[0], 10))
    dialog.setStyleSheet(
        f"""
        QLabel {{
            color: #ffffff;
            font-size: 15px;
        }}
        QPushButton {{
            color: #ffffff;
            border-radius: 5px;
            width: 80%; height: 25%
        }}
        QPushButton#okButton {{
            background-color: {btn_color};
        }}
        QPushButton#cancelButton {{
            background-color: #7f8ca6;
        }}
        QPushButton#okButton:hover {{
            background-color: {modify_hex_color(btn_color, -30)};
        }}
        QPushButton#cancelButton:hover {{
            background-color: {modify_hex_color("#7f8ca6", -30)};
        }}
        QPushButton:focus {{
            border-color: #000000;
            border-width: 1px;
            border-style: solid;
        }}
        QDialog {{
            background-color: #454c5a;
        }}
        QLineEdit {{
            border-radius: 5px;
            height: 25%
        }}
        QLineEdit QMenu {{
            background-color: #454c5a;
            border: none;
            padding: 5px;
            margin: 0px;
            font-size: 13px;
        }}
        QLineEdit QMenu::item {{
            padding: 5px 13px 5px 13px;
            color: #ffffff;
        }}
        QLineEdit QMenu::item:selected {{
            border-radius: 5px;
            background-color: {modify_hex_color(btn_color)};
            color: #000000;
        }}
        """
    )
    line_edit.setFocus()
    result = dialog.exec()
    text = line_edit.text()
    if result == QDialog.Accepted:
        return text
    return None
