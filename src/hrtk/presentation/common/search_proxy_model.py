"""
Haryana Revenue Toolkit (HRTK)

Search Proxy Model.
"""

from __future__ import annotations

# ==========================================================
# Qt
# ==========================================================

from PySide6.QtCore import (
    QRegularExpression,
    Qt,
    QSortFilterProxyModel,
)


class SearchProxyModel(QSortFilterProxyModel):
    """
    Generic search proxy model for HRTK.
    """

    def __init__(self) -> None:
        super().__init__()

        #
        # Search every column.
        #
        self.setFilterKeyColumn(-1)

        #
        # Case-insensitive searching.
        #
        self.setFilterCaseSensitivity(
            Qt.CaseInsensitive,
        )

        #
        # Case-insensitive sorting.
        #
        self.setSortCaseSensitivity(
            Qt.CaseInsensitive,
        )

        self.setDynamicSortFilter(True)

    def set_search_text(
        self,
        text: str,
    ) -> None:
        """
        Apply search text.
        """

        if not text.strip():

            self.setFilterRegularExpression(
                QRegularExpression(),
            )

            return

        expression = QRegularExpression(
            QRegularExpression.escape(
                text,
            ),
            QRegularExpression.CaseInsensitiveOption,
        )

        self.setFilterRegularExpression(
            expression,
        )