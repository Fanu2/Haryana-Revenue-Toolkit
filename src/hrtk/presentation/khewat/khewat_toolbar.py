"""
Haryana Revenue Toolkit (HRTK)

Khewat Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QLineEdit,
    QToolBar,
)


class KhewatToolbar(QToolBar):
    """
    Toolbar for Khewat management.
    """

    add_requested = Signal()
    edit_requested = Signal()
    deactivate_requested = Signal()
    refresh_requested = Signal()
    export_requested = Signal()
    search_text_changed = Signal(str)

    def __init__(self) -> None:
        super().__init__("Khewats")

        self._create_actions()
        self._create_search()

        #
        # Nothing selected initially.
        #
        self.enable_selection_actions(False)

    @property
    def search_text(self) -> str:
        """
        Return the search text.
        """
        return self._search.text()

    def enable_selection_actions(
        self,
        enabled: bool,
    ) -> None:
        """
        Enable actions requiring a selected Khewat.
        """

        self._edit_action.setEnabled(enabled)
        self._deactivate_action.setEnabled(enabled)

    def clear_search(self) -> None:
        """
        Clear the search box.
        """

        self._search.clear()

    def _create_actions(self) -> None:
        """
        Create toolbar actions.
        """

        self._add_action = QAction("Add", self)

        self._edit_action = QAction("Edit", self)

        self._deactivate_action = QAction(
            "Deactivate",
            self,
        )

        self._refresh_action = QAction(
            "Refresh",
            self,
        )

        self._export_action = QAction(
            "Export",
            self,
        )

        self._add_action.triggered.connect(
            self.add_requested.emit
        )

        self._edit_action.triggered.connect(
            self.edit_requested.emit
        )

        self._deactivate_action.triggered.connect(
            self.deactivate_requested.emit
        )

        self._refresh_action.triggered.connect(
            self.refresh_requested.emit
        )

        self._export_action.triggered.connect(
            self.export_requested.emit
        )

        self.addAction(self._add_action)
        self.addAction(self._edit_action)
        self.addAction(self._deactivate_action)

        self.addSeparator()

        self.addAction(self._refresh_action)
        self.addAction(self._export_action)

    def _create_search(self) -> None:
        """
        Create search box.
        """

        self.addSeparator()

        self._search = QLineEdit(self)

        self._search.setPlaceholderText(
            "Search khewats..."
        )

        self._search.textChanged.connect(
            self.search_text_changed.emit
        )

        self.addWidget(self._search)