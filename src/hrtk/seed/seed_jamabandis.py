"""
Haryana Revenue Toolkit (HRTK)

Development Jamabandi Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.jamabandi import (
    Jamabandi,
)

from hrtk.seed.sample_data import (
    JAMABANDI_YEARS,
)

from hrtk.seed.seed_context import (
    create_context,
)


def seed_jamabandis(
    context: ApplicationContext,
) -> None:
    """
    Seed development Jamabandis.
    """

    village = (
        context
        .village_service
        .find_by_code(
            "V001",
        )
    )

    if village is None:

        raise RuntimeError(
            "Village V001 not found."
        )

    khewats = (
        context
        .khewat_service
        .find_by_village(
            village.id,
        )
    )

    service = (
        context
        .jamabandi_service
    )

    for khewat in khewats:

        existing_years = {
            record.year
            for record in service.by_khewat(
                khewat.id,
            )
        }

        for year in JAMABANDI_YEARS:

            if year in existing_years:

                print(
                    f"{year} / "
                    f"Khewat {khewat.khewat_no} "
                    f"already exists."
                )

                continue

            jamabandi = Jamabandi(

                village_id=village.id,

                khewat_id=khewat.id,

                year=year,

                khatauni_number=(
                    khewat.khewat_no
                ),

                remarks="Development Seed",

                status="Active",
            )

            service.add(
                jamabandi,
            )

            print(
                f"Created "
                f"{year} - "
                f"Khewat "
                f"{khewat.khewat_no}"
            )

def main() -> None:
    """
    Run the Jamabandi seeder.
    """

    context = create_context()

    seed_jamabandis(
        context,
    )


if __name__ == "__main__":
    main()