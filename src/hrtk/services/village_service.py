"""
Haryana Revenue Toolkit (HRTK)

Village application service.
"""

from __future__ import annotations

from hrtk.domain.village import Village
from hrtk.repositories.village_repository import VillageRepository
from hrtk.services.base_service import BaseService


class VillageService(BaseService[Village]):
    """
    Application service for Village entities.
    """

    def __init__(
        self,
        repository: VillageRepository,
    ) -> None:
        super().__init__(repository)

    @property
    def repository(self) -> VillageRepository:
        """
        Return the village repository.
        """
        return super().repository

    def register(
        self,
        village: Village,
    ) -> None:
        """
        Register a new village.
        """
        self.repository.add(village)

    def activate(
        self,
        village: Village,
    ) -> None:
        """
        Activate a village.
        """
        village.activate()
        self.repository.update(village)

    def deactivate(
        self,
        village: Village,
    ) -> None:
        """
        Deactivate a village.
        """
        village.deactivate()
        self.repository.update(village)

    def find_by_code(
        self,
        code: str,
    ) -> Village | None:
        """
        Find a village by its code.
        """
        return self.repository.find_by_code(code)