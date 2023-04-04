from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.ui_about import Ui_About


class About(QMainWindow):
    def __init__(self, color: str) -> None:
        QMainWindow.__init__(self)

        self.ui = Ui_About()
        self.ui.setupUi(self)

        self.count = 0

        self.ui.centralwidget.mousePressEvent = lambda event: self.deleteLater()
        self.ui.label_logo_bottom.mousePressEvent = lambda event: self.easter_egg()
        self.setWindowModality(Qt.ApplicationModal)

        self.ui.label_license.setText(QCoreApplication.translate(
            "About", f"<html><head/><body><p>Kanbaru is released under the MIT license. See <a "
                     f"href=\"https://github.com/dulapahv/Kanbaru/blob/main/LICENSE\"><span style=\" text-decoration: "
                     f"underline; color:{color};\">LICENSE</span></a> for more information.</p></body></html>", None))

    def deleteLater(self) -> None:
        if self.ui.label_license.underMouse():
            return
        super().deleteLater()

    def easter_egg(self) -> None:
        self.count += 1
        if self.count == 5:
            print("Easter egg found!")
        ...

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        path = QPainterPath()
        path.addRoundedRect(rect, 20, 20)

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
