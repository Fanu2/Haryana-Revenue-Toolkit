"""
Haryana Revenue Toolkit (HRTK)

Ownership Dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
)

from hrtk.domain.ownership import Ownership
from hrtk.domain.value_objects.fraction import Fraction

from hrtk.presentation.common.base_dialog import (
    BaseDialog,
)

from hrtk.presentation.common.form_mode import (
    FormMode,
)


class OwnershipDialog(BaseDialog):
    """
    Dialog for creating and editing ownership records.
    """

    def __init__(
        self,
        mode: FormMode,
    ) -> None:

        super().__init__(mode)

        self.setWindowTitle(
            "Add Ownership"
            if self.is_create_mode
            else "Edit Ownership"
        )

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._owner_combo = QComboBox(
            self,
        )

        self._numerator_spin = QSpinBox(
            self,
        )

        self._numerator_spin.setMinimum(
            0,
        )

        self._numerator_spin.setMaximum(
            9999,
        )

        self._denominator_spin = QSpinBox(
            self,
        )

        self._denominator_spin.setMinimum(
            1,
        )

        self._denominator_spin.setMaximum(
            9999,
        )

        self._denominator_spin.setValue(
            1,
        )

        self._remarks_edit = QLineEdit(
            self,
        )

        self._button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            |
            QDialogButtonBox.StandardButton.Cancel,
            self,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        form = QFormLayout()

        form.addRow(
            "Owner",
            self._owner_combo,
        )

        form.addRow(
            "Numerator",
            self._numerator_spin,
        )

        form.addRow(
            "Denominator",
            self._denominator_spin,
        )

        form.addRow(
            "Remarks",
            self._remarks_edit,
        )

        layout = QVBoxLayout()

        layout.addLayout(
            form,
        )

        layout.addWidget(
            self._button_box,
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

        self._button_box.accepted.connect(
            self.accept,
        )

        self._button_box.rejected.connect(
            self.reject,
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_owners(
        self,
        owners: list[tuple[str, str]],
    ) -> None:
        """
        Populate the owner combo.
        """

        self._owner_combo.clear()

        for owner_id, owner_name in owners:

            self._owner_combo.addItem(
                owner_name,
                owner_id,
            )

    def ownership_data(
        self,
    ) -> tuple[str, Fraction, str]:
        """
        Build ownership data from dialog.
        """

        owner_id = self._owner_combo.currentData()

        share = Fraction(
            self._numerator_spin.value(),
            self._denominator_spin.value(),
        )

        remarks = (
            self._remarks_edit.text().strip()
        )

        return (
            owner_id,
            share,
            remarks,
        )

    # ---------------------------------------------------------
    # Edit Support
    # ---------------------------------------------------------

    def set_ownership(
        self,
        ownership: Ownership,
    ) -> None:
        """
        Populate dialog from an existing ownership.
        """

        for index in range(
            self._owner_combo.count()
        ):

            if (
                self._owner_combo.itemData(index)
                == str(
                    ownership.owner_id,
                )
            ):

                self._owner_combo.setCurrentIndex(
                    index,
                )

                break

        #
        # Owner cannot be changed while editing.
        #

        self._owner_combo.setEnabled(
            False,
        )

        self._numerator_spin.setValue(
            ownership.share.numerator,
        )

        self._denominator_spin.setValue(
            ownership.share.denominator,
        )

        self._remarks_edit.setText(
            ownership.remarks,
        )

    def update_ownership(
        self,
        ownership: Ownership,
    ) -> None:
        """
        Update an existing ownership from the dialog.
        """

        ownership.share = Fraction(
            self._numerator_spin.value(),
            self._denominator_spin.value(),
        )

        ownership.remarks = (
            self._remarks_edit.text().strip()
        )

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def reset(
        self,
    ) -> None:
        """
        Reset the dialog to its default state.
        """

        self._owner_combo.setEnabled(True)

        self._owner_combo.setCurrentIndex(-1)

        self._numerator_spin.setValue(
            0,
        )

        self._denominator_spin.setValue(
            1,
        )

        self._remarks_edit.clear()