"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel Table View.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.land_records.khewat_parcel import (
    KhewatParcel,
)

from hrtk.presentation.khewat_parcel.khewat_parcel_model import (
    KhewatParcelTableModel,
)


class KhewatParcelTable(QTableView):
    """
    Table view for Khewat-Parcel relationships.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = KhewatParcelTableModel()

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
            QHeaderView.ResizeMode.ResizeToContents,
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
    ) -> KhewatParcelTableModel:

        return self._model

    # ---------------------------------------------------------
    # Selection Helpers
    # ---------------------------------------------------------

    def selected_relationship(
        self,
    ) -> KhewatParcel | None:
        """
        Returns the currently selected relationship.
        """

        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        row = indexes[0].row()

        return self._model.relationships[row]