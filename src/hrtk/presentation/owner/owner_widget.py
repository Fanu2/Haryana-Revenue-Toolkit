"""
Haryana Revenue Toolkit (HRTK)

Owner Widget.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from hrtk.application.selection_context import SelectionContext
from hrtk.domain.village import Village
from hrtk.presentation.common.form_mode import FormMode
from hrtk.presentation.owner.owner_dialog import OwnerDialog
from hrtk.presentation.owner.owner_model import OwnerModel
from hrtk.presentation.owner.owner_table import OwnerTable
from hrtk.presentation.owner.owner_toolbar import OwnerToolbar
from hrtk.services.owner_service import OwnerService

from hrtk.presentation.common.search_proxy_model import (
    SearchProxyModel,
)
from hrtk.presentation.common.message_service import (
    MessageService,
)


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
        print("OwnerWidget SelectionContext id:", id(self._selection))
        self._model = OwnerModel(service)

        #
        # Search Proxy
        #
        self._proxy = SearchProxyModel()

        self._proxy.setSourceModel(
            self._model,
        )

        self._toolbar = OwnerToolbar()

        self._table = OwnerTable(
            self._proxy,
        )

        self._current_village: Village | None = None

        self._build_ui()
        self._connect_signals()
        print("OwnerWidget created")

    @property
    def model(self) -> OwnerModel:
        """
        Return the owner model.
        """
        return self._model

    @property
    def table(self) -> OwnerTable:
        """
        Return the owner table.
        """
        return self._table

    @property
    def toolbar(self) -> OwnerToolbar:
        """
        Return the owner toolbar.
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
            self._add_owner
        )

        self._toolbar.edit_requested.connect(
            self._edit_owner
        )

        self._toolbar.deactivate_requested.connect(
            self._deactivate_owner
        )

        self._toolbar.refresh_requested.connect(
            self._refresh
        )

        self._toolbar.search_text_changed.connect(
            self._search
        )

        self._selection.village_changed.connect(
            self._village_changed
        )

    def _village_changed(
        self,
        village: Village | None,
        ) -> None:
        """
        Handle village selection changes.
        """

        self._current_village = village
        self._toolbar.clear_search()

        if village is None:

            self._model.set_current_village(
                None
            )

        else:

            self._model.set_current_village(
                village.id
            )

    def _add_owner(self) -> None:
        """
        Add a new owner.
        """
        print("Selection village:", self._selection.village)
        print("Current village:", self._current_village)
        if self._current_village is None:

            MessageService.warning(
                self,
                "No Village Selected",
                "Please select a village before adding an owner.",
                )

            return

        dialog = OwnerDialog(
            FormMode.CREATE,
        )

        if not dialog.exec():
            return

        owner = dialog.owner(
            self._current_village.id,
        )

        self._service.register(owner)

        self._model.refresh()

        self._toolbar.clear_search()

        MessageService.success(
            self,
            "Owner created successfully.",
        )

        self._toolbar.enable_selection_actions(
            True,
        )


    def _edit_owner(self) -> None:
        """
        Edit the selected owner.
        """

        owner = self._table.selected_owner()

        if owner is None:
            return

        dialog = OwnerDialog(
            FormMode.EDIT,
        )

        dialog.set_owner(owner)

        if not dialog.exec():
            return

        dialog.update_owner(
        owner,
        )

        self._model.refresh()

        self._toolbar.clear_search()

        MessageService.success(
            self,
            "Owner updated successfully.",
        )
   

    def _deactivate_owner(self) -> None:
        """
        Deactivate the selected owner.
        """

        owner = self._table.selected_owner()

        if owner is None:
            return

        if not MessageService.confirm(
            self,
            "Deactivate Owner",
            f"Deactivate owner '{owner.display_name}'?",
        )       :
            return

        self._service.deactivate(
            owner,
        )

        self._model.refresh()

        self._toolbar.clear_search()

        MessageService.success(
            self,
            "Owner deactivated successfully.",
        )

        self._toolbar.enable_selection_actions(
            False,
        )

    def _search(
        self,
        text: str,
    ) -> None:
        """
        Filter owners.
        """

        self._proxy.set_search_text(
            text,
        )

    def _refresh(
        self,
    ) -> None:
        """
        Refresh the owner list.
        """

        self._model.refresh()
        self._toolbar.clear_search()

        self._toolbar.clear_search()