"""
Haryana Revenue Toolkit (HRTK)

Integration tests for SQLiteParcelRepository.
"""

from __future__ import annotations

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)
from hrtk.infrastructure.sqlite.database import (
    reset_database,
)
from hrtk.infrastructure.sqlite.sqlite_parcel_repository import (
    SQLiteParcelRepository,
)


def test_add_and_get_parcel() -> None:
    """
    Save a parcel and retrieve it.
    """

    reset_database()

    repository = SQLiteParcelRepository()

    parcel = Parcel(
        number=ParcelNumber(
            rectangle=24,
            killa="7",
        ),
        area=Area.from_kms(
            kanal=2,
            marla=13,
            sarsai=4,
        ),
        remarks="Repository Test",
    )

    repository.add(parcel)

    loaded = repository.get(
        ParcelNumber(
            rectangle=24,
            killa="7",
        ),
    )

    assert loaded is not None

    assert loaded.number.rectangle == 24
    assert loaded.number.killa == "7"

    assert loaded.area.kanal == 2
    assert loaded.area.marla == 13
    assert loaded.area.sarsai == 4

    assert loaded.remarks == "Repository Test"