from typing import List

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from db import Database
from kanbaru_objects import Board, Color, Panel
from ui.ui_board_settings import Ui_BoardWindow
from utils import (dialog_factory, input_dialog_factory, keyPressEvent,
                   modify_hex_color, setup_font_db)


class BoardSettings(QMainWindow):
    def __init__(self, board: Board) -> None:
        QMainWindow.__init__(self)

        self.title_txt = None
        self.ui: Ui_BoardWindow = Ui_BoardWindow()
        self.ui.setupUi(self)

        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_rename.clicked.connect(self.rename)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_cancel.clicked.connect(self.close)

        self.ui.btn_delete.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.delete(event))
        self.ui.btn_rename.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.rename(event))
        self.ui.btn_save.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.save)
        self.ui.btn_cancel.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.close)

        self.board = board
        self.title = board.title
        self.color = board.color
        self.panels_to_delete: List[Board] = []

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
        self.ui.lineEdit_title.setStyleSheet(
            f"""
            QLineEdit {{
                background-color: #ebecf0;
                color: #282c33;
                border-radius: 5px;
                padding: 0px 8px 0px 8px
            }}
            QLineEdit:focus {{
                background-color: #ffffff;
                border-color: {self.color};
                border-width: 1.5px;
                border-style: solid;
                padding: 0px 6px 0px 6px
            }}
            """
        )
        self.ui.btn_rename.setStyleSheet(stylesheet)
        self.ui.btn_save.setStyleSheet(stylesheet)

        self.ui.listWidget_manage_panel.addItems(
            [panel.title for panel in self.board.panels])

        self.setup_font()

        self.ui.label_board_desc.setStyleSheet(
            f"""
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, 
                x2:0.95, y2:0.5, stop:0 {self.color},
                stop:1 rgba(69, 76, 90, 255)
            );
            color: #ffffff;
            padding: 0px 0px 0px 10px;
            """
        )

    def delete(self, event) -> None:
        selected_all = self.ui.listWidget_manage_panel.selectedItems()
        if len(selected_all) == 0:
            dialog_factory(None, None, "Invalid Selection",
                           "Please select a panel to delete. You can also select multiple panels to delete at the same time.", yes_no=False, btn_color=self.color)
            return None
        msg_list = '\n'.join(
            ["  - " + item for item in list(map(lambda x: x.text(), selected_all))])
        if dialog_factory(None, None, "Delete Panel",
                          f"Are you sure you want to delete {'these panels' if len(selected_all) > 1 else 'this panel'}?\n{msg_list}\n\nYou can still undo by pressing the Cancel button.", btn_color=self.color):
            for selected_panel in selected_all:
                panel_obj = next(
                    (panel for panel in self.board.panels if panel.title == selected_panel.text()), None)
                self.panels_to_delete.append(panel_obj)
                self.ui.listWidget_manage_panel.takeItem(
                    self.ui.listWidget_manage_panel.row(selected_panel))

    def rename(self, event) -> None:
        selected_all = self.ui.listWidget_manage_panel.selectedItems()
        if len(selected_all) == 0:
            dialog_factory(None, None, "Invalid Selection",
                           "Please select a panel to rename.", yes_no=False, btn_color=self.color)
            return None
        if len(selected_all) > 1:
            dialog_factory(None, None, "Invalid Selection",
                           "Please select only one panel to rename.", yes_no=False, btn_color=self.color)
            return None
        text = input_dialog_factory(
            "Rename Panel", "Enter new panel name:", selected_all[0].text(), btn_color=self.color)
        if text is None:
            return None
        panel_obj = next(
            (panel for panel in self.board.panels if panel.title == selected_all[0].text()), None)
        self.title = text
        Database.get_instance().update_panel(panel_obj, self)
        self.ui.listWidget_manage_panel.takeItem(
            self.ui.listWidget_manage_panel.row(selected_all[0]))
        panel_obj.title = text
        self.ui.listWidget_manage_panel.insertItem(
            self.ui.listWidget_manage_panel.currentRow() + 1, panel_obj.title)

    def save(self) -> None:
        for panel in self.panels_to_delete:
            Database.get_instance().delete_panel(panel)
        self.close()

    @property
    def title_line_edit(self) -> str:
        return self.title_txt

    @property
    def color(self) -> str:
        button = next((btn for btn in (self.ui.btn_color_1, self.ui.btn_color_2, self.ui.btn_color_3,
                                       self.ui.btn_color_4, self.ui.btn_color_5, self.ui.btn_color_6) if btn.isChecked()), None)
        match button:
            case self.ui.btn_color_1:
                return Color.LIGHTBLUE._value_
            case self.ui.btn_color_2:
                return Color.ROSE._value_
            case self.ui.btn_color_3:
                return Color.GOLD._value_
            case self.ui.btn_color_4:
                return Color.GREEN._value_
            case self.ui.btn_color_5:
                return Color.LAVENDER._value_
            case self.ui.btn_color_6:
                return Color.TEAL._value_
            case _:
                return Color.LIGHTBLUE._value_

    @title_line_edit.setter
    def title_line_edit(self, text: str) -> None:
        self.ui.lineEdit_title.setText(text)

    @color.setter
    def color(self, color: str) -> None:
        match color:
            case Color.LIGHTBLUE._value_:
                self.ui.btn_color_1.setChecked(True)
            case Color.ROSE._value_:
                self.ui.btn_color_2.setChecked(True)
            case Color.GOLD._value_:
                self.ui.btn_color_3.setChecked(True)
            case Color.GREEN._value_:
                self.ui.btn_color_4.setChecked(True)
            case Color.LAVENDER._value_:
                self.ui.btn_color_5.setChecked(True)
            case Color.TEAL._value_:
                self.ui.btn_color_6.setChecked(True)
            case _:
                self.ui.btn_color_1.setChecked(True)

    def title_listener(self, text: str) -> None:
        self.title_txt = text

    def setup_font(self) -> None:
        notosans = setup_font_db("NotoSans.ttf")[0]
        toruspro = setup_font_db("TorusPro.ttf")[0]
        self.ui.label_board_desc.setFont(QFont(toruspro, 28))
        self.ui.label_title.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_color.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_panel.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_manage_panel_desc.setFont(QFont(toruspro, 11))
        self.ui.lineEdit_title.setFont(QFont(notosans, 12))
        self.ui.btn_color_1.setFont(QFont(toruspro, 12))
        self.ui.btn_color_2.setFont(QFont(toruspro, 12))
        self.ui.btn_color_3.setFont(QFont(toruspro, 12))
        self.ui.btn_color_4.setFont(QFont(toruspro, 12))
        self.ui.btn_color_5.setFont(QFont(toruspro, 12))
        self.ui.btn_color_6.setFont(QFont(toruspro, 12))
        self.ui.listWidget_manage_panel.setFont(QFont(toruspro, 12))
        self.ui.btn_delete.setFont(QFont(toruspro, 12))
        self.ui.btn_rename.setFont(QFont(toruspro, 12))
        self.ui.btn_cancel.setFont(QFont(toruspro, 12))
        self.ui.btn_save.setFont(QFont(toruspro, 12))
