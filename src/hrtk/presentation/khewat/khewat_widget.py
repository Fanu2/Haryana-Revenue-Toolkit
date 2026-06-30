"""
Haryana Revenue Toolkit (HRTK)

Khewat Widget.
"""
from PySide6.QtWidgets import (
    QMessageBox,
    QVBoxLayout,
    QWidget,
)
from hrtk.application.selection_context import SelectionContext

from hrtk.domain.khewat import Khewat
from hrtk.domain.village import Village

from hrtk.presentation.common.form_mode import FormMode
from hrtk.presentation.common.search_proxy_model import (
    SearchProxyModel,
)

from hrtk.presentation.khewat.khewat_dialog import KhewatDialog
from hrtk.presentation.khewat.khewat_model import KhewatModel
from hrtk.presentation.khewat.khewat_table import KhewatTable
from hrtk.presentation.khewat.khewat_toolbar import KhewatToolbar

from hrtk.services.khewat_service import KhewatService

from hrtk.services.export_service import (
    ExportService,
)

from hrtk.services.export_service import (
    ExportService,
)


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

        #
        # Search Proxy
        #
        self._proxy = SearchProxyModel()

        self._proxy.setSourceModel(
            self._model,
        )

        self._toolbar = KhewatToolbar()

        self._table = KhewatTable(
            self._proxy,
        )

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

        self._toolbar.export_requested.connect(
            self._export_excel
        )

        self._selection.village_changed.connect(
            self._village_changed
        )
        
        self._toolbar.search_text_changed.connect(
            self._search,
        )

        self._toolbar.export_requested.connect(
        self._export_excel,
        )

    def _village_changed(
        self,
        village: Village | None,
    ) -> None:
        """
        Reload Khewats when village changes.
        """

        self._toolbar.clear_search()

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


        self._toolbar.clear_search()

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

        self._toolbar.clear_search()

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

        self._model.refresh()
        self._toolbar.clear_search()

    def _refresh(self) -> None:
        """
        Refresh the Khewat list.
        """

        self._model.refresh()

        self._toolbar.clear_search()

    def _export_excel(
        self,
    ) -> None:
        """
        Export khewats to Excel.
        """

        rows = [
            (
                khewat.khewat_no,
                khewat.khewat_type,
                "Active" if khewat.active else "Inactive",
            )
            for khewat in self._model.khewats
        ]

        ExportService.export_excel(
            parent=self,
            title="Export Khewats",
            default_filename="khewats.xlsx",
            sheet_name="Khewats",
            headers=list(
                KhewatModel.HEADERS,
            ),
            rows=rows,
        )


    def _export_excel(
        self,
    ) -> None:
        """
        Export khewats to Excel.
        """

        rows = [
            (
                khewat.khewat_no,
                khewat.old_khewat_no,
                khewat.jamabandi_year,
                "Active" if khewat.active else "Inactive",
            )
            for khewat in self._model.khewats
        ]

        ExportService.export_excel(
            parent=self,
            title="Export Khewats",
            default_filename="khewats.xlsx",
            sheet_name="Khewats",
            headers=list(
                KhewatModel.HEADERS,
            ),
            rows=rows,
        )

    def _search(
        self,
        text: str,
    ) -> None:
        """
        Filter khewats.
        """

        self._proxy.set_search_text(
            text,
        )