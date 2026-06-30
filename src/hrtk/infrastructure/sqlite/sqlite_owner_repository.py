"""
Haryana Revenue Toolkit (HRTK)

SQLite Owner Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.owner import Owner
from hrtk.infrastructure.sqlite.mappers.owner_mapper import (
    OwnerMapper,
)
from hrtk.infrastructure.sqlite.models.owner_model import (
    OwnerModel,
)
from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)
from hrtk.repositories.owner_repository import (
    OwnerRepository,
)


class SQLiteOwnerRepository(OwnerRepository):
    """
    SQLite implementation of OwnerRepository.
    """

    def add(
        self,
        owner: Owner,
    ) -> None:

        with SessionFactory() as session:

            session.add(
                OwnerMapper.to_model(owner)
            )

            session.commit()

    def update(
        self,
        owner: Owner,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(OwnerModel)
                .filter_by(
                    owner_code=owner.owner_code,
                )
                .first()
            )

            if model is None:
                raise ValueError(
                    f"Owner '{owner.owner_code}' not found."
                )

            model.village_id = str(owner.village_id)
            model.owner_name = owner.owner_name
            model.father_name = owner.father_name
            model.address = owner.address
            model.mobile = owner.mobile
            model.remarks = owner.remarks
            model.active = owner.active

            session.commit()

    def remove(
        self,
        owner: Owner,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(OwnerModel)
                .filter_by(
                    owner_code=owner.owner_code,
                )
                .first()
            )

            if model is None:
                return

            session.delete(model)

            session.commit()

    def get(
        self,
        owner_code: str,
    ) -> Owner | None:

        with SessionFactory() as session:

            model = (
                session.query(OwnerModel)
                .filter_by(
                    owner_code=owner_code,
                )
                .first()
            )

            if model is None:
                return None

            return OwnerMapper.to_domain(model)

    def list(
        self,
    ) -> list[Owner]:

        with SessionFactory() as session:

            models = (
                session.query(OwnerModel)
                .order_by(
                    OwnerModel.owner_name,
                )
                .all()
            )

            return [
                OwnerMapper.to_domain(model)
                for model in models
            ]

    def exists(
        self,
        owner_code: str,
    ) -> bool:

        return (
            self.get(owner_code)
            is not None
        )

    def find_by_code(
        self,
        owner_code: str,
    ) -> Owner | None:
        """
        Find an owner by owner code.
        """

        return self.get(owner_code)

    def find_by_village(
        self,
        village_id: UUID,
    ) -> list[Owner]:
        """
        Return all owners belonging to a village.
        """

        with SessionFactory() as session:

            models = (
                session.query(OwnerModel)
                .filter_by(
                    village_id=str(village_id),
                )
                .order_by(
                    OwnerModel.owner_name,
                )
                .all()
            )

            return [
                OwnerMapper.to_domain(model)
                for model in models
            ]