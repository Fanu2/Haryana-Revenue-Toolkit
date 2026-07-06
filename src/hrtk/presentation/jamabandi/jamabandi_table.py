"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Table View.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)

from hrtk.domain.jamabandi import (
    Jamabandi,
)

from hrtk.presentation.jamabandi.jamabandi_model import (
    JamabandiTableModel,
)


class JamabandiTable(QTableView):
    """
    Table view for Jamabandi records.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = JamabandiTableModel()

        self.setModel(
            self._model,
        )

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )

        self.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )

        self.setAlternatingRowColors(
            True,
        )

        self.setSortingEnabled(
            False,
        )

        self.verticalHeader().hide()

        self.horizontalHeader().setStretchLastSection(
            True,
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
    ) -> JamabandiTableModel:

        return self._model

    # ---------------------------------------------------------
    # Selection Helpers
    # ---------------------------------------------------------

    def selected_jamabandi(
        self,
    ) -> Jamabandi | None:
        """
        Returns the currently selected
        Jamabandi record.
        """

        indexes = (
            self.selectionModel()
            .selectedRows()
        )

        if not indexes:

            return None

        row = indexes[0].row()

        return self._model.records[row]