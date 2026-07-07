"""
Haryana Revenue Toolkit (HRTK)

Partition Allocation Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)

from hrtk.repositories.partition_allocation_repository import (
    PartitionAllocationRepository,
)


class PartitionAllocationService:
    """
    Application service for
    Partition Allocation entities.
    """

    def __init__(
        self,
        repository: PartitionAllocationRepository,
    ) -> None:

        self._repository = repository

    @property
    def repository(
        self,
    ) -> PartitionAllocationRepository:
        """
        Return the repository.
        """

        return self._repository

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def add(
        self,
        allocation: PartitionAllocation,
    ) -> None:
        """
        Add a Partition Allocation.
        """

        self.repository.add(
            allocation,
        )

    def update(
        self,
        allocation: PartitionAllocation,
    ) -> None:
        """
        Update a Partition Allocation.
        """

        self.repository.update(
            allocation,
        )

    def remove(
        self,
        allocation_id: UUID,
    ) -> None:
        """
        Remove a Partition Allocation.
        """

        self.repository.remove(
            allocation_id,
        )

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def get(
        self,
        allocation_id: UUID,
    ) -> PartitionAllocation | None:
        """
        Return an allocation by id.
        """

        return self.repository.get(
            allocation_id,
        )

    def list(
        self,
    ) -> list[
        PartitionAllocation
    ]:
        """
        Return all allocations.
        """

        return self.repository.list()

    def exists(
        self,
        allocation_id: UUID,
    ) -> bool:
        """
        Determine whether an allocation exists.
        """

        return self.repository.exists(
            allocation_id,
        )

    def by_partition_case(
        self,
        partition_case_id: UUID,
    ) -> list[
        PartitionAllocation
    ]:
        """
        Return all allocations for a
        Partition Case.
        """

        return (
            self.repository.find_by_partition_case(
                partition_case_id,
            )
        )