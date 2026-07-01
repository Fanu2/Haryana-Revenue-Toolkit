"""
Haryana Revenue Toolkit (HRTK)

Ownership Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.ownership import Ownership
from hrtk.domain.value_objects.fraction import Fraction
from hrtk.infrastructure.sqlite.models.ownership_model import (
    OwnershipModel,
)


class OwnershipMapper:
    """
    Maps Ownership between Domain and SQLite.
    """

    @staticmethod
    def to_model(
        ownership: Ownership,
    ) -> OwnershipModel:

        return OwnershipModel(
            id=str(ownership.id),
            owner_id=str(ownership.owner_id),
            khewat_id=str(ownership.khewat_id),
            numerator=ownership.share.numerator,
            denominator=ownership.share.denominator,
            remarks=ownership.remarks,
            active=ownership.active,
        )

    @staticmethod
    def to_domain(
        model: OwnershipModel,
    ) -> Ownership:

        return Ownership(
            id=UUID(model.id),
            owner_id=UUID(model.owner_id),
            khewat_id=UUID(model.khewat_id),
            share=Fraction(
                model.numerator,
                model.denominator,
            ),
            remarks=model.remarks,
            active=model.active,
        )