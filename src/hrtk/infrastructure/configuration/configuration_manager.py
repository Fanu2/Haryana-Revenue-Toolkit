"""
Haryana Revenue Toolkit (HRTK)

Configuration Manager.

Responsible for loading, creating and saving the application's
configuration stored as YAML.

Responsibilities
----------------
* Create config.yaml on first run.
* Load configuration.
* Save configuration.
* Get values using dotted keys.
* Set values using dotted keys.

Non-responsibilities
--------------------
* Logging
* Workspace creation
* Business logic
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from hrtk.infrastructure.filesystem import Workspace


class ConfigurationManager:
    """Manages the HRTK YAML configuration."""

    DEFAULT_CONFIGURATION: dict[str, Any] = {
        "application": {
            "name": "Haryana Revenue Toolkit",
            "version": "0.1.0-alpha1",
        },
        "ui": {
            "theme": "light",
            "language": "en",
        },
        "logging": {
            "level": "INFO",
        },
        "workspace": {
            "auto_create": True,
        },
    }

    def __init__(self, workspace: Workspace) -> None:
        self._workspace = workspace
        self._config_file: Path = workspace.config / "config.yaml"
        self._data: dict[str, Any] = {}

        self._ensure_configuration()

    @property
    def path(self) -> Path:
        """Return the configuration file path."""
        return self._config_file

    @property
    def data(self) -> dict[str, Any]:
        """Return the complete configuration."""
        return deepcopy(self._data)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.

        Example
        -------
        config.get("ui.theme")
        """
        value: Any = self._data

        for part in key.split("."):
            if not isinstance(value, dict):
                return default

            if part not in value:
                return default

            value = value[part]

        return value

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.

        Example
        -------
        config.set("ui.theme", "dark")
        """
        parts = key.split(".")
        current = self._data

        for part in parts[:-1]:
            node = current.get(part)

            if not isinstance(node, dict):
                node = {}
                current[part] = node

            current = node

        current[parts[-1]] = value

    def save(self) -> None:
        """Write the configuration to disk."""
        with self._config_file.open(
            "w",
            encoding="utf-8",
        ) as handle:
            yaml.safe_dump(
                self._data,
                handle,
                sort_keys=False,
                allow_unicode=True,
            )

    def reload(self) -> None:
        """Reload the configuration from disk."""
        with self._config_file.open(
            "r",
            encoding="utf-8",
        ) as handle:
            data = yaml.safe_load(handle)

        if data is None:
            data = {}

        self._data = data

    def reset(self) -> None:
        """Reset configuration to defaults."""
        self._data = deepcopy(self.DEFAULT_CONFIGURATION)
        self.save()

    def _ensure_configuration(self) -> None:
        """Create configuration file if required."""
        if not self._config_file.exists():
            self._data = deepcopy(self.DEFAULT_CONFIGURATION)
            self.save()
            return

        self.reload()

    def __contains__(self, key: str) -> bool:
        return self.get(key, None) is not None

    def __getitem__(self, key: str) -> Any:
        value = self.get(key)

        if value is None:
            raise KeyError(key)

        return value

    def __setitem__(self, key: str, value: Any) -> None:
        self.set(key, value)

    def __repr__(self) -> str:
        return (
            f"ConfigurationManager("
            f"path={self._config_file!s})"
        )