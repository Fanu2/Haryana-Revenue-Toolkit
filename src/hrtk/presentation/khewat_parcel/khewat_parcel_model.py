"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.land_records.khewat_parcel import (
    KhewatParcel,
)


class KhewatParcelTableModel(QAbstractTableModel):
    """
    Qt table model for Khewat-Parcel relationships.
    """

    HEADERS = (
        "Khewat",
        "Parcel",
        "Area",
        "Remarks",
    )

    def __init__(
        self,
        relationships: list[KhewatParcel] | None = None,
        khewat_numbers: dict[str, str] | None = None,
        parcel_numbers: dict[str, str] | None = None,
        parcel_areas: dict[str, str] | None = None,
    ) -> None:

        super().__init__()

        self._relationships = relationships or []
        self._khewat_numbers = khewat_numbers or {}
        self._parcel_numbers = parcel_numbers or {}
        self._parcel_areas = parcel_areas or {}

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self._relationships)

    def columnCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self.HEADERS)

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int,
    ):

        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
        ):
            return self.HEADERS[section]

        return None

    def data(
        self,
        index: QModelIndex,
        role: int,
    ):

        if (
            not index.isValid()
            or role != Qt.ItemDataRole.DisplayRole
        ):
            return None

        relationship = self._relationships[index.row()]

        match index.column():

            case 0:
                return self._khewat_numbers.get(
                    str(relationship.khewat_id),
                    "Unknown",
                )

            case 1:
                return self._parcel_numbers.get(
                    str(relationship.parcel_id),
                    "Unknown",
                )

            case 2:
                return self._parcel_areas.get(
                    str(relationship.parcel_id),
                    "",
                )

            case 3:
                return relationship.remarks

        return None

    def set_relationships(
        self,
        relationships: list[KhewatParcel],
        khewat_numbers: dict[str, str],
        parcel_numbers: dict[str, str],
        parcel_areas: dict[str, str],
    ) -> None:

        self.beginResetModel()

        self._relationships = relationships
        self._khewat_numbers = khewat_numbers
        self._parcel_numbers = parcel_numbers
        self._parcel_areas = parcel_areas

        self.endResetModel()

    @property
    def relationships(
        self,
    ) -> list[KhewatParcel]:

        return self._relationships