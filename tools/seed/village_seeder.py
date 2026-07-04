"""
Haryana Revenue Toolkit (HRTK)

Village Seeder.
"""

from __future__ import annotations

from hrtk.domain.village import (
    Village,
)

from sample_data.villages import (
    VILLAGES,
)

from tools.seed.base_seeder import BaseSeeder


class VillageSeeder(BaseSeeder):
    """
    Seed demonstration villages.
    """

    def seed(
        self,
    ) -> None:

        service = (
            self.context.village_service
        )

        for row in VILLAGES:

            #
            # Skip duplicates
            #

            if service.find_by_code(
                row["code"],
            ) is not None:

                self.skipped_one()

                print(
                    f"SKIP  {row['code']} "
                    f"{row['name']}"
                )

                continue

            village = Village(

                code=row["code"],

                name=row["name"],

                tehsil=row["tehsil"],

                district=row["district"],

                state=row.get(
                    "state",
                    "Haryana",
                ),
            )

            try:

                service.register(
                    village,
                )

                self.created_one()

                print(
                    f"ADD   "
                    f"{village.display_name}"
                )

            except Exception as error:

                self.error_one()

                print(
                    f"ERROR {row['code']} "
                    f"{row['name']}"
                )

                print(
                    f"       {type(error).__name__}: "
                    f"{error}"
                )