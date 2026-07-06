"""
Haryana Revenue Toolkit (HRTK)

Development Owner Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.owner import (
    Owner,
)

from hrtk.seed.sample_data import (
    OWNER_NAMES,
)

from hrtk.seed.seed_context import (
    create_context,
)


def seed_owners(
    context: ApplicationContext,
) -> None:
    """
    Seed development owners.
    """

    village = (
        context.village_service.find_by_code(
            "V001",
        )
    )

    if village is None:

        print(
            "Village V001 not found."
        )

        return

    service = context.owner_service

    for index, name in enumerate(
        OWNER_NAMES,
        start=1,
    ):

        owner_code = f"O{index:03d}"

        if service.find_by_code(
            owner_code,
        ) is not None:

            print(
                f"Owner {owner_code} already exists."
            )

            continue

        owner = Owner(

            village_id=village.id,

            owner_code=owner_code,

            owner_name=name,

            father_name="Unknown",

            address="Taruana",

            mobile="",

            remarks="",
        )

        service.register(
            owner,
        )

        print(
            f"Created Owner : "
            f"{owner_code} - "
            f"{name}"
        )


def main() -> None:
    """
    Run the owner seeder.
    """

    context = create_context()

    seed_owners(
        context,
    )


if __name__ == "__main__":
    main()