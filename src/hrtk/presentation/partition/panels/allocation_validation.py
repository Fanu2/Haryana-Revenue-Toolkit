"""
Haryana Revenue Toolkit (HRTK)

Allocation Validation Panel.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QListWidget,
    QVBoxLayout,
    QWidget,
)


class AllocationValidation(QWidget):
    """
    Displays allocation validation messages.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._messages = QListWidget()

        layout = QVBoxLayout()

        layout.addWidget(
            self._messages,
        )

        self.setLayout(
            layout,
        )
    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Remove all validation messages.
        """

        self._messages.clear()

    def add_information(
        self,
        message: str,
    ) -> None:
        """
        Add an informational message.
        """

        self._messages.addItem(
            "ℹ " + message,
        )

    def add_success(
        self,
        message: str,
    ) -> None:
        """
        Add a success message.
        """

        self._messages.addItem(
            "✓ " + message,
        )

    def add_warning(
        self,
        message: str,
    ) -> None:
        """
        Add a warning message.
        """

        self._messages.addItem(
            "⚠ " + message,
        )

    def add_error(
        self,
        message: str,
    ) -> None:
        """
        Add an error message.
        """

        self._messages.addItem(
            "✗ " + message,
        )

    def show_default_state(
        self,
    ) -> None:
        """
        Display initial validation state.
        """

        self.clear()

        self.add_information(
            "Select an owner and a Khasra to begin allocation."
        )

    def show_partition_ready(
        self,
    ) -> None:
        """
        Display successful completion.
        """

        self.clear()

        self.add_success(
            "All owners have received their entitlement."
        )

        self.add_success(
            "All Khasras are fully allocated."
        )

        self.add_success(
            "Partition is ready for finalization."
        )