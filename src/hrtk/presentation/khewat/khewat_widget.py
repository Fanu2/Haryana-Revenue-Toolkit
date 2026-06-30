"""
Haryana Revenue Toolkit (HRTK)

Khewat Widget.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.selection_context import SelectionContext
from hrtk.domain.khewat import Khewat
from hrtk.domain.village import Village
from hrtk.presentation.common.form_mode import FormMode
from hrtk.presentation.khewat.khewat_dialog import KhewatDialog
from hrtk.presentation.khewat.khewat_model import KhewatModel
from hrtk.presentation.khewat.khewat_table import KhewatTable
from hrtk.presentation.khewat.khewat_toolbar import KhewatToolbar
from hrtk.services.khewat_service import KhewatService


class KhewatWidget(QWidget):
    """
    Main widget for Khewat management.
    """

    def __init__(
        self,
        service: KhewatService,
        selection: SelectionContext,
    ) -> None:
        super().__init__()

        self._service = service
        self._selection = selection

        self._model = KhewatModel(service)
        self._toolbar = KhewatToolbar()
        self._table = KhewatTable(self._model)

        self._build_ui()
        self._connect_signals()

        print("[KhewatWidget] Created")

    @property
    def model(self) -> KhewatModel:
        return self._model

    @property
    def table(self) -> KhewatTable:
        return self._table

    @property
    def toolbar(self) -> KhewatToolbar:
        return self._toolbar

    def _build_ui(self) -> None:

        layout = QVBoxLayout()

        layout.addWidget(self._toolbar)
        layout.addWidget(self._table)

        self.setLayout(layout)

    def _connect_signals(self) -> None:

        self._toolbar.add_requested.connect(
            self._add_khewat
        )

        self._toolbar.edit_requested.connect(
            self._edit_khewat
        )

        self._toolbar.deactivate_requested.connect(
            self._deactivate_khewat
        )

        self._toolbar.refresh_requested.connect(
            self._refresh
        )

        self._selection.village_changed.connect(
            self._village_changed
        )

    def _village_changed(
        self,
        village: Village | None,
    ) -> None:
        """
        Reload Khewats when village changes.
        """

        if village is None:

            self._model.set_current_village(
                None
            )

        else:

            self._model.set_current_village(
                village.id
            )

    def _add_khewat(self) -> None:
        """
        Add a new Khewat.
        """

        if self._selection.village is None:

            QMessageBox.warning(
                self,
                "No Village Selected",
                "Please select a village before adding a Khewat.",
            )

            return

        dialog = KhewatDialog(
            FormMode.CREATE,
        )

        if not dialog.exec():
            return

        khewat = dialog.khewat(
            self._selection.village.id,
        )

        self._service.register(
            khewat,
        )

        self._model.refresh()

    def _edit_khewat(self) -> None:
        """
        Edit selected Khewat.
        """

        khewat = self._table.selected_khewat()

        if khewat is None:
            return

        dialog = KhewatDialog(
            FormMode.EDIT,
        )

        dialog.set_khewat(
            khewat,
        )

        if not dialog.exec():
            return

        dialog.update_khewat(
            khewat,
        )

        self._service.update(
            khewat,
        )

        self._model.refresh()

    def _deactivate_khewat(self) -> None:
        """
        Deactivate selected Khewat.
        """

        khewat = self._table.selected_khewat()

        if khewat is None:
            return

        reply = QMessageBox.question(
            self,
            "Deactivate Khewat",
            f"Deactivate Khewat '{khewat.khewat_no}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply != QMessageBox.Yes:
            return

        self._service.deactivate(
            khewat,
        )

        self._model.refresh()

    def _refresh(self) -> None:
        """
        Refresh the Khewat list.
        """

        self._model.refresh()