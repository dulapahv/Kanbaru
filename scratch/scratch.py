import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_activity)
        self.setMouseTracking(True)
        self.printed = False  # Flag to track if "Hello World" has been printed

    def start_timer(self):
        self.timer.start(3000)  # 3 seconds

    def check_activity(self):
        if not QApplication.mouseButtons() and not QApplication.keyboardModifiers():
            if not self.printed:
                print("Hello World")
                self.printed = True
            self.start_timer()

    def mouseMoveEvent(self, event):
        print("Mouse moved")
        self.start_timer()
        self.printed = False

    def keyPressEvent(self, event):
        self.start_timer()
        self.printed = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
