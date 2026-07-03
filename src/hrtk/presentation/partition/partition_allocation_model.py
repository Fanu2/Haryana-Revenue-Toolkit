"""
Haryana Revenue Toolkit (HRTK)

Partition Allocation Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)


class PartitionAllocationModel(
    QAbstractTableModel,
):
    """
    Table model for the Allocation Register.
    """

    HEADERS = (
        "Owner",
        "Khasra",
        "Allocated Area",
        "Remarks",
    )

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._allocations: list[
            PartitionAllocation
        ] = []

        self._owner_names: dict[
            str,
            str,
        ] = {}

        self._parcel_numbers: dict[
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
            self._allocations
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

        allocation = self._allocations[
            index.row()
        ]

        column = index.column()

        if column == 0:

            return self._owner_names.get(
                str(
                    allocation.owner_id
                ),
                "Unknown",
            )

        if column == 1:

            return self._parcel_numbers.get(
                str(
                    allocation.parcel_number
                ),
                str(
                    allocation.parcel_number
                ),
            )

        if column == 2:

            return allocation.display_area()

        if column == 3:

            return allocation.remarks

        return None

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def set_allocations(
        self,
        allocations: list[
            PartitionAllocation
        ],
        owner_names: dict[
            str,
            str,
        ],
        parcel_numbers: dict[
            str,
            str,
        ],
    ) -> None:

        self.beginResetModel()

        self._allocations = allocations

        self._owner_names = owner_names

        self._parcel_numbers = (
            parcel_numbers
        )

        self.endResetModel()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def allocation_at(
        self,
        row: int,
    ) -> PartitionAllocation | None:

        if (
            0 <= row <
            len(
                self._allocations
            )
        ):

            return self._allocations[
                row
            ]

        return None

    def clear(
        self,
    ) -> None:

        self.beginResetModel()

        self._allocations = []

        self._owner_names = {}

        self._parcel_numbers = {}

        self.endResetModel()