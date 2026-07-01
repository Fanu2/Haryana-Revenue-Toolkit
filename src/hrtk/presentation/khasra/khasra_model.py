"""
Haryana Revenue Toolkit (HRTK)

Khasra Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.parcel import Parcel
from hrtk.services.parcel_service import ParcelService


class KhasraModel(QAbstractTableModel):
    """
    Table model for Parcels.
    """

    HEADERS = (
        "Rectangle",
        "Killa",
        "Area",
        "Remarks",
    )

    def __init__(
        self,
        service: ParcelService,
    ) -> None:

        super().__init__()

        self._service = service

        self._parcels: list[Parcel] = []

        self.refresh()

    def refresh(
        self,
    ) -> None:

        self.beginResetModel()

        self._parcels = (
            self._service.list()
        )

        self.endResetModel()

    def parcel(
        self,
        row: int,
    ) -> Parcel | None:

        if 0 <= row < len(self._parcels):

            return self._parcels[row]

        return None

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(
            self._parcels,
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
        role: int = Qt.DisplayRole,
    ):

        if (
            role == Qt.DisplayRole
            and orientation == Qt.Horizontal
        ):
            return self.HEADERS[
                section
            ]

        return None

    def data(
        self,
        index: QModelIndex,
        role: int = Qt.DisplayRole,
    ):

        if (
            not index.isValid()
            or role != Qt.DisplayRole
        ):
            return None

        parcel = self._parcels[
            index.row()
        ]

        match index.column():

            case 0:
                return (
                    parcel.number.rectangle
                )

            case 1:
                return (
                    parcel.number.killa
                )

            case 2:
                return str(
                    parcel.area
        )

            case 3:
                return (
                    parcel.remarks
        )

        return None