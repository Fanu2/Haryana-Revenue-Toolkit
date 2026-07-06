"""
Haryana Revenue Toolkit (HRTK)

Populate Development Villages.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.village import (
    Village,
)

from hrtk.developer.sample_data import (
    STATE,
    DISTRICT,
    TEHSIL,
    VILLAGE,
)


def populate_villages(
    context: ApplicationContext,
) -> None:
    """
    Populate development villages.
    """

    service = context.village_service

    code = VILLAGE["code"]

    existing = service.find_by_code(
        code,
    )

    if existing is not None:

        print(
            f"Village {code} already exists."
        )

        return

    village = Village(

        code=code,

        name=VILLAGE["name"],

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