"""
Haryana Revenue Toolkit (HRTK)

Save File Service.
"""

from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QWidget,
)


class SaveFileService:
    """
    Centralized Save-As dialogs.

    All file save dialogs in HRTK should pass through
    this service.
    """

    @staticmethod
    def save_excel(
        parent: QWidget | None,
        title: str,
        default_filename: str,
    ) -> Path | None:
        """
        Display a Save-As dialog for an Excel workbook.

        Returns
        -------
        Path | None
            Selected filename or None if cancelled.
        """

        filename, _ = QFileDialog.getSaveFileName(
            parent,
            title,
            default_filename,
            "Excel Workbook (*.xlsx)",
        )

        if not filename:
            return None

        path = Path(filename)

        if path.suffix.lower() != ".xlsx":
            path = path.with_suffix(".xlsx")

        return path

    @staticmethod
    def save_csv(
        parent: QWidget | None,
        title: str,
        default_filename: str,
    ) -> Path | None:
        """
        Display a Save-As dialog for a CSV file.
        """

        filename, _ = QFileDialog.getSaveFileName(
            parent,
            title,
            default_filename,
            "CSV File (*.csv)",
        )

        if not filename:
            return None

        path = Path(filename)

        if path.suffix.lower() != ".csv":
            path = path.with_suffix(".csv")

        return path

    @staticmethod
    def save_pdf(
        parent: QWidget | None,
        title: str,
        default_filename: str,
    ) -> Path | None:
        """
        Display a Save-As dialog for a PDF file.
        """

        filename, _ = QFileDialog.getSaveFileName(
            parent,
            title,
            default_filename,
            "PDF File (*.pdf)",
        )

        if not filename:
            return None

        path = Path(filename)

        if path.suffix.lower() != ".pdf":
            path = path.with_suffix(".pdf")

        return path