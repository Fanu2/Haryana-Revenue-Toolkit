"""
Haryana Revenue Toolkit (HRTK)

Village Mapper.
"""

from __future__ import annotations

from hrtk.domain.village import Village
from hrtk.infrastructure.sqlite.models.village_model import (
    VillageModel,
)


class VillageMapper:
    """
    Maps Village <-> VillageModel.
    """

    @staticmethod
    def to_model(
        village: Village,
    ) -> VillageModel:
        """
        Convert a domain Village to a SQLite model.
        """

        return VillageModel(
            code=village.code,
            name=village.name,
            tehsil=village.tehsil,
            district=village.district,
            state=village.state,
            active=village.active,
        )

    @staticmethod
    def to_domain(
        model: VillageModel,
    ) -> Village:
        """
        Convert a SQLite model to a domain Village.
        """

        return Village(
            code=model.code,
            name=model.name,
            tehsil=model.tehsil,
            district=model.district,
            state=model.state,
            active=model.active,
        )