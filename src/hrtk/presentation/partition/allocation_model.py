"""
Haryana Revenue Toolkit (HRTK)

Allocation Table Model.
"""

from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


@dataclass(slots=True)
class AllocationRecord:
    """
    Represents one allocation entry displayed
    in the Allocation Register.
    """

    owner: str

    khasra: str

    area: str

    remarks: str = ""


class AllocationModel(
    QAbstractTableModel,
):
    """
    Table model for allocation records.
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

        self._records: list[
            AllocationRecord
        ] = []

    # ---------------------------------------------------------
    # Qt Model
    # ---------------------------------------------------------

    def rowCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(
            self._records
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

        record = self._records[
            index.row()
        ]

        column = index.column()

        if column == 0:

            return record.owner

        if column == 1:

            return record.khasra

        if column == 2:

            return record.area

        if column == 3:

            return record.remarks

        return None
    
    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def set_records(
        self,
        records: list[AllocationRecord],
    ) -> None:
        """
        Replace all allocation records.
        """

        self.beginResetModel()

        self._records = records

        self.endResetModel()

    def add_record(
        self,
        record: AllocationRecord,
    ) -> None:
        """
        Add one allocation record.
        """

        row = len(
            self._records
        )

        self.beginInsertRows(
            QModelIndex(),
            row,
            row,
        )

        self._records.append(
            record,
        )

        self.endInsertRows()

    def remove_record(
        self,
        row: int,
    ) -> None:
        """
        Remove one allocation record.
        """

        if (
            row < 0
            or row >= len(self._records)
        ):
            return

        self.beginRemoveRows(
            QModelIndex(),
            row,
            row,
        )

        del self._records[row]

        self.endRemoveRows()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @property
    def records(
        self,
    ) -> list[AllocationRecord]:
        """
        Return all allocation records.
        """

        return self._records

    def record_at(
        self,
        row: int,
    ) -> AllocationRecord | None:
        """
        Return one allocation record.
        """

        if (
            0 <= row
            < len(self._records)
        ):

            return self._records[
                row
            ]

        return None

    def clear(
        self,
    ) -> None:
        """
        Remove all records.
        """

        self.beginResetModel()

        self._records = []

        self.endResetModel()

