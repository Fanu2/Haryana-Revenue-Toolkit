"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Repository Interface.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from hrtk.domain.jamabandi import (
    Jamabandi,
)


class JamabandiRepository(Protocol):
    """
    Repository contract for Jamabandi entities.
    """

    # ---------------------------------------------------------
    # Create / Update / Delete
    # ---------------------------------------------------------

    def add(
        self,
        jamabandi: Jamabandi,
    ) -> None:
        ...

    def update(
        self,
        jamabandi: Jamabandi,
    ) -> None:
        ...

    def remove(
        self,
        jamabandi_id: UUID,
    ) -> None:
        ...

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def get(
        self,
        jamabandi_id: UUID,
    ) -> Jamabandi | None:
        ...

    def list(
        self,
    ) -> list[Jamabandi]:
        ...

    def exists(
        self,
        jamabandi_id: UUID,
    ) -> bool:
        ...

    def find_by_id(
        self,
        jamabandi_id: UUID,
    ) -> Jamabandi | None:
        ...

    def find_by_village(
        self,
        village_id: UUID,
    ) -> list[Jamabandi]:
        ...

    def find_by_year(
        self,
        village_id: UUID,
        year: str,
    ) -> Jamabandi | None:
        ...

    def active(
        self,
    ) -> list[Jamabandi]:
        ...

    def by_status(
        self,
        status: str,
    ) -> list[Jamabandi]:
        ...