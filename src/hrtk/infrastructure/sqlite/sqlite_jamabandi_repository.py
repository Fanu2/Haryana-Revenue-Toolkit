"""
Haryana Revenue Toolkit (HRTK)

SQLite Jamabandi Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.jamabandi import (
    Jamabandi,
)

from hrtk.infrastructure.sqlite.mappers.jamabandi_mapper import (
    JamabandiMapper,
)

from hrtk.infrastructure.sqlite.models.jamabandi_model import (
    JamabandiModel,
)

from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)

from hrtk.repositories.jamabandi_repository import (
    JamabandiRepository,
)


class SQLiteJamabandiRepository(
    JamabandiRepository,
):
    """
    SQLite implementation of
    JamabandiRepository.
    """

    # ---------------------------------------------------------
    # Create
    # ---------------------------------------------------------

    def add(
        self,
        jamabandi: Jamabandi,
    ) -> None:

        with SessionFactory() as session:

            session.add(
                JamabandiMapper.to_model(
                    jamabandi,
                )
            )

            session.commit()

    # ---------------------------------------------------------
    # Update
    # ---------------------------------------------------------

    def update(
        self,
        jamabandi: Jamabandi,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    JamabandiModel,
                )
                .filter_by(
                    id=str(
                        jamabandi.id,
                    ),
                )
                .first()
            )

            if model is None:

                raise ValueError(
                    "Jamabandi not found."
                )

            model.village_id = str(
                jamabandi.village_id,
            )

            model.khewat_id = str(
                jamabandi.khewat_id,
            )

            model.year = (
                jamabandi.year
            )

            model.khatauni_number = (
                jamabandi.khatauni_number
            )

            model.remarks = (
                jamabandi.remarks
            )

            model.status = (
                jamabandi.status
            )

            model.active = model.active

            session.commit()

    # ---------------------------------------------------------
    # Delete
    # ---------------------------------------------------------

    def remove(
        self,
        entity_id,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    JamabandiModel,
                )
                .filter_by(
                    id=str(
                        entity_id,
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

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def all(
        self,
    ) -> list[
        Jamabandi,
    ]:

        with SessionFactory() as session:

            models = (
                session.query(
                    JamabandiModel,
                )
                .order_by(
                    JamabandiModel.year,
                )
                .all()
            )

            return [

                JamabandiMapper.to_domain(
                    model,
                )

                for model in models

            ]

    def find_by_id(
        self,
        entity_id,
    ) -> Jamabandi | None:

        with SessionFactory() as session:

            model = (
                session.query(
                    JamabandiModel,
                )
                .filter_by(
                    id=str(
                        entity_id,
                    ),
                )
                .first()
            )

            if model is None:

                return None

            return (
                JamabandiMapper.to_domain(
                    model,
                )
            )

    def find_by_village(
        self,
        village_id: UUID,
    ) -> list[
        Jamabandi,
    ]:

        with SessionFactory() as session:

            models = (
                session.query(
                    JamabandiModel,
                )
                .filter_by(
                    village_id=str(
                        village_id,
                    ),
                )
                .order_by(
                    JamabandiModel.year,
                )
                .all()
            )

            return [

                JamabandiMapper.to_domain(
                    model,
                )

                for model in models

            ]

    def find_by_year(
        self,
        village_id: UUID,
        year: str,
    ) -> Jamabandi | None:
        """
        Return the Jamabandi for a village and year.
        """

        with SessionFactory() as session:

            model = (
                session.query(
                    JamabandiModel,
                )
                .filter_by(
                    village_id=str(
                        village_id,
                    ),
                    year=year,
                )
                .first()
            )

            if model is None:
                return None

            return JamabandiMapper.to_domain(
                model,
            )

    def active(
        self,
    ) -> list[
        Jamabandi,
    ]:

        with SessionFactory() as session:

            models = (
                session.query(
                    JamabandiModel,
                )
                .filter_by(
                    active=True,
                )
                .order_by(
                    JamabandiModel.year,
                )
                .all()
            )

            return [

                JamabandiMapper.to_domain(
                    model,
                )

                for model in models

            ]

    def by_status(
        self,
        status: str,
    ) -> list[Jamabandi]:

        with SessionFactory() as session:

            models = (
                session.query(
                    JamabandiModel,
                )
                .filter_by(
                    status=status,
                )
                .order_by(
                    JamabandiModel.year,
                )
                .all()
            )

            return [
                JamabandiMapper.to_domain(
                    model,
                )
                for model in models
            ]
        
    # ---------------------------------------------------------
    # Compatibility Methods
    # ---------------------------------------------------------

    def list(
        self,
    ) -> list[Jamabandi]:
        """
        Return all Jamabandi records.
        """
        return self.all()

    def get(
        self,
        entity_id,
    ) -> Jamabandi | None:
        """
        Return a Jamabandi by id.
        """
        return self.find_by_id(entity_id)

    def exists(
        self,
        entity_id,
    ) -> bool:
        """
        Check whether a Jamabandi exists.
        """
        return self.get(entity_id) is not None
    
