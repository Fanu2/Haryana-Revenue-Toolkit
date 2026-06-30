"""
Haryana Revenue Toolkit (HRTK)

Base Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)


class BaseModel(QAbstractTableModel):
    """
    Base table model for HRTK.
    """

    HEADERS: tuple[str, ...] = ()

    def __init__(self) -> None:
        super().__init__()

        self._items: list = []

    @property
    def items(self) -> list:
        """
        Return model items.
        """
        return self._items

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        if parent.isValid():
            return 0

        return len(self._items)

    def columnCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        if parent.isValid():
            return 0

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

    def refresh_begin(self) -> None:
        """
        Begin model refresh.
        """

        self.beginResetModel()

    def refresh_end(self) -> None:
        """
        End model refresh.
        """

        self.endResetModel()

    def clear(self) -> None:
        """
        Clear model contents.
        """

        self.beginResetModel()

        self._items.clear()

        self.endResetModel()

    def __len__(self) -> int:
        return len(self._items)