"""
Haryana Revenue Toolkit (HRTK)

SQLite Khewat Parcel Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.land_records.khewat_parcel import (
    KhewatParcel,
)

from hrtk.infrastructure.sqlite.mappers.khewat_parcel_mapper import (
    KhewatParcelMapper,
)

from hrtk.infrastructure.sqlite.models.khewat_parcel_model import (
    KhewatParcelModel,
)

from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)

from hrtk.repositories.khewat_parcel_repository import (
    KhewatParcelRepository,
)


class SQLiteKhewatParcelRepository(
    KhewatParcelRepository,
):
    """
    SQLite implementation of the
    KhewatParcel repository.
    """

    def add(
        self,
        relationship: KhewatParcel,
    ) -> None:

        with SessionFactory() as session:

            session.add(
                KhewatParcelMapper.to_model(
                    relationship,
                )
            )

            session.commit()

    def update(
        self,
        relationship: KhewatParcel,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    KhewatParcelModel,
                )
                .filter_by(
                    entity_id=str(
                        relationship.id,
                    ),
                )
                .first()
            )

            if model is None:

                raise ValueError(
                    "Relationship not found."
                )

            model.khewat_id = str(
                relationship.khewat_id,
            )

            model.parcel_id = str(
                relationship.parcel_id,
            )

            model.remarks = (
                relationship.remarks
            )

            session.commit()

    def remove(
        self,
        relationship_id: UUID,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    KhewatParcelModel,
                )
                .filter_by(
                    entity_id=str(
                        relationship_id,
                    ),
                )
                .first()
            )

            if model is None:
                return

            session.delete(
                model,
            )

            session.commit()

    def get(
        self,
        relationship_id: UUID,
    ) -> KhewatParcel | None:

        with SessionFactory() as session:

            model = (
                session.query(
                    KhewatParcelModel,
                )
                .filter_by(
                    entity_id=str(
                        relationship_id,
                    ),
                )
                .first()
            )

            if model is None:
                return None

            return (
                KhewatParcelMapper.to_domain(
                    model,
                )
            )

    def list(
        self,
    ) -> list[KhewatParcel]:

        with SessionFactory() as session:

            models = (
                session.query(
                    KhewatParcelModel,
                )
                .order_by(
                    KhewatParcelModel.khewat_id,
                )
                .all()
            )

            return [
                KhewatParcelMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def all(
        self,
    ) -> list[KhewatParcel]:
        """
        Compatibility method.
        """

        return self.list()

    def exists(
        self,
        relationship_id: UUID,
    ) -> bool:

        return (
            self.get(
                relationship_id,
            )
            is not None
        )

    def find_by_khewat(
        self,
        khewat_id: UUID,
    ) -> list[KhewatParcel]:

        with SessionFactory() as session:

            models = (
                session.query(
                    KhewatParcelModel,
                )
                .filter_by(
                    khewat_id=str(
                        khewat_id,
                    ),
                )
                .all()
            )

            return [
                KhewatParcelMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def find_by_parcel(
        self,
        parcel_id: UUID,
    ) -> list[KhewatParcel]:

        with SessionFactory() as session:

            models = (
                session.query(
                    KhewatParcelModel,
                )
                .filter_by(
                    parcel_id=str(
                        parcel_id,
                    ),
                )
                .all()
            )

            return [
                KhewatParcelMapper.to_domain(
                    model,
                )
                for model in models
            ]
