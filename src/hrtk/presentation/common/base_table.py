"""
Haryana Revenue Toolkit (HRTK)

Base Table.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)


class BaseTable(QTableView):
    """
    Base class for all HRTK table views.
    """

    def __init__(self) -> None:
        super().__init__()

        self._configure()

    def _configure(self) -> None:
        """
        Configure the table.
        """

        self.setAlternatingRowColors(True)

        self.setSortingEnabled(True)

        self.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.setWordWrap(False)

        self.verticalHeader().hide()

        header = self.horizontalHeader()

        header.setStretchLastSection(True)

        header.setSectionResizeMode(
            QHeaderView.ResizeToContents
        )