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


class OwnershipDialog(QDialog):
    """
    Dialog for adding/editing ownership.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.setWindowTitle(
            "Ownership"
        )

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._owner_combo = QComboBox(
            self,
        )

        self._numerator = QSpinBox(
            self,
        )

        self._denominator = QSpinBox(
            self,
        )

        self._remarks = QLineEdit(
            self,
        )

        self._buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            |
            QDialogButtonBox.StandardButton.Cancel,
            self,
        )

        self._numerator.setMinimum(0)
        self._numerator.setMaximum(9999)

        self._denominator.setMinimum(1)
        self._denominator.setMaximum(9999)

        self._denominator.setValue(1)

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
            self._numerator,
        )

        form.addRow(
            "Denominator",
            self._denominator,
        )

        form.addRow(
            "Remarks",
            self._remarks,
        )

        layout = QVBoxLayout()

        layout.addLayout(
            form,
        )

        layout.addWidget(
            self._buttons,
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

        self._buttons.accepted.connect(
            self.accept,
        )

        self._buttons.rejected.connect(
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
        owners = [(uuid, name), ...]
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
        Returns:
            owner_id,
            Fraction,
            remarks
        """

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