import os
from typing import Callable

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QMainWindow, QMessageBox


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
    path = get_current_directory()
    font_path = os.path.dirname(path)
    font_path = os.path.join(path, "resources", "font", font)
    font_database = QFontDatabase.addApplicationFont(font_path)
    if font_database < 0:
        raise Exception(
            f'Font not found at path "{font_path}"! Exiting...')
    return QFontDatabase.applicationFontFamilies(font_database)


def dialog_factory(parent: QMainWindow, function: Callable, title: str, msg: str) -> None:
    dialog = QMessageBox()
    dialog.setIcon(QMessageBox.Information)
    dialog.setWindowTitle(title)
    dialog.setText(msg)
    dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    if dialog.exec() == QMessageBox.Yes:
        function(parent)
