"""
Haryana Revenue Toolkit (HRTK)

Partition Validation Panel.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QLabel,
)


class ValidationPanel(QGroupBox):
    """
    Displays validation status for the
    current partition.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(
            "Validation",
            parent,
        )

        self._create_widgets()

        self._build_layout()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._ownership = QLabel("Not Checked")

        self._allocation = QLabel("Not Checked")

        self._area = QLabel("Not Checked")

        self._overall = QLabel("Pending")

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QFormLayout()

        layout.addRow(
            "Ownership",
            self._ownership,
        )

        layout.addRow(
            "Allocation",
            self._allocation,
        )

        layout.addRow(
            "Area",
            self._area,
        )

        layout.addRow(
            "Overall",
            self._overall,
        )

        self.setLayout(
            layout,
        )

    # ---------------------------------------------------------
    # Public
    # ---------------------------------------------------------

    def set_ownership_valid(
        self,
        valid: bool,
    ) -> None:

        self._ownership.setText(
            "✔ Valid"
            if valid
            else "✖ Invalid"
        )

    def set_allocation_valid(
        self,
        valid: bool,
    ) -> None:

        self._allocation.setText(
            "✔ Valid"
            if valid
            else "✖ Invalid"
        )

    def set_area_valid(
        self,
        valid: bool,
    ) -> None:

        self._area.setText(
            "✔ Valid"
            if valid
            else "✖ Invalid"
        )

    def update_overall(
        self,
    ) -> None:
        """
        Update overall validation state.
        """

        values = (
            self._ownership.text(),
            self._allocation.text(),
            self._area.text(),
        )

        if all(
            value.startswith("✔")
            for value in values
        ):

            self._overall.setText(
                "✔ Partition Valid"
            )

        else:

            self._overall.setText(
                "⚠ Validation Required"
            )

    def clear(
        self,
    ) -> None:

        self._ownership.setText(
            "Not Checked"
        )

        self._allocation.setText(
            "Not Checked"
        )

        self._area.setText(
            "Not Checked"
        )

        self._overall.setText(
            "Pending"
        )