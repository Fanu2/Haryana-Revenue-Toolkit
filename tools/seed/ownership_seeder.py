"""
Haryana Revenue Toolkit (HRTK)

Ownership Seeder.
"""

from __future__ import annotations

from hrtk.domain.ownership import (
    Ownership,
)

from hrtk.domain.value_objects.fraction import (
    Fraction,
)

from sample_data.ownerships import (
    OWNERSHIPS,
)

from tools.seed.base_seeder import (
    BaseSeeder,
)


class OwnershipSeeder(BaseSeeder):
    """
    Seed demonstration Ownerships.
    """

    def seed(
        self,
    ) -> None:

        owner_service = (
            self.context.owner_service
        )

        khewat_service = (
            self.context.khewat_service
        )

        ownership_service = (
            self.context.ownership_service
        )

        for row in OWNERSHIPS:

            owner = (
                owner_service.find_by_code(
                    row["owner_code"],
                )
            )

            if owner is None:

                self.error_one()

                print(
                    f"ERROR Owner "
                    f"{row['owner_code']} "
                    f"not found."
                )

                continue

            khewat = (
                khewat_service.repository.find_by_number(
                    owner.village_id,
                    row["khewat_no"],
                )
            )

            if khewat is None:

                self.error_one()

                print(
                    f"ERROR Khewat "
                    f"{row['khewat_no']} "
                    f"not found."
                )

                continue

            if ownership_service.exists(
                owner.id,
                khewat.id,
            ):

                self.skipped_one()

                print(
                    f"SKIP  "
                    f"{row['owner_code']} "
                    f"-> "
                    f"{row['khewat_no']}"
                )

                continue

            ownership = Ownership(

                owner_id=owner.id,

                khewat_id=khewat.id,

                share=Fraction.from_string(
                    row["share"],
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

                ownership_service.register(
                    ownership,
                )

                self.created_one()

                print(
                    f"ADD   "
                    f"{row['owner_code']} "
                    f"-> "
                    f"{row['khewat_no']}"
                )

            except Exception as error:

                self.error_one()

                print(
                    f"ERROR "
                    f"{row['owner_code']} "
                    f"-> "
                    f"{row['khewat_no']}"
                )

                print(
                    f"       "
                    f"{type(error).__name__}: "
                    f"{error}"
                )