"""
Haryana Revenue Toolkit (HRTK)

Partition Allocation Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)
from hrtk.domain.value_objects.area import (
    Area,
)
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)
from hrtk.infrastructure.sqlite.models.partition_allocation_model import (
    PartitionAllocationModel,
)


class PartitionAllocationMapper:
    """
    Maps PartitionAllocation <-> PartitionAllocationModel.
    """

    @staticmethod
    def to_model(
        allocation: PartitionAllocation,
    ) -> PartitionAllocationModel:
        """
        Convert a domain PartitionAllocation
        to a SQLite model.
        """

        return PartitionAllocationModel(
            entity_id=str(
                allocation.id,
            ),
            partition_case_id=str(
                allocation.partition_case_id,
            ),
            owner_id=str(
                allocation.owner_id,
            ),
            parcel_number=str(
                allocation.parcel_number,
            ),
            allocated_area=str(
                allocation.allocated_area,
            ),
            remarks=allocation.remarks,
        )

    @staticmethod
    def to_domain(
        model: PartitionAllocationModel,
    ) -> PartitionAllocation:
        """
        Convert a SQLite model
        to a domain PartitionAllocation.
        """

        return PartitionAllocation(
            id=UUID(
                model.entity_id,
            ),
            partition_case_id=UUID(
                model.partition_case_id,
            ),
            owner_id=UUID(
                model.owner_id,
            ),
            parcel_number=ParcelNumber(
                rectangle=int(
                    model.parcel_number.split("//")[0]
                ),
                killa=model.parcel_number.split("//")[1],
            ),
            allocated_area=Area.from_kms(
                kanal=int(
                    model.allocated_area.split("K-")[0]
                ),
                marla=int(
                    model.allocated_area.split("K-")[1].split("M-")[0]
                ),
                sarsai=int(
                    model.allocated_area.split("M-")[1].split("S")[0]
                ),
            ),
            remarks=model.remarks,
        )