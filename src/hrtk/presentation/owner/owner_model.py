"""
Haryana Revenue Toolkit (HRTK)

Owner Model.
"""

from __future__ import annotations

from uuid import UUID

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.owner import Owner
from hrtk.services.owner_service import OwnerService


class OwnerModel(QAbstractTableModel):
    """
    Table model for Owner entities.
    """

    HEADERS = (
        "Code",
        "Name",
        "Father",
        "Mobile",
        "Status",
    )

    def __init__(
        self,
        service: OwnerService,
    ) -> None:
        super().__init__()

        self._service = service
        self._owners: list[Owner] = []

        self._current_village_id: UUID | None = None

        self._filter_text = ""

        self.refresh()

    @property
    def service(self) -> OwnerService:
        """
        Return the owner service.
        """
        return self._service
    
    def set_filter(
        self,
        text: str,
        ) -> None:
        """
        Set the search filter.
        """

        self._filter_text = text.strip().lower()

        self.refresh()

    def set_current_village(
        self,
        village_id: UUID | None,
    ) -> None:
        """
        Set the active village.
        """

        self._current_village_id = village_id

        self.refresh()

    def refresh(self) -> None:
        """
        Reload owners.
        """

        self.beginResetModel()

        if self._current_village_id is None:

            owners = []

        else:

            owners = self.service.find_by_village(
                self._current_village_id
            )

            if self._filter_text:

                owners = [
                    owner
                    for owner in owners
                    if (
                        self._filter_text
                        in owner.owner_code.lower()
                        or self._filter_text
                        in owner.owner_name.lower()
                        or self._filter_text
                        in owner.father_name.lower()
                        or self._filter_text
                        in owner.mobile.lower()
                    )
                ]

        self._owners = owners

        self.endResetModel()

    def owner(
        self,
        row: int,
    ) -> Owner | None:
        """
        Return the owner at a row.
        """

        if 0 <= row < len(self._owners):
            return self._owners[row]

        return None

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:
        return len(self._owners)

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

        owner = self._owners[index.row()]

        match index.column():

            case 0:
                return owner.owner_code

            case 1:
                return owner.owner_name

            case 2:
                return owner.father_name

            case 3:
                return owner.mobile

            case 4:
                return (
                    "Active"
                    if owner.active
                    else "Inactive"
                )

        return None