"""
Haryana Revenue Toolkit (HRTK)

Village Widget.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.selection_context import SelectionContext
from hrtk.domain.village import Village
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
        selection: SelectionContext,
    ) -> None:
        super().__init__()

        self._service = service
        self._selection = selection

        self._model = VillageModel(service)
        self._toolbar = VillageToolbar()
        self._table = VillageTable(self._model)

        self._current_village: Village | None = None

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

        self._toolbar.edit_requested.connect(
            self._edit_village
        )

        self._toolbar.deactivate_requested.connect(
            self._deactivate_village
        )

        self._toolbar.refresh_requested.connect(
            self._refresh
        )

        self._toolbar.search_text_changed.connect(
            self._search
        )

        self._table.village_activated.connect(
            self._select_village
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

        self._toolbar.enable_selection_actions(
            True
        )

    def _edit_village(self) -> None:
        """
        Edit the selected village.
        """

        village = self._table.selected_village()

        if village is None:
            return

        dialog = VillageDialog(
            FormMode.EDIT,
        )

        dialog.set_village(village)

        if not dialog.exec():
            return

        dialog.update_village(village)

        self._service.repository.update(village)

        self._model.refresh()

        self._toolbar.enable_selection_actions(
            True
        )

    def _deactivate_village(self) -> None:
        """
        Deactivate the selected village.
        """

        village = self._table.selected_village()

        if village is None:
            return

        reply = QMessageBox.question(
            self,
            "Deactivate Village",
            (
             f"Deactivate village "
                f"'{village.display_name}'?"
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply != QMessageBox.Yes:
            return

        village.deactivate()

        self._service.repository.update(
            village,
        )

        self._model.refresh()

    def _refresh(self) -> None:
        """
        Refresh the village list.
        """

        self._model.refresh()

    def _search(
        self,
        text: str,
    ) -> None:
        """
        Filter villages.

        Search support will be added using a
        QSortFilterProxyModel.
        """

        _ = text

    def _select_village(
        self,
        village: Village,
    ) -> None:
        print("Village selected:", village)
        print("VillageWidget SelectionContext id:", id(self._selection))

        self._current_village = village
        self._selection.village = village

        self._toolbar.enable_selection_actions(True)