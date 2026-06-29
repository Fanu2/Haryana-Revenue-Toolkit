"""
Haryana Revenue Toolkit (HRTK)

Application Context.

Responsible for bootstrapping the application infrastructure.

Responsibilities
----------------
* Create the Workspace.
* Create the ConfigurationManager.
* Create the LoggingManager.
* Expose shared services.

Non-responsibilities
--------------------
* GUI
* Business logic
* Plugins
"""

from __future__ import annotations

from pathlib import Path

from hrtk.infrastructure.configuration import ConfigurationManager
from hrtk.infrastructure.filesystem import Workspace
from hrtk.infrastructure.logging import LoggingManager


class ApplicationContext:
    """
    Bootstraps the HRTK application.
    """

    def __init__(self, workspace: Path | str | None = None) -> None:
        """
        Parameters
        ----------
        workspace:
            Optional workspace root directory.
        """

        self._workspace = Workspace(workspace)

        self._configuration = ConfigurationManager(
            self._workspace
        )

        self._logging = LoggingManager(
            self._workspace
        )

        self._logging.logger.info(
            "ApplicationContext initialized."
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
        Return the ConfigurationManager service.
        """
        return self._configuration

    @property
    def logging(self) -> LoggingManager:
        """
        Return the LoggingManager service.
        """
        return self._logging

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