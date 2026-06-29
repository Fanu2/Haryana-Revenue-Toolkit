"""
Haryana Revenue Toolkit (HRTK)

Unit tests for BaseRepository.
"""

from __future__ import annotations

import pytest

from hrtk.domain.village import Village
from hrtk.exceptions.exceptions import (
    DuplicateEntityError,
    EntityNotFoundError,
)
from hrtk.repositories.base_repository import BaseRepository


def make_village() -> Village:
    """
    Create a valid village.
    """
    return Village(
        code="001",
        name="Sirsa",
        tehsil="Sirsa",
        district="Sirsa",
    )


# ---------------------------------------------------------
# Construction
# ---------------------------------------------------------


def test_repository_is_empty() -> None:
    repo = BaseRepository[Village]()

    assert len(repo) == 0
    assert repo.count() == 0
    assert not repo


# ---------------------------------------------------------
# Add
# ---------------------------------------------------------


def test_add_entity() -> None:
    repo = BaseRepository[Village]()
    village = make_village()

    repo.add(village)

    assert len(repo) == 1
    assert village in repo


def test_add_duplicate_entity() -> None:
    repo = BaseRepository[Village]()
    village = make_village()

    repo.add(village)

    with pytest.raises(DuplicateEntityError):
        repo.add(village)


# ---------------------------------------------------------
# Get
# ---------------------------------------------------------


def test_get_entity() -> None:
    repo = BaseRepository[Village]()
    village = make_village()

    repo.add(village)

    assert repo.get(village.id) is village


def test_get_missing_entity() -> None:
    repo = BaseRepository[Village]()

    village = make_village()

    assert repo.get(village.id) is None


# ---------------------------------------------------------
# Exists
# ---------------------------------------------------------


def test_exists() -> None:
    repo = BaseRepository[Village]()
    village = make_village()

    repo.add(village)

    assert repo.exists(village.id)


def test_missing_entity_does_not_exist() -> None:
    repo = BaseRepository[Village]()

    village = make_village()

    assert not repo.exists(village.id)


# ---------------------------------------------------------
# Update
# ---------------------------------------------------------


def test_update_entity() -> None:
    repo = BaseRepository[Village]()
    village = make_village()

    repo.add(village)

    village.rename("Rania")

    repo.update(village)

    assert repo.get(village.id).name == "Rania"


def test_update_missing_entity() -> None:
    repo = BaseRepository[Village]()

    village = make_village()

    with pytest.raises(EntityNotFoundError):
        repo.update(village)


# ---------------------------------------------------------
# Remove
# ---------------------------------------------------------


def test_remove_entity() -> None:
    repo = BaseRepository[Village]()
    village = make_village()

    repo.add(village)

    repo.remove(village)

    assert len(repo) == 0


def test_remove_missing_entity() -> None:
    repo = BaseRepository[Village]()

    village = make_village()

    with pytest.raises(EntityNotFoundError):
        repo.remove(village)


# ---------------------------------------------------------
# Clear
# ---------------------------------------------------------


def test_clear_repository() -> None:
    repo = BaseRepository[Village]()

    repo.add(make_village())

    repo.clear()

    assert len(repo) == 0


# ---------------------------------------------------------
# Iteration
# ---------------------------------------------------------


def test_iteration() -> None:
    repo = BaseRepository[Village]()

    village = make_village()

    repo.add(village)

    assert list(repo) == [village]


def test_all_returns_list() -> None:
    repo = BaseRepository[Village]()

    village = make_village()

    repo.add(village)

    assert repo.all() == [village]


# ---------------------------------------------------------
# Representation
# ---------------------------------------------------------


def test_repr_contains_class_name() -> None:
    repo = BaseRepository[Village]()

    assert "BaseRepository" in repr(repo)