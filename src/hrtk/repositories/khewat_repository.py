"""
Haryana Revenue Toolkit (HRTK)

Khewat Repository.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.khewat import Khewat
from hrtk.repositories.base_repository import BaseRepository


class KhewatRepository(BaseRepository[Khewat]):
    """
    Repository for Khewat entities.
    """

    def all(self) -> list[Khewat]:
        """
        Return all Khewats.
        """
        return list(self._items.values())

    def find_by_id(
        self,
        entity_id: UUID,
    ) -> Khewat | None:
        """
        Find a Khewat by ID.
        """
        return self._items.get(entity_id)

    def find_by_village(
        self,
        village_id: UUID,
    ) -> list[Khewat]:
        """
        Return all Khewats for a village.
        """

        return [
            khewat
            for khewat in self._items.values()
            if khewat.village_id == village_id
        ]

    def find_by_number(
        self,
        village_id: UUID,
        khewat_no: str,
    ) -> Khewat | None:
        """
        Find a Khewat by number within a village.
        """

        for khewat in self._items.values():

            if (
                khewat.village_id == village_id
                and khewat.khewat_no == khewat_no
            ):
                return khewat

        return None

    def active(
        self,
    ) -> list[Khewat]:
        """
        Return active Khewats.
        """

        return [
            khewat
            for khewat in self._items.values()
            if khewat.active
        ]