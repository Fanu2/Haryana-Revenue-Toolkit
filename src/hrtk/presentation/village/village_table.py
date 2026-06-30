"""
Haryana Revenue Toolkit (HRTK)

Village Table.
"""

from __future__ import annotations

# ==========================================================
# Qt
# ==========================================================

from PySide6.QtCore import Signal

# ==========================================================
# HRTK
# ==========================================================

from hrtk.domain.village import Village
from hrtk.presentation.common.base_table import BaseTable
from hrtk.presentation.village.village_model import VillageModel


class VillageTable(BaseTable):
    """
    Table view for Village entities.
    """

    village_activated = Signal(Village)

    def __init__(
        self,
        model: VillageModel,
    ) -> None:
        super().__init__()

        self.setModel(model)

        self.clicked.connect(
            self._on_clicked,
        )

    @property
    def village_model(self) -> VillageModel:
        """
        Return the village model.
        """

        model = self.model()

        assert isinstance(
            model,
            VillageModel,
        )

        return model

    def selected_village(
        self,
    ) -> Village | None:
        """
        Return the selected village.
        """

        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return None

        return self.village_model.village(
            indexes[0].row(),
        )

    def _on_clicked(
        self,
        index,
    ) -> None:
        """
        Handle row selection.
        """

        village = self.village_model.village(
            index.row(),
        )

        if village is not None:

            self.village_activated.emit(
                village,
            )