"""
Haryana Revenue Toolkit (HRTK)

Export Service.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PySide6.QtWidgets import QWidget

from hrtk.export.excel_exporter import ExcelExporter
from hrtk.presentation.common.message_service import (
    MessageService,
)
from hrtk.presentation.common.save_file_service import (
    SaveFileService,
)


class ExportService:
    """
    Coordinates export operations.

    Widgets should use this service instead of calling
    ExcelExporter directly.
    """

    @staticmethod
    def export_excel(
        parent: QWidget | None,
        title: str,
        default_filename: str,
        sheet_name: str,
        headers: list[str],
        rows: Iterable[Iterable],
    ) -> bool:
        """
        Export tabular data to Excel.

        Returns
        -------
        bool
            True if export succeeded.
            False if cancelled or failed.
        """

        filename = SaveFileService.save_excel(
            parent,
            title,
            default_filename,
        )

        if filename is None:
            return False

        try:

            ExcelExporter.export(
                filename=filename,
                sheet_name=sheet_name,
                headers=headers,
                rows=rows,
            )

        except Exception as error:

            MessageService.critical(
                parent,
                "Export Failed",
                str(error),
            )

            return False

        MessageService.success(
            parent,
            "Export completed successfully.",
        )

        return True