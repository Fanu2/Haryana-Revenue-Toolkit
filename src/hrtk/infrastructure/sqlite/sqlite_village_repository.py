"""
Haryana Revenue Toolkit (HRTK)

SQLite Village Repository.
"""

from __future__ import annotations

from hrtk.domain.village import Village
from hrtk.infrastructure.sqlite.mappers.village_mapper import (
    VillageMapper,
)
from hrtk.infrastructure.sqlite.models.village_model import (
    VillageModel,
)
from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)
from hrtk.repositories.village_repository import (
    VillageRepository,
)


class SQLiteVillageRepository(VillageRepository):
    """
    SQLite implementation of VillageRepository.
    """

    def add(
        self,
        village: Village,
    ) -> None:

        with SessionFactory() as session:

            session.add(
                VillageMapper.to_model(
                    village,
                )
            )

            session.commit()

    def update(
        self,
        village: Village,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    VillageModel,
                )
                .filter_by(
                    code=village.code,
                )
                .first()
            )

            if model is None:
                raise ValueError(
                    f"Village '{village.code}' not found."
                )

            model.name = village.name
            model.tehsil = village.tehsil
            model.district = village.district
            model.state = village.state
            model.active = village.active

            session.commit()

    def remove(
        self,
        village: Village,
    ) -> None:

        with SessionFactory() as session:

            model = (
                session.query(
                    VillageModel,
                )
                .filter_by(
                    code=village.code,
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
        code: str,
    ) -> Village | None:

        with SessionFactory() as session:

            model = (
                session.query(
                    VillageModel,
                )
                .filter_by(
                    code=code,
                )
                .first()
            )

            if model is None:
                return None

            return VillageMapper.to_domain(
                model,
            )

    def list(
        self,
    ) -> list[Village]:

        with SessionFactory() as session:

            models = (
                session.query(
                    VillageModel,
                )
                .order_by(
                    VillageModel.name,
                )
                .all()
            )

            return [
                VillageMapper.to_domain(
                    model,
                )
                for model in models
            ]

    def exists(
        self,
        code: str,
    ) -> bool:

        return (
            self.get(code)
            is not None
        )

    def find_by_code(
        self,
        code: str,
    ) -> Village | None:
        """
        Find a village by its revenue code.
        """

        return self.get(
            code,
        )
    
    
    def all(self) -> list[Village]:
        """
        Return all villages.

        Compatibility method for BaseService.
        """
        return self.list()