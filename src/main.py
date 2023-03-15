import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        fontDatabase = QFontDatabase()
        fontDatabase.addApplicationFont("./resources/font/TorusPro-Bold.otf")
        fontDatabase.addApplicationFont(
            "./resources/font/TorusPro-BoldItalic.otf")
        fontDatabase.addApplicationFont("./resources/font/TorusPro-Italic.otf")
        fontDatabase.addApplicationFont("./resources/font/TorusPro-Light.otf")
        fontDatabase.addApplicationFont(
            "./resources/font/TorusPro-LightItalic.otf")
        fontDatabase.addApplicationFont("./resources/font/TorusPro-Medium.otf")
        fontDatabase.addApplicationFont(
            "./resources/font/TorusPro-MediumItalic.otf")
        fontDatabase.addApplicationFont(
            "./resources/font/TorusPro-Regular.otf")
        fontDatabase.addApplicationFont(
            "./resources/font/TorusPro-SemiBold.otf")
        fontDatabase.addApplicationFont(
            "./resources/font/TorusPro-SemiBoldItalic.otf")
        fontDatabase.addApplicationFont("./resources/font/TorusPro-Thin.otf")
        fontDatabase.addApplicationFont(
            "./resources/font/TorusPro-ThinItalic.otf")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for obj in self.findChildren(QObject):
            if hasattr(obj, "setFont"):
                print(obj)
                obj.setFont(QFont("Torus Pro", 12))
        self.ui.label_list_1.setFont(QFont("Torus Pro", 12, QFont.Bold))
        self.ui.label_list_2.setFont(QFont("Torus Pro", 12, QFont.Bold))
        self.ui.label_list_3.setFont(QFont("Torus Pro", 12, QFont.Bold))
        self.ui.label_logo.setFont(QFont("Torus Pro", 36))
        self.ui.label_board.setFont(QFont("Torus Pro", 28))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    sys.exit(main())
