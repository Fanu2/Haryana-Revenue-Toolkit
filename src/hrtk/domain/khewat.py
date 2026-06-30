"""
Haryana Revenue Toolkit (HRTK)

Khewat domain entity.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity


@dataclass(slots=True)
class Khewat(BaseEntity):
    """
    Represents a revenue Khewat (Account).
    """

    village_id: UUID

    khewat_no: str

    old_khewat_no: str = ""

    jamabandi_year: str = ""

    remarks: str = ""

    active: bool = True

    def activate(self) -> None:
        """
        Mark the Khewat as active.
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Mark the Khewat as inactive.
        """
        self.active = False

    @property
    def display_name(self) -> str:
        """
        Return the display name.
        """
        return self.khewat_no

    def __str__(self) -> str:
        return (
            f"Khewat {self.khewat_no}"
        )