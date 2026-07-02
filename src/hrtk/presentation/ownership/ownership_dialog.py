"""
Haryana Revenue Toolkit (HRTK)

Ownership Dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
)

from hrtk.domain.ownership import Ownership
from hrtk.domain.value_objects.fraction import Fraction
from hrtk.presentation.common.form_mode import FormMode


class OwnershipDialog(QDialog):
    """
    Dialog for creating/editing Ownership.
    """

    def __init__(
        self,
        mode: FormMode,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._mode = mode

        if mode == FormMode.CREATE:
            self.setWindowTitle("Add Ownership")
        else:
            self.setWindowTitle("Edit Ownership")

        self._create_widgets()
        self._build_layout()
        self._connect_signals()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self._owner_combo = QComboBox(self)

        self._numerator = QSpinBox(self)
        self._numerator.setRange(0, 9999)

        self._denominator = QSpinBox(self)
        self._denominator.setRange(1, 9999)
        self._denominator.setValue(1)

        self._remarks = QLineEdit(self)

        self._buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            |
            QDialogButtonBox.StandardButton.Cancel,
            self,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        form = QFormLayout()

        form.addRow("Owner", self._owner_combo)
        form.addRow("Numerator", self._numerator)
        form.addRow("Denominator", self._denominator)
        form.addRow("Remarks", self._remarks)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self._buttons)

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(self) -> None:

        self._buttons.accepted.connect(self.accept)
        self._buttons.rejected.connect(self.reject)

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_owners(
        self,
        owners: list[tuple[str, str]],
    ) -> None:

        self._owner_combo.clear()

        for owner_id, owner_name in owners:
            self._owner_combo.addItem(
                owner_name,
                owner_id,
            )

    def ownership_data(
        self,
    ) -> tuple[str, Fraction, str]:

        owner_id = self._owner_combo.currentData()

        share = Fraction(
            self._numerator.value(),
            self._denominator.value(),
        )

        remarks = self._remarks.text().strip()

        return (
            owner_id,
            share,
            remarks,
        )

    # ---------------------------------------------------------
    # Future Edit Support
    # ---------------------------------------------------------

    def set_ownership(
        self,
        ownership: Ownership,
    ) -> None:
        """
        Populate dialog from an existing Ownership.

        (Used by EDIT mode.)
        """

        for index in range(self._owner_combo.count()):

            if (
                self._owner_combo.itemData(index)
                == str(ownership.owner_id)
            ):
                self._owner_combo.setCurrentIndex(index)
                break

        #
        # Owner should not change during edit.
        #
        self._owner_combo.setEnabled(False)

        self._numerator.setValue(
            ownership.share.numerator
        )

        self._denominator.setValue(
            ownership.share.denominator
        )

        self._remarks.setText(
            ownership.remarks
        )

    def update_ownership(
        self,
        ownership: Ownership,
    ) -> None:
        """
        Copy edited values back into the domain object.

        (Used by EDIT mode.)
        """

        ownership.share = Fraction(
            self._numerator.value(),
            self._denominator.value(),
        )

        ownership.remarks = (
            self._remarks.text().strip()
        )