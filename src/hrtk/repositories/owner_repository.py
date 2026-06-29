"""
Haryana Revenue Toolkit (HRTK)

Owner Repository.
"""

from __future__ import annotations

from hrtk.domain.owner import Owner
from hrtk.repositories.base_repository import BaseRepository


class OwnerRepository(BaseRepository[Owner]):
    """
    Repository for Owner entities.
    """

    def find_by_code(
        self,
        owner_code: str,
    ) -> Owner | None:
        """
        Find an owner by owner code.
        """

        for owner in self:

            if owner.owner_code == owner_code:
                return owner

        return None

    def find_by_village(
        self,
        village_id,
    ) -> list[Owner]:
        """
        Return all owners belonging to a village.
        """

        return [
            owner
            for owner in self
            if owner.village_id == village_id
        ]