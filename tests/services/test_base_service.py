"""
Haryana Revenue Toolkit (HRTK)

Unit tests for BaseService.
"""

from __future__ import annotations

from hrtk.domain.village import Village
from hrtk.repositories.base_repository import BaseRepository
from hrtk.services.base_service import BaseService


def make_village() -> Village:
    """
    Create a valid Village for testing.
    """
    return Village(
        code="001",
        name="Sirsa",
        tehsil="Sirsa",
        district="Sirsa",
    )


def make_service() -> BaseService[Village]:
    """
    Create a service with an empty repository.
    """
    repository = BaseRepository[Village]()
    return BaseService(repository)


# ---------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------


def test_service_can_be_created() -> None:
    service = make_service()

    assert isinstance(service, BaseService)


def test_repository_property() -> None:
    service = make_service()

    assert service.repository is not None


# ---------------------------------------------------------------------
# Empty Repository
# ---------------------------------------------------------------------


def test_empty_service() -> None:
    service = make_service()

    assert service.count() == 0
    assert len(service) == 0
    assert not service


# ---------------------------------------------------------------------
# Query Operations
# ---------------------------------------------------------------------


def test_get_entity() -> None:
    service = make_service()

    village = make_village()

    service.repository.add(village)

    assert service.get(village.id) is village


def test_exists() -> None:
    service = make_service()

    village = make_village()

    service.repository.add(village)

    assert service.exists(village.id)


def test_all() -> None:
    service = make_service()

    village = make_village()

    service.repository.add(village)

    assert service.all() == [village]


def test_count() -> None:
    service = make_service()

    village = make_village()

    service.repository.add(village)

    assert service.count() == 1


# ---------------------------------------------------------------------
# Representation
# ---------------------------------------------------------------------


def test_repr() -> None:
    service = make_service()

    assert "BaseService" in repr(service)