"""
Haryana Revenue Toolkit (HRTK)

Ownership Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class OwnershipToolbar(QWidget):
    """
    Toolbar for Ownership Workspace.
    """

    add_requested = Signal()

    edit_requested = Signal()

    delete_requested = Signal()

    validate_requested = Signal()

    refresh_requested = Signal()

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._add_button = QPushButton(
            "Add",
            self,
        )

        self._edit_button = QPushButton(
            "Edit",
            self,
        )

        self._delete_button = QPushButton(
            "Delete",
            self,
        )

        self._validate_button = QPushButton(
            "Validate",
            self,
        )

        self._refresh_button = QPushButton(
            "Refresh",
            self,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QHBoxLayout()

        layout.addWidget(
            self._add_button,
        )

        layout.addWidget(
            self._edit_button,
        )

        layout.addWidget(
            self._delete_button,
        )

        layout.addSpacing(
            20,
        )

        layout.addWidget(
            self._validate_button,
        )

        layout.addStretch()

        layout.addWidget(
            self._refresh_button,
        )

        self.setLayout(
            layout,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(
        self,
    ) -> None:

        self._add_button.clicked.connect(
            self.add_requested.emit
        )

        self._edit_button.clicked.connect(
            self.edit_requested.emit
        )

        self._delete_button.clicked.connect(
            self.delete_requested.emit
        )

        self._validate_button.clicked.connect(
            self.validate_requested.emit
        )

        self._refresh_button.clicked.connect(
            self.refresh_requested.emit
        )