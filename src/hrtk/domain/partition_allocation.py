"""
Haryana Revenue Toolkit (HRTK)

Partition Allocation Entity.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity
from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)


@dataclass(
    slots=True,
)
class PartitionAllocation(
    BaseEntity,
):
    """
    Represents allocation of land from one
    Khasra (Parcel) to one Owner during
    Partition proceedings.
    """

    partition_case_id: UUID

    owner_id: UUID

    parcel_number: ParcelNumber

    allocated_area: Area

    remarks: str = ""

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def is_empty(
        self,
    ) -> bool:
        """
        Return True if no area has been allocated.
        """

        return (
            self.allocated_area.total_sarsai
            == 0
        )

    @property
    def has_remarks(
        self,
    ) -> bool:
        """
        Return True if remarks are present.
        """

        return bool(
            self.remarks.strip()
        )

    # ---------------------------------------------------------
    # Business Methods
    # ---------------------------------------------------------

    def display_area(
        self,
    ) -> str:
        """
        Return formatted allocated area.
        """

        return (
            self.allocated_area.display()
        )

    def update_area(
        self,
        area: Area,
    ) -> None:
        """
        Update the allocated area.
        """

        self.allocated_area = area

    def update_remarks(
        self,
        remarks: str,
    ) -> None:
        """
        Update allocation remarks.
        """

        self.remarks = remarks.strip()

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    def summary(
        self,
    ) -> str:
        """
        Return a concise allocation summary.
        """

        return (
            f"Owner={self.owner_id} | "
            f"Parcel={self.parcel_number} | "
            f"Area={self.display_area()}"
        )

    def __str__(
        self,
    ) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.parcel_number} : "
            f"{self.display_area()}"
        )

    def __repr__(
        self,
    ) -> str:
        """
        Developer representation.
        """

        return (
            "PartitionAllocation("
            f"owner_id={self.owner_id}, "
            f"parcel_number={self.parcel_number}, "
            f"area={self.display_area()}"
            ")"
        )