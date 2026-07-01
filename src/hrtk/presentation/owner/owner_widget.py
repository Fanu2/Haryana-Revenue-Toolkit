"""
Haryana Revenue Toolkit (HRTK)

Owner Widget.
"""

from __future__ import annotations

from PySide6.QtWidgets import QVBoxLayout, QWidget

from hrtk.application.selection_context import SelectionContext
from hrtk.domain.owner import Owner
from hrtk.domain.village import Village
from hrtk.presentation.common.form_mode import FormMode
from hrtk.presentation.common.message_service import MessageService
from hrtk.presentation.common.search_proxy_model import SearchProxyModel
from hrtk.presentation.owner.owner_dialog import OwnerDialog
from hrtk.presentation.owner.owner_model import OwnerModel
from hrtk.presentation.owner.owner_table import OwnerTable
from hrtk.presentation.owner.owner_toolbar import OwnerToolbar
from hrtk.services.export_service import ExportService
from hrtk.services.owner_service import OwnerService


class OwnerWidget(QWidget):
    """
    Main widget for Owner management.
    """

    def __init__(
        self,
        service: OwnerService,
        selection: SelectionContext,
    ) -> None:
        super().__init__()

        self._service = service
        self._selection = selection
        self._current_village: Village | None = None

        self._model = OwnerModel(service)

        self._proxy = SearchProxyModel()
        self._proxy.setSourceModel(self._model)

        self._toolbar = OwnerToolbar()
        self._table = OwnerTable(self._proxy)

        self._build_ui()
        self._connect_signals()

        # No owner selected initially
        self._toolbar.enable_selection_actions(False)

    @property
    def model(self) -> OwnerModel:
        return self._model

    @property
    def table(self) -> OwnerTable:
        return self._table

    @property
    def toolbar(self) -> OwnerToolbar:
        return self._toolbar

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.addWidget(self._toolbar)
        layout.addWidget(self._table)

    def _connect_signals(self) -> None:

        self._toolbar.add_requested.connect(self._add_owner)
        self._toolbar.edit_requested.connect(self._edit_owner)
        self._toolbar.deactivate_requested.connect(self._deactivate_owner)
        self._toolbar.refresh_requested.connect(self._refresh)
        self._toolbar.export_requested.connect(self._export_excel)
        self._toolbar.search_text_changed.connect(self._search)

        self._selection.village_changed.connect(
            self._village_changed
        )

        # IMPORTANT
        if hasattr(self._table, "owner_activated"):
            self._table.owner_activated.connect(
                self._owner_selected
            )

    def _village_changed(
        self,
        village: Village | None,
    ) -> None:

        self._current_village = village

        self._toolbar.clear_search()

        if village is None:
            self._model.set_current_village(None)
        else:
            self._model.set_current_village(village.id)

        self._toolbar.enable_selection_actions(False)

    def _owner_selected(
        self,
        owner: Owner,
    ) -> None:
        """
        Called whenever an owner row is selected.
        """
        self._toolbar.enable_selection_actions(True)

    def _add_owner(self) -> None:

        if self._current_village is None:

            MessageService.warning(
                self,
                "No Village Selected",
                "Please select a village before adding an owner.",
            )
            return

        dialog = OwnerDialog(FormMode.CREATE)

        if not dialog.exec():
            return

        owner = dialog.owner(
            self._current_village.id,
        )

        print("Current Village ID :", self._current_village.id)
        print("Owner Village ID   :", owner.village_id)

        self._service.register(owner)

        self._model.set_current_village(
            self._current_village.id,
        )

        self._toolbar.clear_search()

        MessageService.success(
            self,
            "Owner created successfully.",
        )

    def _edit_owner(self) -> None:

        owner = self._table.selected_owner()

        if owner is None:
            return

        dialog = OwnerDialog(FormMode.EDIT)

        dialog.set_owner(owner)

        if not dialog.exec():
            return

        dialog.update_owner(owner)

        self._model.set_current_village(
            self._current_village.id
        )

        self._toolbar.clear_search()

        MessageService.success(
            self,
            "Owner updated successfully.",
        )

    def _deactivate_owner(self) -> None:

        owner = self._table.selected_owner()

        if owner is None:
            return

        if not MessageService.confirm(
            self,
            "Deactivate Owner",
            f"Deactivate owner '{owner.display_name}'?",
        ):
            return

        self._service.deactivate(owner)

        self._model.set_current_village(
            self._current_village.id
        )

        self._toolbar.clear_search()

        self._toolbar.enable_selection_actions(False)

        MessageService.success(
            self,
            "Owner deactivated successfully.",
        )

    def _refresh(self) -> None:

        if self._current_village is None:
            self._model.set_current_village(None)
        else:
            self._model.set_current_village(
                self._current_village.id
            )

        self._toolbar.clear_search()

    def _search(
        self,
        text: str,
    ) -> None:

        self._proxy.set_search_text(text)

    def _export_excel(self) -> None:

        rows = [
            (
                owner.owner_code,
                owner.owner_name,
                owner.father_name,
                owner.mobile,
                "Active" if owner.active else "Inactive",
            )
            for owner in self._model.owners
        ]

        ExportService.export_excel(
            parent=self,
            title="Export Owners",
            default_filename="owners.xlsx",
            sheet_name="Owners",
            headers=list(OwnerModel.HEADERS),
            rows=rows,
        )