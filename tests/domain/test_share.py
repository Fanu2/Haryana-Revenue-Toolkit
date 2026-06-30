"""
Haryana Revenue Toolkit (HRTK)

Unit tests for Share value object.
"""

from __future__ import annotations

import pytest

from hrtk.domain.value_objects.share import Share


# ==========================================================
# Construction
# ==========================================================


def test_create_share() -> None:

    share = Share(
        numerator=1,
        denominator=4,
    )

    assert share.numerator == 1
    assert share.denominator == 4


def test_normalization() -> None:

    share = Share(
        numerator=2,
        denominator=4,
    )

    assert share.numerator == 1
    assert share.denominator == 2


def test_zero_share() -> None:

    share = Share(
        numerator=0,
        denominator=1,
    )

    assert str(share) == "0/1"


# ==========================================================
# Formatting
# ==========================================================


def test_string() -> None:

    share = Share(
        numerator=7,
        denominator=96,
    )

    assert str(share) == "7/96"


def test_display() -> None:

    share = Share(
        numerator=7,
        denominator=96,
    )

    assert (
        share.display()
        == "7 Share out of 96"
    )


def test_repr() -> None:

    share = Share(
        numerator=1,
        denominator=2,
    )

    assert repr(share) == "Share(1/2)"


# ==========================================================
# Percentage
# ==========================================================


def test_percentage() -> None:

    share = Share(
        numerator=1,
        denominator=4,
    )

    assert share.percentage == 25.0


def test_fraction_property() -> None:

    share = Share(
        numerator=3,
        denominator=8,
    )

    assert str(share.fraction) == "3/8"


# ==========================================================
# Arithmetic
# ==========================================================


def test_addition() -> None:

    first = Share(1, 4)
    second = Share(1, 4)

    result = first + second

    assert str(result) == "1/2"


def test_subtraction() -> None:

    first = Share(3, 4)
    second = Share(1, 4)

    result = first - second

    assert str(result) == "1/2"


# ==========================================================
# Validation
# ==========================================================


def test_negative_numerator() -> None:

    with pytest.raises(ValueError):

        Share(
            numerator=-1,
            denominator=2,
        )


def test_zero_denominator() -> None:

    with pytest.raises(ValueError):

        Share(
            numerator=1,
            denominator=0,
        )


def test_negative_denominator() -> None:

    with pytest.raises(ValueError):

        Share(
            numerator=1,
            denominator=-2,
        )


def test_negative_result() -> None:

    with pytest.raises(ValueError):

        Share(1, 4) - Share(1, 2)