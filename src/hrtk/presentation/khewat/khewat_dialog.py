"""
Haryana Revenue Toolkit (HRTK)

Khewat Dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

from hrtk.domain.khewat import Khewat
from hrtk.presentation.common.base_dialog import BaseDialog
from hrtk.presentation.common.form_mode import FormMode


class KhewatDialog(BaseDialog):
    """
    Dialog for creating and editing Khewats.
    """

    def __init__(
        self,
        mode: FormMode,
    ) -> None:
        super().__init__(mode)

        self.setWindowTitle(
            "Add Khewat"
            if self.is_create_mode
            else "Edit Khewat"
        )

        self._create_widgets()
        self._build_layout()
        self._connect_signals()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self._khewat_no_edit = QLineEdit(self)

        self._old_khewat_no_edit = QLineEdit(self)

        self._jamabandi_year_edit = QLineEdit(self)

        self._remarks_edit = QLineEdit(self)

        self._button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel,
            self,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        form = QFormLayout()

        form.addRow(
            "Khewat No",
            self._khewat_no_edit,
        )

        form.addRow(
            "Old Khewat No",
            self._old_khewat_no_edit,
        )

        form.addRow(
            "Jamabandi Year",
            self._jamabandi_year_edit,
        )

        form.addRow(
            "Remarks",
            self._remarks_edit,
        )

        layout = QVBoxLayout()

        layout.addLayout(form)

        layout.addWidget(
            self._button_box,
        )

        self.setLayout(layout)

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(self) -> None:

        self._button_box.accepted.connect(
            self.accept,
        )

        self._button_box.rejected.connect(
            self.reject,
        )

    # ---------------------------------------------------------
    # Data Binding
    # ---------------------------------------------------------

    def khewat(
        self,
        village_id,
    ) -> Khewat:
        """
        Build a Khewat from the dialog.
        """

        return Khewat(
            village_id=village_id,
            khewat_no=self._khewat_no_edit.text().strip(),
            old_khewat_no=self._old_khewat_no_edit.text().strip(),
            jamabandi_year=self._jamabandi_year_edit.text().strip(),
            remarks=self._remarks_edit.text().strip(),
        )

    def set_khewat(
        self,
        khewat: Khewat,
    ) -> None:
        """
        Populate the dialog.
        """

        self._khewat_no_edit.setText(
            khewat.khewat_no,
        )

        self._old_khewat_no_edit.setText(
            khewat.old_khewat_no,
        )

        self._jamabandi_year_edit.setText(
            khewat.jamabandi_year,
        )

        self._remarks_edit.setText(
            khewat.remarks,
        )

    def update_khewat(
        self,
        khewat: Khewat,
    ) -> None:
        """
        Update an existing Khewat.
        """

        khewat.khewat_no = (
            self._khewat_no_edit.text().strip()
        )

        khewat.old_khewat_no = (
            self._old_khewat_no_edit.text().strip()
        )

        khewat.jamabandi_year = (
            self._jamabandi_year_edit.text().strip()
        )

        khewat.remarks = (
            self._remarks_edit.text().strip()
        )