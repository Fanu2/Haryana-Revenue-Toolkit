"""
Haryana Revenue Toolkit (HRTK)

Parcel Status.
"""

from __future__ import annotations

from enum import Enum


class ParcelStatus(str, Enum):
    """
    Lifecycle states of a parcel.
    """

    ACTIVE = "Active"

    HISTORICAL = "Historical"

    MERGED = "Merged"

    CANCELLED = "Cancelled"

    CORRECTED = "Corrected"

    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return self.value