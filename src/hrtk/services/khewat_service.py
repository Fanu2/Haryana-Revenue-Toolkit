"""
Haryana Revenue Toolkit (HRTK)

Khewat Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.khewat import Khewat
from hrtk.repositories.khewat_repository import KhewatRepository


class KhewatService:
    """
    Business service for Khewat entities.
    """

    def __init__(
        self,
        repository: KhewatRepository,
    ) -> None:

        self._repository = repository

    @property
    def repository(self) -> KhewatRepository:
        """
        Return the repository.
        """
        return self._repository

    def register(
        self,
        khewat: Khewat,
    ) -> None:
        """
        Register a new Khewat.
        """

        existing = self.repository.find_by_number(
            khewat.village_id,
            khewat.khewat_no,
        )

        if existing is not None:
            raise ValueError(
                f"Khewat '{khewat.khewat_no}' already exists."
            )

        self.repository.add(khewat)

    def update(
        self,
        khewat: Khewat,
    ) -> None:
        """
        Update an existing Khewat.
        """

        self.repository.update(khewat)

    def delete(
        self,
        khewat: Khewat,
    ) -> None:
        """
        Delete a Khewat.
        """

        self.repository.remove(khewat.id)

    def activate(
        self,
        khewat: Khewat,
    ) -> None:
        """
        Activate a Khewat.
        """

        khewat.activate()

        self.repository.update(khewat)

    def deactivate(
        self,
        khewat: Khewat,
    ) -> None:
        """
        Deactivate a Khewat.
        """

        khewat.deactivate()

        self.repository.update(khewat)

    def all(
        self,
    ) -> list[Khewat]:
        """
        Return all Khewats.
        """

        return self.repository.all()

    def active(
        self,
    ) -> list[Khewat]:
        """
        Return active Khewats.
        """

        return self.repository.active()

    def find_by_id(
        self,
        entity_id: UUID,
    ) -> Khewat | None:
        """
        Find a Khewat by ID.
        """

        return self.repository.find_by_id(
            entity_id,
        )

    def find_by_village(
        self,
        village_id: UUID,
    ) -> list[Khewat]:
        """
        Return Khewats for a village.
        """

        return self.repository.find_by_village(
            village_id,
        )