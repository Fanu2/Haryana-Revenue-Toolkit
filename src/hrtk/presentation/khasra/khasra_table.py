"""
Haryana Revenue Toolkit (HRTK)

Khasra Table View.
"""

from __future__ import annotations

from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.presentation.khasra.khasra_model import (
    KhasraModel,
)


class KhasraTable(QTableView):
    """
    Table view for parcels.
    """

    def __init__(
        self,
        model: KhasraModel,
    ) -> None:

        super().__init__()

        self.setModel(model)

        self.setSelectionBehavior(
            QAbstractItemView.SelectRows,
        )

        self.setSelectionMode(
            QAbstractItemView.SingleSelection,
        )

        self.setEditTriggers(
            QAbstractItemView.NoEditTriggers,
        )

        self.setAlternatingRowColors(
            True,
        )

        self.setSortingEnabled(
            True,
        )

        self.setWordWrap(
            False,
        )

        self.verticalHeader().setVisible(
            False,
        )

        self.horizontalHeader().setStretchLastSection(
            True,
        )

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents,
        )

    def selected_parcel(self):
        """
        Return the selected parcel.
        """

        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        return self.model().parcel(
            indexes[0].row(),
        )