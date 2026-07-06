"""
Haryana Revenue Toolkit (HRTK)

Parcel Entity.
"""

from __future__ import annotations

from dataclasses import (
    dataclass,
    field,
)

from uuid import UUID

from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)


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

    # ---------------------------------------------------------
    # Identity
    # ---------------------------------------------------------

    id: UUID

    # ---------------------------------------------------------
    # Parcel Details
    # ---------------------------------------------------------

    number: ParcelNumber

    area: Area

    remarks: str = field(
        default="",
    )

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def is_empty(
        self,
    ) -> bool:
        """
        Return True if the parcel has zero area.
        """

        return (
            self.area.total_sarsai == 0
        )

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    def display(
        self,
    ) -> str:
        """
        Human-readable description.
        """

        return (
            f"{self.number} "
            f"({self.area.display()})"
        )

    def __str__(
        self,
    ) -> str:

        return str(
            self.number,
        )

    def __repr__(
        self,
    ) -> str:

        return (
            "Parcel("
            f"id={self.id}, "
            f"number={self.number}, "
            f"area={self.area}"
            ")"
        )