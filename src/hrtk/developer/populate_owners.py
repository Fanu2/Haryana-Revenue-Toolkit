"""
Haryana Revenue Toolkit (HRTK)

Populate Development Owners.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.owner import (
    Owner,
)

from hrtk.developer.sample_data import (
    OWNER_NAMES,
    VILLAGE,
)


def populate_owners(
    context: ApplicationContext,
) -> None:
    """
    Populate development owners.
    """

    village = (
        context.village_service.find_by_code(
            VILLAGE["code"],
        )
    )

    if village is None:

        raise RuntimeError(
            "Development village not found."
        )

    service = context.owner_service

    for index, owner_name in enumerate(
        OWNER_NAMES,
        start=1,
    ):

        owner_code = f"O{index:03d}"

        if service.find_by_code(owner_code):

            print(
                f"Owner {owner_code} already exists."
            )

            continue

        owner = Owner(

            village_id=village.id,

            owner_code=owner_code,

            owner_name=owner_name,

            father_name=f"Father {index}",

            address=(
                f"{VILLAGE['name']}, "
                "Tehsil Kalanwali"
            ),

            mobile="",

            remarks="Development Data",

            active=True,
        )

        service.register(owner)

        print(
            f"Created Owner "
            f"{owner.owner_code} "
            f"{owner.owner_name}"
        )