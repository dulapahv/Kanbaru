import logging
from base64 import b64decode

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QPainter, QPainterPath, QPixmap, QRegion
from PySide6.QtWidgets import QMainWindow

from ui.about_ui import Ui_About
from utils import get_current_directory, overrides


class About(QMainWindow):
    def __init__(self, color: str) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_About = Ui_About()
        self.ui.setupUi(self)

        self.count: int = 0

        self.ui.centralwidget.mousePressEvent = lambda event: \
            self.deleteLater()
        self.ui.label_logo_bottom.mousePressEvent = lambda event: \
            self.easter_egg()
        self.setWindowModality(Qt.ApplicationModal)

        self.ui.label_description_2.setText(QCoreApplication.translate(
            "About",
            "<html><head/><body>"
            "<p>1. Dulapah Vibulsanti"
            "(<a href='https://github.com/dulapahv'>"
            "<span style='font-weight:700; text-decoration: underline;"
            f"color:{color};'>github/dulapahv</span></a>)</p>"
            "<p>2. Anucha Cheewachanon"
            "(<a href='https://github.com/SpiralNuggets'>"
            "<span style='font-weight:700; text-decoration: underline;"
            f"color:{color};'>github/SpiralNuggets</span></a>)</p>"
            "<p>3. Annopdanai Pamarapa"
            "(<a href='https://github.com/beam2546'>"
            "<span style='font-weight:700; text-decoration: underline;"
            f"color:{color};'>github/beam2546</span></a>)</p>"
            "<p><span style='font-weight:700;'>View Kanbaru on </span>"
            "<a href='https://github.com/dulapahv/Kanbaru'>"
            "<span style='font-weight:700; text-decoration: underline;"
            f"color:{color};'>Github</span></a></p>"
            "</body></html>",
            None)
        )

        self.ui.label_license.setText(QCoreApplication.translate(
            "About",
            "<html><head/><body>"
            "<p>Kanbaru is released under the MIT license. See "
            "<a href='https://github.com/dulapahv/Kanbaru/blob/main/LICENSE'>"
            "<span style=\"font-weight:700; text-decoration: underline;"
            f"color:{color};\">LICENSE</span></a>"
            " for more information.</p>"
            "</body></html>",
            None)
        )

    @overrides(QMainWindow)
    def deleteLater(self) -> None:
        """Override deleteLater() to prevent closing the window when
        clicking on the label.
        """
        if self.ui.label_license.underMouse() or \
                self.ui.label_description_2.underMouse():
            return None
        super().deleteLater()

    def easter_egg(self) -> None:
        """Easter egg for the logo."""
        self.count += 1
        if self.count == 5:
            logging.info("Easter egg activated!")
            with open(get_current_directory() +
                      "\\resources\\img\\rainydevil.txt", "rb") as f:
                b64data = f.read()
                data = b64decode(b64data)
                rainydevilpic = QPixmap()
                rainydevilpic.loadFromData(data, "PNG")
                rainydevilpic = rainydevilpic.scaled(
                    100, 100, Qt.KeepAspectRatio)
                self.ui.label_logo_bottom.setPixmap(rainydevilpic)
                self.ui.label_logo_bottom.setScaledContents(True)
                self.ui.label_logo_bottom.setContentsMargins(0, 0, 0, 0)
                self.ui.label_logo_bottom.setFixedSize(100, 100)
                self.setFixedSize(628, 458)

    @overrides(QMainWindow)
    def paintEvent(self, event):
        """Override paintEvent() to make the window rounded."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        path = QPainterPath()
        path.addRoundedRect(rect, 20, 20)

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
