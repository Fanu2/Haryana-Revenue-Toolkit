"""
Haryana Revenue Toolkit (HRTK)

Ownership Entity.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity
from hrtk.domain.value_objects.fraction import (
    Fraction,
)


@dataclass(slots=True, kw_only=True)
class Ownership(BaseEntity):
    """
    Ownership of a Khewat by an Owner.
    """

    owner_id: UUID

    khewat_id: UUID

    share: Fraction

    remarks: str = ""

    active: bool = True