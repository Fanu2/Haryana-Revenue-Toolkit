"""
Haryana Revenue Toolkit (HRTK)

Reusable Excel styles.
"""

from __future__ import annotations

from openpyxl.styles import (
    Alignment,
    Border,
    Font,
    PatternFill,
    Side,
)


class ExcelStyles:
    """
    Shared styles for Excel exports.
    """

    HEADER_FONT = Font(
        bold=True,
        color="FFFFFF",
    )

    HEADER_FILL = PatternFill(
        fill_type="solid",
        fgColor="1F4E78",
    )

    HEADER_ALIGNMENT = Alignment(
        horizontal="center",
        vertical="center",
    )

    THIN_BORDER = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )

    CELL_ALIGNMENT = Alignment(
        vertical="center",
    )