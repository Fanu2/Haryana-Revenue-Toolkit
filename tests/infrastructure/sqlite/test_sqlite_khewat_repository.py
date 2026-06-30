"""
Haryana Revenue Toolkit (HRTK)

Integration tests for SQLiteKhewatRepository.
"""

from __future__ import annotations

from uuid import uuid4

from hrtk.domain.khewat import Khewat
from hrtk.infrastructure.sqlite.database import (
    reset_database,
)
from hrtk.infrastructure.sqlite.sqlite_khewat_repository import (
    SQLiteKhewatRepository,
)


def test_add_and_find_number() -> None:

    reset_database()

    repository = SQLiteKhewatRepository()

    village_id = uuid4()

    khewat = Khewat(
        village_id=village_id,
        khewat_no="15",
        old_khewat_no="10",
        jamabandi_year="2023-24",
        remarks="Integration Test",
    )

    repository.add(khewat)

    loaded = repository.find_by_number(
        village_id,
        "15",
    )

    assert loaded is not None

    assert loaded.khewat_no == "15"
    assert loaded.old_khewat_no == "10"
    assert loaded.jamabandi_year == "2023-24"
    assert loaded.remarks == "Integration Test"
    assert loaded.active


def test_find_by_village() -> None:

    reset_database()

    repository = SQLiteKhewatRepository()

    village_id = uuid4()

    repository.add(
        Khewat(
            village_id=village_id,
            khewat_no="1",
        )
    )

    repository.add(
        Khewat(
            village_id=village_id,
            khewat_no="2",
        )
    )

    result = repository.find_by_village(
        village_id,
    )

    assert len(result) >= 2