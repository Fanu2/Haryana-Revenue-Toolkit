"""
Haryana Revenue Toolkit (HRTK)

Partition Case Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.partition_case import PartitionCase
from hrtk.domain.partition_status import PartitionStatus
from hrtk.infrastructure.sqlite.models.partition_case_model import (
    PartitionCaseModel,
)


class PartitionCaseMapper:
    """
    Maps PartitionCase <-> PartitionCaseModel.
    """

    @staticmethod
    def to_model(
        case: PartitionCase,
    ) -> PartitionCaseModel:
        """
        Convert a domain PartitionCase to a SQLite model.
        """

        return PartitionCaseModel(
            id=str(case.id),
            village_id=str(case.village_id),
            khewat_id=str(case.khewat_id),
            jamabandi_year=case.jamabandi_year,
            status=case.status.value,
            remarks=case.remarks,
    )

    @staticmethod
    def to_domain(
        model: PartitionCaseModel,
    ) -> PartitionCase:
        """
        Convert a SQLite model to a domain PartitionCase.
        """

        return PartitionCase(
            id=UUID(model.id),
            village_id=UUID(model.village_id),
            khewat_id=UUID(model.khewat_id),
            jamabandi_year=model.jamabandi_year,
            status=PartitionStatus(model.status),
            remarks=model.remarks,
        )
