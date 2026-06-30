"""
Haryana Revenue Toolkit (HRTK)

Integration tests for SQLiteVillageRepository.
"""

from __future__ import annotations

from hrtk.domain.village import Village
from hrtk.infrastructure.sqlite.database import (
    reset_database,
)
from hrtk.infrastructure.sqlite.sqlite_village_repository import (
    SQLiteVillageRepository,
)


def test_add_and_get_village() -> None:
    """
    Save and reload a village.
    """

    reset_database()

    repository = SQLiteVillageRepository()

    village = Village(
        code="HR001",
        name="Taruana",
        tehsil="Kalanwali",
        district="Sirsa",
    )

    repository.add(village)

    loaded = repository.get("HR001")

    assert loaded is not None
    assert loaded.code == "HR001"
    assert loaded.name == "Taruana"
    assert loaded.tehsil == "Kalanwali"
    assert loaded.district == "Sirsa"
    assert loaded.state == "Haryana"
    assert loaded.active