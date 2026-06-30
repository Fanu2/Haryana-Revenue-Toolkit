"""
Haryana Revenue Toolkit (HRTK)

Khewat Table.
"""

from __future__ import annotations

# ==========================================================
# Qt
# ==========================================================

from PySide6.QtCore import Signal

# ==========================================================
# HRTK
# ==========================================================

from hrtk.domain.khewat import Khewat
from hrtk.presentation.common.base_table import BaseTable
from hrtk.presentation.khewat.khewat_model import KhewatModel


class KhewatTable(BaseTable):
    """
    Table view for Khewat entities.
    """

    khewat_activated = Signal(Khewat)

    def __init__(
        self,
        model: KhewatModel,
    ) -> None:
        super().__init__()

        self.setModel(model)

        self.clicked.connect(
            self._on_clicked,
        )

    @property
    def khewat_model(self) -> KhewatModel:
        """
        Return the source Khewat model.
        """

        model = self.source_model()

        assert isinstance(
            model,
            KhewatModel,
        )

        return model

    def selected_khewat(
        self,
    ) -> Khewat | None:
        """
        Return the selected Khewat.
        """

        row = self.selected_source_row()

        if row is None:
            return None

        return self.khewat_model.khewat(
            row,
        )

    def _on_clicked(
        self,
        index,
    ) -> None:
        """
        Handle row selection.
        """

        source_index = self.map_to_source(
            index,
        )

        khewat = self.khewat_model.khewat(
            source_index.row(),
        )

        if khewat is not None:

            self.khewat_activated.emit(
                khewat,
            )