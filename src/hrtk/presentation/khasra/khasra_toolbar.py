"""
Haryana Revenue Toolkit (HRTK)

Khasra Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class KhasraToolbar(QWidget):
    """
    Toolbar for Khasra management.
    """

    add_requested = Signal()

    edit_requested = Signal()

    delete_requested = Signal()

    refresh_requested = Signal()

    search_text_changed = Signal(str)

    def __init__(self) -> None:

        super().__init__()

        self._build_ui()

        self._connect_signals()

    def _build_ui(self) -> None:

        layout = QHBoxLayout()

        self._add_button = QPushButton(
            "Add",
        )

        self._edit_button = QPushButton(
            "Edit",
        )

        self._delete_button = QPushButton(
            "Delete",
        )

        self._refresh_button = QPushButton(
            "Refresh",
        )

        self._search_edit = QLineEdit()

        self._search_edit.setPlaceholderText(
            "Search Khasra..."
        )

        layout.addWidget(
            self._add_button,
        )

        layout.addWidget(
            self._edit_button,
        )

        layout.addWidget(
            self._delete_button,
        )

        layout.addWidget(
            self._refresh_button,
        )

        layout.addStretch()

        layout.addWidget(
            self._search_edit,
        )

        self.setLayout(
            layout,
        )

    def _connect_signals(self) -> None:

        self._add_button.clicked.connect(
            self.add_requested,
        )

        self._edit_button.clicked.connect(
            self.edit_requested,
        )

        self._delete_button.clicked.connect(
            self.delete_requested,
        )

        self._refresh_button.clicked.connect(
            self.refresh_requested,
        )

        self._search_edit.textChanged.connect(
            self.search_text_changed,
        )

    def clear_search(self) -> None:
        """
        Clear the search box.
        """

        self._search_edit.clear()

    def search_text(self) -> str:
        """
        Return the current search text.
        """

        return self._search_edit.text()

    def enable_selection_actions(
        self,
        enabled: bool,
    ) -> None:
        """
        Enable or disable actions that require
        a selected parcel.
        """

        self._edit_button.setEnabled(
            enabled,
        )

        self._delete_button.setEnabled(
            enabled,
        )