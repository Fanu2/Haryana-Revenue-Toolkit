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


def seed_owners(
    context: ApplicationContext,
) -> None:
    """
    Seed development owners.
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

    service = context.owner_service

    for index, owner_name in enumerate(
        OWNER_NAMES,
        start=1,
    ):

        owner_code = (
            f"O{index:03d}"
        )

        if (
            service.find_by_code(
                owner_code,
            )
            is not None
        ):

            print(
                f"Owner {owner_code} already exists."
            )

            continue

        owner = Owner(

            village_id=village.id,

            owner_code=owner_code,

            owner_name=owner_name,

            father_name="Unknown",

            address="Taruana",

            mobile="",

            remarks="Development Seed",

        )

        service.register(
            owner,
        )

        print(
            f"Created Owner : "
            f"{owner.owner_code} - "
            f"{owner.owner_name}"
        )