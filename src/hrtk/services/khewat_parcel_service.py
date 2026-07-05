"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.land_records.khewat_parcel import (
    KhewatParcel,
)

from hrtk.repositories.khewat_parcel_repository import (
    KhewatParcelRepository,
)

from hrtk.services.base_service import (
    BaseService,
)


class KhewatParcelService(
    BaseService[KhewatParcel],
):
    """
    Service for Khewat-Parcel relationships.
    """

    def __init__(
        self,
        repository: KhewatParcelRepository,
    ) -> None:

        super().__init__(
            repository,
        )

    @property
    def repository(
        self,
    ) -> KhewatParcelRepository:

        return super().repository

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def register(
        self,
        relationship: KhewatParcel,
    ) -> None:

        self.repository.add(
            relationship,
        )

    def update(
        self,
        relationship: KhewatParcel,
    ) -> None:

        self.repository.update(
            relationship,
        )

    def remove(
        self,
        relationship_id: UUID,
    ) -> None:

        self.repository.remove(
            relationship_id,
        )

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def find_by_khewat(
        self,
        khewat_id: UUID,
    ) -> list[KhewatParcel]:

        return self.repository.find_by_khewat(
            khewat_id,
        )

    def find_by_parcel(
        self,
        parcel_id: UUID,
    ) -> list[KhewatParcel]:

        return self.repository.find_by_parcel(
            parcel_id,
        )