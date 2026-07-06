"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class JamabandiToolbar(QWidget):
    """
    Toolbar for the Jamabandi workspace.
    """

    refresh_requested = Signal()

    add_requested = Signal()

    edit_requested = Signal()

    delete_requested = Signal()

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self.add_button = QPushButton(
            "Add",
        )

        self.edit_button = QPushButton(
            "Edit",
        )

        self.delete_button = QPushButton(
            "Delete",
        )

        self.refresh_button = QPushButton(
            "Refresh",
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QHBoxLayout(self)

        layout.addWidget(
            self.add_button,
        )

        layout.addWidget(
            self.edit_button,
        )

        layout.addWidget(
            self.delete_button,
        )

        layout.addStretch()

        layout.addWidget(
            self.refresh_button,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(
        self,
    ) -> None:

        self.add_button.clicked.connect(
            self.add_requested,
        )

        self.edit_button.clicked.connect(
            self.edit_requested,
        )

        self.delete_button.clicked.connect(
            self.delete_requested,
        )

        self.refresh_button.clicked.connect(
            self.refresh_requested,
        )
        