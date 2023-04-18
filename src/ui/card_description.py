from PySide6.QtCore import QDate, QTime
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow

from db import Database
from dialog import dialog_factory
from kanbaru_objects import Card
from ui.card_description_ui import Ui_CardWindow
from utils import hex_to_rgba, keyPressEvent, modify_hex_color, setup_font_db


class CardDescription(QMainWindow):
    def __init__(self, card: Card, color: str) -> None:
        QMainWindow.__init__(self)

        self.title_txt = None
        self.ui: Ui_CardWindow = Ui_CardWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_title.textChanged.connect(self.title_listener)

        self.ui.btn_delete.clicked.connect(
            lambda: dialog_factory(
                function=self.delete,
                title="Delete Card",
                msg="Are you sure you want to delete this card?\n"
                "This action cannot be undone.",
                btn_color=color
            )
        )
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save)

        self.ui.btn_delete.keyPressEvent = lambda event: keyPressEvent(
            event, function=dialog_factory(
                function=self.delete,
                title="Delete Card",
                msg="Are you sure you want to delete this card?\n"
                "This action cannot be undone.",
                btn_color=color
            )
        )
        self.ui.btn_cancel.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.close)
        self.ui.btn_save.keyPressEvent = lambda event: keyPressEvent(
            event, function=self.save)

        self.card = card
        self.color = color
        self.title = card.title
        self.date = card.date
        self.time = card.time
        self.description = card.description

        color = hex_to_rgba(color)
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
        self.ui.label_card_desc.setStyleSheet(
            f"""
            background-color: qlineargradient(
                spread:pad,
                x1:0.5,
                y1:0.5,
                x2:0.95,
                y2:0.5,
                stop:0 {self.color},
                stop:1 rgba(69, 76, 90, 255)
            );
            color: #ffffff;
            padding: 0 0 0 10px;
            """
        )
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
                background-color: #f5f5f5;
                border: none;
                padding: 5px;
                margin: 0px;
                font-size: 13px;
            }}
            QLineEdit QMenu::item {{
                padding: 5px 13px 5px 13px;
            }}
            QLineEdit QMenu::item:selected {{
                border-radius: 5px;
                background-color: {modify_hex_color(self.color)};
                color: #ffffff;
            }}
            """
        )
        self.ui.calendarWidget.setStyleSheet(
            f"""
            QCalendarWidget QWidget {{
                background-color: {modify_hex_color(self.color)};
            }}
            QCalendarWidget QAbstractItemView:!enabled {{
                color: #cecece
            }}
            QCalendarWidget QAbstractItemView:enabled {{
                color: #000000
            }}
            QCalendarWidget QToolButton {{
                padding: 5px;
            }}
            QCalendarWidget QMenu {{
                background-color: #f5f5f5;
                border: none;
                padding: 5px;
                margin: 0px;
                font-size: 14px;
            }}
            QCalendarWidget QMenu::item {{
                padding: 5px 15px 5px 15px;
            }}
            QCalendarWidget QMenu::item:selected {{
                border-radius: 5px;
                background-color: {modify_hex_color(self.color)};
                color: #ffffff;
            }}
            QCalendarWidget QToolButton {{
                icon-size: 18px;
            }}
            QCalendarWidget QToolButton#qt_calendar_prevmonth {{
                qproperty-icon: url(:/img/resources/img/left-arrow.png);
            }}
            QCalendarWidget QToolButton#qt_calendar_nextmonth {{
                qproperty-icon: url(:/img/resources/img/right-arrow.png);
            }}
            QCalendarWidget QToolButton:pressed {{
                background-color: {modify_hex_color(self.color, -30)};
            }}
            QCalendarWidget QSpinBox {{
                border: none;
                color: #000000;
            }}
            QCalendarWidget QSpinBox::up-button,
            QCalendarWidget QSpinBox::down-button {{
                border-radius: 5px;
            }}
            QCalendarWidget QSpinBox::up-arrow {{
                image: url(:/img/resources/img/up-arrow.png);
                width: 10px;
                height: 10px
            }}
            QCalendarWidget QSpinBox::down-arrow {{
                image: url(:/img/resources/img/down-arrow.png);
                width: 10px;
                height: 10px
            }}
            QCalendarWidget QSpinBox::up-arrow:pressed,
            QCalendarWidget QSpinBox::down-arrow:pressed {{
                width: 7px;
                height: 7px;
            }}
            """
        )
        self.ui.timeEdit.setStyleSheet(
            f"""
            QTimeEdit {{
                background-color: {modify_hex_color(self.color)};
                color: #ffffff;
                border-radius: 5px;
                padding: 0 5px 0 5px
            }}
            QTimeEdit:focus {{
                border-color: #000000;
                border-width: 1.5px;
                border-style: solid;
                padding: 0 3px 0 3px
            }}
            QTimeEdit::up-button,
            QTimeEdit::down-button {{
                border-radius: 5px;
            }}
            QTimeEdit::up-arrow {{
                image: url(:/img/resources/img/up-arrow.png);
                width: 15px;
                height: 15px
            }}
            QTimeEdit::down-arrow {{
                image: url(:/img/resources/img/down-arrow.png);
                width: 15px;
                height: 15px
            }}
            QTimeEdit::up-arrow:pressed,
            QTimeEdit::down-arrow:pressed {{
                width: 12px;
                height: 12px;
            }}
            QTimeEdit QMenu {{
                background-color: #f5f5f5;
                border: none;
                padding: 5px;
                margin: 0px;
                font-size: 13px;
            }}
            QTimeEdit QMenu::item {{
                padding: 5px 13px 5px 13px;
            }}
            QTimeEdit QMenu::item:selected {{
                border-radius: 5px;
                background-color: {modify_hex_color(self.color)};
                color: #ffffff;
            }}
            """
        )
        self.ui.textEdit_description.setStyleSheet(
            f"""QTextEdit {{
                background-color: #ebecf0;
                color: #282c33;
                border-radius:5px;
                padding: 4px 8px 4px 8px
            }}
            QTextEdit:focus {{
                background-color: #ffffff;
                border-color: {self.color};
                border-width: 1.5px;
                border-style: solid;
            }}
            QScrollBar:vertical {{
                width: 10px;
                margin: 0 0 0 0;
                background-color: #acb2bf
            }}
            QTextEdit QMenu {{
                background-color: #f5f5f5;
                border: none;
                padding: 5px;
                margin: 0px;
                font-size: 13px;
            }}
            QTextEdit QMenu::item {{
                padding: 5px 13px 5px 13px;
            }}
            QTextEdit QMenu::item:selected {{
                border-radius: 5px;
                background-color: {modify_hex_color(self.color)};
                color: #ffffff;
            }}
            """
        )
        self.ui.btn_save.setStyleSheet(stylesheet)

        self.setup_font()

    def save(self) -> None:
        """Saves the card to the database."""
        if self.title_txt == "":
            dialog_factory(
                title="Invalid Title",
                msg="Card title cannot be empty!",
                yes_no=False,
                btn_color=self.color
            )
            return None
        card_old = Card(self.card.title, self.card.date,
                        self.card.time, self.card.description)
        if card_old.title != self.title_txt:
            for board in Database.get_instance().boards:
                for panel in board.panels:
                    for card in panel.cards:
                        if card.title == self.title_txt:
                            dialog_factory(
                                title="Invalid Title",
                                msg="Card already exists!",
                                yes_no=False,
                                btn_color=self.color
                            )
                            return None
        if card_old != self:
            Database.get_instance().update_card(card_old, self)
        self.close()

    def delete(self, event) -> None:
        """Deletes the card from the database."""
        Database.get_instance().delete_card(self)
        self.close()

    @property
    def title(self) -> str:
        return self.title_txt

    @property
    def date(self) -> str:
        return self.ui.calendarWidget.selectedDate().toString("dd-MM-yyyy")

    @property
    def time(self) -> str:
        return self.ui.timeEdit.time().toString("hh:mm")

    @property
    def description(self) -> str:
        return self.ui.textEdit_description.toPlainText()

    @title.setter
    def title(self, title: str) -> None:
        self.ui.lineEdit_title.setText(title)

    @date.setter
    def date(self, date: str) -> None:
        self.ui.calendarWidget.setSelectedDate(
            QDate.fromString(date, "dd-MM-yyyy"))

    @time.setter
    def time(self, time: str) -> None:
        self.ui.timeEdit.setTime(QTime.fromString(time, "hh:mm"))

    @description.setter
    def description(self, description: str) -> None:
        self.ui.textEdit_description.setText(description)

    def title_listener(self, text: str) -> None:
        self.title_txt = text

    def setup_font(self) -> None:
        notosans = setup_font_db("NotoSans.ttf")[0]
        toruspro = setup_font_db("TorusPro.ttf")[0]
        self.ui.label_card_desc.setFont(QFont(toruspro, 28))
        self.ui.label_title.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_date.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_time.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.label_description.setFont(QFont(toruspro, 14, QFont.Bold))
        self.ui.lineEdit_title.setFont(QFont(notosans, 12))
        self.ui.calendarWidget.setFont(QFont(notosans, 12))
        self.ui.timeEdit.setFont(QFont(notosans, 16, QFont.Bold))
        self.ui.textEdit_description.setFont(QFont(notosans, 12))
        self.ui.btn_delete.setFont(QFont(toruspro, 12))
        self.ui.btn_cancel.setFont(QFont(toruspro, 12))
        self.ui.btn_save.setFont(QFont(toruspro, 12))
