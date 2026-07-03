"""
Haryana Revenue Toolkit (HRTK)

Partition Case Repository Interface.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from hrtk.domain.partition_case import (
    PartitionCase,
)


class PartitionCaseRepository(
    Protocol,
):
    """
    Repository contract for PartitionCase.
    """

    def add(
        self,
        case: PartitionCase,
    ) -> None:
        ...

    def update(
        self,
        case: PartitionCase,
    ) -> None:
        ...

    def remove(
        self,
        case_id: UUID,
    ) -> None:
        ...

    def get(
        self,
        case_id: UUID,
    ) -> PartitionCase | None:
        ...

    def list(
        self,
    ) -> list[PartitionCase]:
        ...

    def exists(
        self,
        case_id: UUID,
    ) -> bool:
        ...