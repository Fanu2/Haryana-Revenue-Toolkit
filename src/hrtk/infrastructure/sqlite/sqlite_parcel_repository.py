"""
Haryana Revenue Toolkit (HRTK)

SQLite Parcel Repository.
"""

from __future__ import annotations

from sqlalchemy import select

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)
from hrtk.infrastructure.common.unit_of_work import (
    unit_of_work,
)
from hrtk.infrastructure.mapper.parcel_mapper import (
    ParcelMapper,
)
from hrtk.infrastructure.sqlite.models.parcel_model import (
    ParcelModel,
)
from hrtk.repositories.parcel_repository import (
    ParcelRepository,
)


class SQLiteParcelRepository(ParcelRepository):
    """
    SQLite implementation of ParcelRepository.
    """

    def add(
        self,
        parcel: Parcel,
    ) -> None:

        model = ParcelMapper.to_model(
            parcel,
        )

        with unit_of_work() as session:

            session.add(
                model,
            )

    def get(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:

        with unit_of_work() as session:

            stmt = select(
                ParcelModel,
            ).where(
                ParcelModel.rectangle
                == number.rectangle,
                ParcelModel.killa
                == number.killa,
            )

            model = session.scalar(
                stmt,
            )

            if model is None:
                return None

            return ParcelMapper.to_domain(
                model,
            )

    def exists(
        self,
        number: ParcelNumber,
    ) -> bool:

        return (
            self.get(
                number,
            )
            is not None
        )

    def list(
        self,
    ) -> list[Parcel]:

        with unit_of_work() as session:

            stmt = select(
                ParcelModel,
            )

            models = session.scalars(
                stmt,
            ).all()

            return [
                ParcelMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def update(
        self,
        parcel: Parcel,
    ) -> None:

        raise NotImplementedError

    def remove(
        self,
        number: ParcelNumber,
    ) -> None:

        raise NotImplementedError