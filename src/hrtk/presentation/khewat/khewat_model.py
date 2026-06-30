"""
Haryana Revenue Toolkit (HRTK)

Khewat Model.
"""

from __future__ import annotations

from uuid import UUID

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.khewat import Khewat
from hrtk.services.khewat_service import KhewatService


class KhewatModel(QAbstractTableModel):
    """
    Table model for Khewat entities.
    """

    HEADERS = (
        "Khewat No",
        "Old No",
        "Jamabandi",
        "Status",
    )

    def __init__(
        self,
        service: KhewatService,
    ) -> None:
        super().__init__()

        self._service = service
        self._khewats: list[Khewat] = []

        self._current_village_id: UUID | None = None

        self.refresh()

    @property
    def service(self) -> KhewatService:
        """
        Return the service.
        """
        return self._service

    def set_current_village(
        self,
        village_id: UUID | None,
    ) -> None:
        """
        Set the current village.
        """

        self._current_village_id = village_id

        self.refresh()

    def refresh(self) -> None:
        """
        Reload Khewats.
        """

        self.beginResetModel()

        if self._current_village_id is None:

            self._khewats = []

        else:

            self._khewats = (
                self.service.find_by_village(
                    self._current_village_id,
                )
            )

        self.endResetModel()

    def khewat(
        self,
        row: int,
    ) -> Khewat | None:
        """
        Return the Khewat at a row.
        """

        if 0 <= row < len(self._khewats):
            return self._khewats[row]

        return None

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self._khewats)

    def columnCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self.HEADERS)

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
            return self.HEADERS[section]

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

        khewat = self._khewats[index.row()]

        match index.column():

            case 0:
                return khewat.khewat_no

            case 1:
                return khewat.old_khewat_no

            case 2:
                return khewat.jamabandi_year

            case 3:
                return (
                    "Active"
                    if khewat.active
                    else "Inactive"
                )

        return None