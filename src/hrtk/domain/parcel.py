"""
Haryana Revenue Toolkit (HRTK)

Parcel Entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import ParcelNumber


@dataclass(
    slots=True,
)
class Parcel:
    """
    Represents a physical parcel of land.

    A Parcel represents land only.

    Ownership, Khewat and Mutation
    relationships are maintained separately.
    """

    number: ParcelNumber

    area: Area

    remarks: str = field(
        default="",
    )

    @property
    def is_empty(self) -> bool:
        """
        Return True if the parcel has zero area.
        """

        return (
            self.area.total_sarsai == 0
        )

    def display(self) -> str:
        """
        Human-readable description.
        """

        return (
            f"{self.number} "
            f"({self.area.display()})"
        )

    def __str__(self) -> str:
        """
        Compact representation.
        """

        return (
            f"{self.number}"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """

        return (
            "Parcel("
            f"{self.number}, "
            f"{self.area}"
            ")"
        )