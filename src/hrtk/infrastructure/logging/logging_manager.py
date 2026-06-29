"""
Haryana Revenue Toolkit (HRTK)

Logging Manager.

Responsible for configuring the application's logging system.
"""

from __future__ import annotations

import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path

from hrtk.infrastructure.filesystem import Workspace


class LoggingManager:
    """Configure and manage the HRTK logging system."""

    LOGGER_NAME = "hrtk"
    LOG_FILE_NAME = "hrtk.log"

    def __init__(
        self,
        workspace: Workspace,
        level: int = logging.INFO,
        console: bool = True,
    ) -> None:

        self._workspace = workspace
        self._log_directory = workspace.logs
        self._log_file = self._log_directory / self.LOG_FILE_NAME

        self._level = level
        self._console = console

        self._logger = logging.getLogger(self.LOGGER_NAME)

        self._configure()

    @property
    def logger(self) -> Logger:
        return self._logger

    @property
    def log_directory(self) -> Path:
        return self._log_directory

    @property
    def log_file(self) -> Path:
        return self._log_file

    def get_logger(self, name: str) -> Logger:
        if name == self.LOGGER_NAME:
            return self._logger

        return logging.getLogger(f"{self.LOGGER_NAME}.{name}")

    def set_level(self, level: int) -> None:
        self._level = level
        self._logger.setLevel(level)

        for handler in self._logger.handlers:
            handler.setLevel(level)

    def _configure(self) -> None:

        self._log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._logger.setLevel(self._level)
        self._logger.propagate = False

        #
        # IMPORTANT
        #
        # Remove handlers left behind by previous LoggingManager
        # instances (especially during pytest).
        #
        for handler in list(self._logger.handlers):
            handler.flush()
            handler.close()
            self._logger.removeHandler(handler)

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = RotatingFileHandler(
            filename=self._log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )

        file_handler.setLevel(self._level)
        file_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)

        if self._console:

            console_handler = logging.StreamHandler()

            console_handler.setLevel(self._level)
            console_handler.setFormatter(formatter)

            self._logger.addHandler(console_handler)

    def shutdown(self) -> None:
        """
        Flush, close and remove all handlers.
        """

        for handler in list(self._logger.handlers):
            handler.flush()
            handler.close()
            self._logger.removeHandler(handler)

        logging.shutdown()

    def __repr__(self) -> str:
        return f"LoggingManager(log_file={self._log_file!s})"