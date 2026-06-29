"""
Unit tests for ApplicationContext.
"""

from hrtk.application import ApplicationContext
from hrtk.infrastructure.configuration import ConfigurationManager
from hrtk.infrastructure.filesystem import Workspace
from hrtk.infrastructure.logging import LoggingManager


def test_workspace_created(tmp_path):
    app = ApplicationContext(tmp_path / "workspace")

    assert isinstance(app.workspace, Workspace)


def test_configuration_created(tmp_path):
    app = ApplicationContext(tmp_path / "workspace")

    assert isinstance(
        app.configuration,
        ConfigurationManager,
    )


def test_logging_created(tmp_path):
    app = ApplicationContext(tmp_path / "workspace")

    assert isinstance(
        app.logging,
        LoggingManager,
    )


def test_configuration_file_exists(tmp_path):
    app = ApplicationContext(tmp_path / "workspace")

    assert app.configuration.path.exists()


def test_log_directory_exists(tmp_path):
    app = ApplicationContext(tmp_path / "workspace")

    assert app.logging.log_directory.exists()


def test_shutdown(tmp_path):
    app = ApplicationContext(tmp_path / "workspace")

    app.shutdown()

    assert True


def test_repr_contains_class_name(tmp_path):
    app = ApplicationContext(tmp_path / "workspace")

    assert "ApplicationContext" in repr(app)