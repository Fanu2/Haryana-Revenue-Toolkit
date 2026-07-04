"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Seeder.
"""

from __future__ import annotations

from hrtk.domain.jamabandi import (
    Jamabandi,
)

from sample_data.jamabandis import (
    JAMABANDIS,
)

from tools.seed.base_seeder import (
    BaseSeeder,
)


class JamabandiSeeder(BaseSeeder):
    """
    Seed demonstration Jamabandis.
    """

    def seed(
        self,
    ) -> None:

        village_service = (
            self.context.village_service
        )

        jamabandi_service = (
            self.context.jamabandi_service
        )

        for row in JAMABANDIS:

            village = (
                village_service.find_by_code(
                    row["village_code"],
                )
            )

            if village is None:

                self.error_one()

                print(
                    f"ERROR Village "
                    f"{row['village_code']} "
                    f"not found."
                )

                continue

            if jamabandi_service.exists(
                village.id,
                row["year"],
            ):

                self.skipped_one()

                print(
                    f"SKIP  "
                    f"{row['year']}"
                )

                continue

            jamabandi = Jamabandi(

                village_id=village.id,

                year=row["year"],

                mutation_no=row.get(
                    "mutation_no",
                    "",
                ),

                remarks=row.get(
                    "remarks",
                    "",
                ),

                finalized=row.get(
                    "finalized",
                    False,
                ),

                active=row.get(
                    "active",
                    True,
                ),
            )

            try:

                jamabandi_service.register(
                    jamabandi,
                )

                self.created_one()

                print(
                    f"ADD   "
                    f"{jamabandi.year}"
                )

            except Exception as error:

                self.error_one()

                print(
                    f"ERROR "
                    f"{row['year']}"
                )

                print(
                    f"       "
                    f"{type(error).__name__}: "
                    f"{error}"
                )