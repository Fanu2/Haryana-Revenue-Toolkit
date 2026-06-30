"""
Haryana Revenue Toolkit (HRTK)

Village Toolbar.
"""

from __future__ import annotations

# ==========================================================
# HRTK
# ==========================================================

from hrtk.presentation.common.base_toolbar import (
    BaseToolbar,
)


class VillageToolbar(BaseToolbar):
    """
    Toolbar for Village management.
    """

    def __init__(self) -> None:
        super().__init__(
            "Villages",
            "Search villages...",
        )