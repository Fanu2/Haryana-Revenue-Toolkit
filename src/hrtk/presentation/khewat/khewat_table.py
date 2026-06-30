"""
Haryana Revenue Toolkit (HRTK)

Khewat Table.
"""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.khewat import Khewat
from hrtk.presentation.khewat.khewat_model import KhewatModel


class KhewatTable(QTableView):
    """
    Table view for Khewat entities.
    """

    khewat_activated = Signal(Khewat)

    def __init__(
        self,
        model: KhewatModel,
    ) -> None:
        super().__init__()

        self.setModel(model)

        self._configure()

        #
        # Single click selects a Khewat.
        #
        self.clicked.connect(
            self._on_clicked,
        )

    @property
    def khewat_model(self) -> KhewatModel:
        """
        Return the Khewat model.
        """

        model = self.model()

        assert isinstance(
            model,
            KhewatModel,
        )

        return model

    def selected_khewat(
        self,
    ) -> Khewat | None:
        """
        Return the selected Khewat.
        """

        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        return self.khewat_model.khewat(
            indexes[0].row(),
        )

    def _configure(self) -> None:
        """
        Configure the table.
        """

        self.setAlternatingRowColors(True)

        self.setSortingEnabled(True)

        self.setSelectionBehavior(
            QAbstractItemView.SelectRows,
        )

        self.setSelectionMode(
            QAbstractItemView.SingleSelection,
        )

        self.setEditTriggers(
            QAbstractItemView.NoEditTriggers,
        )

        self.setWordWrap(False)

        self.verticalHeader().hide()

        header = self.horizontalHeader()

        header.setStretchLastSection(True)

        header.setSectionResizeMode(
            QHeaderView.ResizeToContents,
        )

    def _on_clicked(
        self,
        index,
    ) -> None:
        """
        Handle row selection.
        """

        khewat = self.khewat_model.khewat(
            index.row(),
        )

        if khewat is not None:
            self.khewat_activated.emit(
                khewat,
            )