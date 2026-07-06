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
    KHEWAT_NUMBERS,
    JAMABANDI_YEARS,
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

        raise RuntimeError(
            "Village V001 not found. "
            "Run seed_villages first."
        )

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
            f"Created Khewat {khewat_no}"
        )