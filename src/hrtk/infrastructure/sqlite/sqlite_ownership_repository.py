"""
Haryana Revenue Toolkit (HRTK)

SQLite Ownership Repository.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select

from hrtk.domain.ownership import Ownership
from hrtk.infrastructure.common.unit_of_work import (
    unit_of_work,
)
from hrtk.infrastructure.sqlite.mappers.ownership_mapper import (
    OwnershipMapper,
)
from hrtk.infrastructure.sqlite.models.ownership_model import (
    OwnershipModel,
)
from hrtk.repositories.ownership_repository import (
    OwnershipRepository,
)


class SQLiteOwnershipRepository(
    OwnershipRepository,
):

    def add(
        self,
        ownership: Ownership,
    ) -> None:

        with unit_of_work() as session:

            session.add(
                OwnershipMapper.to_model(
                    ownership,
                )
            )

    def update(
        self,
        ownership: Ownership,
    ) -> None:

        raise NotImplementedError

    def remove(
        self,
        ownership_id: UUID,
    ) -> None:

        raise NotImplementedError

    def get(
        self,
        ownership_id: UUID,
    ) -> Ownership | None:

        with unit_of_work() as session:

            model = session.get(
                OwnershipModel,
                str(ownership_id),
            )

            if model is None:
                return None

            return OwnershipMapper.to_domain(
                model,
            )

    def list(
        self,
    ) -> list[Ownership]:

        with unit_of_work() as session:

            models = (
                session.scalars(
                    select(
                        OwnershipModel,
                    )
                ).all()
            )

            return [
                OwnershipMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def find_by_owner(
        self,
        owner_id: UUID,
    ) -> list[Ownership]:

        with unit_of_work() as session:

            models = (
                session.scalars(
                    select(
                        OwnershipModel,
                    ).where(
                        OwnershipModel.owner_id
                        == str(owner_id)
                    )
                ).all()
            )

            return [
                OwnershipMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def find_by_khewat(
        self,
        khewat_id: UUID,
    ) -> list[Ownership]:

        with unit_of_work() as session:

            models = (
                session.scalars(
                    select(
                        OwnershipModel,
                    ).where(
                        OwnershipModel.khewat_id
                        == str(khewat_id)
                    )
                ).all()
            )

            return [
                OwnershipMapper.to_domain(
                    model,
                )
                for model in models
            ]