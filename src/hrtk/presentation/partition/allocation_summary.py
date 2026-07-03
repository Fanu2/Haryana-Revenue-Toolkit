"""
Haryana Revenue Toolkit (HRTK)

Allocation Summary Panel.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class AllocationSummary(QWidget):
    """
    Displays live allocation summary
    for the current partition.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._create_widgets()

        self._build_layout()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:
        """
        Create summary labels.
        """

        #
        # Owner Summary
        #

        self._required_area = QLabel(
            "0K-0M-0S"
        )

        self._allocated_area = QLabel(
            "0K-0M-0S"
        )

        self._remaining_area = QLabel(
            "0K-0M-0S"
        )

        #
        # Khasra Summary
        #

        self._khasra_total = QLabel(
            "0K-0M-0S"
        )

        self._khasra_allocated = QLabel(
            "0K-0M-0S"
        )

        self._khasra_balance = QLabel(
            "0K-0M-0S"
        )
    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:
        """
        Build the summary layout.
        """

        #
        # Owner
        #

        owner_group = QGroupBox(
            "Owner Summary"
        )

        owner_layout = QFormLayout()

        owner_layout.addRow(
            "Required",
            self._required_area,
        )

        owner_layout.addRow(
            "Allocated",
            self._allocated_area,
        )

        owner_layout.addRow(
            "Remaining",
            self._remaining_area,
        )

        owner_group.setLayout(
            owner_layout,
        )

        #
        # Khasra
        #

        khasra_group = QGroupBox(
            "Khasra Summary"
        )

        khasra_layout = QFormLayout()

        khasra_layout.addRow(
            "Total Area",
            self._khasra_total,
        )

        khasra_layout.addRow(
            "Allocated",
            self._khasra_allocated,
        )

        khasra_layout.addRow(
            "Balance",
            self._khasra_balance,
        )

        khasra_group.setLayout(
            khasra_layout,
        )

        layout = QVBoxLayout()

        layout.addWidget(
            owner_group,
        )

        layout.addWidget(
            khasra_group,
        )

        layout.addStretch()

        self.setLayout(
            layout,
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def update_owner(
        self,
        required: str,
        allocated: str,
        remaining: str,
    ) -> None:
        """
        Update owner summary.
        """

        self._required_area.setText(
            required,
        )

        self._allocated_area.setText(
            allocated,
        )

        self._remaining_area.setText(
            remaining,
        )

    def update_khasra(
        self,
        total: str,
        allocated: str,
        balance: str,
    ) -> None:
        """
        Update Khasra summary.
        """

        self._khasra_total.setText(
            total,
        )

        self._khasra_allocated.setText(
            allocated,
        )

        self._khasra_balance.setText(
            balance,
        )

    def clear(
        self,
    ) -> None:
        """
        Reset the summary.
        """

        self.update_owner(
            "0K-0M-0S",
            "0K-0M-0S",
            "0K-0M-0S",
        )

        self.update_khasra(
            "0K-0M-0S",
            "0K-0M-0S",
            "0K-0M-0S",
        )