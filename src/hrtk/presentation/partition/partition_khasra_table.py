"""
Haryana Revenue Toolkit (HRTK)

Partition Khasra Table.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.parcel import Parcel

from hrtk.presentation.partition.partition_khasra_model import (
    PartitionKhasraModel,
)


class PartitionKhasraTable(
    QTableView,
):
    """
    Khasra table used by the
    Partition Workbench.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = PartitionKhasraModel(
            self,
        )

        self.setModel(
            self._model,
        )

        self._configure()

    # ---------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------

    def _configure(
        self,
    ) -> None:

        self.setSelectionBehavior(
            QAbstractItemView.SelectRows,
        )

        self.setSelectionMode(
            QAbstractItemView.SingleSelection,
        )

        self.setAlternatingRowColors(
            True,
        )

        self.setSortingEnabled(
            False,
        )

        self.setEditTriggers(
            QAbstractItemView.NoEditTriggers,
        )

        self.verticalHeader().setVisible(
            False,
        )

        header = self.horizontalHeader()

        header.setStretchLastSection(
            True,
        )

        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch,
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents,
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents,
        )

        header.setSectionResizeMode(
            3,
            QHeaderView.Stretch,
        )

    # ---------------------------------------------------------
    # Public
    # ---------------------------------------------------------

    @property
    def model(
        self,
    ) -> PartitionKhasraModel:

        return self._model

    def selected_khasra(
        self,
    ) -> Parcel | None:
        """
        Return the selected Khasra.
        """

        indexes = (
            self.selectionModel()
            .selectedRows()
        )

        if not indexes:

            return None

        return self._model.khasra_at(
            indexes[0].row(),
        )

    def clear_selection(
        self,
    ) -> None:

        self.clearSelection()

    def clear(
        self,
    ) -> None:

        self._model.clear()