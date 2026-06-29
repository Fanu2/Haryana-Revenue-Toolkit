"""
Haryana Revenue Toolkit (HRTK)

Domain validation utilities.
"""

from __future__ import annotations

from hrtk.exceptions.exceptions import DomainValidationError


def validate_required(
    value: str,
    field_name: str,
) -> str:
    """
    Validate that a required string is not empty.
    """

    value = value.strip()

    if not value:
        raise DomainValidationError(
            f"{field_name} is required."
        )

    return value


def validate_length(
    value: str,
    field_name: str,
    *,
    minimum: int = 1,
    maximum: int = 255,
) -> str:
    """
    Validate string length.
    """

    length = len(value)

    if length < minimum:
        raise DomainValidationError(
            f"{field_name} must contain at least "
            f"{minimum} characters."
        )

    if length > maximum:
        raise DomainValidationError(
            f"{field_name} must contain no more than "
            f"{maximum} characters."
        )

    return value


def validate_village_code(
    code: str,
) -> str:
    """
    Validate village code.
    """

    code = validate_required(
        code,
        "Village code",
    )

    return validate_length(
        code,
        "Village code",
        maximum=20,
    )


def validate_village_name(
    name: str,
) -> str:
    """
    Validate village name.
    """

    name = validate_required(
        name,
        "Village name",
    )

    return validate_length(
        name,
        "Village name",
        maximum=100,
    )


def validate_tehsil(
    tehsil: str,
) -> str:
    """
    Validate tehsil.
    """

    tehsil = validate_required(
        tehsil,
        "Tehsil",
    )

    return validate_length(
        tehsil,
        "Tehsil",
        maximum=100,
    )


def validate_district(
    district: str,
) -> str:
    """
    Validate district.
    """

    district = validate_required(
        district,
        "District",
    )

    return validate_length(
        district,
        "District",
        maximum=100,
    )


def validate_state(
    state: str,
) -> str:
    """
    Validate state.
    """

    state = validate_required(
        state,
        "State",
    )

    return validate_length(
        state,
        "State",
        maximum=100,
    )