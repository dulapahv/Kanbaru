import logging
from typing import List

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow

from db import Database
from dialog import dialog_factory, input_dialog_factory
from kanbaru_objects import Board
from ui.about import About
from ui.ui_app_settings import Ui_SettingsWindow
from utils import keyPressEvent, modify_hex_color, setup_font_db


class AppSettings(QMainWindow):
    def __init__(self, parent: QMainWindow, board: Board) -> None:
        QMainWindow.__init__(self)

        self.ui: Ui_SettingsWindow = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.board: Board = board
        self.title: str = board.title
        self.color: str = board.color
        self.boards_to_delete: List[Board] = []

        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_rename.clicked.connect(self.rename)
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_logout.clicked.connect(
            lambda: dialog_factory(parent, self.logout, "Logout", "Are you sure you want to logout?", btn_color=self.color))
        self.ui.btn_delete_account.clicked.connect(
            lambda: dialog_factory(parent, self.delete_account, "Delete Account",
                                   "Are you sure you want to delete your account?\nThis action cannot be undone.", btn_color=self.color))

        self.ui.btn_delete.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.delete(event))
        self.ui.btn_rename.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.rename(event))
        self.ui.btn_cancel.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.close)
        self.ui.btn_save.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.save)
        self.ui.btn_logout.keyPressEvent = lambda event: keyPressEvent(
            event, parent,
            dialog_factory(parent, self.logout, "Logout", "Are you sure you want to logout?"))
        self.ui.btn_delete_account.keyPressEvent = lambda event: keyPressEvent(
            event, parent, dialog_factory(parent, self.delete_account, "Delete Account",
                                          "Are you sure you want to delete your account?\nThis action cannot be undone."))

        self.ui.listWidget_manage_board.verticalScrollBar().setSingleStep(10)

        self.setup_font()

        self.ui.listWidget_manage_board.addItems(
            [board.title for board in Database.get_instance().boards])

        stylesheet = \
            f"""
            QPushButton {{
                background-color: {self.color};
                color: #ffffff;
            }}
            QPushButton:hover {{
                background-color: {modify_hex_color(self.color, -30)};
            }}
            QPushButton:focus {{
                border-color: #000000;
                border-width: 1.5px;
                border-style: solid;
            }}
            """
        self.ui.label_app_settings.setStyleSheet(
            f"""
            background-color: qlineargradient(
                spread: pad,
                x1: 0.5,
                y1: 0.5,
                x2: 0.95,
                y2: 0.5,
                stop: 0 {self.color},
                stop: 1 rgba(69, 76, 90, 255)
            );
            color: #ffffff;
            padding: 0px 0px 0px 10px;
            """
        )
        self.ui.btn_rename.setStyleSheet(stylesheet)
        self.ui.btn_about.setStyleSheet(stylesheet)
        self.ui.btn_save.setStyleSheet(stylesheet)

        self.ui.btn_about.clicked.connect(
            lambda event: self.show_about(event, board.color))

    def show_about(self, event, color: str) -> None:
        """Shows the about dialog"""
        self.about: About = About(color)
        self.about.show()

    def delete(self, event) -> None:
        selected_all = self.ui.listWidget_manage_board.selectedItems()
        if len(selected_all) == 0:
            dialog_factory(None, None, "Invalid Selection",
                           "Please select a board to delete. You can also select multiple boards to delete at the same time.", yes_no=False, btn_color=self.color)
            return None
        msg_list = '\n'.join(
            ["  - " + item for item in list(map(lambda x: x.text(), selected_all))])
        if dialog_factory(None, None, "Delete Board",
                          f"Are you sure you want to delete {'these boards' if len(selected_all) > 1 else 'this board'}?\n{msg_list}\n\nYou can still undo by pressing the Cancel button.", btn_color=self.color):
            for selected_board in selected_all:
                board_obj = next(
                    (board for board in Database.get_instance().boards if board.title == selected_board.text()), None)
                self.boards_to_delete.append(board_obj)
                self.ui.listWidget_manage_board.takeItem(
                    self.ui.listWidget_manage_board.row(selected_board))

    def rename(self, event) -> None:
        selected_all = self.ui.listWidget_manage_board.selectedItems()
        if len(selected_all) == 0:
            dialog_factory(None, None, "Invalid Selection",
                           "Please select a board to rename.", yes_no=False, btn_color=self.color)
            return None
        if len(selected_all) > 1:
            dialog_factory(None, None, "Invalid Selection",
                           "Please select only one board to rename.", yes_no=False, btn_color=self.color)
            return None
        text = input_dialog_factory(
            "Rename Board", "Enter new board name:", selected_all[0].text(), btn_color=self.color)
        if text is None:
            return None
        board_obj = next(
            (board for board in Database.get_instance().boards if board.title == selected_all[0].text()), None)
        self.title = text
        Database.get_instance().update_board(board_obj, self)
        self.ui.listWidget_manage_board.takeItem(
            self.ui.listWidget_manage_board.row(selected_all[0]))
        board_obj.title = text
        self.ui.listWidget_manage_board.insertItem(
            self.ui.listWidget_manage_board.currentRow() + 1, board_obj.title)

    def save(self) -> None:
        for board in self.boards_to_delete:
            Database.get_instance().delete_board(board)
        self.close()

    def logout(self, parent: QMainWindow):
        Database.get_instance().logout()
        logging.info("Going to welcome screen...")
        self.close()
        from ui.welcome import WelcomeScreen
        WelcomeScreen(parent)

    def delete_account(self, parent: QMainWindow):
        Database.get_instance().delete_account()
        logging.info("Going to welcome screen...")
        self.close()
        from ui.welcome import WelcomeScreen
        WelcomeScreen(parent)

    def get_board_index(self) -> int:
        return self.ui.listWidget_manage_board.currentRow()

    def setup_font(self) -> None:
        toruspro = setup_font_db("TorusPro.ttf")[0]
        self.ui.label_app_settings.setFont(QFont(toruspro, 28))
        self.ui.label_manage_board.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_account.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_board_desc.setFont(QFont(toruspro, 11))
        self.ui.btn_delete.setFont(QFont(toruspro, 12))
        self.ui.btn_rename.setFont(QFont(toruspro, 12))
        self.ui.btn_logout.setFont(QFont(toruspro, 12))
        self.ui.btn_delete_account.setFont(QFont(toruspro, 12))
        self.ui.btn_cancel.setFont(QFont(toruspro, 12))
        self.ui.btn_save.setFont(QFont(toruspro, 12))
