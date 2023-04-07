import datetime
import logging

from PySide6.QtCore import QCoreApplication, QSize, Qt, Slot
from PySide6.QtGui import QCursor, QDropEvent, QFont
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea,
                               QApplication, QFrame, QLabel, QListWidget,
                               QListWidgetItem, QMainWindow, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from db import Database
from kanbaru_objects import Board, Card, Panel
from ui.about import About
from ui.app_settings import AppSettings
from ui.board_settings import BoardSettings
from ui.card_description import CardDescription
from ui.ui_main import Ui_MainWindow
from utils import (dialog_factory, hex_to_rgba, input_dialog_factory,
                   keyPressEvent, modify_hex_color, setup_font_db)


class MainScreen(QMainWindow):
    def __init__(self, parent: QMainWindow) -> None:
        QMainWindow.__init__(self)

        parent.ui = Ui_MainWindow()
        parent.ui.setupUi(parent)

        self.current_board: Board = Database.get_instance().boards[0]

        parent.ui.btn_app_settings.clicked.connect(
            lambda: self.show_app_settings(parent))
        parent.ui.btn_board_settings.clicked.connect(
            lambda event: self.show_board_settings(event, parent))
        parent.ui.btn_add_board.clicked.connect(
            lambda: self.add_board(parent))

        parent.ui.btn_app_settings.keyPressEvent = lambda event: keyPressEvent(
            event, parent, self.show_app_settings(parent))
        parent.ui.btn_board_settings.keyPressEvent = lambda event: keyPressEvent(
            event, parent, self.show_board_settings(event, parent))
        parent.ui.btn_add_board.keyPressEvent = lambda event: keyPressEvent(
            event, parent, self.add_board(parent))

        self.update_whole_page(parent)

    def update_whole_page(self, parent: QMainWindow) -> None:
        logging.info(
            f"Loaded {len(Database.get_instance().boards)} board(s) from database")

        parent.ui.qpushbutton = QPushButton()
        new_name = f"{parent.ui.qpushbutton.__class__.__name__}_{id(parent.ui.qpushbutton)}"
        setattr(parent.ui, new_name, parent.ui.qpushbutton)
        push_button = getattr(parent.ui, new_name)
        push_button.setObjectName(new_name)
        delattr(parent.ui, "qpushbutton")
        push_button = self.board_factory(
            parent, Database.get_instance().boards[0], "TorusPro.ttf")
        push_button.clicked.connect(lambda: self.change_board(
            parent, Database.get_instance().boards[0]))
        parent.ui.verticalLayout_4.addWidget(push_button)
        for index, board in enumerate(Database.get_instance().boards[1:]):
            parent.ui.qpushbutton = QPushButton()
            new_name = f"{parent.ui.qpushbutton.__class__.__name__}_{id(parent.ui.qpushbutton)}"
            setattr(parent.ui, new_name, parent.ui.qpushbutton)
            push_button = getattr(parent.ui, new_name)
            push_button.setObjectName(new_name)
            delattr(parent.ui, "qpushbutton")
            push_button = self.board_factory(
                parent, self.get_updated_board(
                    Database.get_instance().boards[index + 1]), "TorusPro.ttf",
                is_constructed=False)
            setattr(push_button, "board",
                    Database.get_instance().boards[index + 1])
            push_button.clicked.connect(lambda: self.change_board(
                parent, self.get_updated_board(Database.get_instance().boards[index + 1])))
            parent.ui.verticalLayout_4.addWidget(push_button)
            # TODO: Fix changing board connections

        parent.ui.vertSpacer_scrollAreaContent = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        parent.ui.verticalLayout_4.addItem(
            parent.ui.vertSpacer_scrollAreaContent)

        self.add_panel_button(
            parent, Database.get_instance().boards[0], "TorusPro.ttf")

        parent.ui.label_board.setText(
            Database.get_instance().boards[0].title[:40] + (Database.get_instance().boards[0].title[40:] and '...'))

        self.setup_font(parent, "TorusPro.ttf")

        parent.ui.label_logo.mousePressEvent = lambda event: self.show_about(
            event)

    def show_about(self, event) -> None:
        """Shows the about dialog"""
        self.about = About(self.current_board.color)
        self.about.show()

    def board_factory(self, parent: Ui_MainWindow, board: Board, font: str, is_constructed: bool = True) -> QPushButton:
        """Credsfates a board widget
        - Add a push button widget to the parent UI with specified style
        - If the board is displayed, construct the list widgets and card widgets

        Parameters
        ----------
        parent : QMainWindow
            The parent window
        board : Board
            The board object
        font : str
            The font to use
        is_constructed : bool, optional
            Load the board if True, by default True
        Returns
        -------
        QPushButton
            The board widget
        """
        if board is None:
            self.current_board = Database.get_instance().boards[-1]
            board = self.current_board

        logging.info(
            f'Loaded {len(board.panels)} panel(s) from board "{board.title}" [{board.color = }] [{is_constructed = }]')

        parent.ui.label_board.setText(
            board.title[:40] + (board.title[40:] and '...'))

        parent.ui.btn_board = QPushButton(
            parent.ui.scrollAreaContent_panel_left)
        parent.ui.btn_board.setObjectName(u"btn_board")
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            parent.ui.btn_board.sizePolicy().hasHeightForWidth())
        parent.ui.btn_board.setSizePolicy(size_policy)
        parent.ui.btn_board.setMinimumSize(QSize(0, 40))
        parent.ui.btn_board.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_board.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_board.setStyleSheet(
            """
            QPushButton {
                background-color: """ + f"{board.color}" + """;
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: """ + f"{modify_hex_color(board.color, -30)}" + """;
            }
            QPushButton:focus {
                border-color: #000000;
                border-width: 1.5px;
                border-style: solid;
            }
            """
        )
        parent.ui.btn_board.setText(
            board.title[:12] + (board.title[12:] and '...'))
        font_db = setup_font_db(font)[0]
        parent.ui.btn_board.setFont(QFont(font_db, 12))

        if is_constructed:
            color = hex_to_rgba(board.color)
            parent.ui.label_board.setStyleSheet(
                f"""
                background-color: qlineargradient(
                    spread:pad,
                    x1:0.5, y1:0.5,
                    x2:0.95, y2:0.5,
                    stop:0 {color},
                    stop:1 rgba(69, 76, 90, 255)
                );
                color: #FFFFFF;
                """
            )
            for panel in board.panels:
                qwidget = self.panel_factory(parent, panel, font, board.color)
                parent.ui.horizontalLayout_5.addWidget(qwidget)
        return parent.ui.btn_board

    def panel_factory(self, parent: Ui_MainWindow, panel: Panel, font: str, color: str) -> QWidget:
        """Creates a panel widget
        - Add a panel widget to the parent UI with specified style
        - Create a new name for the panel with its class name and id
        - Set the new name as an attribute of the parent UI and as the
          object name of the panel
        - Delete the old name attribute from the parent UI
        - Set the panel data attribute as the Panel class object

        Parameters
        ----------
        color
        parent : QMainWindow
            The parent window
        panel : Panel
            The panel object
        font : str
            The font to use

        Returns
        -------
        QWidget
            The panel widget
        """
        logging.info(
            f'Loaded {len(panel.cards)} card(s) from panel "{panel.title}"')

        size_policy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)

        parent.ui.panel = QWidget(parent.ui.scrollAreaContent_panel_right)
        parent.ui.panel.setObjectName(u"panel")

        size_policy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        size_policy2.setHorizontalStretch(0)
        size_policy2.setVerticalStretch(0)
        size_policy2.setHeightForWidth(
            parent.ui.panel.sizePolicy().hasHeightForWidth())
        parent.ui.panel.setSizePolicy(size_policy2)
        parent.ui.panel.setMinimumSize(QSize(250, 0))
        parent.ui.verticalLayout_1 = QVBoxLayout(parent.ui.panel)
        parent.ui.verticalLayout_1.setSpacing(0)
        parent.ui.verticalLayout_1.setObjectName(u"verticalLayout_1")
        parent.ui.verticalLayout_1.setContentsMargins(0, 0, 0, 0)

        parent.ui.widget = QWidget(parent.ui.panel)
        parent.ui.widget.setObjectName(u"widget_list_1")

        size_policy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        size_policy3.setHorizontalStretch(0)
        size_policy3.setVerticalStretch(0)
        size_policy3.setHeightForWidth(
            parent.ui.widget.sizePolicy().hasHeightForWidth())
        parent.ui.widget.setSizePolicy(size_policy3)
        parent.ui.widget.setStyleSheet(
            """
            background-color: #ebecf0;
            border-radius: 10px;
            """
        )
        parent.ui.verticalLayout_2 = QVBoxLayout(parent.ui.widget)
        parent.ui.verticalLayout_2.setObjectName(u"verticalLayout_11")
        parent.ui.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        parent.ui.label_list = QLabel(parent.ui.widget)
        parent.ui.label_list.setObjectName(u"label_list")
        size_policy1.setHeightForWidth(
            parent.ui.label_list.sizePolicy().hasHeightForWidth())
        parent.ui.label_list.setSizePolicy(size_policy1)
        parent.ui.label_list.setMinimumSize(QSize(0, 30))
        parent.ui.label_list.setStyleSheet(
            """
            color: #282c33;
            background-color: #ebecf0;
            border-radius: 5px;
            padding: 5px 0px 0px 5px;
            """
        )
        parent.ui.label_list.setMargin(0)
        parent.ui.verticalLayout_2.addWidget(parent.ui.label_list)

        parent.ui.listWidget = CustomListWidget(
            parent.ui.scrollArea_panel_right, modify_hex_color(color))
        parent.ui.verticalLayout_2.addWidget(parent.ui.listWidget)

        parent.ui.widget_add_card = QWidget(parent.ui.widget)
        parent.ui.widget_add_card.setObjectName(u"widget_add_card")
        size_policy1.setHeightForWidth(
            parent.ui.widget_add_card.sizePolicy().hasHeightForWidth())
        parent.ui.widget_add_card.setSizePolicy(size_policy1)

        parent.ui.verticalLayout_3 = QVBoxLayout(parent.ui.widget_add_card)
        parent.ui.verticalLayout_3.setObjectName(u"verticalLayout_6")
        parent.ui.verticalLayout_3.setContentsMargins(6, 0, 6, 6)

        parent.ui.btn_add_card = QPushButton(parent.ui.widget_add_card)
        parent.ui.btn_add_card.setObjectName(u"btn_add_card_list_1")
        parent.ui.btn_add_card.setMinimumSize(QSize(0, 25))
        parent.ui.btn_add_card.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_add_card.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_add_card.setStyleSheet(
            """
            QPushButton {
                background-color: #ebecf0;
                color: #6a758b;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #dadbe2;
                color: #505b76;
            }
            QPushButton:focus {
                border-color: #000000;
                border-width: 1.5px;
                border-style: solid;
            }
            """
        )
        parent.ui.verticalLayout_3.addWidget(parent.ui.btn_add_card)
        parent.ui.verticalLayout_2.addWidget(parent.ui.widget_add_card)
        parent.ui.verticalLayout_1.addWidget(parent.ui.widget)
        parent.ui.listWidget.setSortingEnabled(False)

        font_db = setup_font_db(font)
        parent.ui.label_list.setFont(QFont(font_db[0], 12, QFont.Bold))
        parent.ui.btn_add_card.setFont(QFont(font_db[0], 12))

        parent.ui.btn_add_card.clicked.connect(
            lambda: self.add_card(parent, panel))

        new_name = f"{parent.ui.listWidget.__class__.__name__}_{id(parent.ui.listWidget)}"
        setattr(parent.ui, new_name, parent.ui.listWidget)
        listWidget = getattr(parent.ui, new_name)
        listWidget.setObjectName(new_name)
        delattr(parent.ui, "listWidget")
        setattr(listWidget, "data", panel)

        for index, card in enumerate(panel.cards):
            qlistwidgetitem = self.card_factory(
                listWidget, parent, card, font, index)
            listWidget.addItem(qlistwidgetitem)

        listWidget.clicked.connect(
            lambda event: self.show_card_description(event, listWidget, parent, color))

        parent.ui.label_list.setText(
            QCoreApplication.translate("MainWindow", panel.title[:25] + (panel.title[25:] and '...'), None))
        parent.ui.btn_add_card.setText(
            QCoreApplication.translate("MainWindow", u"+ Add a card", None))

        return parent.ui.panel

    @staticmethod
    def card_factory(qlistwidget: QListWidget, parent: Ui_MainWindow, card: Card, font: str,
                     index: int) -> QListWidgetItem:
        """Create a card item at the given QListWidget index
        - Create a new name for the card with its class name and id
        - Set the new name as an attribute of the parent UI and as the
          object name of the card
        - Delete the old name attribute from the parent UI
        - Set the card flags
        - Set the card data as the Card class object

        Parameters
        ----------
        qlistwidget : QListWidget
            The QListWidget to add the card item to
        parent : Ui_MainWindow
            The parent UI
        card : Card
            The card to add to the panel
        font : str
            The font to use
        index : int
            The index to add the card item to

        Returns
        -------
        QListWidgetItem
            The card item
        """
        parent.ui.qlistwidgetitem = QListWidgetItem(qlistwidget)
        new_name = f"{parent.ui.qlistwidgetitem.__class__.__name__}_{id(parent.ui.qlistwidgetitem)}"
        setattr(parent.ui, new_name, parent.ui.qlistwidgetitem)
        list_widget_item = getattr(parent.ui, new_name)
        delattr(parent.ui, "qlistwidgetitem")
        list_widget_item.setFlags(
            Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        list_widget_item = qlistwidget.item(index)
        list_widget_item.setData(Qt.UserRole, card)
        list_widget_item.setText(
            QCoreApplication.translate("MainWindow", card.title[:24] + (card.title[24:] and '...'), None))
        font_db = setup_font_db(font)[0]
        list_widget_item.setFont(QFont(font_db, 12))

        return list_widget_item

    def add_panel_button(self, parent: Ui_MainWindow, board: Board, font: str) -> None:
        """Add a button to add a new panel

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        board : Board
            The board to add the panel to
        font : str
            The font to use
        """
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        parent.ui.list_add = QWidget(parent.ui.scrollAreaContent_panel_right)
        parent.ui.list_add.setObjectName(u"list_add")
        size_policy.setHeightForWidth(
            parent.ui.list_add.sizePolicy().hasHeightForWidth())
        parent.ui.list_add.setSizePolicy(size_policy)
        parent.ui.list_add.setMinimumSize(QSize(250, 0))
        parent.ui.verticalLayout_9 = QVBoxLayout(parent.ui.list_add)
        parent.ui.verticalLayout_9.setSpacing(0)
        parent.ui.verticalLayout_9.setObjectName(u"verticalLayout_9")
        parent.ui.verticalLayout_9.setContentsMargins(0, 0, 6, 0)
        parent.ui.btn_add_list = QPushButton(parent.ui.list_add)
        parent.ui.btn_add_list.setObjectName(u"btn_add_list")
        parent.ui.btn_add_list.setMinimumSize(QSize(0, 30))
        parent.ui.btn_add_list.setCursor(QCursor(Qt.PointingHandCursor))
        parent.ui.btn_add_list.setFocusPolicy(Qt.TabFocus)
        parent.ui.btn_add_list.setStyleSheet(
            """
            QPushButton {
                background-color: #acb2bf;
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #7e828c;
            }
            QPushButton:focus {
                border-color: #000000;
                border-width: 1.5px;
                border-style: solid;
            }
            """
        )
        parent.ui.verticalLayout_9.addWidget(parent.ui.btn_add_list)
        parent.ui.vertSpacer_list_add = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        parent.ui.verticalLayout_9.addItem(parent.ui.vertSpacer_list_add)
        parent.ui.btn_add_list.setText(
            QCoreApplication.translate("MainWindow", u"+ Add a panel", None))
        parent.ui.scrollAreaContent_panel_right.layout().addWidget(parent.ui.list_add)
        parent.ui.horzSpacer_panel_right = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        parent.ui.horizontalLayout_5.addItem(parent.ui.horzSpacer_panel_right)
        parent.ui.btn_add_list.clicked.connect(
            lambda: self.add_panel(parent, board))

        font_db = setup_font_db(font)[0]
        parent.ui.btn_add_list.setFont(QFont(font_db, 12))

    def show_app_settings(self, parent: Ui_MainWindow) -> None:
        """Show the application settings window

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        """
        app_settings = AppSettings(parent, self.current_board)
        app_settings.setWindowModality(Qt.ApplicationModal)
        app_settings.show()
        while app_settings.isVisible():
            QCoreApplication.processEvents()
        self.clear_page(parent)
        self.update_whole_page(parent)
        index = app_settings.get_board_index()
        if index != -1:
            self.change_board(parent, Database.get_instance().boards[index])

    def show_board_settings(self, event, parent: QMainWindow) -> None:
        """Show the board settings window

        Parameters
        ----------
        event
        parent : Ui_MainWindow
            The main window
        """
        board_settings = BoardSettings(self.current_board)
        board_settings.setWindowModality(Qt.ApplicationModal)
        board_settings.show()
        while board_settings.isVisible():
            QCoreApplication.processEvents()
        self.clear_page(parent)
        self.update_whole_page(parent)
        self.change_board(parent, self.get_updated_board(self.current_board))

    def show_card_description(self, event, list_widget: QListWidget, parent: QMainWindow, color: str) -> None:
        """Show the card description window

        Parameters
        ----------
        list_widget
        color
        event : QMouseEvent
            The mouse event
        parent : QListWidget
            The parent QListWidget
        """
        card = list_widget.item(event.row()).data(Qt.UserRole)
        card_description = CardDescription(card, color)
        card_description.setWindowModality(Qt.ApplicationModal)
        card_description.show()
        while card_description.isVisible():
            QCoreApplication.processEvents()
        self.clear_page(parent)
        self.update_whole_page(parent)
        self.change_board(parent, self.get_updated_board(self.current_board))

    @staticmethod
    def get_updated_board(current_board: Board) -> Board:
        """Get the current board

        Returns
        -------
        Board
            The current board
        """
        for board in Database.get_instance().boards:
            if board.title == current_board.title:
                return board

    def add_board(self, parent: Ui_MainWindow) -> None:
        """Add a new board

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        """
        while True:
            text = input_dialog_factory(
                "Add a board", "Enter a new board title: ", btn_color=self.current_board.color)
            if text is None:
                return None
            elif text:
                break
            dialog_factory(None, None, "Invalid Title",
                           "Board title cannot be empty!", yes_no=False, btn_color=self.current_board.color)
        if any(board.title == text for board in Database.get_instance().boards):
            dialog_factory(None, None, "Invalid Title",
                           "Board already exists!", yes_no=False, btn_color=self.current_board.color)
        else:
            data = Database.get_instance().data
            data["_Database__data"].append(
                {"_Board__title": text, "_Board__panels_lists": [], "_Board__color": "LIGHTBLUE"})
            Database.get_instance().data = data
            Database.get_instance().write()
            self.clear_page(parent)
            self.update_whole_page(parent)
            self.change_board(parent, Database.get_instance().boards[-1])
            return None

    def add_panel(self, parent: Ui_MainWindow, board: Board) -> None:
        """Add a new panel

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        board : Board
            The board to add the panel to
        """
        while True:
            text = input_dialog_factory(
                "New panel", "Enter a new panel title:", btn_color=self.current_board.color)
            if text is None:
                return None
            if text:
                break
            dialog_factory(None, None, "Invalid Title",
                           "Panel title cannot be empty!", yes_no=False, btn_color=self.current_board.color)
        if any(panel.title == text for other_board in Database.get_instance().boards for panel in other_board.panels):
            dialog_factory(None, None, "Invalid Title",
                           "Panel already exists!", yes_no=False, btn_color=self.current_board.color)
        else:
            data = Database.get_instance().data
            for i, db_board in enumerate(Database.get_instance().boards):
                if db_board.title == board.title:
                    panels_list = data["_Database__data"][i]["_Board__panels_lists"]
                    try:
                        panel = {"_Panel__title": text,
                                 "_Board__panels": []}
                        panels_list.append(panel)
                    except KeyError:
                        panels_list = [
                            {"_Panel__title": text, "_Board__panels": []}]
                        data["_Database__data"][i]["_Board__panels_lists"] = panels_list
                    Database.get_instance().data = data
                    Database.get_instance().write()
                    self.change_board(
                        parent, Database.get_instance().boards[i])
                    parent.ui.scrollArea_panel_right.horizontalScrollBar().setValue(
                        parent.ui.scrollArea_panel_right.horizontalScrollBar().maximum())
                    return None

    def add_card(self, parent: Ui_MainWindow, panel: Panel) -> None:
        """Add a new card

        Parameters
        ----------
        parent : Ui_MainWindow
            The main window
        panel : Panel
            The panel to add the card to
        """
        while True:
            text = input_dialog_factory(
                "New card", "Enter a new card title:", btn_color=self.current_board.color)
            if text is None:
                return None
            if text:
                break
            dialog_factory(None, None, "Invalid Title",
                           "Card title cannot be empty!", yes_no=False, btn_color=self.current_board.color)
        data = Database.get_instance().data
        for i, board in enumerate(Database.get_instance().boards):
            for j, panel_ in enumerate(board.panels):
                if panel_.title == panel.title:
                    if any(card.title == text for card in panel_.cards):
                        dialog_factory(None, None, "Invalid Title",
                                       "Card already exists!", yes_no=False, btn_color=self.current_board.color)
                        self.add_card(parent, panel)
                        return None
                    try:
                        data["_Database__data"][i]["_Board__panels_lists"][j]["_Board__panels"].append(
                            {"_Card__title": text, "_Card__description": "",
                             "_Card__date": datetime.date.today().strftime("%d-%m-%Y"),
                             "_Card__time": datetime.datetime.now().strftime("%H:%M")})
                    except KeyError:
                        data["_Database__data"][i]["_Board__panels_lists"][j]["_Board__panels"] = [
                            {"_Card__title": text, "_Card__description": "",
                             "_Card__date": datetime.date.today().strftime("%d-%m-%Y"),
                             "_Card__time": datetime.datetime.now().strftime("%H:%M")}]
                    Database.get_instance().data = data
                    Database.get_instance().write()
                    self.change_board(
                        parent, Database.get_instance().boards[i])

    def change_board(self, parent: Ui_MainWindow, board: Board) -> None:
        """Change the board to the specified board
        - Remove all widgets from the layout
        - Create the new board
        - Remove the add panel button and horizontal spacer then add panel button again

        Parameters
        ----------
        parent : Ui_MainWindow
            The parent widget
        board : Board
            The board to change to
        """
        self.current_board = board
        layout = parent.ui.scrollAreaContent_panel_right.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()
        self.board_factory(parent, board, "TorusPro.ttf")
        parent.ui.list_add.setParent(None)
        parent.ui.horizontalLayout_5.removeItem(
            parent.ui.horzSpacer_panel_right)
        self.add_panel_button(parent, board, "TorusPro.ttf")

    @staticmethod
    def change_card(source: Panel, destination: Panel, card: Card, index: int = None) -> None:
        """Change the card in a panel to another panel
        - Get the data from the database
        - Find the source panel and the specified card
        - Find the destination panel and add the card at a specified index
        - Remove the card from the source panel
        - Update the database

        Parameters
        ----------
        source : Panel
            The source panel
        destination : Panel
            The destination panel
        card : Card
            The card to move
        index : int, optional
            The index position to add the card in the destination panel, by default None (adds at the end)
        """
        data = Database.get_instance().data
        source_list = next((lst for lst in data.get("_Database__data", [{}])[0].get("_Board__panels_lists", [])
                            if lst.get("_Panel__title") == getattr(source, "data").title), {})
        card_to_move = next((card_ for card_ in source_list.get("_Board__panels", [])
                            if card_.get("_Card__title") == card.title), {})
        if card_to_move:
            source_list["_Board__panels"].remove(card_to_move)
            dest_list = next((lst for lst in data.get("_Database__data", [{}])[0].get("_Board__panels_lists", [])
                              if lst.get("_Panel__title") == getattr(destination, "data").title), {})
            try:
                if index is None or index >= len(dest_list["_Board__panels"]):
                    dest_list["_Board__panels"].append(card_to_move)
                else:
                    dest_list["_Board__panels"].insert(index, card_to_move)
            except KeyError:
                dest_list["_Board__panels"] = [card_to_move]
            Database.get_instance().data = data

    @staticmethod
    def clear_page(parent: Ui_MainWindow) -> None:
        """Clear the page
        - Remove all widgets from the layout

        Parameters
        ----------
        parent : Ui_MainWindow
            The parent widget
        """
        layout = parent.ui.scrollAreaContent_panel_right.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()
        layout = parent.ui.scrollAreaContent_panel_left.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()
        parent.ui.verticalLayout_4.removeItem(
            parent.ui.vertSpacer_scrollAreaContent)
        parent.ui.horzSpacer_panel_right.changeSize(
            0, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

    @staticmethod
    def setup_font(parent: Ui_MainWindow, font: str) -> None:
        toruspro = setup_font_db(font)[0]
        parent.ui.label_logo.setFont(QFont(toruspro, 36))
        parent.ui.label_board.setFont(QFont(toruspro, 28))
        parent.ui.btn_add_board.setFont(QFont(toruspro, 12))
        parent.ui.btn_board_settings.setFont(QFont(toruspro, 12))
        parent.ui.btn_app_settings.setFont(QFont(toruspro, 12))


class CustomListWidget(QListWidget):
    """Custom QListWidget class"""

    def __init__(self: QListWidget, parent: QMainWindow, color: str) -> None:
        super().__init__()
        self.parent_ = parent
        self.setObjectName(u"listWidget")
        size_policy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        size_policy2.setHorizontalStretch(0)
        size_policy2.setVerticalStretch(0)
        size_policy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy2)
        self.setMaximumSize(QSize(250, 16777215))
        self.setFocusPolicy(Qt.TabFocus)
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.NoFrame)
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.setAutoScroll(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setProperty("isWrapping", False)
        self.setSpacing(5)
        self.setUniformItemSizes(True)
        self.setWordWrap(True)
        self.verticalScrollBar().setSingleStep(10)
        self.setStyleSheet(
            f"""
            QListWidget {{
                background-color: #ebecf0;
                border-radius: 10px;
                color: #000000;
            }}
            QListWidget::item {{
                height: 40px;
                padding: 0px 8px 0px 8px;
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5,
                    stop:0 {color},
                    stop:0.0338983 {color},
                    stop:0.039548 rgba(255, 255, 255, 255),
                    stop:1 rgba(255, 255, 255, 255)
                );
                color: #000000;
                border-radius: 5px;
            }}
            QListWidget::item:hover {{
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5,
                    stop:0 {color},
                    stop:0.0338983 {color},
                    stop:0.039548 rgba(226, 228, 233, 255),
                    stop:1 rgba(226, 228, 233, 255)
                );
                color: #000000;
            }}
            QListWidget::item:selected {{
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5,
                    stop:0 {color},
                    stop:0.0338983 {color},
                    stop:0.039548 rgba(204, 204, 204, 255),
                    stop:1 rgba(204, 204, 204, 255)
                );
                color: #000000;
            }}
            QListWidget::item:focus {{
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:0.95, y2:0.5,
                    stop:0 {color},
                    stop:0.0338983 {color},
                    stop:0.039548 rgba(204, 204, 204, 255),
                    stop:1 rgba(204, 204, 204, 255));
                    color: #000000
            }}
            QScrollBar:vertical {{
                width: 10px;
                margin: 0px 0px 0px 0px;
                background-color: #acb2bf
            }}
            QScrollBar:horizontal {{
                height: 10px;
                margin: 0px 0px 0px 0px;
                background-color: #acb2bf
            }}
            """
        )

    @Slot()
    def dragMoveEvent(self, event) -> None:
        if QCursor().pos().x() > self.parent_.width() + self.parent_.x() + 340:
            self.parent_.horizontalScrollBar().setValue(
                self.parent_.horizontalScrollBar().value() + 8)
        elif QCursor().pos().x() < self.parent_.width() - self.parent_.x() - 240:
            self.parent_.horizontalScrollBar().setValue(
                self.parent_.horizontalScrollBar().value() - 8)
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            panel = QApplication.widgetAt(QCursor().pos()).parent()
            if isinstance(panel, QListWidget):
                if QCursor.pos().y() > self.parent_.height() + self.parent_.y() + 100:
                    panel.verticalScrollBar().setValue(
                        panel.verticalScrollBar().value() + 3)
                elif QCursor.pos().y() < self.parent_.height() - self.parent_.y() - 200:
                    panel.verticalScrollBar().setValue(
                        panel.verticalScrollBar().value() - 3)
            event.accept()
        else:
            event.ignore()
        super().dragMoveEvent(event)

    @Slot()
    def dropEvent(self, event: QDropEvent) -> None:
        """Override the dropEvent method to customize the drop event
        - Check if the item to be dropped has the qabstractitemmodeldatalist format
        - Get the source widget
        - Get the widget at the current mouse position
        - Get the items that is being dragged
        - Remove those items from the source widget
        - Add those items to the destination widget at the mouse position

        Parameters
        ----------
        event : QDropEvent
            The drop event
        """
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            source_widget = event.source()
            dest_widget = QApplication.widgetAt(QCursor().pos()).parent()
            items = source_widget.selectedItems()
            for item in items:
                source_widget.takeItem(source_widget.row(item))
                dest_row = dest_widget.row(dest_widget.itemAt(event.pos()))
                if dest_row == -1:
                    dest_row = dest_widget.count()
                if source_widget == dest_widget:
                    dest_widget.insertItem(dest_row, item)
                logging.info(
                    f'Moved {len(items)} Card(s) ({list(map(lambda x: getattr(x, "data")(Qt.UserRole).title, items))}) '
                    f'from panel "{getattr(source_widget, "data").title}" to panel "{getattr(dest_widget, "data").title}"')
                MainScreen.change_card(source_widget, dest_widget,
                                       item.data(Qt.UserRole), dest_row)
                Database.get_instance().write()
                event.accept()
        else:
            event.ignore()
        super().dropEvent(event)
