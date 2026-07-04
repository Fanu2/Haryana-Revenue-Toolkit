"""
Haryana Revenue Toolkit (HRTK)

Calculation Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.owner import Owner

from hrtk.domain.parcel import Parcel

from hrtk.domain.partition_case import (
    PartitionCase,
)

from hrtk.domain.value_objects.area import (
    Area,
)

from hrtk.services.allocation_service import (
    AllocationService,
)


class CalculationService:
    """
    Performs all mathematical
    calculations for Partition
    proceedings.

    The service contains no
    persistence or presentation
    logic.
    """

    def __init__(
        self,
        allocation_service: AllocationService,
    ) -> None:

        self._allocation_service = (
            allocation_service
        )

    # ---------------------------------------------------------
    # Owner Calculations
    # ---------------------------------------------------------
    def owner_allocated_area(
        self,
        case_id: UUID,
        owner: Owner,
    ) -> Area:
        """
        Return the total area allocated
        to an owner.
        """

        return (
            self._allocation_service.owner_total(
                case_id,
                owner.id,
            )
        )

    def owner_allocation_count(
        self,
        case_id: UUID,
        owner: Owner,
    ) -> int:
        """
        Return the number of
        allocations for an owner.
        """

        return len(
            self._allocation_service.by_owner(
                case_id,
                owner.id,
            )
        )

    def owner_has_allocation(
        self,
        case_id: UUID,
        owner: Owner,
    ) -> bool:
        """
        Return True if the owner
        has allocations.
        """

        return (
            self.owner_allocation_count(
                case_id,
                owner,
            )
            > 0
        )
    
    # ---------------------------------------------------------
    # Parcel Calculations
    # ---------------------------------------------------------

    def parcel_allocated_area(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> Area:
        """
        Return allocated area
        of a parcel.
        """

        return (
            self._allocation_service.parcel_total(
                case_id,
                parcel,
            )
        )

    def parcel_remaining_area(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> Area:
        """
        Return remaining area
        of a parcel.
        """

        return (
            self._allocation_service.remaining_area(
                case_id,
                parcel,
            )
        )

    def parcel_is_complete(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> bool:
        """
        Return True if the parcel
        has been fully allocated.
        """

        return (
            self._allocation_service.is_fully_allocated(
                case_id,
                parcel,
            )
        )
    
    # ---------------------------------------------------------
    # Overall Calculations
    # ---------------------------------------------------------

    def total_allocated_area(
        self,
        case_id: UUID,
    ) -> Area:
        """
        Return total allocated area
        of the partition.
        """

        return (
            self._allocation_service.allocated_area(
                case_id,
            )
        )

    def total_allocations(
        self,
        case_id: UUID,
    ) -> int:
        """
        Return total number
        of allocations.
        """

        return (
            self._allocation_service.allocation_count(
                case_id,
            )
        )

    def has_allocations(
        self,
        case_id: UUID,
    ) -> bool:
        """
        Return True if
        allocations exist.
        """

        return (
            self.total_allocations(
                case_id,
            )
            > 0
        )
    
    # ---------------------------------------------------------
    # Helper Methods
    # ---------------------------------------------------------

    def case(
        self,
        case_id: UUID,
    ) -> PartitionCase:
        """
        Return the Partition Case.
        """

        case = (
            self._allocation_service.get_case(
                case_id,
            )
        )

        if case is None:

            raise ValueError(
                "Partition case not found."
            )

        return case

