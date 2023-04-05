from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.ui_about import Ui_About
from base64 import b64decode


class About(QMainWindow):
    def __init__(self, color: str) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_About()
        self.ui.setupUi(self)

        self.count = 0

        self.ui.centralwidget.mousePressEvent = lambda event: self.deleteLater()
        self.ui.label_logo_bottom.mousePressEvent = lambda event: self.easter_egg()
        self.setWindowModality(Qt.ApplicationModal)

        self.ui.label_description_2.setText(QCoreApplication.translate(
            "About",
            f"<html><head/><body>"
            f"<p>1. Dulapah Vibulsanti (<a href=\"https://github.com/dulapahv\">"
            f"<span style=\"font-weight:700; text-decoration: underline; color:{color};\">github/dulapahv</span>"
            f"</a>)</p>"
            f"<p>2. Anucha Cheewachanon (<a href=\"https://github.com/SpiralNuggets\">"
            f"<span style=\"font-weight:700; text-decoration: underline; color:{color};\">github/SpiralNuggets</span>"
            f"</a>)</p>"
            f"<p>3. Annopdanai Pamarapa (<a href=\"https://github.com/beam2546\">"
            f"<span style=\"font-weight:700; text-decoration: underline; color:{color};\">github/beam2546</span>"
            f"</a>)</p>"
            f"<p><span style=\"font-weight:700;\">View Kanbaru on </span>"
            f"<a href=\"https://github.com/dulapahv/Kanbaru\">"
            f"<span style=\"font-weight:700; text-decoration: underline; color:{color};\">Github</span></a></p>"
            f"</body></html>",
            None))

        self.ui.label_license.setText(QCoreApplication.translate(
            "About",
            f"<html><head/><body>"
            f"<p>Kanbaru is released under the MIT license. See "
            f"<a href=\"https://github.com/dulapahv/Kanbaru/blob/main/LICENSE\">"
            f"<span style=\"font-weight:700; text-decoration: underline; color:{color};\">LICENSE</span></a>"
            f" for more information.</p>"
            f"</body></html>",
            None))

    def deleteLater(self) -> None:
        if self.ui.label_license.underMouse() or self.ui.label_description_2.underMouse():
            return None
        super().deleteLater()

# TODO: Make Suruga Kanbaru not stretched out
    def easter_egg(self) -> None:
        self.count += 1
        if self.count == 5:
            print("Easter egg found!")
            with open("src/resources/img/rainydevil.txt", "r") as f:
                b64data = f.read()
                data = b64decode(b64data)
                rainydevilpic = QPixmap()
                rainydevilpic.loadFromData(data, "PNG")
                rainydevilpic = rainydevilpic.scaled(
                    100, 100, Qt.KeepAspectRatio)
                self.ui.label_logo_bottom.setPixmap(rainydevilpic)
                self.ui.label_logo_bottom.setScaledContents(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        path = QPainterPath()
        path.addRoundedRect(rect, 20, 20)

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
