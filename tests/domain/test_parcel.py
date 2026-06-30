"""
Haryana Revenue Toolkit (HRTK)

Unit tests for Parcel entity.
"""

from __future__ import annotations

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import ParcelNumber


# ==========================================================
# Construction
# ==========================================================


def test_create_parcel() -> None:

    parcel = Parcel(
        number=ParcelNumber(
            rectangle=24,
            killa="7",
        ),
        area=Area.from_kms(
            kanal=8,
            marla=12,
            sarsai=5,
        ),
    )

    assert parcel.number.rectangle == 24
    assert parcel.number.killa == "7"
    assert parcel.area.kanal == 8
    assert parcel.area.marla == 12
    assert parcel.area.sarsai == 5


# ==========================================================
# Empty Parcel
# ==========================================================


def test_empty_parcel() -> None:

    parcel = Parcel(
        number=ParcelNumber(
            rectangle=10,
            killa="5",
        ),
        area=Area.zero(),
    )

    assert parcel.is_empty is True


def test_non_empty_parcel() -> None:

    parcel = Parcel(
        number=ParcelNumber(
            rectangle=10,
            killa="5",
        ),
        area=Area.from_kms(
            kanal=1,
        ),
    )

    assert parcel.is_empty is False


# ==========================================================
# Formatting
# ==========================================================


def test_string() -> None:

    parcel = Parcel(
        number=ParcelNumber(
            rectangle=24,
            killa="7/1",
        ),
        area=Area.from_kms(
            kanal=3,
            marla=5,
        ),
    )

    assert str(parcel) == "24//7/1"


def test_display() -> None:

    parcel = Parcel(
        number=ParcelNumber(
            rectangle=24,
            killa="7",
        ),
        area=Area.from_kms(
            kanal=2,
            marla=10,
            sarsai=3,
        ),
    )

    assert (
        parcel.display()
        == "24//7 (2 Kanal 10 Marla 3 Sarsai)"
    )


def test_repr() -> None:

    parcel = Parcel(
        number=ParcelNumber(
            rectangle=24,
            killa="7",
        ),
        area=Area.from_kms(
            kanal=1,
        ),
    )

    assert "Parcel(" in repr(parcel)