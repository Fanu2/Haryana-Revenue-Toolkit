"""
Haryana Revenue Toolkit (HRTK)

Development Village Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.village import (
    Village,
)

from hrtk.seed.sample_data import (
    DISTRICT,
    STATE,
    TEHSIL,
    VILLAGES,
)

from hrtk.seed.seed_context import (
    create_context,
)


def seed_villages(
    context: ApplicationContext,
) -> None:
    """
    Seed development villages.
    """

    service = context.village_service

    for index, village_name in enumerate(
        VILLAGES,
        start=1,
    ):

        code = f"V{index:03d}"

        if service.find_by_code(
            code,
        ) is not None:

            print(
                f"Village {code} already exists."
            )

            continue

        village = Village(
            code=code,
            name=village_name,
            tehsil=TEHSIL,
            district=DISTRICT,
            state=STATE,
        )

        service.register(
            village,
        )

        print(
            f"Created Village : "
            f"{village.display_name}"
        )


def main() -> None:
    """
    Run the village seeder.
    """

    context = create_context()

    seed_villages(
        context,
    )


if __name__ == "__main__":
    main()