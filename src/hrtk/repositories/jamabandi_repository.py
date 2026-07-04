"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.jamabandi import Jamabandi
from hrtk.repositories.base_repository import BaseRepository


class JamabandiRepository(
    BaseRepository[
        Jamabandi
    ]
):
    """
    Repository for Jamabandi entities.
    """

    # ---------------------------------------------------------
    # Basic Queries
    # ---------------------------------------------------------

    def all(
        self,
    ) -> list[
        Jamabandi
    ]:
        """
        Return all Jamabandi records.
        """

        return list(
            self._items.values()
        )

    def find_by_id(
        self,
        entity_id: UUID,
    ) -> Jamabandi | None:
        """
        Find a Jamabandi by ID.
        """

        return self._items.get(
            entity_id,
        )

    # ---------------------------------------------------------
    # Village Queries
    # ---------------------------------------------------------

    def find_by_village(
        self,
        village_id: UUID,
    ) -> list[
        Jamabandi
    ]:
        """
        Return all Jamabandis
        belonging to a Village.
        """

        return [

            jamabandi

            for jamabandi

            in self._items.values()

            if (
                jamabandi.village_id
                ==
                village_id
            )
        ]

    # ---------------------------------------------------------
    # Year Queries
    # ---------------------------------------------------------

    def find_by_year(
        self,
        village_id: UUID,
        year: str,
    ) -> Jamabandi | None:
        """
        Return the Jamabandi
        for a Village and Year.
        """

        for jamabandi in (
            self._items.values()
        ):

            if (

                jamabandi.village_id
                ==
                village_id

                and

                jamabandi.year
                ==
                year

            ):

                return jamabandi

        return None

    # ---------------------------------------------------------
    # Active Records
    # ---------------------------------------------------------

    def active(
        self,
    ) -> list[
        Jamabandi
    ]:
        """
        Return active
        Jamabandi records.
        """

        return [

            jamabandi

            for jamabandi

            in self._items.values()

            if jamabandi.active

        ]

    # ---------------------------------------------------------
    # Finalized Records
    # ---------------------------------------------------------

    def finalized(
        self,
    ) -> list[
        Jamabandi
    ]:
        """
        Return finalized
        Jamabandi records.
        """

        return [

            jamabandi

            for jamabandi

            in self._items.values()

            if jamabandi.finalized

        ]