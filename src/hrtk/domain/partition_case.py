"""
Haryana Revenue Toolkit (HRTK)

Partition Case Aggregate Root.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity

from hrtk.domain.partition_status import (
    PartitionStatus,
)

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)


@dataclass(
    slots=True,
)
class PartitionCase(
    BaseEntity,
):
    """
    Represents one Partition proceeding.
    """

    village_id: UUID

    khewat_id: UUID

    jamabandi_year: str

    status: PartitionStatus = (
        PartitionStatus.DRAFT
    )

    allocations: list[
        PartitionAllocation
    ] = field(
        default_factory=list,
    )

    remarks: str = ""

    # ---------------------------------------------------------
    # Allocation Management
    # ---------------------------------------------------------

    def add_allocation(
        self,
        allocation: PartitionAllocation,
    ) -> None:
        """
        Add an allocation to this partition case.
        """

        if (
            allocation.partition_case_id
            != self.id
        ):
            raise ValueError(
                "Allocation does not belong to this Partition Case."
            )

        self.allocations.append(
            allocation,
        )

    def remove_allocation(
        self,
        allocation_id: UUID,
    ) -> bool:
        """
        Remove an allocation by its identifier.

        Returns True if removed.
        """

        for index, allocation in enumerate(
            self.allocations
        ):

            if allocation.id == allocation_id:

                del self.allocations[
                    index
                ]

                return True

        return False

    def clear_allocations(
        self,
    ) -> None:
        """
        Remove all allocations.
        """

        self.allocations.clear()

    @property
    def allocation_count(
        self,
    ) -> int:
        """
        Return the number of allocations.
        """

        return len(
            self.allocations
        )
    
    # ---------------------------------------------------------
    # Status Management
    # ---------------------------------------------------------

    def validate(
        self,
    ) -> None:
        """
        Mark the partition case as validated.
        """

        if self.status == PartitionStatus.COMPLETED:

            raise ValueError(
                "Completed partition cannot be validated again."
            )

        if self.status == PartitionStatus.CANCELLED:

            raise ValueError(
                "Cancelled partition cannot be validated."
            )

        self.status = (
            PartitionStatus.VALIDATED
        )

    def complete(
        self,
    ) -> None:
        """
        Mark the partition case as completed.
        """

        if self.status != (
            PartitionStatus.VALIDATED
        ):
            raise ValueError(
                "Partition must be validated before completion."
            )

        self.status = (
            PartitionStatus.COMPLETED
        )

    def cancel(
        self,
    ) -> None:
        """
        Cancel the partition case.
        """

        if self.status == (
            PartitionStatus.COMPLETED
        ):
            raise ValueError(
                "Completed partition cannot be cancelled."
            )

        self.status = (
            PartitionStatus.CANCELLED
        )

    def reopen(
        self,
    ) -> None:
        """
        Reopen a cancelled partition.
        """

        if self.status != (
            PartitionStatus.CANCELLED
        ):
            raise ValueError(
                "Only cancelled partitions can be reopened."
            )

        self.status = (
            PartitionStatus.DRAFT
        )

    # ---------------------------------------------------------
    # State
    # ---------------------------------------------------------

    @property
    def is_draft(
        self,
    ) -> bool:
        """
        Return True if the partition is in Draft state.
        """

        return (
            self.status
            == PartitionStatus.DRAFT
        )

    @property
    def is_validated(
        self,
    ) -> bool:
        """
        Return True if the partition is validated.
        """

        return (
            self.status
            == PartitionStatus.VALIDATED
        )

    @property
    def is_completed(
        self,
    ) -> bool:
        """
        Return True if the partition is completed.
        """

        return (
            self.status
            == PartitionStatus.COMPLETED
        )

    @property
    def is_cancelled(
        self,
    ) -> bool:
        """
        Return True if the partition is cancelled.
        """

        return (
            self.status
            == PartitionStatus.CANCELLED
        )

    @property
    def has_allocations(
        self,
    ) -> bool:
        """
        Return True if allocations exist.
        """

        return bool(
            self.allocations
        )

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    def summary(
        self,
    ) -> str:
        """
        Return a concise summary.
        """

        return (
            f"Khewat={self.khewat_id} | "
            f"Status={self.status.display_name} | "
            f"Allocations={self.allocation_count}"
        )

    def __str__(
        self,
    ) -> str:
        """
        Human-readable representation.
        """

        return (
            f"Partition "
            f"({self.status.display_name})"
        )

    def __repr__(
        self,
    ) -> str:
        """
        Developer representation.
        """

        return (
            "PartitionCase("
            f"khewat_id={self.khewat_id}, "
            f"status={self.status.display_name}, "
            f"allocations={self.allocation_count}"
            ")"
        )
    
