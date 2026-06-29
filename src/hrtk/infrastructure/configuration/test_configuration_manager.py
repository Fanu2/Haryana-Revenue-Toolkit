"""
Unit tests for ConfigurationManager.
"""

from pathlib import Path

import yaml

from hrtk.infrastructure.configuration import ConfigurationManager
from hrtk.infrastructure.filesystem import Workspace


def test_configuration_file_created(tmp_path):
    """
    ConfigurationManager should automatically create config.yaml.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    assert config.path.exists()
    assert config.path.is_file()


def test_default_values_loaded(tmp_path):
    """
    Default configuration should be available.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    assert config.get("application.name") == "Haryana Revenue Toolkit"
    assert config.get("ui.theme") == "light"
    assert config.get("logging.level") == "INFO"


def test_get_unknown_key_returns_default(tmp_path):
    """
    Missing keys should return the supplied default.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    assert config.get("does.not.exist", "default") == "default"


def test_set_value(tmp_path):
    """
    Values should be changeable.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    config.set("ui.theme", "dark")

    assert config.get("ui.theme") == "dark"


def test_save_and_reload(tmp_path):
    """
    Saved configuration should survive reload.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    config.set("ui.theme", "dark")
    config.save()

    config.reload()

    assert config.get("ui.theme") == "dark"


def test_reset_restores_defaults(tmp_path):
    """
    Reset should restore default configuration.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    config.set("ui.theme", "dark")
    config.reset()

    assert config.get("ui.theme") == "light"


def test_contains_operator(tmp_path):
    """
    __contains__ should work with dotted keys.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    assert "ui.theme" in config
    assert "ui.invalid" not in config


def test_getitem_operator(tmp_path):
    """
    __getitem__ should return values.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    assert config["ui.theme"] == "light"


def test_setitem_operator(tmp_path):
    """
    __setitem__ should update values.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    config["logging.level"] = "DEBUG"

    assert config["logging.level"] == "DEBUG"


def test_configuration_written_as_yaml(tmp_path):
    """
    Configuration file should contain valid YAML.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    config.set("ui.theme", "dark")
    config.save()

    with config.path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    assert data["ui"]["theme"] == "dark"


def test_data_property_returns_copy(tmp_path):
    """
    data property should return a defensive copy.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    data = config.data

    data["ui"]["theme"] = "modified"

    assert config.get("ui.theme") == "light"


def test_repr_contains_class_name(tmp_path):
    """
    __repr__ should identify the class.
    """
    workspace = Workspace(tmp_path / "workspace")

    config = ConfigurationManager(workspace)

    assert "ConfigurationManager" in repr(config)