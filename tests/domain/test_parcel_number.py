"""
Haryana Revenue Toolkit (HRTK)

Unit tests for ParcelNumber.
"""

from __future__ import annotations

import pytest

from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)


# ==========================================================
# Construction
# ==========================================================


def test_create_simple() -> None:

    number = ParcelNumber(
        rectangle=24,
        killa="7",
    )

    assert number.rectangle == 24
    assert number.killa == "7"


def test_create_subdivision() -> None:

    number = ParcelNumber(
        rectangle=24,
        killa="7/1",
    )

    assert str(number) == "24//7/1"


def test_create_nested_subdivision() -> None:

    number = ParcelNumber(
        rectangle=24,
        killa="7/1/2",
    )

    assert str(number) == "24//7/1/2"


# ==========================================================
# Formatting
# ==========================================================


def test_string() -> None:

    number = ParcelNumber(
        rectangle=31,
        killa="18/2",
    )

    assert str(number) == "31//18/2"


def test_display() -> None:

    number = ParcelNumber(
        rectangle=31,
        killa="18/2",
    )

    assert (
        number.display()
        == "Rectangle 31 Killa 18/2"
    )


def test_repr() -> None:

    number = ParcelNumber(
        rectangle=5,
        killa="3",
    )

    assert (
        repr(number)
        == "ParcelNumber(5//3)"
    )


# ==========================================================
# Validation
# ==========================================================


def test_invalid_rectangle_zero() -> None:

    with pytest.raises(ValueError):

        ParcelNumber(
            rectangle=0,
            killa="7",
        )


def test_invalid_rectangle_negative() -> None:

    with pytest.raises(ValueError):

        ParcelNumber(
            rectangle=-1,
            killa="7",
        )


def test_empty_killa() -> None:

    with pytest.raises(ValueError):

        ParcelNumber(
            rectangle=24,
            killa="",
        )


def test_space_in_killa() -> None:

    with pytest.raises(ValueError):

        ParcelNumber(
            rectangle=24,
            killa="7 /1",
        )


def test_leading_slash() -> None:

    with pytest.raises(ValueError):

        ParcelNumber(
            rectangle=24,
            killa="/7",
        )


def test_trailing_slash() -> None:

    with pytest.raises(ValueError):

        ParcelNumber(
            rectangle=24,
            killa="7/",
        )


def test_double_slash() -> None:

    with pytest.raises(ValueError):

        ParcelNumber(
            rectangle=24,
            killa="7//1",
        )