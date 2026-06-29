"""
Unit tests for LoggingManager.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from hrtk.infrastructure.filesystem import Workspace
from hrtk.infrastructure.logging import LoggingManager


def test_log_directory_exists(tmp_path):
    """LoggingManager should create the log directory."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    assert manager.log_directory.exists()
    assert manager.log_directory.is_dir()


def test_log_file_path(tmp_path):
    """Log file path should be correct."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    assert manager.log_file.name == "hrtk.log"


def test_default_logger_returned(tmp_path):
    """logger property should return a Logger instance."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    assert isinstance(manager.logger, logging.Logger)


def test_named_logger_returned(tmp_path):
    """Child loggers should be created under hrtk."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    logger = manager.get_logger("filesystem")

    assert logger.name == "hrtk.filesystem"


def test_log_message_written(tmp_path):
    """Messages should be written to the log file."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    manager.logger.info("Hello HRTK")

    # Flush all handlers
    for handler in manager.logger.handlers:
        handler.flush()

    assert manager.log_file.exists()

    text = manager.log_file.read_text(encoding="utf-8")

    assert "Hello HRTK" in text


def test_set_level(tmp_path):
    """Logging level should be changeable."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    manager.set_level(logging.DEBUG)

    assert manager.logger.level == logging.DEBUG


def test_rotating_handler_exists(tmp_path):
    """A RotatingFileHandler should be configured."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    handlers = [
        handler
        for handler in manager.logger.handlers
        if isinstance(handler, RotatingFileHandler)
    ]

    assert len(handlers) == 1


def test_console_logging_optional(tmp_path):
    """Console logging can be disabled."""
    workspace = Workspace(tmp_path / "workspace")

    manager = LoggingManager(
        workspace,
        console=False,
    )

    stream_handlers = [
        handler
        for handler in manager.logger.handlers
        if isinstance(handler, logging.StreamHandler)
        and not isinstance(handler, RotatingFileHandler)
    ]

    assert len(stream_handlers) == 0


def test_repr_contains_class_name(tmp_path):
    """__repr__ should identify the class."""
    workspace = Workspace(tmp_path / "workspace")
    manager = LoggingManager(workspace)

    assert "LoggingManager" in repr(manager)