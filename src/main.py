import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        fontDatabase = QFontDatabase.addApplicationFont(
            "src\\resources\\font\\TorusPro-Regular.ttf")
        if fontDatabase < 0:
            sys.exit("Font not found")
        fontFamilies = QFontDatabase.applicationFontFamilies(fontDatabase)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for obj in self.findChildren(QObject):
            if hasattr(obj, "setFont"):
                obj.setFont(QFont(fontFamilies[0], 12))
        self.ui.label_list_1.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        self.ui.label_list_2.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        self.ui.label_list_3.setFont(QFont(fontFamilies[0], 12, QFont.Bold))
        self.ui.label_logo.setFont(QFont(fontFamilies[0], 36))
        self.ui.label_board.setFont(QFont(fontFamilies[0], 28))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    sys.exit(main())
