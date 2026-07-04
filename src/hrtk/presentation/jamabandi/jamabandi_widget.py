"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Workspace.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

from hrtk.presentation.jamabandi.dialogs.jamabandi_dialog import (
    JamabandiDialog,
)

from hrtk.presentation.jamabandi.jamabandi_toolbar import (
    JamabandiToolbar,
)

from hrtk.presentation.jamabandi.tables.jamabandi_table import (
    JamabandiTable,
)


class JamabandiWidget(QWidget):
    """
    Jamabandi management workspace.
    """

    def __init__(
        self,
        context,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._context = context

        self._selected_village = None

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

        self._refresh()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._toolbar = (
            JamabandiToolbar()
        )

        self._table = (
            JamabandiTable()
        )

        self._status = QLabel(
            "Ready."
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QVBoxLayout()

        layout.addWidget(
            self._toolbar,
        )

        layout.addWidget(
            self._table,
        )

        layout.addWidget(
            self._status,
        )

        self.setLayout(
            layout,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(
        self,
    ) -> None:

        self._toolbar.add_requested.connect(
            self._new,
        )

        self._toolbar.edit_requested.connect(
            self._edit,
        )

        self._toolbar.delete_requested.connect(
            self._delete,
        )

        self._toolbar.refresh_requested.connect(
            self._refresh,
        )

        self._toolbar.finalize_requested.connect(
            self._finalize,
        )

        self._toolbar.reopen_requested.connect(
            self._reopen,
        )

        self._table.selectionModel().selectionChanged.connect(
            self._selection_changed,
        )

        self._context.selection.village_changed.connect(
            self._village_changed,
        )

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def _refresh(
        self,
    ) -> None:

        records = (
            self._context
            .jamabandi_service
            .all()
        )

        self._table.set_jamabandis(
            records,
        )

        self._status.setText(
            f"{len(records)} Jamabandi record(s)."
        )

        self._toolbar.enable_selection_actions(
            False,
        )

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def _new(
        self,
    ) -> None:

        if self._selected_village is None:

            QMessageBox.information(
                self,
                "Jamabandi",
                "Select a Village first.",
            )

            return

        dialog = JamabandiDialog(
            self._selected_village,
            parent=self,
        )

        if not dialog.exec():

            return

        self._context.jamabandi_service.register(
            dialog.jamabandi(),
        )

        self._refresh()

    def _edit(
        self,
    ) -> None:

        record = (
            self._table.selected_jamabandi()
        )

        if record is None:

            return

        dialog = JamabandiDialog(
            record.village_id,
            record,
            self,
        )

        if not dialog.exec():

            return

        self._context.jamabandi_service.update(
            dialog.jamabandi(),
        )

        self._refresh()

    def _delete(
        self,
    ) -> None:

        record = (
            self._table.selected_jamabandi()
        )

        if record is None:

            return

        answer = QMessageBox.question(
            self,
            "Delete",
            "Delete selected Jamabandi?",
        )

        if answer != QMessageBox.Yes:

            return

        self._context.jamabandi_service.remove(
            record.id,
        )

        self._refresh()

    # ---------------------------------------------------------
    # Status Changes
    # ---------------------------------------------------------

    def _finalize(
        self,
    ) -> None:

        record = (
            self._table.selected_jamabandi()
        )

        if record is None:

            return

        self._context.jamabandi_service.finalize(
            record.id,
        )

        self._refresh()

    def _reopen(
        self,
    ) -> None:

        record = (
            self._table.selected_jamabandi()
        )

        if record is None:

            return

        self._context.jamabandi_service.reopen(
            record.id,
        )

        self._refresh()

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def _selection_changed(
        self,
    ) -> None:

        selected = (
            self._table.selected_jamabandi()
            is not None
        )

        self._toolbar.enable_selection_actions(
            selected,
        )

    def _village_changed(
        self,
        village,
    ) -> None:
        """
        Track the currently selected village.
        """

        self._selected_village = village

        if village is None:

            self._status.setText(
                "No village selected.",
            )

        else:

            self._status.setText(
                f"Village: {village.name}",
            )