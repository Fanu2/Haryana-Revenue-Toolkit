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
    Maps Jamabandi <-> JamabandiModel.
    """

    # ---------------------------------------------------------
    # Domain -> SQLite
    # ---------------------------------------------------------

    @staticmethod
    def to_model(
        jamabandi: Jamabandi,
    ) -> JamabandiModel:
        """
        Convert a domain entity into
        a SQLite model.
        """

        return JamabandiModel(

            id=str(
                jamabandi.id,
            ),

            village_id=str(
                jamabandi.village_id,
            ),

            year=jamabandi.year,

            mutation_no=jamabandi.mutation_no,

            remarks=jamabandi.remarks,

            finalized=jamabandi.finalized,

            active=jamabandi.active,
        )

    # ---------------------------------------------------------
    # SQLite -> Domain
    # ---------------------------------------------------------

    @staticmethod
    def to_domain(
        model: JamabandiModel,
    ) -> Jamabandi:
        """
        Convert a SQLite model into
        a domain entity.
        """

        return Jamabandi(

            id=UUID(
                model.id,
            ),

            village_id=UUID(
                model.village_id,
            ),

            year=model.year,

            mutation_no=model.mutation_no,

            remarks=model.remarks,

            finalized=model.finalized,

            active=model.active,
        )