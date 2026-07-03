"""
Haryana Revenue Toolkit (HRTK)

Allocation Table.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.presentation.partition.allocation_model import (
    AllocationModel,
    AllocationRecord,
)


class AllocationTable(
    QTableView,
):
    """
    Table displaying allocation records.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = AllocationModel(
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
        """
        Configure the table.
        """

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
    ) -> AllocationModel:

        return self._model

    def set_records(
        self,
        records: list[
            AllocationRecord
        ],
    ) -> None:
        """
        Load allocation records.
        """

        self._model.set_records(
            records,
        )

    def selected_record(
        self,
    ) -> AllocationRecord | None:
        """
        Return the selected allocation.
        """

        indexes = (
            self.selectionModel()
            .selectedRows()
        )

        if not indexes:

            return None

        return self._model.record_at(
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

