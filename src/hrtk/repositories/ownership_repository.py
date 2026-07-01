"""
Haryana Revenue Toolkit (HRTK)

Ownership Repository Contract.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from hrtk.domain.ownership import Ownership


class OwnershipRepository(Protocol):
    """
    Repository contract for Ownership.
    """

    def add(
        self,
        ownership: Ownership,
    ) -> None:
        ...

    def update(
        self,
        ownership: Ownership,
    ) -> None:
        ...

    def remove(
        self,
        ownership_id: UUID,
    ) -> None:
        ...

    def get(
        self,
        ownership_id: UUID,
    ) -> Ownership | None:
        ...

    def list(
        self,
    ) -> list[Ownership]:
        ...

    def find_by_owner(
        self,
        owner_id: UUID,
    ) -> list[Ownership]:
        ...

    def find_by_khewat(
        self,
        khewat_id: UUID,
    ) -> list[Ownership]:
        ...

    def exists(
        self,
        owner_id: UUID,
        khewat_id: UUID,
    ) -> bool:
        """
        True if the owner already has an ownership
        record in the specified Khewat.
        """
        ...       

    def count(
        self,
    ) -> int:
        """
        Return total ownership records.
        """
        ...

    def exists(
        self,
        owner_id: UUID,
        khewat_id: UUID,
    ) -> bool:
     ...