"""
Haryana Revenue Toolkit (HRTK)

Parcel Selection Table.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.parcel import Parcel

from hrtk.presentation.khewat_parcel.parcel_selection_model import (
    ParcelSelectionTableModel,
)


class ParcelSelectionTable(QTableView):
    """
    Table for selecting parcels.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = ParcelSelectionTableModel()

        self.setModel(
            self._model,
        )

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )

        self.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )

        self.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )

        self.setAlternatingRowColors(
            True,
        )

        self.setSortingEnabled(
            True,
        )

        self.verticalHeader().hide()

        self.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.ResizeMode.ResizeToContents,
        )

        self.horizontalHeader().setSectionResizeMode(
            1,
            QHeaderView.ResizeMode.Stretch,
        )

    @property
    def model(
        self,
    ) -> ParcelSelectionTableModel:

        return self._model

    def selected_parcel(
        self,
    ) -> Parcel | None:
        """
        Return the currently selected parcel.
        """

        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        row = indexes[0].row()

        return self._model.parcels[row]

    def clear_selection(
        self,
    ) -> None:

        self.clearSelection()