"""
Haryana Revenue Toolkit (HRTK)

Parcel Mapper.
"""

from __future__ import annotations

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)
from hrtk.infrastructure.sqlite.models.parcel_model import (
    ParcelModel,
)


class ParcelMapper:
    """
    Converts between ParcelModel
    and Parcel.
    """

    @staticmethod
    def to_domain(
        model: ParcelModel,
    ) -> Parcel:
        """
        Convert SQLite model to domain.
        """

        return Parcel(
            number=ParcelNumber(
                rectangle=model.rectangle,
                killa=model.killa,
            ),
            area=Area.from_kms(
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
        """
        Convert domain object
        to SQLite model.
        """

        return ParcelModel(
            rectangle=parcel.number.rectangle,
            killa=parcel.number.killa,
            kanal=parcel.area.kanal,
            marla=parcel.area.marla,
            sarsai=parcel.area.sarsai,
            remarks=parcel.remarks,
        )