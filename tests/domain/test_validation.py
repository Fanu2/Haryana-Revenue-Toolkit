"""
Unit tests for domain validation.
"""

from __future__ import annotations

import pytest

from hrtk.domain.validation import (
    validate_district,
    validate_length,
    validate_required,
    validate_state,
    validate_tehsil,
    validate_village_code,
    validate_village_name,
)
from hrtk.exceptions.exceptions import DomainValidationError


# ------------------------------------------------------------------
# validate_required
# ------------------------------------------------------------------

def test_validate_required_accepts_value() -> None:
    assert validate_required("Sirsa", "Village") == "Sirsa"


def test_validate_required_trims_whitespace() -> None:
    assert validate_required("  Sirsa  ", "Village") == "Sirsa"


@pytest.mark.parametrize(
    "value",
    [
        "",
        "   ",
    ],
)
def test_validate_required_rejects_empty(value: str) -> None:
    with pytest.raises(DomainValidationError):
        validate_required(value, "Village")


# ------------------------------------------------------------------
# validate_length
# ------------------------------------------------------------------

def test_validate_length_accepts_valid_string() -> None:
    assert (
        validate_length(
            "Sirsa",
            "Village",
            minimum=3,
            maximum=10,
        )
        == "Sirsa"
    )


def test_validate_length_rejects_short_string() -> None:
    with pytest.raises(DomainValidationError):
        validate_length(
            "AB",
            "Village",
            minimum=3,
            maximum=10,
        )


def test_validate_length_rejects_long_string() -> None:
    with pytest.raises(DomainValidationError):
        validate_length(
            "A" * 25,
            "Village",
            minimum=1,
            maximum=20,
        )


# ------------------------------------------------------------------
# Village-specific validators
# ------------------------------------------------------------------

def test_validate_village_code() -> None:
    assert validate_village_code("001") == "001"


def test_validate_village_name() -> None:
    assert validate_village_name("Sirsa") == "Sirsa"


def test_validate_tehsil() -> None:
    assert validate_tehsil("Sirsa") == "Sirsa"


def test_validate_district() -> None:
    assert validate_district("Sirsa") == "Sirsa"


def test_validate_state() -> None:
    assert validate_state("Haryana") == "Haryana"


# ------------------------------------------------------------------
# Invalid values
# ------------------------------------------------------------------

@pytest.mark.parametrize(
    "validator",
    [
        validate_village_code,
        validate_village_name,
        validate_tehsil,
        validate_district,
        validate_state,
    ],
)
def test_specific_validators_reject_empty(validator) -> None:
    with pytest.raises(DomainValidationError):
        validator("")


@pytest.mark.parametrize(
    "validator",
    [
        validate_village_code,
        validate_village_name,
        validate_tehsil,
        validate_district,
        validate_state,
    ],
)
def test_specific_validators_reject_whitespace(validator) -> None:
    with pytest.raises(DomainValidationError):
        validator("     ")