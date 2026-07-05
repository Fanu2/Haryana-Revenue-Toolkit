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
    Workspace for managing Jamabandi records.

    The workspace automatically tracks the
    currently selected Village and displays only
    the Jamabandis belonging to that Village.
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
            "No village selected."
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
        """
        Refresh the Jamabandi table for the
        currently selected Village.
        """

        if self._selected_village is None:

            records = []

            self._status.setText(
                "No village selected.",
            )

        else:

            records = (
                self._context
                .jamabandi_service
                .by_village(
                    self._selected_village.id,
                )
            )

            finalized = sum(
                1
                for record in records
                if record.finalized
            )

            draft = (
                len(records)
                - finalized
            )

            self._status.setText(
                f"Village: {self._selected_village.name} | "
                f"{len(records)} Jamabandi(s) | "
                f"{draft} Draft | "
                f"{finalized} Finalized"
            )

        self._table.set_jamabandis(
            records,
        )

        self._toolbar.update_state(
            selected=False,
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
                "Please select a Village first.",
            )

            return

        dialog = JamabandiDialog(
            self._selected_village.id,
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

        if record.finalized:

            QMessageBox.information(
                self,
                "Jamabandi",
                "Finalized Jamabandis cannot be edited.\n"
                "Reopen the record first.",
            )

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

        if record.finalized:

            QMessageBox.information(
                self,
                "Jamabandi",
                "Finalized Jamabandis cannot be deleted.\n"
                "Reopen the record first.",
            )

            return

        answer = QMessageBox.question(
            self,
            "Delete Jamabandi",
            "Delete the selected Jamabandi?",
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

        if record.finalized:

            QMessageBox.information(
                self,
                "Jamabandi",
                "The selected Jamabandi is already finalized.",
            )

            return

        answer = QMessageBox.question(
            self,
            "Finalize Jamabandi",
            (
                "Finalize the selected Jamabandi?\n\n"
                "A finalized Jamabandi becomes read-only "
                "until it is reopened."
            ),
        )

        if answer != QMessageBox.Yes:

            return

        self._context.jamabandi_service.finalize(
            record.id,
        )

        QMessageBox.information(
            self,
            "Jamabandi",
            "Jamabandi finalized successfully.",
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

        if not record.finalized:

            QMessageBox.information(
                self,
                "Jamabandi",
                "The selected Jamabandi is already open.",
            )

            return

        answer = QMessageBox.question(
            self,
            "Reopen Jamabandi",
            (
                "Reopen the selected Jamabandi?\n\n"
                "Editing will be enabled again."
            ),
        )

        if answer != QMessageBox.Yes:

            return

        self._context.jamabandi_service.reopen(
            record.id,
        )

        QMessageBox.information(
            self,
            "Jamabandi",
            "Jamabandi reopened successfully.",
        )

        self._refresh()

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def _selection_changed(
        self,
    ) -> None:
        """
        Update the toolbar according to the
        selected Jamabandi.
        """

        record = (
            self._table.selected_jamabandi()
        )

        if record is None:

            self._toolbar.update_state(
                selected=False,
            )

            return

        self._toolbar.update_state(
            selected=True,
            finalized=record.finalized,
        )

    def _village_changed(
        self,
        village,
    ) -> None:
        """
        Respond to a change in the
        currently selected Village.
        """

        self._selected_village = village

        self._refresh()