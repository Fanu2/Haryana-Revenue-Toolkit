"""
Haryana Revenue Toolkit (HRTK)

Parcel Repository Interface.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)


class ParcelRepository(Protocol):
    """
    Repository contract for Parcel entities.
    """

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def add(
        self,
        parcel: Parcel,
    ) -> None:
        ...

    def update(
        self,
        parcel: Parcel,
    ) -> None:
        ...

    def remove(
        self,
        parcel_id: UUID,
    ) -> None:
        ...

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def get(
        self,
        parcel_id: UUID,
    ) -> Parcel | None:
        ...

    def list(
        self,
    ) -> list[Parcel]:
        ...

    def exists(
        self,
        parcel_id: UUID,
    ) -> bool:
        ...

    def find_by_number(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:
        ...