"""
Haryana Revenue Toolkit (HRTK)

SQLite Partition Allocation Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.partition_allocation import PartitionAllocation
from hrtk.infrastructure.sqlite.mappers.partition_allocation_mapper import (
    PartitionAllocationMapper,
)
from hrtk.infrastructure.sqlite.models.partition_allocation_model import (
    PartitionAllocationModel,
)
from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)
from hrtk.repositories.partition_allocation_repository import (
    PartitionAllocationRepository,
)


class SQLitePartitionAllocationRepository(
    PartitionAllocationRepository,
):
    """
    SQLite implementation of
    PartitionAllocationRepository.
    """

    def add(
        self,
        allocation: PartitionAllocation,
    ) -> None:

        with SessionFactory() as session:

            session.add(
                PartitionAllocationMapper.to_model(
                    allocation
                )
            )

            session.commit()

    def update(
        self,
        allocation: PartitionAllocation,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    PartitionAllocationModel
                )
                .filter_by(
                    id=str(
                        allocation.id
                    ),
                )
                .first()
            )

            if model is None:
                raise ValueError(
                    "Partition allocation not found."
                )

            model.partition_case_id = str(
                allocation.partition_case_id
            )

            model.owner_id = str(
                allocation.owner_id
            )

            model.parcel_number = str(
                allocation.parcel_number
            )

            model.allocated_area = str(
                allocation.allocated_area
            )

            model.remarks = (
                allocation.remarks
            )

            session.commit()

    def remove(
        self,
        allocation_id: UUID,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    PartitionAllocationModel
                )
                .filter_by(
                    id=str(
                        allocation_id
                    ),
                )
                .first()
            )

            if model is None:
                return

            session.delete(model)

            session.commit()

    def get(
        self,
        allocation_id: UUID,
    ) -> PartitionAllocation | None:

        with SessionFactory() as session:

            model = (
                session.query(
                    PartitionAllocationModel
                )
                .filter_by(
                    id=str(
                        allocation_id
                    ),
                )
                .first()
            )

            if model is None:
                return None

            return (
                PartitionAllocationMapper
                .to_domain(model)
            )

    def list(
        self,
    ) -> list[PartitionAllocation]:

        with SessionFactory() as session:

            models = (
                session.query(
                    PartitionAllocationModel
                ).all()
            )

            return [
                PartitionAllocationMapper
                .to_domain(model)
                for model in models
            ]

    def all(
        self,
    ) -> list[PartitionAllocation]:
        """
        Compatibility method.
        """

        return self.list()

    def find_by_partition_case(
        self,
        partition_case_id: UUID,
    ) -> list[PartitionAllocation]:

        with SessionFactory() as session:

            models = (
                session.query(
                    PartitionAllocationModel
                )
                .filter_by(
                    partition_case_id=str(
                        partition_case_id,
                    ),
                )
                .all()
            )

            return [
                PartitionAllocationMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def exists(
        self,
        allocation_id: UUID,
    ) -> bool:

        return (
            self.get(
                allocation_id
            )
            is not None
        )
