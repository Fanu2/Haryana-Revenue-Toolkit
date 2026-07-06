"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.land_records.khewat_parcel import (
    KhewatParcel,
)

from hrtk.infrastructure.sqlite.models.khewat_parcel_model import (
    KhewatParcelModel,
)


class KhewatParcelMapper:
    """
    Maps KhewatParcel <-> KhewatParcelModel.
    """

    @staticmethod
    def to_model(
        relationship: KhewatParcel,
    ) -> KhewatParcelModel:
        """
        Convert domain entity to SQLite model.
        """

        return KhewatParcelModel(
            id=str(
                relationship.id,
            ),
            khewat_id=str(
                relationship.khewat_id,
            ),
            parcel_id=str(
                relationship.parcel_id,
            ),
            remarks=relationship.remarks,
        )

    @staticmethod
    def to_domain(
        model: KhewatParcelModel,
    ) -> KhewatParcel:
        """
        Convert SQLite model to domain entity.
        """

        return KhewatParcel(
            id=UUID(
                model.id,
            ),
            khewat_id=UUID(
                model.khewat_id,
            ),
            parcel_id=UUID(
                model.parcel_id,
            ),
            remarks=model.remarks,
        )
