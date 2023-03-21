import os
from typing import Callable

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QMainWindow, QMessageBox


def getCurrentDirectory() -> str:
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


def setupFontDB(font: str) -> QFontDatabase:
    path = getCurrentDirectory()
    fontPath = os.path.dirname(path)
    fontPath = os.path.join(path, "resources", "font", font)
    fontDatabase = QFontDatabase.addApplicationFont(fontPath)
    if fontDatabase < 0:
        raise Exception(
            f'Font not found at path "{fontPath}"! Exiting...')
    return QFontDatabase.applicationFontFamilies(fontDatabase)


def dialogFactory(parent: QMainWindow, function: Callable, title: str, msg: str) -> None:
    dialog = QMessageBox()
    dialog.setIcon(QMessageBox.Information)
    dialog.setWindowTitle(title)
    dialog.setText(msg)
    dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    if dialog.exec() == QMessageBox.Yes:
        function(parent)
