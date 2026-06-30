"""
Haryana Revenue Toolkit (HRTK)

Owner Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.owner import Owner
from hrtk.infrastructure.sqlite.models.owner_model import (
    OwnerModel,
)


class OwnerMapper:
    """
    Maps Owner <-> OwnerModel.
    """

    @staticmethod
    def to_model(
        owner: Owner,
    ) -> OwnerModel:
        """
        Convert a domain Owner to a SQLite model.
        """

        return OwnerModel(
            village_id=str(owner.village_id),
            owner_code=owner.owner_code,
            owner_name=owner.owner_name,
            father_name=owner.father_name,
            address=owner.address,
            mobile=owner.mobile,
            remarks=owner.remarks,
            active=owner.active,
        )

    @staticmethod
    def to_domain(
        model: OwnerModel,
    ) -> Owner:
        """
        Convert a SQLite model to a domain Owner.
        """

        return Owner(
            village_id=UUID(model.village_id),
            owner_code=model.owner_code,
            owner_name=model.owner_name,
            father_name=model.father_name,
            address=model.address,
            mobile=model.mobile,
            remarks=model.remarks,
            active=model.active,
        )