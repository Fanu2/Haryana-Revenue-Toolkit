"""
Haryana Revenue Toolkit (HRTK)

Partition Allocation Repository Interface.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)


class PartitionAllocationRepository(
    Protocol,
):
    """
    Repository contract for
    PartitionAllocation.
    """

    def add(
        self,
        allocation: PartitionAllocation,
    ) -> None:
        ...

    def update(
        self,
        allocation: PartitionAllocation,
    ) -> None:
        ...

    def remove(
        self,
        allocation_id: UUID,
    ) -> None:
        ...

    def get(
        self,
        allocation_id: UUID,
    ) -> PartitionAllocation | None:
        ...

    def list(
        self,
    ) -> list[PartitionAllocation]:
        ...

    def exists(
        self,
        allocation_id: UUID,
    ) -> bool:
        ...