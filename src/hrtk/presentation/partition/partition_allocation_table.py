"""
Haryana Revenue Toolkit (HRTK)

Partition Allocation Table.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)

from hrtk.presentation.partition.partition_allocation_model import (
    PartitionAllocationModel,
)


class PartitionAllocationTable(
    QTableView,
):
    """
    Allocation Register table used by the
    Partition Workbench.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = PartitionAllocationModel(
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
        Configure the table appearance and behavior.
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
    # Data
    # ---------------------------------------------------------

    def set_allocations(
        self,
        allocations,
        owner_names,
        parcel_numbers,
    ) -> None:
        """
        Load allocations into the table.
        """

        self._model.set_allocations(
            allocations,
            owner_names,
            parcel_numbers,
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    @property
    def model(
        self,
    ) -> PartitionAllocationModel:
        """
        Return the underlying table model.
        """

        return self._model

    def selected_allocation(
        self,
    ) -> PartitionAllocation | None:
        """
        Return the selected allocation.
        """

        indexes = (
            self.selectionModel()
            .selectedRows()
        )

        if not indexes:

            return None

        return self._model.allocation_at(
            indexes[0].row(),
        )

    def refresh(
        self,
    ) -> None:
        """
        Refresh the table view.
        """

        self.viewport().update()

    def clear_selection(
        self,
    ) -> None:
        """
        Clear the current selection.
        """

        self.clearSelection()

    def clear(
        self,
    ) -> None:
        """
        Remove all allocations.
        """

        self._model.clear()