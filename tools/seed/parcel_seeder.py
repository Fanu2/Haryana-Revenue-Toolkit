"""
Haryana Revenue Toolkit (HRTK)

Parcel Seeder.
"""

from __future__ import annotations

from hrtk.domain.parcel import (
    Parcel,
)
from hrtk.domain.value_objects.area import (
    Area,
)
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)

from sample_data.parcels import (
    PARCELS,
)

from tools.seed.base_seeder import (
    BaseSeeder,
)


class ParcelSeeder(BaseSeeder):
    """
    Seed demonstration Parcels.
    """

    def seed(
        self,
    ) -> None:

        parcel_service = (
            self.context.parcel_service
        )

        for row in PARCELS:

            number = ParcelNumber(

                rectangle=row["rectangle"],

                killa=row["killa"],

            )

            if parcel_service.exists(
                number,
            ):

                self.skipped_one()

                print(
                    f"SKIP  {number}"
                )

                continue

            parcel = Parcel(

                number=number,

                area=Area.from_kms(

                    kanal=row.get(
                        "kanal",
                        0,
                    ),

                    marla=row.get(
                        "marla",
                        0,
                    ),

                    sarsai=row.get(
                        "sarsai",
                        0,
                    ),

                ),

                remarks=row.get(
                    "remarks",
                    "",
                ),

            )

            try:

                parcel_service.create(
                    parcel,
                )

                self.created_one()

                print(
                    f"ADD   {number}"
                )

            except Exception as error:

                self.error_one()

                print(
                    f"ERROR {number}"
                )

                print(
                    f"       "
                    f"{type(error).__name__}: "
                    f"{error}"
                )