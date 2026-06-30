"""
Haryana Revenue Toolkit (HRTK)

Village Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.village import Village
from hrtk.services.village_service import VillageService


class VillageModel(QAbstractTableModel):
    """
    Qt table model for Village entities.
    """

    COLUMN_CODE = 0
    COLUMN_NAME = 1
    COLUMN_TEHSIL = 2
    COLUMN_DISTRICT = 3
    COLUMN_STATE = 4
    COLUMN_STATUS = 5

    COLUMN_COUNT = 6

    HEADERS = (
        "Code",
        "Name",
        "Tehsil",
        "District",
        "State",
        "Status",
    )

    def __init__(
        self,
        service: VillageService,
    ) -> None:
        super().__init__()

        self._service = service
        self._villages: list[Village] = []

        self.refresh()

    @property
    def service(self) -> VillageService:
        """
        Return the village service.
        """
        return self._service
    
    @property
    def villages(self) -> list[Village]:
        """
        Return a copy of all villages.
        """

        return list(
            self._villages,
        )

    def refresh(self) -> None:
        """
        Reload villages from the service.
        """
        self.beginResetModel()

        self._villages = self.service.all()

        self.endResetModel()

    def village(
        self,
        row: int,
    ) -> Village | None:
        """
        Return the village at the specified row.
        """
        if 0 <= row < len(self._villages):
            return self._villages[row]

        return None

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:
        """
        Return the number of rows.
        """
        if parent.isValid():
            return 0

        return len(self._villages)

    def columnCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:
        """
        Return the number of columns.
        """
        if parent.isValid():
            return 0

        return self.COLUMN_COUNT

    def data(
        self,
        index: QModelIndex,
        role: int = Qt.DisplayRole,
    ) -> str | None:
        """
        Return cell data.
        """
        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        village = self._villages[index.row()]

        column = index.column()

        if column == self.COLUMN_CODE:
            return village.code

        if column == self.COLUMN_NAME:
            return village.name

        if column == self.COLUMN_TEHSIL:
            return village.tehsil

        if column == self.COLUMN_DISTRICT:
            return village.district

        if column == self.COLUMN_STATE:
            return village.state

        if column == self.COLUMN_STATUS:
            return "Active" if village.active else "Inactive"

        return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.DisplayRole,
    ) -> str | None:
        """
        Return header text.
        """
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.HEADERS[section]

        return str(section + 1)

    def __len__(self) -> int:
        """
        Return the number of villages.
        """
        return len(self._villages)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(rows={len(self)})"
        )