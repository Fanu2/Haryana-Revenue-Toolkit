"""
Haryana Revenue Toolkit (HRTK)

Village Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QLineEdit, QToolBar


class VillageToolbar(QToolBar):
    """
    Toolbar for Village management.
    """

    add_requested = Signal()
    edit_requested = Signal()
    deactivate_requested = Signal()
    refresh_requested = Signal()
    export_requested = Signal()
    search_text_changed = Signal(str)

    def __init__(self) -> None:
        super().__init__("Village")

        self._create_actions()
        self._create_search()

    @property
    def search_text(self) -> str:
        """
        Return the current search text.
        """
        return self._search.text()

    def _create_actions(self) -> None:
        """
        Create toolbar actions.
        """

        add_action = QAction("Add", self)
        edit_action = QAction("Edit", self)
        deactivate_action = QAction("Deactivate", self)
        refresh_action = QAction("Refresh", self)
        export_action = QAction("Export", self)

        add_action.triggered.connect(self.add_requested.emit)
        edit_action.triggered.connect(self.edit_requested.emit)
        deactivate_action.triggered.connect(
            self.deactivate_requested.emit
        )
        refresh_action.triggered.connect(
            self.refresh_requested.emit
        )
        export_action.triggered.connect(
            self.export_requested.emit
        )

        self.addAction(add_action)
        self.addAction(edit_action)
        self.addAction(deactivate_action)

        self.addSeparator()

        self.addAction(refresh_action)
        self.addAction(export_action)

    def _create_search(self) -> None:
        """
        Create the search box.
        """

        self.addSeparator()

        self._search = QLineEdit(self)

        self._search.setPlaceholderText(
            "Search villages..."
        )

        self._search.textChanged.connect(
            self.search_text_changed.emit
        )

        self.addWidget(self._search)

    def clear_search(self) -> None:
        """
        Clear the search box.
        """
        self._search.clear()