"""
Haryana Revenue Toolkit (HRTK)

SQLite Partition Case Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.partition_case import PartitionCase
from hrtk.infrastructure.sqlite.mappers.partition_case_mapper import (
    PartitionCaseMapper,
)
from hrtk.infrastructure.sqlite.models.partition_case_model import (
    PartitionCaseModel,
)
from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)
from hrtk.repositories.partition_case_repository import (
    PartitionCaseRepository,
)


class SQLitePartitionCaseRepository(
    PartitionCaseRepository,
):
    """
    SQLite implementation of PartitionCaseRepository.
    """

    def add(
        self,
        case: PartitionCase,
    ) -> None:

        with SessionFactory() as session:

            session.add(
                PartitionCaseMapper.to_model(case)
            )

            session.commit()

    def update(
        self,
        case: PartitionCase,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    PartitionCaseModel
                )
                .filter_by(
                    entity_id=str(case.id),
                )
                .first()
            )

            if model is None:
                raise ValueError(
                    "Partition case not found."
                )

            model.village_id = str(
                case.village_id
            )

            model.khewat_id = str(
                case.khewat_id
            )

            model.jamabandi_year = (
                case.jamabandi_year
            )

            model.status = (
                case.status.value
            )

            model.remarks = (
                case.remarks
            )

            session.commit()

    def remove(
        self,
        case_id: UUID,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    PartitionCaseModel
                )
                .filter_by(
                    entity_id=str(case_id),
                )
                .first()
            )

            if model is None:
                return

            session.delete(model)

            session.commit()

    def get(
        self,
        case_id: UUID,
    ) -> PartitionCase | None:

        with SessionFactory() as session:

            model = (
                session.query(
                    PartitionCaseModel
                )
                .filter_by(
                    entity_id=str(case_id),
                )
                .first()
            )

            if model is None:
                return None

            return (
                PartitionCaseMapper
                .to_domain(model)
            )

    def list(
        self,
    ) -> list[PartitionCase]:

        with SessionFactory() as session:

            models = (
                session.query(
                    PartitionCaseModel
                )
                .order_by(
                    PartitionCaseModel.jamabandi_year,
                )
                .all()
            )

            return [
                PartitionCaseMapper.to_domain(model)
                for model in models
            ]

    def all(
        self,
    ) -> list[PartitionCase]:
        """
        Compatibility method for BaseService.
        """

        return self.list()


    def find_by_record(
        self,
        village_id,
        khewat_id,
        jamabandi_year,
    ) -> PartitionCase | None:

        with SessionFactory() as session:

            model = (
                session.query(
                    PartitionCaseModel
                )
                .filter_by(
                    village_id=str(village_id),
                    khewat_id=str(khewat_id),
                    jamabandi_year=jamabandi_year,
                )
                .first()
            )

            if model is None:
                return None

            return (
                PartitionCaseMapper.to_domain(
                    model,
                )
            )

    def exists(
        self,
        case_id: UUID,
    ) -> bool:

        return (
            self.get(case_id)
            is not None
        )