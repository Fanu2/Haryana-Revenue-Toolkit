"""
Haryana Revenue Toolkit (HRTK)

Ownership Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.ownership import Ownership
from hrtk.repositories.ownership_repository import (
    OwnershipRepository,
)


class OwnershipService:
    """
    Application service for Ownership.
    """

    def __init__(
        self,
        repository: OwnershipRepository,
    ) -> None:

        self._repository = repository

    def register(
        self,
        ownership: Ownership,
    ) -> None:

        self._repository.add(
            ownership,
        )

    def update(
        self,
        ownership: Ownership,
    ) -> None:

        self._repository.update(
            ownership,
        )

    def remove(
        self,
        ownership_id: UUID,
    ) -> None:

        self._repository.remove(
            ownership_id,
        )

    def all(
        self,
    ) -> list[Ownership]:

        return self._repository.list()

    def by_owner(
        self,
        owner_id: UUID,
    ) -> list[Ownership]:

        return self._repository.find_by_owner(
            owner_id,
        )

    def by_khewat(
        self,
        khewat_id: UUID,
    ) -> list[Ownership]:

        return self._repository.find_by_khewat(
            khewat_id,
        )