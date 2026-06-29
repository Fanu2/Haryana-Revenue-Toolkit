"""
Haryana Revenue Toolkit (HRTK)

Village Table.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidget,
)


class VillageTable(QTableWidget):
    """
    Displays villages.
    """

    HEADERS = (
        "Code",
        "Village",
        "Tehsil",
        "District",
        "State",
        "Status",
    )

    def __init__(self) -> None:
        super().__init__()

        self._configure()

    def _configure(self) -> None:
        """Configure the table."""

        self.setColumnCount(len(self.HEADERS))
        self.setHorizontalHeaderLabels(self.HEADERS)

        self.setAlternatingRowColors(True)

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.setSortingEnabled(True)

        self.verticalHeader().setVisible(False)

        header = self.horizontalHeader()

        header.setStretchLastSection(True)

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.setShowGrid(True)

    @property
    def selected_row(self) -> int:
        """Return the selected row."""

        rows = self.selectionModel().selectedRows()

        if not rows:
            return -1

        return rows[0].row()

    def clear_data(self) -> None:
        """Remove all rows."""

        self.setRowCount(0)

    def __repr__(self) -> str:
        return (
            f"VillageTable("
            f"rows={self.rowCount()}, "
            f"columns={self.columnCount()})"
        )