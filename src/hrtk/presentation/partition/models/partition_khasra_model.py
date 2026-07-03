"""
Haryana Revenue Toolkit (HRTK)

Partition Khasra Table Model.
"""

from __future__ import annotations

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
)

from hrtk.domain.parcel import Parcel


class PartitionKhasraModel(QAbstractTableModel):
    """
    Table model used by the Partition Workbench
    to display Khasras (Parcel domain objects).
    """

    HEADERS = (
        "Khasra",
        "Area",
        "Status",
        "Allocated To",
    )

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._khasras: list[Parcel] = []

    # ---------------------------------------------------------
    # Qt Model
    # ---------------------------------------------------------

    def rowCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(self._khasras)

    def columnCount(
        self,
        parent=QModelIndex(),
    ) -> int:

        return len(self.HEADERS)

    def headerData(
        self,
        section,
        orientation,
        role,
    ):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.HEADERS[section]

        return str(section + 1)

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

        khasra = self._khasras[index.row()]

        column = index.column()

        if column == 0:

            if hasattr(khasra, "display_name"):
                return khasra.display_name

            if hasattr(khasra, "parcel_no"):
                return khasra.parcel_no

            if hasattr(khasra, "number"):
                return khasra.number

            return str(khasra.id)

        if column == 1:

            if hasattr(khasra, "area"):
                return str(khasra.area)

            return "-"

        if column == 2:
            return "Available"

        if column == 3:
            return "-"

        return None

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def set_khasras(
        self,
        khasras: list[Parcel],
    ) -> None:

        self.beginResetModel()

        self._khasras = khasras

        self.endResetModel()

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @property
    def khasras(
        self,
    ) -> list[Parcel]:

        return self._khasras

    def khasra_at(
        self,
        row: int,
    ) -> Parcel | None:

        if 0 <= row < len(self._khasras):
            return self._khasras[row]

        return None

    def clear(
        self,
    ) -> None:

        self.beginResetModel()

        self._khasras = []

        self.endResetModel()