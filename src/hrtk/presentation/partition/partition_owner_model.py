"""
Haryana Revenue Toolkit (HRTK)

Partition Owner Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.ownership import Ownership


class PartitionOwnerModel(
    QAbstractTableModel,
):
    """
    Owner table model used by the
    Partition Workbench.
    """

    HEADERS = (
        "Owner",
        "Share",
        "Allocated",
        "Remaining",
    )

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._ownerships: list[
            Ownership
        ] = []

        self._owner_names: dict[
            str,
            str,
        ] = {}

    # ---------------------------------------------------------
    # Qt Model
    # ---------------------------------------------------------

    def rowCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(
            self._ownerships
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
            or role != Qt.DisplayRole
        ):
            return None

        ownership = self._ownerships[
            index.row()
        ]

        owner_name = (
            self._owner_names.get(
                str(
                    ownership.owner_id
                ),
                "Unknown Owner",
            )
        )

        column = index.column()

        if column == 0:
            return owner_name

        if column == 1:
            return str(
                ownership.share
            )

        #
        # Future Allocation Engine
        #

        if column == 2:
            return "-"

        if column == 3:
            return "-"

        return None

    # ---------------------------------------------------------
    # Data Loading
    # ---------------------------------------------------------

    def set_ownerships(
        self,
        ownerships: list[Ownership],
        owner_names: dict[str, str],
    ) -> None:

        self.beginResetModel()

        self._ownerships = ownerships

        self._owner_names = owner_names

        self.endResetModel()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @property
    def ownerships(
        self,
    ) -> list[Ownership]:

        return self._ownerships

    def ownership_at(
        self,
        row: int,
    ) -> Ownership | None:

        if (
            0 <= row
            <
            len(
                self._ownerships
            )
        ):

            return self._ownerships[
                row
            ]

        return None

    def clear(
        self,
    ) -> None:

        self.beginResetModel()

        self._ownerships = []

        self._owner_names = {}

        self.endResetModel()