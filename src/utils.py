import os

from PySide6.QtGui import QFontDatabase


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


def setupFontDB(font: str | list[str]) -> QFontDatabase:
    path = getCurrentDirectory()
    if font is not list:
        font = [font]
    for f in font:
        fontPath = os.path.dirname(path)
        fontPath = os.path.join(path, "resources", "font", f)
        fontDatabase = QFontDatabase.addApplicationFont(fontPath)
        if fontDatabase < 0:
            raise Exception(
                f'Font not found at path "{fontPath}"! Exiting...')
    return QFontDatabase.applicationFontFamilies(fontDatabase)
