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

from hrtk.services.base_service import (
    BaseService,
)


class JamabandiService(
    BaseService,
):
    """
    Service for Jamabandi records.
    """

    def __init__(
        self,
        repository: JamabandiRepository,
    ) -> None:
        """
        Initialize the service.
        """

        super().__init__(
            repository,
        )

        self._repository = repository

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def register(
        self,
        jamabandi: Jamabandi,
    ) -> None:
        """
        Register a new Jamabandi.
        """

        self._repository.add(
            jamabandi,
        )

    def update(
        self,
        jamabandi: Jamabandi,
    ) -> None:
        """
        Update an existing Jamabandi.
        """

        self._repository.update(
            jamabandi,
        )

    def remove(
        self,
        entity_id: UUID,
    ) -> None:
        """
        Remove a Jamabandi.
        """

        self._repository.remove(
            entity_id,
        )

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def all(
        self,
    ) -> list[
        Jamabandi
    ]:
        """
        Return all Jamabandis.
        """

        return self._repository.all()

    def by_id(
        self,
        entity_id: UUID,
    ) -> Jamabandi | None:
        """
        Return a Jamabandi by ID.
        """

        return self._repository.find_by_id(
            entity_id,
        )

    def by_village(
        self,
        village_id: UUID,
    ) -> list[
        Jamabandi
    ]:
        """
        Return all Jamabandis
        for a Village.
        """

        return (
            self._repository.find_by_village(
                village_id,
            )
        )

    def by_year(
        self,
        village_id: UUID,
        year: str,
    ) -> Jamabandi | None:
        """
        Return a Jamabandi for
        Village + Year.
        """

        return (
            self._repository.find_by_year(
                village_id,
                year,
            )
        )

    def active(
        self,
    ) -> list[
        Jamabandi
    ]:
        """
        Return active Jamabandis.
        """

        return (
            self._repository.active()
        )

    def finalized(
        self,
    ) -> list[
        Jamabandi
    ]:
        """
        Return finalized
        Jamabandis.
        """

        return (
            self._repository.finalized()
        )

    # ---------------------------------------------------------
    # Business Rules
    # ---------------------------------------------------------

    def exists(
        self,
        village_id: UUID,
        year: str,
    ) -> bool:
        """
        Determine whether a
        Jamabandi already exists.
        """

        return (

            self.by_year(
                village_id,
                year,
            )

            is not None

        )

    def finalize(
        self,
        entity_id: UUID,
    ) -> None:
        """
        Finalize a Jamabandi.
        """

        jamabandi = self.by_id(
            entity_id,
        )

        if jamabandi is None:

            raise ValueError(
                "Jamabandi not found."
            )

        jamabandi.finalize()

        self.update(
            jamabandi,
        )

    def reopen(
        self,
        entity_id: UUID,
    ) -> None:
        """
        Re-open a finalized
        Jamabandi.
        """

        jamabandi = self.by_id(
            entity_id,
        )

        if jamabandi is None:

            raise ValueError(
                "Jamabandi not found."
            )

        jamabandi.reopen()

        self.update(
            jamabandi,
        )