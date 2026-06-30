"""
Haryana Revenue Toolkit (HRTK)

Unit tests for Area value object.
"""

from __future__ import annotations

import pytest

from hrtk.domain.value_objects.area import Area


# ==========================================================
# Construction
# ==========================================================


def test_zero() -> None:
    """
    Zero area.
    """

    area = Area.zero()

    assert area.total_sarsai == 0
    assert area.kanal == 0
    assert area.marla == 0
    assert area.sarsai == 0


def test_from_total_sarsai() -> None:
    """
    Construct directly from total sarsai.
    """

    area = Area.from_total_sarsai(
        180,
    )

    assert area.total_sarsai == 180
    assert area.kanal == 1
    assert area.marla == 0
    assert area.sarsai == 0


def test_from_kms() -> None:
    """
    Construct from Kanal-Marla-Sarsai.
    """

    area = Area.from_kms(
        kanal=2,
        marla=13,
        sarsai=4,
    )

    assert area.total_sarsai == 481


# ==========================================================
# Conversion
# ==========================================================


def test_conversion() -> None:
    """
    Convert total sarsai back to KMS.
    """

    area = Area.from_total_sarsai(
        481,
    )

    assert area.kanal == 2
    assert area.marla == 13
    assert area.sarsai == 4


def test_one_kanal() -> None:
    """
    Exactly one kanal.
    """

    area = Area.from_total_sarsai(
        180,
    )

    assert area.kanal == 1
    assert area.marla == 0
    assert area.sarsai == 0


def test_one_marla() -> None:
    """
    Exactly one marla.
    """

    area = Area.from_total_sarsai(
        9,
    )

    assert area.kanal == 0
    assert area.marla == 1
    assert area.sarsai == 0


def test_one_sarsai() -> None:
    """
    Exactly one sarsai.
    """

    area = Area.from_total_sarsai(
        1,
    )

    assert area.kanal == 0
    assert area.marla == 0
    assert area.sarsai == 1


# ==========================================================
# Formatting
# ==========================================================


def test_string() -> None:
    """
    Short string representation.
    """

    area = Area.from_kms(
        kanal=2,
        marla=13,
        sarsai=4,
    )

    assert str(area) == "2K-13M-4S"


def test_display() -> None:
    """
    Long display string.
    """

    area = Area.from_kms(
        kanal=2,
        marla=13,
        sarsai=4,
    )

    assert (
        area.display()
        == "2 Kanal 13 Marla 4 Sarsai"
    )


# ==========================================================
# Validation
# ==========================================================


def test_negative_total_sarsai() -> None:
    """
    Negative total sarsai is invalid.
    """

    with pytest.raises(ValueError):
        Area.from_total_sarsai(
            -1,
        )


def test_negative_kanal() -> None:
    """
    Negative kanal is invalid.
    """

    with pytest.raises(ValueError):
        Area.from_kms(
            kanal=-1,
        )


def test_negative_marla() -> None:
    """
    Negative marla is invalid.
    """

    with pytest.raises(ValueError):
        Area.from_kms(
            marla=-1,
        )


def test_negative_sarsai() -> None:
    """
    Negative sarsai is invalid.
    """

    with pytest.raises(ValueError):
        Area.from_kms(
            sarsai=-1,
        )