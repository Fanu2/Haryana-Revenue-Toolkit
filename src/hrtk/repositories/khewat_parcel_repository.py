"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel Repository Interface.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from hrtk.domain.land_records.khewat_parcel import (
    KhewatParcel,
)


class KhewatParcelRepository(
    Protocol,
):
    """
    Repository contract for
    KhewatParcel.
    """

    def add(
        self,
        relationship: KhewatParcel,
    ) -> None:
        ...

    def update(
        self,
        relationship: KhewatParcel,
    ) -> None:
        ...

    def remove(
        self,
        relationship_id: UUID,
    ) -> None:
        ...

    def get(
        self,
        relationship_id: UUID,
    ) -> KhewatParcel | None:
        ...

    def list(
        self,
    ) -> list[KhewatParcel]:
        ...

    def exists(
        self,
        relationship_id: UUID,
    ) -> bool:
        ...

    def find_by_khewat(
        self,
        khewat_id: UUID,
    ) -> list[KhewatParcel]:
        ...

    def find_by_parcel(
        self,
        parcel_id: UUID,
    ) -> list[KhewatParcel]:
        ...