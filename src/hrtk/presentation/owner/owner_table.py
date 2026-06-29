"""
Haryana Revenue Toolkit (HRTK)

Owner Table.
"""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.owner import Owner
from hrtk.presentation.owner.owner_model import OwnerModel


class OwnerTable(QTableView):
    """
    Table view for Owner entities.
    """

    owner_activated = Signal(Owner)

    def __init__(
        self,
        model: OwnerModel,
    ) -> None:
        super().__init__()

        self.setModel(model)

        self._configure()

        self.doubleClicked.connect(
            self._on_double_clicked
        )

    @property
    def owner_model(self) -> OwnerModel:
        """
        Return the owner model.
        """
        model = self.model()
        assert isinstance(model, OwnerModel)
        return model

    def selected_owner(
        self,
    ) -> Owner | None:
        """
        Return the selected owner.
        """
        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        return self.owner_model.owner(
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

        owner = self.owner_model.owner(
            index.row()
        )

        if owner is not None:
            self.owner_activated.emit(
                owner
            )