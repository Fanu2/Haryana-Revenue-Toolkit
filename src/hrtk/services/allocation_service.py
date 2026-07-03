"""
Haryana Revenue Toolkit (HRTK)

Allocation Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.partition_case import (
    PartitionCase,
)

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)

from hrtk.domain.value_objects.area import (
    Area,
)

from hrtk.repositories.partition_case_repository import (
    PartitionCaseRepository,
)

from hrtk.repositories.partition_allocation_repository import (
    PartitionAllocationRepository,
)
class AllocationService:
    """
    Application service responsible for
    Partition Allocation operations.
    """

    def __init__(
        self,
        case_repository: PartitionCaseRepository,
        allocation_repository: PartitionAllocationRepository,
    ) -> None:

        self._case_repository = (
            case_repository
        )

        self._allocation_repository = (
            allocation_repository
        )

    # ---------------------------------------------------------
    # Partition Cases
    # ---------------------------------------------------------

    def create_case(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Create a new partition case.
        """

        if self._case_repository.exists(
            case.id,
        ):
            raise ValueError(
                "Partition case already exists."
            )

        self._case_repository.add(
            case,
        )

    def get_case(
        self,
        case_id: UUID,
    ) -> PartitionCase | None:
        """
        Return a partition case.
        """

        return self._case_repository.get(
            case_id,
        )

    def save_case(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Update an existing partition case.
        """

        self._case_repository.update(
            case,
        )

    def delete_case(
        self,
        case_id: UUID,
    ) -> None:
        """
        Delete a partition case.
        """

        self._case_repository.remove(
            case_id,
        )

    def list_cases(
        self,
    ) -> list[PartitionCase]:
        """
        Return all partition cases.
        """

        return self._case_repository.list()

    def exists(
        self,
        case_id: UUID,
    ) -> bool:
        """
        Determine whether a partition case exists.
        """

        return self._case_repository.exists(
            case_id,
        )
    
    # ---------------------------------------------------------
    # Allocation Management
    # ---------------------------------------------------------

    def add_allocation(
        self,
        case_id: UUID,
        allocation: PartitionAllocation,
    ) -> None:
        """
        Add an allocation to a partition case.
        """

        case = self.get_case(
            case_id,
        )

        if case is None:

            raise ValueError(
                "Partition case not found."
            )

        case.add_allocation(
            allocation,
        )

        self._allocation_repository.add(
            allocation,
        )

        self.save_case(
            case,
        )

    def remove_allocation(
        self,
        case_id: UUID,
        allocation_id: UUID,
    ) -> None:
        """
        Remove an allocation from a partition case.
        """

        case = self.get_case(
            case_id,
        )

        if case is None:

            raise ValueError(
                "Partition case not found."
            )

        removed = case.remove_allocation(
            allocation_id,
        )

        if not removed:

            raise ValueError(
                "Allocation not found."
            )

        self._allocation_repository.remove(
            allocation_id,
        )

        self.save_case(
            case,
        )

    def allocations(
        self,
        case_id: UUID,
    ) -> list[PartitionAllocation]:
        """
        Return all allocations belonging
        to a partition case.
        """

        case = self.get_case(
            case_id,
        )

        if case is None:

            return []

        return case.allocations

    def allocation_count(
        self,
        case_id: UUID,
    ) -> int:
        """
        Return number of allocations.
        """

        case = self.get_case(
            case_id,
        )

        if case is None:

            return 0

        return case.allocation_count
    
    # ---------------------------------------------------------
    # Business Operations
    # ---------------------------------------------------------

    def allocate_area(
        self,
        case_id: UUID,
        owner_id: UUID,
        parcel_id: UUID,
        area: Area,
        remarks: str = "",
    ) -> PartitionAllocation:
        """
        Allocate an area from a parcel
        to an owner.
        """

        case = self.get_case(
            case_id,
        )

        if case is None:

            raise ValueError(
                "Partition case not found."
            )

        allocation = PartitionAllocation(
            partition_case_id=case.id,
            owner_id=owner_id,
            parcel_id=parcel_id,
            allocated_area=area,
            remarks=remarks,
        )

        case.add_allocation(
            allocation,
        )

        self._allocation_repository.add(
            allocation,
        )

        self.save_case(
            case,
        )

        return allocation
    
    def allocate_entire_parcel(
        self,
        case_id: UUID,
        owner_id: UUID,
        parcel,
        remarks: str = "",
    ) -> PartitionAllocation:
        """
        Allocate an entire parcel.
        """

        return self.allocate_area(
            case_id=case_id,
            owner_id=owner_id,
            parcel_id=parcel.id,
            area=parcel.area,
            remarks=remarks,
        )
    
