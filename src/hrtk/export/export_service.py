"""
Haryana Revenue Toolkit (HRTK)

Export Service.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from hrtk.export.excel_exporter import ExcelExporter


class ExportService:
    """
    High-level export service.
    """

    @staticmethod
    def export_excel(
        filename: str | Path,
        sheet_name: str,
        headers: list[str],
        rows: Iterable[Iterable],
    ) -> None:
        """
        Export tabular data to Excel.
        """

        ExcelExporter.export(
            filename=filename,
            sheet_name=sheet_name,
            headers=headers,
            rows=rows,
        )