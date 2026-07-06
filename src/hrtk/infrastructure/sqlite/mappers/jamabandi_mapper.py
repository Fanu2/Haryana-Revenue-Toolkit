"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.jamabandi import (
    Jamabandi,
)

from hrtk.infrastructure.sqlite.models.jamabandi_model import (
    JamabandiModel,
)


class JamabandiMapper:
    """
    Maps between Jamabandi domain entities
    and SQLite models.
    """

    @staticmethod
    def to_domain(
        model: JamabandiModel,
    ) -> Jamabandi:

        return Jamabandi(

            id=UUID(model.id),

            village_id=UUID(
                model.village_id,
            ),

            khewat_id=UUID(
                model.khewat_id,
            ),

            year=model.year,

            khatauni_number=(
                model.khatauni_number
            ),

            remarks=model.remarks,

            status=model.status,
        )

    @staticmethod
    def to_model(
        jamabandi: Jamabandi,
    ) -> JamabandiModel:

        return JamabandiModel(

            id=str(
                jamabandi.id,
            ),

            village_id=str(
                jamabandi.village_id,
            ),

            khewat_id=str(
                jamabandi.khewat_id,
            ),

            year=jamabandi.year,

            khatauni_number=(
                jamabandi.khatauni_number
            ),

            remarks=jamabandi.remarks,

            status=jamabandi.status,

            active=True,
        )