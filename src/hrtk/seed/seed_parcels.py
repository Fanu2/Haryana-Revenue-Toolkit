"""
Haryana Revenue Toolkit (HRTK)

Development Parcel Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.parcel import (
    Parcel,
)

from hrtk.domain.value_objects.area import (
    Area,
)

from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)

from hrtk.seed.sample_data import (
    DEFAULT_KANAL,
    DEFAULT_MARLA,
    DEFAULT_SARSAI,
    PARCELS,
)

from hrtk.seed.seed_context import (
    create_context,
)


def seed_parcels(
    context: ApplicationContext,
) -> None:
    """
    Seed development parcels.
    """

    service = context.parcel_service

    for rectangle, killa in PARCELS:

        number = ParcelNumber(
            rectangle=rectangle,
            killa=killa,
        )

        if service.exists(
            number,
        ):

            print(
                f"Parcel {rectangle}//{killa} already exists."
            )

            continue

        parcel = Parcel(

            number=number,

            area=Area.from_kms(
                kanal=DEFAULT_KANAL,
                marla=DEFAULT_MARLA,
                 sarsai=DEFAULT_SARSAI,
            ),

            remarks="Development Seed",
        )

        service.create(
            parcel,
        )

        print(
            f"Created Parcel : "
            f"{rectangle}//{killa}"
        )


def main() -> None:
    """
    Run the parcel seeder.
    """

    context = create_context()

    seed_parcels(
        context,
    )


if __name__ == "__main__":
    main()