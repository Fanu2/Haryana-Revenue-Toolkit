"""
Haryana Revenue Toolkit (HRTK)

Khewat Seeder.
"""

from __future__ import annotations

from hrtk.domain.khewat import Khewat

from sample_data.khewats import (
    KHEWATS,
)

from tools.seed.base_seeder import (
    BaseSeeder,
)


class KhewatSeeder(BaseSeeder):
    """
    Seed demonstration Khewats.
    """

    def seed(self) -> None:

        village_service = self.context.village_service
        khewat_service = self.context.khewat_service

        for row in KHEWATS:

            village = village_service.find_by_code(
                row["village_code"]
            )

            if village is None:

                self.error_one()

                print(
                    f"ERROR Village {row['village_code']} not found."
                )

                continue

            if (
                khewat_service.repository.find_by_number(
                    village.id,
                    row["khewat_no"],
                )
                is not None
            ):

                self.skipped_one()

                print(
                    f"SKIP  {row['khewat_no']}"
                )

                continue

            khewat = Khewat(

                village_id=village.id,

                khewat_no=row["khewat_no"],

                old_khewat_no=row.get(
                    "old_khewat_no",
                    "",
                ),

                jamabandi_year=row.get(
                    "jamabandi_year",
                    "",
                ),

                remarks=row.get(
                    "remarks",
                    "",
                ),

                active=row.get(
                    "active",
                    True,
                ),
            )

            try:

                khewat_service.register(
                    khewat,
                )

                self.created_one()

                print(
                    f"ADD   Khewat {khewat.khewat_no}"
                )

            except Exception as error:

                self.error_one()

                print(
                    f"ERROR {row['khewat_no']}"
                )

                print(
                    f"       {type(error).__name__}: {error}"
                )