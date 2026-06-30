"""
Haryana Revenue Toolkit (HRTK)

Application Context.

Responsible for bootstrapping the application infrastructure.

Responsibilities
----------------
* Create the Workspace.
* Create the ConfigurationManager.
* Create the LoggingManager.
* Create application repositories.
* Create application services.
* Create the SelectionContext.
* Expose shared services.

Non-responsibilities
--------------------
* GUI
* Business logic
* Plugins
"""

from __future__ import annotations

from pathlib import Path

from hrtk.application.selection_context import SelectionContext
from hrtk.infrastructure.configuration import ConfigurationManager
from hrtk.infrastructure.filesystem import Workspace
from hrtk.infrastructure.logging import LoggingManager

from hrtk.repositories.owner_repository import OwnerRepository
from hrtk.repositories.village_repository import VillageRepository

from hrtk.services.owner_service import OwnerService
from hrtk.services.village_service import VillageService

from hrtk.repositories.khewat_repository import KhewatRepository
from hrtk.services.khewat_service import KhewatService


class ApplicationContext:
    """
    Bootstraps the HRTK application.
    """

    def __init__(
        self,
        workspace: Path | str | None = None,
    ) -> None:
        """
        Parameters
        ----------
        workspace:
            Optional workspace root directory.
        """

        #
        # Infrastructure
        #

        self._workspace = Workspace(workspace)

        self._configuration = ConfigurationManager(
            self._workspace
        )

        self._logging = LoggingManager(
            self._workspace
        )

        #
        # Application state
        #

        self._selection = SelectionContext()

        #
        # Repositories
        #

        self._village_repository = VillageRepository()

        self._owner_repository = OwnerRepository()

        self.khewat_repository = KhewatRepository()

        #
        # Services
        #

        self._village_service = VillageService(
            self._village_repository
        )

        self._owner_service = OwnerService(
            self._owner_repository
        )

        self._logging.logger.info(
            "ApplicationContext initialized."
        )

        self.khewat_service = KhewatService(
            self.khewat_repository,
        )

    @property
    def workspace(self) -> Workspace:
        """
        Return the Workspace service.
        """
        return self._workspace

    @property
    def configuration(self) -> ConfigurationManager:
        """
        Return the ConfigurationManager.
        """
        return self._configuration

    @property
    def logging(self) -> LoggingManager:
        """
        Return the LoggingManager.
        """
        return self._logging

    @property
    def selection(self) -> SelectionContext:
        """
        Return the SelectionContext.
        """
        return self._selection

    @property
    def village_repository(
        self,
    ) -> VillageRepository:
        """
        Return the VillageRepository.
        """
        return self._village_repository

    @property
    def village_service(
        self,
    ) -> VillageService:
        """
        Return the VillageService.
        """
        return self._village_service

    @property
    def owner_repository(
        self,
    ) -> OwnerRepository:
        """
        Return the OwnerRepository.
        """
        return self._owner_repository

    @property
    def owner_service(
        self,
    ) -> OwnerService:
        """
        Return the OwnerService.
        """
        return self._owner_service

    def shutdown(self) -> None:
        """
        Shutdown all services.
        """

        self._logging.logger.info(
            "ApplicationContext shutting down."
        )

        self._logging.shutdown()

    def __repr__(self) -> str:
        return (
            "ApplicationContext("
            f"workspace={self.workspace.root!s})"
        )