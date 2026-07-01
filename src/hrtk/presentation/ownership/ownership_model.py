"""
Haryana Revenue Toolkit (HRTK)

Ownership Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.ownership import Ownership


class OwnershipTableModel(QAbstractTableModel):
    """
    Qt table model for Ownership records.
    """

    HEADERS = (
        "Owner",
        "Share",
        "%",
        "Remarks",
    )

    def __init__(
        self,
        ownerships: list[Ownership] | None = None,
        owner_names: dict[str, str] | None = None,
    ) -> None:

        super().__init__()

        self._ownerships = ownerships or []
        self._owner_names = owner_names or {}

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self._ownerships)

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

        ownership = self._ownerships[index.row()]

        match index.column():

            case 0:
                return self._owner_names.get(
                    str(ownership.owner_id),
                    "Unknown",
                )

            case 1:
                return str(
                    ownership.share,
                )

            case 2:
                return (
                    f"{ownership.share.percentage:.2f}"
                )

            case 3:
                return ownership.remarks

        return None

    def set_ownerships(
        self,
        ownerships: list[Ownership],
        owner_names: dict[str, str],
    ) -> None:

        self.beginResetModel()

        self._ownerships = ownerships
        self._owner_names = owner_names

        self.endResetModel()

    @property
    def ownerships(
        self,
    ) -> list[Ownership]:

        return self._ownerships