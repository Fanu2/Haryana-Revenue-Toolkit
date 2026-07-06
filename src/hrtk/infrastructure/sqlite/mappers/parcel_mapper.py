"""
Haryana Revenue Toolkit (HRTK)

Parcel Mapper.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.parcel import (
    Parcel,
)

from hrtk.domain.value_objects.area import (
    Area,
)

from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)

from hrtk.infrastructure.sqlite.models.parcel_model import (
    ParcelModel,
)


class ParcelMapper:
    """
    Maps between Parcel domain objects
    and SQLite models.
    """

    @staticmethod
    def to_domain(
        model: ParcelModel,
    ) -> Parcel:

        return Parcel(
            id=UUID(model.id),
            number=ParcelNumber(
                rectangle=model.rectangle,
                killa=model.killa,
            ),
            area=Area(
                kanal=model.kanal,
                marla=model.marla,
                sarsai=model.sarsai,
            ),
            remarks=model.remarks,
        )

    @staticmethod
    def to_model(
        parcel: Parcel,
    ) -> ParcelModel:

        return ParcelModel(
            id=str(parcel.id),
            rectangle=parcel.number.rectangle,
            killa=parcel.number.killa,
            kanal=parcel.area.kanal,
            marla=parcel.area.marla,
            sarsai=parcel.area.sarsai,
            remarks=parcel.remarks,
            status="Active",
            active=True,
        )
