"""
Haryana Revenue Toolkit (HRTK)

Workspace implementation.

The Workspace class represents the root filesystem layout used by the
application. It is responsible only for creating and exposing the
directory structure required by HRTK.

Responsibilities
----------------
* Create the workspace directory tree.
* Expose important directories as pathlib.Path objects.
* Never delete user data.
* Be safe to construct multiple times.

Non-responsibilities
--------------------
* Configuration
* Logging
* Database access
* Plugin loading
"""

from __future__ import annotations

from pathlib import Path


class Workspace:
    """
    Represents the application's workspace.

    Parameters
    ----------
    root:
        Optional root directory.

        If omitted, a workspace directory named ``workspace`` is created
        under the current working directory.
    """

    _DIRECTORIES = (
        "cache",
        "config",
        "database",
        "downloads",
        "logs",
        "plugins",
        "reports",
        "temp",
    )

    def __init__(self, root: Path | str | None = None) -> None:
        if root is None:
            self._root = Path.cwd() / "workspace"
        else:
            self._root = Path(root).expanduser().resolve()

        self._create_workspace()

    def _create_workspace(self) -> None:
        """
        Create the complete workspace tree.

        Safe to call multiple times.
        """

        self._root.mkdir(parents=True, exist_ok=True)

        for directory in self._DIRECTORIES:
            (self._root / directory).mkdir(
                parents=True,
                exist_ok=True,
            )

    @property
    def root(self) -> Path:
        """Workspace root directory."""
        return self._root

    @property
    def cache(self) -> Path:
        return self._root / "cache"

    @property
    def config(self) -> Path:
        return self._root / "config"

    @property
    def database(self) -> Path:
        return self._root / "database"

    @property
    def downloads(self) -> Path:
        return self._root / "downloads"

    @property
    def logs(self) -> Path:
        return self._root / "logs"

    @property
    def plugins(self) -> Path:
        return self._root / "plugins"

    @property
    def reports(self) -> Path:
        return self._root / "reports"

    @property
    def temp(self) -> Path:
        return self._root / "temp"

    def __str__(self) -> str:
        return str(self._root)

    def __repr__(self) -> str:
        return f"Workspace(root={self._root!s})"