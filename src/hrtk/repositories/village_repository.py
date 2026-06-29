"""
Haryana Revenue Toolkit (HRTK)

Village Repository.
"""

from __future__ import annotations

from hrtk.domain.village import Village
from hrtk.repositories.base_repository import BaseRepository


class VillageRepository(BaseRepository[Village]):
    """
    Repository for Village entities.
    """

    def find_by_code(
        self,
        code: str,
    ) -> Village | None:
        """
        Find a village by its code.
        """
        for village in self:
            if village.code == code:
                return village

        return None