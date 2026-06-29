"""
Haryana Revenue Toolkit (HRTK)

Village Dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

from hrtk.presentation.common.base_dialog import BaseDialog
from hrtk.presentation.common.form_mode import FormMode
from hrtk.domain.village import Village


class VillageDialog(BaseDialog):
    """
    Dialog for creating and editing villages.
    """

    def __init__(
        self,
        mode: FormMode,
    ) -> None:
        super().__init__(mode)

        self.setWindowTitle(
            "Add Village"
            if self.is_create_mode
            else "Edit Village"
        )

        self._create_widgets()
        self._build_layout()
        self._connect_signals()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:
        """
        Create all dialog widgets.
        """

        self._code_edit = QLineEdit(self)

        self._name_edit = QLineEdit(self)

        self._tehsil_edit = QLineEdit(self)

        self._district_edit = QLineEdit(self)

        self._state_edit = QLineEdit(self)

        self._button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel,
            self,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:
        """
        Build the dialog layout.
        """

        form = QFormLayout()

        form.addRow("Code", self._code_edit)
        form.addRow("Name", self._name_edit)
        form.addRow("Tehsil", self._tehsil_edit)
        form.addRow("District", self._district_edit)
        form.addRow("State", self._state_edit)

        layout = QVBoxLayout()

        layout.addLayout(form)
        layout.addWidget(self._button_box)

        self.setLayout(layout)

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(self) -> None:
        """
        Connect dialog signals.
        """

        self._button_box.accepted.connect(
            self.accept
        )

        self._button_box.rejected.connect(
            self.reject
        )

        # ---------------------------------------------------------
    # Data Binding
    # ---------------------------------------------------------

    def village(self) -> Village:
        """
        Return a Village built from the dialog fields.
        """

        return Village(
            code=self._code_edit.text().strip(),
            name=self._name_edit.text().strip(),
            tehsil=self._tehsil_edit.text().strip(),
            district=self._district_edit.text().strip(),
            state=self._state_edit.text().strip(),
        )

    def set_village(
        self,
        village: Village,
    ) -> None:
        """
        Populate the dialog from an existing Village.
        """

        self._code_edit.setText(village.code)
        self._name_edit.setText(village.name)
        self._tehsil_edit.setText(village.tehsil)
        self._district_edit.setText(village.district)
        self._state_edit.setText(village.state)
    def update_village(
        self,
        village: Village,
    ) -> None:
        """
        Update an existing Village from the dialog.
        """

        village.change_code(
            self._code_edit.text().strip()
        )

        village.rename(
            self._name_edit.text().strip()
        )

        village.change_tehsil(
            self._tehsil_edit.text().strip()
        )

        village.change_district(
            self._district_edit.text().strip()
        )

        village.change_state(
            self._state_edit.text().strip()
        )