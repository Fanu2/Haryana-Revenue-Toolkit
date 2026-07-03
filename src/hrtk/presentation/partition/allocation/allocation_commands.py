"""
Haryana Revenue Toolkit (HRTK)

Allocation Commands.
"""

from __future__ import annotations

from enum import Enum


class AllocationCommand(
    Enum,
):
    """
    Supported Allocation commands.
    """

    ALLOCATE = "allocate"

    UNDO = "undo"

    CLEAR = "clear"

    REFRESH = "refresh"