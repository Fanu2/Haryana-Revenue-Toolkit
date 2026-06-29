"""
Haryana Revenue Toolkit (HRTK)

Village Table.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.village import Village
from hrtk.presentation.village.village_model import VillageModel


class VillageTable(QTableView):
    """
    Table view for Village entities.
    """

    village_activated = Signal(Village)

    def __init__(
        self,
        model: VillageModel,
    ) -> None:
        super().__init__()

        self.setModel(model)

        self._configure()

        self.doubleClicked.connect(
            self._on_double_clicked
        )

    @property
    def village_model(self) -> VillageModel:
        """
        Return the village model.
        """
        return self.model()

    def selected_village(
        self,
    ) -> Village | None:
        """
        Return the selected village.
        """
        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        return self.village_model.village(
            indexes[0].row()
        )

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

    def _on_double_clicked(
        self,
        index,
    ) -> None:
        """
        Handle double-click.
        """

        village = self.village_model.village(
            index.row()
        )

        if village is not None:
            self.village_activated.emit(
                village
            )