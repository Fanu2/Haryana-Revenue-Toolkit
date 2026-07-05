"""
Haryana Revenue Toolkit (HRTK)

Partition application service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.partition_case import PartitionCase
from hrtk.repositories.partition_case_repository import (
    PartitionCaseRepository,
)
from hrtk.services.base_service import BaseService


class PartitionService(
    BaseService[PartitionCase],
):
    """
    Application service for PartitionCase entities.
    """

    def __init__(
        self,
        repository: PartitionCaseRepository,
    ) -> None:

        super().__init__(repository)

    @property
    def repository(
        self,
    ) -> PartitionCaseRepository:
        """
        Return the partition repository.
        """

        return super().repository

    def register(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Register a new partition case.
        """

        self.repository.add(case)

    def update(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Persist changes.
        """

        self.repository.update(case)

    def cancel(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Cancel a partition case.
        """

        case.cancel()

        self.repository.update(case)

    def validate(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Validate a partition case.
        """

        case.validate()

        self.repository.update(case)

    def complete(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Complete a partition case.
        """

        case.complete()

        self.repository.update(case)

    def reopen(
        self,
        case: PartitionCase,
    ) -> None:
        """
        Reopen a cancelled partition case.
        """

        case.reopen()

        self.repository.update(case)

    def find_by_record(
        self,
        village_id,
        khewat_id,
        jamabandi_year,
    ) -> PartitionCase | None:
        """
        Find a partition case by
        village, khewat and year.
        """

        return (
            self.repository.find_by_record(
                village_id,
                khewat_id,
                jamabandi_year,
            )
        )

    def find(
        self,
        case_id: UUID,
    ) -> PartitionCase | None:
        """
        Find a partition case by UUID.
        """

        return self.repository.get(case_id)