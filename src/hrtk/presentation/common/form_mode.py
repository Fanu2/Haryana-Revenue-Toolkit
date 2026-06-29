"""
Haryana Revenue Toolkit (HRTK)

Form modes.
"""

from __future__ import annotations

from enum import Enum, auto


class FormMode(Enum):
    """
    Dialog operating modes.
    """

    CREATE = auto()
    EDIT = auto()