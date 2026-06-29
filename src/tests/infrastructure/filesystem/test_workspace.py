"""
Unit tests for the Workspace class.
"""

from pathlib import Path

from hrtk.infrastructure.filesystem import Workspace


def test_default_workspace_created(tmp_path, monkeypatch):
    """
    A default workspace should be created in the current working directory.
    """
    monkeypatch.chdir(tmp_path)

    workspace = Workspace()

    assert workspace.root.exists()
    assert workspace.root.is_dir()


def test_custom_workspace_created(tmp_path):
    """
    A custom workspace root should be created automatically.
    """
    root = tmp_path / "MyWorkspace"

    workspace = Workspace(root)

    assert workspace.root == root
    assert root.exists()


def test_all_directories_created(tmp_path):
    """
    Every required workspace directory should exist.
    """
    workspace = Workspace(tmp_path / "workspace")

    expected = [
        workspace.cache,
        workspace.config,
        workspace.database,
        workspace.downloads,
        workspace.logs,
        workspace.plugins,
        workspace.reports,
        workspace.temp,
    ]

    for directory in expected:
        assert directory.exists()
        assert directory.is_dir()


def test_workspace_properties_are_paths(tmp_path):
    """
    Every property should return a pathlib.Path.
    """
    workspace = Workspace(tmp_path / "workspace")

    assert isinstance(workspace.root, Path)
    assert isinstance(workspace.cache, Path)
    assert isinstance(workspace.config, Path)
    assert isinstance(workspace.database, Path)
    assert isinstance(workspace.downloads, Path)
    assert isinstance(workspace.logs, Path)
    assert isinstance(workspace.plugins, Path)
    assert isinstance(workspace.reports, Path)
    assert isinstance(workspace.temp, Path)


def test_workspace_can_be_created_twice(tmp_path):
    """
    Creating the same workspace twice should not fail.
    """
    root = tmp_path / "workspace"

    Workspace(root)
    Workspace(root)

    assert root.exists()


def test_string_root_is_supported(tmp_path):
    """
    The constructor should accept string paths.
    """
    root = str(tmp_path / "workspace")

    workspace = Workspace(root)

    assert workspace.root.exists()


def test_string_representation(tmp_path):
    """
    __str__ should return the workspace root.
    """
    workspace = Workspace(tmp_path / "workspace")

    assert str(workspace) == str(workspace.root)


def test_repr_contains_workspace(tmp_path):
    """
    __repr__ should contain the class name.
    """
    workspace = Workspace(tmp_path / "workspace")

    assert "Workspace" in repr(workspace)