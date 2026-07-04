"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Table.
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

from hrtk.presentation.jamabandi.models.jamabandi_model import (
    JamabandiModel,
)


class JamabandiTable(
    QTableView,
):
    """
    Table used by the
    Jamabandi Workspace.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._model = JamabandiModel(
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
            True,
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
    # Public API
    # ---------------------------------------------------------

    @property
    def model(
        self,
    ) -> JamabandiModel:

        return self._model

    def set_jamabandis(
        self,
        jamabandis: list[
            Jamabandi,
        ],
    ) -> None:
        """
        Load Jamabandi records.
        """

        self._model.set_jamabandis(
            jamabandis,
        )

    def selected_jamabandi(
        self,
    ) -> Jamabandi | None:
        """
        Return the selected
        Jamabandi.
        """

        indexes = (
            self.selectionModel()
            .selectedRows()
        )

        if not indexes:

            return None

        return (
            self._model.jamabandi_at(
                indexes[0].row(),
            )
        )

    def clear_selection(
        self,
    ) -> None:
        """
        Clear the current selection.
        """

        self.clearSelection()

    def refresh(
        self,
    ) -> None:
        """
        Refresh the table view.
        """

        self.viewport().update()