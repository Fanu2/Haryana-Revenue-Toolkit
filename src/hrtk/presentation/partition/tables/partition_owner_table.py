"""
Haryana Revenue Toolkit (HRTK)

Partition Owner Table.
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

from hrtk.domain.ownership import Ownership

from hrtk.presentation.partition.models.partition_owner_model import (
    PartitionOwnerModel,
)


class PartitionOwnerTable(
    QTableView,
):
    """
    Owner table used by the
    Partition Workbench.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = PartitionOwnerModel(
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
            QHeaderView.ResizeToContents,
        )

    # ---------------------------------------------------------
    # Public
    # ---------------------------------------------------------

    @property
    def model(
        self,
    ) -> PartitionOwnerModel:

        return self._model
    
    def set_ownerships(
        self,
        ownerships,
        owner_names,
    ) -> None:
        """
        Load ownership records into the table.
        """

        self._model.set_ownerships(
            ownerships,
            owner_names,
    )

    def selected_ownership(
        self,
    ) -> Ownership | None:
        """
        Return the selected ownership.
        """

        indexes = (
            self.selectionModel()
            .selectedRows()
        )

        if not indexes:
            return None

        return self._model.ownership_at(
            indexes[0].row(),
        )

    def selected_owner_name(
        self,
    ) -> str:
        """
        Return the selected owner's display name.
        """

        indexes = (
            self.selectionModel()
            .selectedRows()
        )

        if not indexes:
            return "---"

        return self._model.owner_name_at(
            indexes[0].row(),
        )

    def clear_selection(
        self,
    ) -> None:
        """
        Clear the current selection.
        """

        self.clearSelection()
