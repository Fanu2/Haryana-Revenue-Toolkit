"""
Haryana Revenue Toolkit (HRTK)

Village domain entity.
"""

from __future__ import annotations

from dataclasses import dataclass

from hrtk.domain.base_entity import BaseEntity
from hrtk.domain.validation import (
    validate_district,
    validate_state,
    validate_tehsil,
    validate_village_code,
    validate_village_name,
)


@dataclass(slots=True, kw_only=True)
class Village(BaseEntity):
    """
    Represents a revenue village.
    """

    code: str
    name: str
    tehsil: str
    district: str

    state: str = "Haryana"
    active: bool = True

    def __post_init__(self) -> None:
        """
        Validate the initial state.
        """
        self.code = validate_village_code(self.code)
        self.name = validate_village_name(self.name)
        self.tehsil = validate_tehsil(self.tehsil)
        self.district = validate_district(self.district)
        self.state = validate_state(self.state)

    @property
    def display_name(self) -> str:
        """
        Return the display name.
        """
        return f"{self.name} ({self.code})"

    def rename(self, name: str) -> None:
        """
        Rename the village.
        """
        self.name = validate_village_name(name)
        self.touch()

    def change_code(self, code: str) -> None:
        """
        Change the village code.
        """
        self.code = validate_village_code(code)
        self.touch()

    def change_tehsil(self, tehsil: str) -> None:
        """
        Change the tehsil.
        """
        self.tehsil = validate_tehsil(tehsil)
        self.touch()

    def change_district(self, district: str) -> None:
        """
        Change the district.
        """
        self.district = validate_district(district)
        self.touch()

    def change_state(self, state: str) -> None:
        """
        Change the state.
        """
        self.state = validate_state(state)
        self.touch()

    def activate(self) -> None:
        """
        Activate the village.
        """
        if not self.active:
            self.active = True
            self.touch()

    def deactivate(self) -> None:
        """
        Deactivate the village.
        """
        if self.active:
            self.active = False
            self.touch()

    def __str__(self) -> str:
        """
        Return the display name.
        """
        return self.display_name