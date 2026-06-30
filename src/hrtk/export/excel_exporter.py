"""
Haryana Revenue Toolkit (HRTK)

Generic Excel Exporter.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from hrtk.export.excel_styles import ExcelStyles


class ExcelExporter:
    """
    Generic Excel exporter.
    """

    @staticmethod
    def export(
        filename: str | Path,
        sheet_name: str,
        headers: list[str],
        rows: Iterable[Iterable],
    ) -> None:
        """
        Export tabular data to an Excel workbook.
        """

        workbook = Workbook()

        worksheet = workbook.active
        assert worksheet is not None

        worksheet.title = sheet_name

        ExcelExporter._write_headers(
            worksheet,
            headers,
        )

        ExcelExporter._write_rows(
            worksheet,
            rows,
        )

        ExcelExporter._autosize_columns(
            worksheet,
        )

        worksheet.freeze_panes = "A2"

        workbook.save(
            filename,
        )

    # ---------------------------------------------------------
    # Private helpers
    # ---------------------------------------------------------

    @staticmethod
    def _write_headers(
        worksheet: Worksheet,
        headers: list[str],
    ) -> None:

        worksheet.append(
            headers,
        )

        for cell in worksheet[1]:

            cell.font = ExcelStyles.HEADER_FONT

            cell.fill = ExcelStyles.HEADER_FILL

            cell.alignment = ExcelStyles.HEADER_ALIGNMENT

            cell.border = ExcelStyles.THIN_BORDER

    @staticmethod
    def _write_rows(
        worksheet: Worksheet,
        rows: Iterable[Iterable],
    ) -> None:

        for row in rows:

            worksheet.append(
                list(row),
            )

        for row in worksheet.iter_rows(
            min_row=2,
        ):

            for cell in row:

                cell.alignment = ExcelStyles.CELL_ALIGNMENT

                cell.border = ExcelStyles.THIN_BORDER

    @staticmethod
    def _autosize_columns(
        worksheet: Worksheet,
    ) -> None:

        for column in worksheet.columns:

            maximum = 0

            letter = column[0].column_letter

            for cell in column:

                value = str(
                    cell.value
                    if cell.value is not None
                    else ""
                )

                maximum = max(
                    maximum,
                    len(value),
                )

            worksheet.column_dimensions[
                letter
            ].width = maximum + 3