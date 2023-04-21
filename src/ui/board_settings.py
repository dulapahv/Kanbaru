from typing import List

from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow

from db import Database
from dialog import dialog_factory, input_dialog_factory
from kanbaru_objects import Board, Color, Panel
from ui.board_settings_ui import Ui_BoardWindow
from utils import keyPressEvent, modify_hex_color, setup_font_db


class BoardSettings(QMainWindow):
    def __init__(self, board: Board) -> None:
        QMainWindow.__init__(self)

        self.title_txt: str = None
        self.ui: Ui_BoardWindow = Ui_BoardWindow()
        self.ui.setupUi(self)

        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_rename.clicked.connect(self.rename)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_cancel.clicked.connect(self.close)

        self.ui.lineEdit_title.textChanged.connect(self.title_listener)

        self.ui.btn_delete.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.delete(event))
        self.ui.btn_rename.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.rename(event))
        self.ui.btn_save.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.save)
        self.ui.btn_cancel.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.close)

        self.ui.listWidget_manage_panel.verticalScrollBar().setSingleStep(10)
        self.ui.listWidget_manage_panel.model().rowsMoved.connect(
            self.rowsMoved)

        self.board = board
        self.old_board: Board = board
        self.title = board.title
        self.color = board.color
        self.panels = board.panels
        self.panels_to_delete: List[Board] = []
        self.new_panel_order: List[Board] = []
        self.colors_to_change: Color.name = None

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
                padding: 0 8px 0 8px
            }}
            QLineEdit:focus {{
                background-color: #ffffff;
                border-color: {self.color};
                border-width: 1.5px;
                border-style: solid;
                padding: 0 6px 0 6px
            }}
            QLineEdit QMenu {{
                background-color: #454c5a;
                border: none;
                padding: 5px;
                margin: 0px;
                font-size: 13px;
            }}
            QLineEdit QMenu::item {{
                padding: 5px 13px 5px 13px;
                color: #ffffff;
            }}
            QLineEdit QMenu::item:selected {{
                border-radius: 5px;
                background-color: {modify_hex_color(self.color)};
                color: #000000;
            }}
            """
        )
        self.ui.scrollArea.setStyleSheet(
            f"""
            QScrollBar:vertical {{
                border: none;
                background: #f4f5f7;
                width: 10px;
                margin: 1px 0 0 0;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical {{
                background-color: #bfc0c5;
                min-height: 30px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: #afb0b4;
            }}

            QScrollBar::handle:vertical:pressed {{
                background-color: #929497;
            }}
            QScrollBar::sub-line:vertical {{
                height: 0;
            }}
            QScrollBar::add-line:vertical {{
                height: 0;
            }}
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {{
                background: none;
            }}
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {{
                background: none;
            }}
            QScrollBar QMenu {{
                background-color: #454c5a;
                border: none;
                padding: 5px;
                margin: 0px;
                font-size: 13px;
            }}
            QScrollBar QMenu::item {{
                padding: 5px 13px 5px 13px;
                color: #ffffff;
            }}
            QScrollBar QMenu::item:selected {{
                border-radius: 5px;
                background-color: {modify_hex_color(self.color)};
                color: #000000;
            }}
            """
        )
        self.ui.listWidget_manage_panel.setStyleSheet(
            f"""
            QListWidget::item {{
                height: 40px;
                padding: 0 8px 0 8px
            }}
            QListWidget::item {{
                background-color: #ffffff;
                color: #000000;
                border-radius: 5px
            }}
            QListWidget::item:hover {{
                background-color: #e2e4e9;
                color: #000000
            }}
            QListWidget::item:selected {{
                background-color: #cccccc;
                color: #000000
            }}
            QListWidget::item:focus {{
                background-color: #cccccc;
                color: #000000
            }}
            QScrollBar:vertical {{
                border: none;
                background: #f4f5f7;
                width: 10px;
                margin: 1px 0 0 0;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical {{
                background-color: #bfc0c5;
                min-height: 30px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: #afb0b4;
            }}
            QScrollBar::handle:vertical:pressed {{
                background-color: #929497;
            }}
            QScrollBar::sub-line:vertical {{
                height: 0;
            }}
            QScrollBar::add-line:vertical {{
                height: 0;
            }}
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {{
                background: none;
            }}
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {{
                background: none;
            }}
            QScrollBar QMenu {{
                background-color: #454c5a;
                border: none;
                padding: 5px;
                margin: 0px;
                font-size: 13px;
            }}
            QScrollBar QMenu::item {{
                padding: 5px 13px 5px 13px;
                color: #ffffff;
            }}
            QScrollBar QMenu::item:selected {{
                border-radius: 5px;
                background-color: {modify_hex_color(self.color)};
                color: #000000;
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
            padding: 0 0 0 10px;
            """
        )

    def delete(self, event) -> None:
        """Delete all selected panels."""
        selected_all = self.ui.listWidget_manage_panel.selectedItems()
        if len(selected_all) == 0:
            dialog_factory(
                title="Invalid Selection",
                msg="Please select a panel to delete. You can also select "
                "multiple panels to delete at the same time.",
                yes_no=False,
                btn_color=self.color
            )
            return None
        msg_list = '\n'.join(
            ["  - " + item for item in list(
                map(lambda x: x.text(), selected_all))])
        if dialog_factory(
            title="Delete Panel",
            msg="Are you sure you want to delete "
            f"{'these panels' if len(selected_all) > 1 else 'this panel'}"
            f"?\n{msg_list}\n\nYou can still undo by pressing the Cancel "
            "button.",
            btn_color=self.color
        ):
            for selected_panel in selected_all:
                panel_obj = next(
                    (panel for panel in self.board.panels if
                     panel.title == selected_panel.text()), None)
                self.panels_to_delete.append(panel_obj)
                self.ui.listWidget_manage_panel.takeItem(
                    self.ui.listWidget_manage_panel.row(selected_panel))

    def rename(self, event) -> None:
        """Rename selected panel."""
        selected_all = self.ui.listWidget_manage_panel.selectedItems()
        if len(selected_all) == 0:
            dialog_factory(
                title="Invalid Selection",
                msg="Please select a panel to rename.",
                yes_no=False,
                btn_color=self.color
            )
            return None
        if len(selected_all) > 1:
            dialog_factory(
                title="Invalid Selection",
                msg="Please select only one panel to rename.",
                yes_no=False,
                btn_color=self.color
            )
            return None
        text = input_dialog_factory(
            title="Rename Panel",
            msg="Enter new panel name:",
            default=selected_all[0].text(),
            btn_color=self.color
        )
        if text is None:
            return None
        for board in Database.get_instance().boards:
            for panel in board.panels:
                if panel.title == text:
                    dialog_factory(
                        title="Invalid Name",
                        msg="A panel with this name already exists.",
                        yes_no=False,
                        btn_color=self.color
                    )
                    self.rename(event)
                    return None
        panel_obj = next(
            (panel for panel in self.board.panels if
             panel.title == selected_all[0].text()), None)
        new_panel = Panel(
            title=text,
            card_lists=panel_obj.cards
        )
        Database.get_instance().update_panel(panel_obj, new_panel)
        self.ui.listWidget_manage_panel.takeItem(
            self.ui.listWidget_manage_panel.row(selected_all[0]))
        panel_obj.title = text
        self.ui.listWidget_manage_panel.insertItem(
            self.ui.listWidget_manage_panel.currentRow() + 1, panel_obj.title)

    def save(self) -> None:
        """Deletes the selected panels and saves the board order."""
        for panel in self.panels_to_delete:
            Database.get_instance().delete_panel(panel)
        if self.old_board != self:
            Database.get_instance().update_board(self.old_board, self)
        if len(self.new_panel_order) != 0:
            Database.get_instance().update_panel_order(
                self.board, self.new_panel_order)
        self.close()

    @property
    def title(self) -> str:
        return self.title_txt

    @property
    def color(self) -> str:
        button = next(
            (btn for btn in (
                self.ui.btn_color_1, self.ui.btn_color_2, self.ui.btn_color_3,
                self.ui.btn_color_4, self.ui.btn_color_5, self.ui.btn_color_6
            ) if btn.isChecked()), None)
        match button:
            case self.ui.btn_color_1:
                return Color.LIGHTBLUE.value
            case self.ui.btn_color_2:
                return Color.ROSE.value
            case self.ui.btn_color_3:
                return Color.GOLD.value
            case self.ui.btn_color_4:
                return Color.GREEN.value
            case self.ui.btn_color_5:
                return Color.LAVENDER.value
            case self.ui.btn_color_6:
                return Color.TEAL.value
            case _:
                return Color.LIGHTBLUE.value

    @title.setter
    def title(self, text: str) -> None:
        self.ui.lineEdit_title.setText(text)
        self.title_txt = text

    @color.setter
    def color(self, color: str) -> None:
        match color:
            case Color.LIGHTBLUE.value:
                self.ui.btn_color_1.setChecked(True)
            case Color.ROSE.value:
                self.ui.btn_color_2.setChecked(True)
            case Color.GOLD.value:
                self.ui.btn_color_3.setChecked(True)
            case Color.GREEN.value:
                self.ui.btn_color_4.setChecked(True)
            case Color.LAVENDER.value:
                self.ui.btn_color_5.setChecked(True)
            case Color.TEAL.value:
                self.ui.btn_color_6.setChecked(True)
            case _:
                self.ui.btn_color_1.setChecked(True)

    def rowsMoved(self, source_parent: QModelIndex, source_start: int,
                  source_end: int, dest_parent: QModelIndex,
                  dest_row: int) -> None:
        """Updates the new panel order when the user moves a panel."""
        self.new_panel_order = [self.ui.listWidget_manage_panel.item(
            i).text() for i in range(self.ui.listWidget_manage_panel.count())]
        self.new_panel_order = [
            next((panel for panel in self.board.panels
                  if panel.title == panel_title), None)
            for panel_title in self.new_panel_order
        ]

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
