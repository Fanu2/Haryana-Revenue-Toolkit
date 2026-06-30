"""
Haryana Revenue Toolkit (HRTK)

Khasra Widget.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from hrtk.presentation.khasra.khasra_dialog import (
    KhasraDialog,
)
from hrtk.presentation.khasra.khasra_model import (
    KhasraModel,
)
from hrtk.presentation.khasra.khasra_table import (
    KhasraTable,
)
from hrtk.presentation.khasra.khasra_toolbar import (
    KhasraToolbar,
)
from hrtk.services.parcel_service import (
    ParcelService,
)


class KhasraWidget(QWidget):
    """
    Main widget for Khasra management.
    """

    def __init__(
        self,
        service: ParcelService,
    ) -> None:

        super().__init__()

        self._service = service

        self._model = KhasraModel(
            service,
        )

        self._toolbar = KhasraToolbar()

        self._table = KhasraTable(
            self._model,
        )

        self._build_ui()

        self._connect_signals()

    def _build_ui(
        self,
    ) -> None:

        layout = QVBoxLayout()

        layout.addWidget(
            self._toolbar,
        )

        layout.addWidget(
            self._table,
        )

        self.setLayout(
            layout,
        )

    def _connect_signals(
        self,
    ) -> None:

        self._toolbar.add_requested.connect(
            self._add_parcel,
        )

        self._toolbar.refresh_requested.connect(
            self._refresh,
        )

        self._toolbar.search_text_changed.connect(
            self._search,
        )

    def _add_parcel(
        self,
    ) -> None:
        """
        Create a parcel.
        """

        dialog = KhasraDialog(
            self,
        )

        if not dialog.exec():
            return

        parcel = dialog.value()

        self._service.create(
            parcel,
        )

        self._model.refresh()

        self._toolbar.clear_search()

    def _refresh(
        self,
    ) -> None:
        """
        Refresh parcel list.
        """

        self._model.refresh()

    def _search(
        self,
        text: str,
    ) -> None:
        """
        Search placeholder.

        Search proxy model will be added
        in the next sprint.
        """

        del text

        self._model.refresh()