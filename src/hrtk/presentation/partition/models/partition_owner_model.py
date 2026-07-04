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

        #
        # Allocation display values.
        # Populated by PartitionWidget.
        #

        self._allocated: dict[
            str,
            str,
        ] = {}

        self._remaining: dict[
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

        ownership = (
            self._ownerships[
                index.row()
            ]
        )

        owner_name = (
            self._owner_names.get(
                str(
                    ownership.owner_id,
                ),
                "Unknown Owner",
            )
        )

        column = (
            index.column()
        )

        if column == 0:

            return owner_name

        if column == 1:

            return str(
                ownership.share,
            )

        if column == 2:

            return self._allocated.get(
                str(
                    ownership.owner_id,
                ),
                "-",
            )

        if column == 3:

            return self._remaining.get(
                str(
                    ownership.owner_id,
                ),
                "-",
            )

        return None

    # ---------------------------------------------------------
    # Data Loading
    # ---------------------------------------------------------

    def set_ownerships(
        self,
        ownerships: list[
            Ownership,
        ],
        owner_names: dict[
            str,
            str,
        ],
    ) -> None:
        """
        Load ownership records.
        """

        self.beginResetModel()

        self._ownerships = (
            ownerships
        )

        self._owner_names = (
            owner_names
        )

        self.endResetModel()

    def set_allocation_data(
        self,
        allocated: dict[
            str,
            str,
        ],
        remaining: dict[
            str,
            str,
        ],
    ) -> None:
        """
        Update allocated and remaining
        values shown in the table.
        """

        self._allocated = (
            allocated
        )

        self._remaining = (
            remaining
        )

        self.layoutChanged.emit()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @property
    def ownerships(
        self,
    ) -> list[
        Ownership
    ]:

        return (
            self._ownerships
        )

    def ownership_at(
        self,
        row: int,
    ) -> Ownership | None:

        if (
            0 <= row
            < len(
                self._ownerships
            )
        ):

            return (
                self._ownerships[
                    row
                ]
            )

        return None

    def owner_name_at(
        self,
        row: int,
    ) -> str:
        """
        Return the owner's display name.
        """

        ownership = (
            self.ownership_at(
                row,
            )
        )

        if ownership is None:

            return "---"

        return self._owner_names.get(
            str(
                ownership.owner_id,
            ),
            "Unknown Owner",
        )

    def clear(
        self,
    ) -> None:
        """
        Clear the model.
        """

        self.beginResetModel()

        self._ownerships = []

        self._owner_names = {}

        self._allocated = {}

        self._remaining = {}

        self.endResetModel()