"""
Haryana Revenue Toolkit (HRTK)

Khewat Toolbar.
"""

from __future__ import annotations

# ==========================================================
# HRTK
# ==========================================================

from hrtk.presentation.common.base_toolbar import (
    BaseToolbar,
)


class KhewatToolbar(BaseToolbar):
    """
    Toolbar for Khewat management.
    """

    def __init__(self) -> None:
        super().__init__(
            "Khewats",
            "Search khewats...",
        )