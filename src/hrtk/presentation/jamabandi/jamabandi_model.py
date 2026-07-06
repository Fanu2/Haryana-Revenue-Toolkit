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


class JamabandiTableModel(QAbstractTableModel):
    """
    Qt table model for Jamabandi records.
    """

    HEADERS = (
        "Year",
        "Khewat",
        "Village",
        "Remarks",
    )

    def __init__(
        self,
        records: list[Jamabandi] | None = None,
        khewat_numbers: dict[str, str] | None = None,
        village_names: dict[str, str] | None = None,
    ) -> None:

        super().__init__()

        self._records = records or []

        self._khewat_numbers = (
            khewat_numbers or {}
        )

        self._village_names = (
            village_names or {}
        )

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(
            self._records,
        )

    def columnCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(
            self.HEADERS,
        )

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int,
    ):

        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation
            == Qt.Orientation.Horizontal
        ):
            return self.HEADERS[
                section
            ]

        return None

    def data(
        self,
        index: QModelIndex,
        role: int,
    ):

        if (
            not index.isValid()
            or role
            != Qt.ItemDataRole.DisplayRole
        ):
            return None

        record = self._records[
            index.row()
        ]

        match index.column():

            case 0:
                return record.year

            case 1:
                return self._khewat_numbers.get(
                    str(record.khewat_id),
                    "Unknown",
                )

            case 2:
                return self._village_names.get(
                    str(record.village_id),
                    "Unknown",
                )

            case 3:
                return record.remarks

        return None

    def set_records(
        self,
        records: list[Jamabandi],
        khewat_numbers: dict[str, str] | None = None,
        village_names: dict[str, str] | None = None,
    ) -> None:

        self.beginResetModel()

        self._records = records

        if khewat_numbers is not None:
            self._khewat_numbers = (
                khewat_numbers
            )

        if village_names is not None:
            self._village_names = (
                village_names
            )

        self.endResetModel()

    @property
    def records(
        self,
    ) -> list[Jamabandi]:

        return self._records