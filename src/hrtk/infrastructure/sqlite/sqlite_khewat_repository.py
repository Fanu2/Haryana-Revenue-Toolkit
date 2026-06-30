"""
Haryana Revenue Toolkit (HRTK)

SQLite Khewat Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.khewat import Khewat
from hrtk.infrastructure.sqlite.mappers.khewat_mapper import (
    KhewatMapper,
)
from hrtk.infrastructure.sqlite.models.khewat_model import (
    KhewatModel,
)
from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)
from hrtk.repositories.khewat_repository import (
    KhewatRepository,
)


class SQLiteKhewatRepository(KhewatRepository):
    """
    SQLite implementation of KhewatRepository.
    """

    def add(
        self,
        khewat: Khewat,
    ) -> None:

        with SessionFactory() as session:

            session.add(
                KhewatMapper.to_model(
                    khewat,
                )
            )

            session.commit()

    def update(
        self,
        khewat: Khewat,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(KhewatModel)
                .filter_by(
                    village_id=str(khewat.village_id),
                    khewat_no=khewat.khewat_no,
                )
                .first()
            )

            if model is None:
                raise ValueError(
                    f"Khewat '{khewat.khewat_no}' not found."
                )

            model.old_khewat_no = (
                khewat.old_khewat_no
            )

            model.jamabandi_year = (
                khewat.jamabandi_year
            )

            model.remarks = (
                khewat.remarks
            )

            model.active = (
                khewat.active
            )

            session.commit()

    def remove(
        self,
        entity_id,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(KhewatModel)
                .filter_by(id=entity_id)
                .first()
            )

            if model is None:
                return

            session.delete(model)

            session.commit()

    def all(
        self,
    ) -> list[Khewat]:

        with SessionFactory() as session:

            models = (
                session.query(KhewatModel)
                .order_by(
                    KhewatModel.khewat_no,
                )
                .all()
            )

            return [
                KhewatMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def find_by_id(
        self,
        entity_id,
    ) -> Khewat | None:

        with SessionFactory() as session:

            model = (
                session.query(KhewatModel)
                .filter_by(id=entity_id)
                .first()
            )

            if model is None:
                return None

            return KhewatMapper.to_domain(
                model,
            )

    def find_by_village(
        self,
        village_id: UUID,
    ) -> list[Khewat]:

        with SessionFactory() as session:

            models = (
                session.query(KhewatModel)
                .filter_by(
                    village_id=str(village_id),
                )
                .order_by(
                    KhewatModel.khewat_no,
                )
                .all()
            )

            return [
                KhewatMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def find_by_number(
        self,
        village_id: UUID,
        khewat_no: str,
    ) -> Khewat | None:

        with SessionFactory() as session:

            model = (
                session.query(KhewatModel)
                .filter_by(
                    village_id=str(village_id),
                    khewat_no=khewat_no,
                )
                .first()
            )

            if model is None:
                return None

            return KhewatMapper.to_domain(
                model,
            )

    def active(
        self,
    ) -> list[Khewat]:

        with SessionFactory() as session:

            models = (
                session.query(KhewatModel)
                .filter_by(
                    active=True,
                )
                .order_by(
                    KhewatModel.khewat_no,
                )
                .all()
            )

            return [
                KhewatMapper.to_domain(
                    model,
                )
                for model in models
            ]