"""
Haryana Revenue Toolkit (HRTK)

Partition Workbench Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class PartitionToolbar(QWidget):
    """
    Toolbar for the Partition Workbench.
    """

    allocate_requested = Signal()

    validate_requested = Signal()

    save_requested = Signal()

    undo_requested = Signal()

    report_requested = Signal()

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

        self._allocate_button = QPushButton(
            "Allocate",
            self,
        )

        self._validate_button = QPushButton(
            "Validate",
            self,
        )

        self._save_button = QPushButton(
            "Save",
            self,
        )

        self._undo_button = QPushButton(
            "Undo",
            self,
        )

        self._report_button = QPushButton(
            "Report",
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
            self._allocate_button,
        )

        layout.addWidget(
            self._validate_button,
        )

        layout.addWidget(
            self._save_button,
        )

        layout.addWidget(
            self._undo_button,
        )

        layout.addSpacing(
            20,
        )

        layout.addWidget(
            self._report_button,
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

        self._allocate_button.clicked.connect(
            self.allocate_requested.emit,
        )

        self._validate_button.clicked.connect(
            self.validate_requested.emit,
        )

        self._save_button.clicked.connect(
            self.save_requested.emit,
        )

        self._undo_button.clicked.connect(
            self.undo_requested.emit,
        )

        self._report_button.clicked.connect(
            self.report_requested.emit,
        )

        self._refresh_button.clicked.connect(
            self.refresh_requested.emit,
        )