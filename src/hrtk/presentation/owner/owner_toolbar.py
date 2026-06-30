"""
Haryana Revenue Toolkit (HRTK)

Owner Toolbar.
"""

from __future__ import annotations

# ==========================================================
# HRTK
# ==========================================================

from hrtk.presentation.common.base_toolbar import (
    BaseToolbar,
)


class OwnerToolbar(BaseToolbar):
    """
    Toolbar for Owner management.
    """

    def __init__(self) -> None:
        super().__init__(
            "Owners",
            "Search owners...",
        )