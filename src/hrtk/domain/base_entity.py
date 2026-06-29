"""
Haryana Revenue Toolkit (HRTK)

Base domain entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(slots=True, kw_only=True)
class BaseEntity:
    """
    Base class for all HRTK domain entities.

    Responsibilities
    ----------------
    * Unique identity.
    * Creation timestamp.
    * Modification timestamp.
    """

    id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def touch(self) -> None:
        """
        Update the modification timestamp.
        """
        self.updated_at = datetime.now(UTC)

    @property
    def identity(self) -> UUID:
        """
        Return the unique identity.
        """
        return self.id

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(id={self.id})"
        )