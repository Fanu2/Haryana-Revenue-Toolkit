"""
Haryana Revenue Toolkit (HRTK)

Owner Seeder.
"""

from __future__ import annotations

from hrtk.domain.owner import Owner

from sample_data.owners import (
    OWNERS,
)

from tools.seed.base_seeder import (
    BaseSeeder,
)


class OwnerSeeder(BaseSeeder):
    """
    Seed demonstration owners.
    """

    def seed(
        self,
    ) -> None:

        village_service = (
            self.context.village_service
        )

        owner_service = (
            self.context.owner_service
        )

        for row in OWNERS:

            #
            # Skip duplicates
            #

            if owner_service.find_by_code(
                row["owner_code"],
            ) is not None:

                self.skipped_one()

                print(
                    f"SKIP  "
                    f"{row['owner_code']} "
                    f"{row['owner_name']}"
                )

                continue

            #
            # Find village
            #

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

            owner = Owner(

                village_id=village.id,

                owner_code=row["owner_code"],

                owner_name=row["owner_name"],

                father_name=row.get(
                    "father_name",
                    "",
                ),

                address=row.get(
                    "address",
                    "",
                ),

                mobile=row.get(
                    "mobile",
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

                owner_service.register(
                    owner,
                )

                self.created_one()

                print(
                    f"ADD   "
                    f"{owner.owner_code} "
                    f"{owner.owner_name}"
                )

            except Exception as error:

                self.error_one()

                print(
                    f"ERROR "
                    f"{row['owner_code']} "
                    f"{row['owner_name']}"
                )

                print(
                    f"       "
                    f"{type(error).__name__}: "
                    f"{error}"
                )