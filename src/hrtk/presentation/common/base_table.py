"""
Haryana Revenue Toolkit (HRTK)

Base Table.
"""

from __future__ import annotations

# ==========================================================
# Qt
# ==========================================================

from PySide6.QtCore import QModelIndex
from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableView,
)


class BaseTable(QTableView):
    """
    Base class for all HRTK table views.

    Automatically supports both direct models and
    QSortFilterProxyModel.
    """

    def __init__(self) -> None:
        super().__init__()

        self._configure()

    # ---------------------------------------------------------
    # Proxy Support
    # ---------------------------------------------------------

    def source_model(self):
        """
        Return the underlying source model.
        """

        model = self.model()

        if isinstance(
            model,
            QSortFilterProxyModel,
        ):
            return model.sourceModel()

        return model

    def map_to_source(
        self,
        index: QModelIndex,
    ) -> QModelIndex:
        """
        Convert a proxy index into a source index.
        """

        model = self.model()

        if isinstance(
            model,
            QSortFilterProxyModel,
        ):
            return model.mapToSource(index)

        return index

    def selected_source_row(
        self,
    ) -> int | None:
        """
        Return selected row in the source model.
        """

        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        source_index = self.map_to_source(
            indexes[0],
        )

        return source_index.row()

    # ---------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------

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