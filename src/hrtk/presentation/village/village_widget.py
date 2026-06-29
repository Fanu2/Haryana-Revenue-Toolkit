"""
Haryana Revenue Toolkit (HRTK)

Village Management Widget.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.application_context import ApplicationContext
from hrtk.presentation.village.village_table import VillageTable
from hrtk.presentation.village.village_toolbar import VillageToolbar


class VillageWidget(QWidget):
    """
    Village Management page.
    """

    def __init__(
        self,
        context: ApplicationContext,
    ) -> None:
        super().__init__()

        self._context = context

        self._toolbar = VillageToolbar()
        self._table = VillageTable()
        self._status = QLabel("0 villages")

        self._build_ui()

    @property
    def context(self) -> ApplicationContext:
        """Return the application context."""
        return self._context

    @property
    def toolbar(self) -> VillageToolbar:
        """Return the village toolbar."""
        return self._toolbar

    @property
    def table(self) -> VillageTable:
        """Return the village table."""
        return self._table

    def _build_ui(self) -> None:
        """Construct the page."""

        layout = QVBoxLayout(self)

        #
        # Title
        #
        title = QLabel("Village Management")

        font = QFont()
        font.setPointSize(16)
        font.setBold(True)

        title.setFont(font)

        title.setAlignment(
            Qt.AlignmentFlag.AlignLeft
        )

        layout.addWidget(title)

        #
        # Toolbar
        #
        layout.addWidget(self._toolbar)

        #
        # Table
        #
        layout.addWidget(self._table)

        #
        # Status
        #
        self._status.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        layout.addWidget(self._status)

    def set_village_count(
        self,
        count: int,
    ) -> None:
        """
        Update the status label.
        """

        if count == 1:
            text = "1 village"
        else:
            text = f"{count} villages"

        self._status.setText(text)

    def __repr__(self) -> str:
        return (
            f"VillageWidget("
            f"rows={self.table.rowCount()})"
        )