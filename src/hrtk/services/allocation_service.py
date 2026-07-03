"""
Haryana Revenue Toolkit (HRTK)

Allocation Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.owner import Owner

from hrtk.domain.parcel import Parcel

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
    Coordinates all Partition Allocation
    business operations.

    The service manages Partition Cases,
    Allocation workflow and repository
    persistence.

    Business rules remain inside the
    domain model whenever appropriate.
    """

    def __init__(
        self,
        case_repository: PartitionCaseRepository,
        allocation_repository: (
            PartitionAllocationRepository
        ),
    ) -> None:

        self._case_repository = (
            case_repository
        )

        self._allocation_repository = (
            allocation_repository
        )

    # ---------------------------------------------------------
    # Case Management
    # ---------------------------------------------------------

    def create_case(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Create a new Partition Case.
        """

        if self.exists(
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
        Return a Partition Case.
        """

        return self._case_repository.get(
            case_id,
        )

    def save_case(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Persist changes to a
        Partition Case.
        """

        self._case_repository.update(
            case,
        )

    def delete_case(
        self,
        case_id: UUID,
    ) -> None:
        """
        Delete a Partition Case.
        """

        self._case_repository.remove(
            case_id,
        )

    def list_cases(
        self,
    ) -> list[PartitionCase]:
        """
        Return all Partition Cases.
        """

        return self._case_repository.list()

    def exists(
        self,
        case_id: UUID,
    ) -> bool:
        """
        Return True if the
        Partition Case exists.
        """

        return (
            self._case_repository.exists(
                case_id,
            )
        )
    
"""
Haryana Revenue Toolkit (HRTK)

Allocation Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.owner import Owner

from hrtk.domain.parcel import Parcel

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
    Coordinates all Partition Allocation
    business operations.

    The service manages Partition Cases,
    Allocation workflow and repository
    persistence.

    Business rules remain inside the
    domain model whenever appropriate.
    """

    def __init__(
        self,
        case_repository: PartitionCaseRepository,
        allocation_repository: (
            PartitionAllocationRepository
        ),
    ) -> None:

        self._case_repository = (
            case_repository
        )

        self._allocation_repository = (
            allocation_repository
        )

    # ---------------------------------------------------------
    # Case Management
    # ---------------------------------------------------------

    def create_case(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Create a new Partition Case.
        """

        if self.exists(
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
        Return a Partition Case.
        """

        return self._case_repository.get(
            case_id,
        )

    def save_case(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Persist changes to a
        Partition Case.
        """

        self._case_repository.update(
            case,
        )

    def delete_case(
        self,
        case_id: UUID,
    ) -> None:
        """
        Delete a Partition Case.
        """

        self._case_repository.remove(
            case_id,
        )

    def list_cases(
        self,
    ) -> list[PartitionCase]:
        """
        Return all Partition Cases.
        """

        return self._case_repository.list()

    def exists(
        self,
        case_id: UUID,
    ) -> bool:
        """
        Return True if the
        Partition Case exists.
        """

        return (
            self._case_repository.exists(
                case_id,
            )
        )
    
    # ---------------------------------------------------------
    # Query Operations
    # ---------------------------------------------------------

    def allocations(
        self,
        case_id: UUID,
    ) -> list[PartitionAllocation]:
        """
        Return all allocations belonging
        to a partition case.
        """

        case = self._validate_case(
            case_id,
        )

        return list(
            case.allocations,
        )

    def allocation_count(
        self,
        case_id: UUID,
    ) -> int:
        """
        Return the number of allocations.
        """

        return len(
            self.allocations(
                case_id,
            )
        )

    def by_owner(
        self,
        case_id: UUID,
        owner_id: UUID,
    ) -> list[PartitionAllocation]:
        """
        Return allocations belonging
        to one owner.
        """

        return [

            allocation

            for allocation in self.allocations(
                case_id,
            )

            if allocation.owner_id == owner_id

        ]

    def by_parcel(
        self,
        case_id: UUID,
        parcel,
    ) -> list[PartitionAllocation]:
        """
        Return allocations belonging
        to one parcel.
        """

        return [

            allocation

            for allocation in self.allocations(
                case_id,
            )

            if (
                allocation.parcel_number
                ==
                parcel.number
            )

        ]

    def contains(
        self,
        case_id: UUID,
        allocation_id: UUID,
    ) -> bool:
        """
        Return True if an allocation
        exists in the partition case.
        """

        case = self._validate_case(
            case_id,
        )

        return case.has_allocation(
            allocation_id,
        )
    
    # ---------------------------------------------------------
    # Calculation Operations
    # ---------------------------------------------------------

    def allocated_area(
        self,
        case_id: UUID,
    ) -> Area:
        """
        Return the total allocated area
        for the partition case.
        """

        total = Area.from_kms(
            kanal=0,
            marla=0,
            sarsai=0,
        )

        for allocation in self.allocations(
            case_id,
        ):

            total = (
                total
                + allocation.allocated_area
            )

        return total

    def owner_total(
        self,
        case_id: UUID,
        owner_id: UUID,
    ) -> Area:
        """
        Return the total area allocated
        to one owner.
        """

        total = Area.from_kms(
            kanal=0,
            marla=0,
            sarsai=0,
        )

        for allocation in self.by_owner(
            case_id,
            owner_id,
        ):

            total = (
                total
                + allocation.allocated_area
            )

        return total

    def parcel_total(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> Area:
        """
        Return the total allocated area
        of one parcel.
        """

        total = Area.from_kms(
            kanal=0,
            marla=0,
            sarsai=0,
        )

        for allocation in self.by_parcel(
            case_id,
            parcel,
        ):

            total = (
                total
                + allocation.allocated_area
            )

        return total

    def remaining_area(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> Area:
        """
        Return the remaining area
        available in a parcel.
        """

        return (
            parcel.area
            - self.parcel_total(
                case_id,
                parcel,
            )
        )

    def is_fully_allocated(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> bool:
        """
        Return True if the parcel has
        no remaining area.
        """

        return (
            self.remaining_area(
                case_id,
                parcel,
            ).total_sarsai
            == 0
        )
    
    # ---------------------------------------------------------
    # Internal Helpers
    # ---------------------------------------------------------

    def _validate_case(
        self,
        case_id: UUID,
    ) -> PartitionCase:
        """
        Return a valid Partition Case.
        """

        case = self.get_case(
            case_id,
        )

        if case is None:

            raise ValueError(
                "Partition case not found."
            )

        return case

    def _create_allocation(
        self,
        *,
        case: PartitionCase,
        owner: Owner,
        parcel: Parcel,
        area: Area,
        remarks: str,
    ) -> PartitionAllocation:
        """
        Create a new allocation.
        """

        return PartitionAllocation(

            partition_case_id=case.id,

            owner_id=owner.id,

            parcel_number=parcel.number,

            allocated_area=area,

            remarks=remarks,
        )

    def _store_allocation(
        self,
        case: PartitionCase,
        allocation: PartitionAllocation,
    ) -> None:
        """
        Store an allocation.
        """

        case.add_allocation(
            allocation,
        )

        self._allocation_repository.add(
            allocation,
        )

        self.save_case(
            case,
        )

    def _remove_allocation(
        self,
        case: PartitionCase,
        allocation_id: UUID,
    ) -> None:
        """
        Remove an allocation.
        """

        if not case.remove_allocation(
            allocation_id,
        ):

            raise ValueError(
                "Allocation not found."
            )

        self._allocation_repository.remove(
            allocation_id,
        )