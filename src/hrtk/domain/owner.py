"""
Haryana Revenue Toolkit (HRTK)

Owner domain entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity


@dataclass(slots=True)
class Owner(BaseEntity):
    """
    Represents a land owner.
    """

    village_id: UUID

    owner_code: str

    owner_name: str

    father_name: str = ""

    address: str = ""

    mobile: str = ""

    remarks: str = ""

    active: bool = True

    def activate(self) -> None:
        """
        Mark the owner as active.
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Mark the owner as inactive.
        """
        self.active = False

    @property
    def display_name(self) -> str:
        """
        Return the display name of the owner.
        """
        return self.owner_name

    def __str__(self) -> str:
        return (
            f"{self.owner_code} - "
            f"{self.owner_name}"
        )