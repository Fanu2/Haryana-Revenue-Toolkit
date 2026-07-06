"""
Haryana Revenue Toolkit (HRTK)

Development Khewat Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.khewat import (
    Khewat,
)

from hrtk.seed.sample_data import (
    JAMABANDI_YEARS,
    KHEWAT_NUMBERS,
)

from hrtk.seed.seed_context import (
    create_context,
)


def seed_khewats(
    context: ApplicationContext,
) -> None:
    """
    Seed development Khewats.
    """

    village = (
        context
        .village_service
        .find_by_code(
            "V001",
        )
    )

    if village is None:

        print(
            "Village V001 not found."
        )

        return

    service = context.khewat_service

    existing = {
        k.khewat_no
        for k in service.find_by_village(
            village.id,
        )
    }

    for number in KHEWAT_NUMBERS:

        khewat_no = str(number)

        if khewat_no in existing:

            print(
                f"Khewat {khewat_no} already exists."
            )

            continue

        khewat = Khewat(

            village_id=village.id,

            khewat_no=khewat_no,

            old_khewat_no="",

            jamabandi_year=JAMABANDI_YEARS[-1],

            remarks="Development Seed",
        )

        service.register(
            khewat,
        )

        print(
            f"Created Khewat : "
            f"{khewat_no}"
        )


def main() -> None:
    """
    Run the Khewat seeder.
    """

    context = create_context()

    seed_khewats(
        context,
    )


if __name__ == "__main__":
    main()