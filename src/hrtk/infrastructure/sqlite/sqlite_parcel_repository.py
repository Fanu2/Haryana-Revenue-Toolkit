"""
Haryana Revenue Toolkit (HRTK)

SQLite Parcel Repository.
"""

from __future__ import annotations

from uuid import UUID

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


class SQLiteParcelRepository(
    ParcelRepository,
):
    """
    SQLite implementation of ParcelRepository.
    """

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def add(
        self,
        parcel: Parcel,
    ) -> None:

        with unit_of_work() as session:

            session.add(
                ParcelMapper.to_model(
                    parcel,
                )
            )

    def update(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Update an existing parcel.
        """

        with unit_of_work() as session:

            stmt = (
                select(
                    ParcelModel,
                )
                .where(
                    ParcelModel.id
                    == str(parcel.id),
                )
            )

            model = session.scalar(
                stmt,
            )

            if model is None:

                raise ValueError(
                    f"Parcel '{parcel.number}' does not exist."
                )

            model.rectangle = (
                parcel.number.rectangle
            )

            model.killa = (
                parcel.number.killa
            )

            model.kanal = (
                parcel.area.kanal
            )

            model.marla = (
                parcel.area.marla
            )

            model.sarsai = (
                parcel.area.sarsai
            )

            model.remarks = (
                parcel.remarks
            )

    def remove(
        self,
        parcel_id: UUID,
    ) -> None:
        """
        Remove a parcel.
        """

        with unit_of_work() as session:

            stmt = (
                select(
                    ParcelModel,
                )
                .where(
                    ParcelModel.id
                    == str(parcel_id),
                )
            )

            model = session.scalar(
                stmt,
            )

            if model is None:

                raise ValueError(
                    "Parcel does not exist."
                )

            session.delete(
                model,
            )

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def get(
        self,
        parcel_id: UUID,
    ) -> Parcel | None:

        with unit_of_work() as session:

            stmt = (
                select(
                    ParcelModel,
                )
                .where(
                    ParcelModel.id
                    == str(parcel_id),
                )
            )

            model = session.scalar(
                stmt,
            )

            if model is None:
                return None

            return ParcelMapper.to_domain(
                model,
            )

    def find_by_number(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:

        with unit_of_work() as session:

            stmt = (
                select(
                    ParcelModel,
                )
                .where(
                    ParcelModel.rectangle
                    == number.rectangle,
                    ParcelModel.killa
                    == number.killa,
                )
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
        parcel_id: UUID,
    ) -> bool:

        return (
            self.get(
                parcel_id,
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

            models = (
                session.scalars(
                    stmt,
                )
                .all()
            )

            return [
                ParcelMapper.to_domain(
                    model,
                )
                for model in models
            ]