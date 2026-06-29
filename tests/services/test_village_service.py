"""
Haryana Revenue Toolkit (HRTK)

Unit tests for VillageService.
"""

from __future__ import annotations

from hrtk.domain.village import Village
from hrtk.repositories.village_repository import VillageRepository
from hrtk.services.village_service import VillageService


def make_service() -> VillageService:
    """
    Create a VillageService for testing.
    """
    repository = VillageRepository()
    return VillageService(repository)


def make_village() -> Village:
    """
    Create a valid Village.
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


def test_service_can_be_created() -> None:
    service = make_service()

    assert isinstance(service, VillageService)


# ---------------------------------------------------------
# Register
# ---------------------------------------------------------


def test_register_village() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    assert service.count() == 1


# ---------------------------------------------------------
# Activate / Deactivate
# ---------------------------------------------------------


def test_deactivate_village() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    service.deactivate(village)

    assert village.active is False


def test_activate_village() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    service.deactivate(village)
    service.activate(village)

    assert village.active is True


# ---------------------------------------------------------
# Find
# ---------------------------------------------------------


def test_find_by_code() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    assert service.find_by_code("001") is village


# ---------------------------------------------------------
# Query Operations
# ---------------------------------------------------------


def test_get() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    assert service.get(village.id) is village


def test_exists() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    assert service.exists(village.id)


def test_all() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    assert service.all() == [village]


def test_count() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    assert service.count() == 1


# ---------------------------------------------------------
# Representation
# ---------------------------------------------------------


def test_repr() -> None:
    service = make_service()

    assert "VillageService" in repr(service)