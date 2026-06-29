"""
Unit tests for Village.
"""

from __future__ import annotations

from time import sleep

import pytest

from hrtk.domain.village import Village
from hrtk.exceptions.exceptions import DomainValidationError


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


# ----------------------------------------------------------------------
# Construction
# ----------------------------------------------------------------------


def test_default_state() -> None:
    village = make_village()

    assert village.state == "Haryana"
    assert village.active is True


def test_display_name() -> None:
    village = make_village()

    assert village.display_name == "Sirsa (001)"


def test_string_representation() -> None:
    village = make_village()

    assert str(village) == "Sirsa (001)"


# ----------------------------------------------------------------------
# Rename
# ----------------------------------------------------------------------


def test_rename() -> None:
    village = make_village()

    village.rename("Rania")

    assert village.name == "Rania"


def test_change_code() -> None:
    village = make_village()

    village.change_code("002")

    assert village.code == "002"


def test_change_tehsil() -> None:
    village = make_village()

    village.change_tehsil("Rania")

    assert village.tehsil == "Rania"


def test_change_district() -> None:
    village = make_village()

    village.change_district("Hisar")

    assert village.district == "Hisar"


def test_change_state() -> None:
    village = make_village()

    village.change_state("Punjab")

    assert village.state == "Punjab"


# ----------------------------------------------------------------------
# Active Flag
# ----------------------------------------------------------------------


def test_deactivate() -> None:
    village = make_village()

    village.deactivate()

    assert village.active is False


def test_activate() -> None:
    village = make_village()

    village.deactivate()
    village.activate()

    assert village.active is True


def test_activate_twice() -> None:
    village = make_village()

    village.activate()
    village.activate()

    assert village.active is True


def test_deactivate_twice() -> None:
    village = make_village()

    village.deactivate()
    village.deactivate()

    assert village.active is False


# ----------------------------------------------------------------------
# Timestamp
# ----------------------------------------------------------------------


def test_touch_updates_timestamp() -> None:
    village = make_village()

    previous = village.updated_at

    sleep(0.001)

    village.rename("Rania")

    assert village.updated_at > previous


# ----------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "code",
    [
        "",
        "   ",
    ],
)
def test_invalid_code(code: str) -> None:
    with pytest.raises(DomainValidationError):
        Village(
            code=code,
            name="Sirsa",
            tehsil="Sirsa",
            district="Sirsa",
        )


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(DomainValidationError):
        Village(
            code="001",
            name=name,
            tehsil="Sirsa",
            district="Sirsa",
        )


@pytest.mark.parametrize(
    "tehsil",
    [
        "",
        "   ",
    ],
)
def test_invalid_tehsil(tehsil: str) -> None:
    with pytest.raises(DomainValidationError):
        Village(
            code="001",
            name="Sirsa",
            tehsil=tehsil,
            district="Sirsa",
        )


@pytest.mark.parametrize(
    "district",
    [
        "",
        "   ",
    ],
)
def test_invalid_district(district: str) -> None:
    with pytest.raises(DomainValidationError):
        Village(
            code="001",
            name="Sirsa",
            tehsil="Sirsa",
            district=district,
        )


@pytest.mark.parametrize(
    "state",
    [
        "",
        "   ",
    ],
)
def test_invalid_state(state: str) -> None:
    with pytest.raises(DomainValidationError):
        Village(
            code="001",
            name="Sirsa",
            tehsil="Sirsa",
            district="Sirsa",
            state=state,
        )