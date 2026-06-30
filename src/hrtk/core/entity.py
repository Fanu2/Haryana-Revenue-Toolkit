"""
Haryana Revenue Toolkit (HRTK)

Base Entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(slots=True)
class Entity:
    """
    Root entity for all domain objects.
    """

    id: UUID = field(
        default_factory=uuid4,
    )