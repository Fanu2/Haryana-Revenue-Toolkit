"""
Haryana Revenue Toolkit (HRTK)

Owner application service.
"""

from __future__ import annotations

from hrtk.domain.owner import Owner
from hrtk.repositories.owner_repository import OwnerRepository
from hrtk.services.base_service import BaseService


class OwnerService(BaseService[Owner]):
    """
    Application service for Owner entities.
    """

    def __init__(
        self,
        repository: OwnerRepository,
    ) -> None:
        super().__init__(repository)

    @property
    def repository(self) -> OwnerRepository:
        """
        Return the owner repository.
        """
        return super().repository

    def register(
        self,
        owner: Owner,
    ) -> None:
        """
        Register a new owner.
        """
        self.repository.add(owner)

    def activate(
        self,
        owner: Owner,
        ) -> None:
        """
        Activate an owner.
        """

        owner.activate()

        self.repository.update(owner)


    def deactivate(
        self,
        owner: Owner,
        ) -> None:
        """
        Deactivate an owner.
        """

        owner.deactivate()

        self.repository.update(owner)

    def find_by_code(
        self,
        owner_code: str,
    ) -> Owner | None:
        """
        Find an owner by owner code.
        """
        return self.repository.find_by_code(
            owner_code
        )

    def find_by_village(
        self,
        village_id,
    ) -> list[Owner]:
        """
        Return all owners for a village.
        """
        return self.repository.find_by_village(
            village_id
        )