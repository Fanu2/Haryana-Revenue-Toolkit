"""
Haryana Revenue Toolkit (HRTK)

Application Context.

Composition root for the application.
"""

from __future__ import annotations

from pathlib import Path

from hrtk.application.selection_context import SelectionContext

from hrtk.infrastructure.configuration import (
    ConfigurationManager,
)
from hrtk.infrastructure.filesystem import (
    Workspace,
)
from hrtk.infrastructure.logging import (
    LoggingManager,
)

from hrtk.infrastructure.sqlite.database import (
    create_database,
)

from hrtk.infrastructure.sqlite.sqlite_village_repository import (
    SQLiteVillageRepository,
)
from hrtk.infrastructure.sqlite.sqlite_owner_repository import (
    SQLiteOwnerRepository,
)
from hrtk.infrastructure.sqlite.sqlite_khewat_repository import (
    SQLiteKhewatRepository,
)
from hrtk.infrastructure.sqlite.sqlite_parcel_repository import (
    SQLiteParcelRepository,
)

from hrtk.infrastructure.sqlite.sqlite_ownership_repository import (
    SQLiteOwnershipRepository,
)

from hrtk.services.village_service import (
    VillageService,
)
from hrtk.services.owner_service import (
    OwnerService,
)
from hrtk.services.khewat_service import (
    KhewatService,
)
from hrtk.services.parcel_service import (
    ParcelService,
)

from hrtk.services.ownership_service import (
    OwnershipService,
)



class ApplicationContext:
    """
    Composition root of HRTK.
    """

    def __init__(
        self,
        workspace: Path | str | None = None,
    ) -> None:

        #
        # Infrastructure
        #

        self._workspace = Workspace(workspace)

        self._configuration = ConfigurationManager(
            self._workspace,
        )

        self._logging = LoggingManager(
            self._workspace,
        )

        #
        # Database
        #

        create_database()

        self._logging.logger.info(
            "SQLite database initialized."
        )

        #
        # Shared application state
        #

        self._selection = SelectionContext()

        #
        # Repositories
        #

        self._village_repository = (
            SQLiteVillageRepository()
        )

        self._owner_repository = (
            SQLiteOwnerRepository()
        )

        self._khewat_repository = (
            SQLiteKhewatRepository()
        )

        self._parcel_repository = (
            SQLiteParcelRepository()
        )

        self._ownership_repository = (
            SQLiteOwnershipRepository()
        )

        #
        # Services
        #

        self._village_service = VillageService(
            self._village_repository,
        )

        self._owner_service = OwnerService(
            self._owner_repository,
        )

        self._khewat_service = KhewatService(
            self._khewat_repository,
        )

        self._parcel_service = ParcelService(
            self._parcel_repository,
        )

        self._ownership_service = OwnershipService(
        self._ownership_repository,
        )

        self._logging.logger.info(
            "ApplicationContext initialized."
        )

    # ---------------------------------------------------------
    # Infrastructure
    # ---------------------------------------------------------

    @property
    def workspace(self) -> Workspace:
        return self._workspace

    @property
    def configuration(
        self,
    ) -> ConfigurationManager:
        return self._configuration

    @property
    def logging(self) -> LoggingManager:
        return self._logging

    @property
    def selection(
        self,
    ) -> SelectionContext:
        return self._selection

    # ---------------------------------------------------------
    # Repositories
    # ---------------------------------------------------------

    @property
    def village_repository(
        self,
    ) -> SQLiteVillageRepository:
        return self._village_repository

    @property
    def owner_repository(
        self,
    ) -> SQLiteOwnerRepository:
        return self._owner_repository

    @property
    def khewat_repository(
        self,
    ) -> SQLiteKhewatRepository:
        return self._khewat_repository

    @property
    def parcel_repository(
        self,
    ) -> SQLiteParcelRepository:
        return self._parcel_repository
    
    @property
    def ownership_repository(
        self,
    ) -> SQLiteOwnershipRepository:
        return self._ownership_repository

    # ---------------------------------------------------------
    # Services
    # ---------------------------------------------------------

    @property
    def village_service(
        self,
    ) -> VillageService:
        return self._village_service

    @property
    def owner_service(
        self,
    ) -> OwnerService:
        return self._owner_service

    @property
    def khewat_service(
        self,
    ) -> KhewatService:
        return self._khewat_service

    @property
    def parcel_service(
        self,
    ) -> ParcelService:
        return self._parcel_service
    
    @property
    def ownership_service(
        self,
    ) -> OwnershipService:
        return self._ownership_service

    # ---------------------------------------------------------
    # Shutdown
    # ---------------------------------------------------------

    def shutdown(self) -> None:
        """
        Shutdown application services.
        """

        self._logging.logger.info(
            "ApplicationContext shutting down."
        )

        self._logging.shutdown()

    def __repr__(
        self,
    ) -> str:

        return (
            "ApplicationContext("
            f"workspace={self.workspace.root!s})"
        )