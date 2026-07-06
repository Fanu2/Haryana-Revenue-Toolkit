"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class KhewatParcelToolbar(QWidget):
    """
    Toolbar for the Khewat–Parcel Relationship Workspace.
    """

    assign_requested = Signal()
    remove_requested = Signal()
    refresh_requested = Signal()
    export_requested = Signal()

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._assign_button = QPushButton(
            "Assign Parcel",
        )

        self._remove_button = QPushButton(
            "Remove Assignment",
        )

        self._refresh_button = QPushButton(
            "Refresh",
        )

        self._export_button = QPushButton(
            "Export",
        )

        #
        # Export is reserved for a future release.
        #

        self._export_button.setEnabled(False)

        layout = QHBoxLayout()

        layout.addWidget(
            self._assign_button,
        )

        layout.addWidget(
            self._remove_button,
        )

        layout.addSpacing(20)

        layout.addWidget(
            self._refresh_button,
        )

        layout.addStretch()

        layout.addWidget(
            self._export_button,
        )

        self.setLayout(
            layout,
        )

        #
        # Signals
        #

        self._assign_button.clicked.connect(
            self.assign_requested,
        )

        self._remove_button.clicked.connect(
            self.remove_requested,
        )

        self._refresh_button.clicked.connect(
            self.refresh_requested,
        )

        self._export_button.clicked.connect(
            self.export_requested,
        )

    @property
    def assign_button(
        self,
    ) -> QPushButton:

        return self._assign_button

    @property
    def remove_button(
        self,
    ) -> QPushButton:

        return self._remove_button

    @property
    def refresh_button(
        self,
    ) -> QPushButton:

        return self._refresh_button

    @property
    def export_button(
        self,
    ) -> QPushButton:

        return self._export_button