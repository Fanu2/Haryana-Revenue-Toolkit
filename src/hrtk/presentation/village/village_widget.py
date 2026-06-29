"""
Haryana Revenue Toolkit (HRTK)

Village Widget.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from hrtk.presentation.common.form_mode import FormMode
from hrtk.presentation.village.village_dialog import VillageDialog
from hrtk.presentation.village.village_model import VillageModel
from hrtk.presentation.village.village_table import VillageTable
from hrtk.presentation.village.village_toolbar import VillageToolbar
from hrtk.services.village_service import VillageService


class VillageWidget(QWidget):
    """
    Main widget for Village management.
    """

    def __init__(
        self,
        service: VillageService,
    ) -> None:
        super().__init__()

        self._service = service

        self._model = VillageModel(service)
        self._toolbar = VillageToolbar()
        self._table = VillageTable(self._model)

        self._build_ui()
        self._connect_signals()

    @property
    def model(self) -> VillageModel:
        """
        Return the village model.
        """
        return self._model

    @property
    def table(self) -> VillageTable:
        """
        Return the village table.
        """
        return self._table

    @property
    def toolbar(self) -> VillageToolbar:
        """
        Return the village toolbar.
        """
        return self._toolbar

    def _build_ui(self) -> None:
        """
        Build the user interface.
        """

        layout = QVBoxLayout()

        layout.addWidget(self._toolbar)
        layout.addWidget(self._table)

        self.setLayout(layout)

    def _connect_signals(self) -> None:
        """
        Connect widget signals.
        """

        self._toolbar.add_requested.connect(
            self._add_village
        )

    def _add_village(self) -> None:
        """
        Add a new village.
        """

        dialog = VillageDialog(
            FormMode.CREATE,
        )

        if not dialog.exec():
            return

        village = dialog.village()

        self._service.register(village)

        self._model.refresh()