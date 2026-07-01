"""
Haryana Revenue Toolkit (HRTK)

Khewat Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.khewat import Khewat
from hrtk.infrastructure.sqlite.models.khewat_model import (
    KhewatModel,
)


class KhewatMapper:
    """
    Maps Khewat <-> KhewatModel.
    """

    @staticmethod
    def to_model(
        khewat: Khewat,
    ) -> KhewatModel:

        return KhewatModel(
            id=str(khewat.id),
            village_id=str(khewat.village_id),
            khewat_no=khewat.khewat_no,
            old_khewat_no=khewat.old_khewat_no,
            jamabandi_year=khewat.jamabandi_year,
            remarks=khewat.remarks,
            active=khewat.active,
        )

    @staticmethod
    def to_domain(
        model: KhewatModel,
    ) -> Khewat:

        return Khewat(
            id=UUID(model.id),
            village_id=UUID(model.village_id),
            khewat_no=model.khewat_no,
            old_khewat_no=model.old_khewat_no,
            jamabandi_year=model.jamabandi_year,
            remarks=model.remarks,
            active=model.active,
        )