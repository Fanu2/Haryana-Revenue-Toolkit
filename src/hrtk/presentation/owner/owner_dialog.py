"""
Haryana Revenue Toolkit (HRTK)

Owner Dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

from hrtk.domain.owner import Owner
from hrtk.presentation.common.base_dialog import BaseDialog
from hrtk.presentation.common.form_mode import FormMode


class OwnerDialog(BaseDialog):
    """
    Dialog for creating and editing owners.
    """

    def __init__(
        self,
        mode: FormMode,
    ) -> None:
        super().__init__(mode)

        self.setWindowTitle(
            "Add Owner"
            if self.is_create_mode
            else "Edit Owner"
        )

        self._create_widgets()
        self._build_layout()
        self._connect_signals()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self._owner_code_edit = QLineEdit(self)

        self._owner_name_edit = QLineEdit(self)

        self._father_name_edit = QLineEdit(self)

        self._address_edit = QLineEdit(self)

        self._mobile_edit = QLineEdit(self)

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
            "Owner Code",
            self._owner_code_edit,
        )

        form.addRow(
            "Owner Name",
            self._owner_name_edit,
        )

        form.addRow(
            "Father Name",
            self._father_name_edit,
        )

        form.addRow(
            "Address",
            self._address_edit,
        )

        form.addRow(
            "Mobile",
            self._mobile_edit,
        )

        form.addRow(
            "Remarks",
            self._remarks_edit,
        )

        layout = QVBoxLayout()

        layout.addLayout(form)
        layout.addWidget(self._button_box)

        self.setLayout(layout)

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(self) -> None:

        self._button_box.accepted.connect(
            self.accept
        )

        self._button_box.rejected.connect(
            self.reject
        )

    # ---------------------------------------------------------
    # Data Binding
    # ---------------------------------------------------------

    def owner(
        self,
        village_id,
    ) -> Owner:
        """
        Build an Owner from the dialog.
        """

        return Owner(
            village_id=village_id,
            owner_code=self._owner_code_edit.text().strip(),
            owner_name=self._owner_name_edit.text().strip(),
            father_name=self._father_name_edit.text().strip(),
            address=self._address_edit.text().strip(),
            mobile=self._mobile_edit.text().strip(),
            remarks=self._remarks_edit.text().strip(),
        )

    def set_owner(
        self,
        owner: Owner,
    ) -> None:
        """
        Populate the dialog.
        """

        self._owner_code_edit.setText(
            owner.owner_code
        )

        self._owner_name_edit.setText(
            owner.owner_name
        )

        self._father_name_edit.setText(
            owner.father_name
        )

        self._address_edit.setText(
            owner.address
        )

        self._mobile_edit.setText(
            owner.mobile
        )

        self._remarks_edit.setText(
            owner.remarks
        )

    def update_owner(
        self,
        owner: Owner,
        ) -> None:
        
        """
        Update an existing owner.
        """

        owner.owner_code = (
        self._owner_code_edit.text().strip()
        )

        owner.owner_name = (
        self._owner_name_edit.text().strip()
        )

        owner.father_name = (
        self._father_name_edit.text().strip()
        )

        owner.address = (
        self._address_edit.text().strip()
        )

        owner.mobile = (
        self._mobile_edit.text().strip()
        )

        owner.remarks = (
        self._remarks_edit.text().strip()
        )