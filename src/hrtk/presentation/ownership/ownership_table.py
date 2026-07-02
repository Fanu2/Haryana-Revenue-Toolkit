"""
Haryana Revenue Toolkit (HRTK)

Ownership Table View.
"""

from __future__ import annotations

from hrtk.domain.ownership import Ownership

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.presentation.ownership.ownership_model import (
    OwnershipTableModel,
)


class OwnershipTable(QTableView):
    """
    Table view for Ownership records.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = OwnershipTableModel()

        self.setModel(self._model)

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.setAlternatingRowColors(True)

        self.setSortingEnabled(False)

        self.verticalHeader().hide()

        self.horizontalHeader().setStretchLastSection(
            True
        )

        self.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.ResizeMode.Stretch,
        )

        self.horizontalHeader().setSectionResizeMode(
            1,
            QHeaderView.ResizeMode.ResizeToContents,
        )

        self.horizontalHeader().setSectionResizeMode(
            2,
            QHeaderView.ResizeMode.ResizeToContents,
        )

        self.horizontalHeader().setSectionResizeMode(
            3,
            QHeaderView.ResizeMode.Stretch,
        )

    @property
    def model(
        self,
    ) -> OwnershipTableModel:

        return self._model

    # ---------------------------------------------------------
    # Selection Helpers
    # ---------------------------------------------------------

    def selected_ownership(
        self,
    ) -> Ownership | None:
        """
        Returns the currently selected ownership.
        """

        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        row = indexes[0].row()

        return self._model.ownerships[row]