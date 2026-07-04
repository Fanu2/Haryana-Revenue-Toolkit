"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.jamabandi import (
    Jamabandi,
)


class JamabandiModel(
    QAbstractTableModel,
):
    """
    Qt model used by the
    Jamabandi table.
    """

    HEADERS = (
        "Year",
        "Mutation",
        "Finalized",
        "Active",
    )

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._jamabandis: list[
            Jamabandi
        ] = []

    # ---------------------------------------------------------
    # Qt Model
    # ---------------------------------------------------------

    def rowCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(
            self._jamabandis
        )

    def columnCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(
            self.HEADERS
        )

    def headerData(
        self,
        section,
        orientation,
        role,
    ):

        if role != Qt.DisplayRole:

            return None

        if orientation == Qt.Horizontal:

            return self.HEADERS[
                section
            ]

        return str(
            section + 1
        )

    def data(
        self,
        index,
        role,
    ):

        if (

            not index.isValid()

            or

            role != Qt.DisplayRole

        ):

            return None

        jamabandi = self._jamabandis[
            index.row()
        ]

        column = index.column()

        if column == 0:

            return jamabandi.year

        if column == 1:

            return (
                jamabandi.mutation_no
                or
                "-"
            )

        if column == 2:

            return (
                "Yes"
                if jamabandi.finalized
                else "No"
            )

        if column == 3:

            return (
                "Yes"
                if jamabandi.active
                else "No"
            )

        return None

    # ---------------------------------------------------------
    # Data Loading
    # ---------------------------------------------------------

    def set_jamabandis(
        self,
        jamabandis: list[
            Jamabandi,
        ],
    ) -> None:
        """
        Load Jamabandi records.
        """

        self.beginResetModel()

        self._jamabandis = (
            jamabandis
        )

        self.endResetModel()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @property
    def jamabandis(
        self,
    ) -> list[
        Jamabandi
    ]:

        return self._jamabandis

    def jamabandi_at(
        self,
        row: int,
    ) -> Jamabandi | None:
        """
        Return the Jamabandi
        at the specified row.
        """

        if (

            0 <= row
            <
            len(
                self._jamabandis
            )

        ):

            return self._jamabandis[
                row
            ]

        return None

    def clear(
        self,
    ) -> None:
        """
        Remove all rows.
        """

        self.beginResetModel()

        self._jamabandis = []

        self.endResetModel()