"""
Haryana Revenue Toolkit (HRTK)

Message Service.
"""

from __future__ import annotations

# ==========================================================
# Qt
# ==========================================================

from PySide6.QtWidgets import (
    QMessageBox,
    QWidget,
)


class MessageService:
    """
    Centralized message dialogs for HRTK.
    """

    # ---------------------------------------------------------
    # Information
    # ---------------------------------------------------------

    @staticmethod
    def information(
        parent: QWidget | None,
        title: str,
        message: str,
    ) -> None:

        QMessageBox.information(
            parent,
            title,
            message,
        )

    # ---------------------------------------------------------
    # Warning
    # ---------------------------------------------------------

    @staticmethod
    def warning(
        parent: QWidget | None,
        title: str,
        message: str,
    ) -> None:

        QMessageBox.warning(
            parent,
            title,
            message,
        )

    # ---------------------------------------------------------
    # Error
    # ---------------------------------------------------------

    @staticmethod
    def critical(
        parent: QWidget | None,
        title: str,
        message: str,
    ) -> None:

        QMessageBox.critical(
            parent,
            title,
            message,
        )

    # ---------------------------------------------------------
    # Confirmation
    # ---------------------------------------------------------

    @staticmethod
    def confirm(
        parent: QWidget | None,
        title: str,
        message: str,
    ) -> bool:
        """
        Yes / Cancel confirmation.
        """

        reply = QMessageBox.question(
            parent,
            title,
            message,
            QMessageBox.Yes | QMessageBox.Cancel,
            QMessageBox.Cancel,
        )

        return reply == QMessageBox.Yes

    # ---------------------------------------------------------
    # Success
    # ---------------------------------------------------------

    @staticmethod
    def success(
        parent: QWidget | None,
        message: str,
    ) -> None:
        """
        Display a success message.
        """

        QMessageBox.information(
            parent,
            "Success",
            message,
        )