"""
Haryana Revenue Toolkit (HRTK)

Parcel Selection Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.parcel import Parcel


class ParcelSelectionTableModel(QAbstractTableModel):
    """
    Table model for selecting parcels.
    """

    HEADERS = (
        "Parcel",
        "Area",
    )

    def __init__(
        self,
        parcels: list[Parcel] | None = None,
    ) -> None:

        super().__init__()

        self._parcels = parcels or []

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self._parcels)

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

        parcel = self._parcels[index.row()]

        if index.column() == 0:
            return str(parcel.number)

        if index.column() == 1:
            return str(parcel.area)

        return None

    def set_parcels(
        self,
        parcels: list[Parcel],
    ) -> None:

        self.beginResetModel()

        self._parcels = parcels

        self.endResetModel()

    @property
    def parcels(
        self,
    ) -> list[Parcel]:

        return self._parcels