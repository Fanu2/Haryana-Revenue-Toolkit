"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.jamabandi import (
    Jamabandi,
)

from hrtk.repositories.jamabandi_repository import (
    JamabandiRepository,
)


class JamabandiService:
    """
    Application service for Jamabandi entities.
    """

    def __init__(
        self,
        repository: JamabandiRepository,
    ) -> None:

        self._repository = repository

    @property
    def repository(
        self,
    ) -> JamabandiRepository:

        return self._repository

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def add(
        self,
        jamabandi: Jamabandi,
    ) -> None:

        self.repository.add(
            jamabandi,
        )

    def update(
        self,
        jamabandi: Jamabandi,
    ) -> None:

        self.repository.update(
            jamabandi,
        )

    def remove(
        self,
        jamabandi_id: UUID,
    ) -> None:

        self.repository.remove(
            jamabandi_id,
        )

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def get(
        self,
        jamabandi_id: UUID,
    ) -> Jamabandi | None:

        return self.repository.get(
            jamabandi_id,
        )

    def all(
        self,
    ) -> list[Jamabandi]:

        return self.repository.list()

    def list(
        self,
    ) -> list[Jamabandi]:

        return self.repository.list()

    def exists(
        self,
        jamabandi_id: UUID,
    ) -> bool:

        return self.repository.exists(
            jamabandi_id,
        )

    def by_village(
        self,
        village_id: UUID,
    ) -> list[Jamabandi]:

        return self.repository.find_by_village(
            village_id,
        )

    def by_year(
        self,
        village_id: UUID,
        year: str,
    ) -> Jamabandi | None:

        return self.repository.find_by_year(
            village_id,
            year,
        )

    def active(
        self,
    ) -> list[Jamabandi]:

        return self.repository.active()

    def by_status(
        self,
        status: str,
    ) -> list[Jamabandi]:

        return self.repository.by_status(
            status,
        )