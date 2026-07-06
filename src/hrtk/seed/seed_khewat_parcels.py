"""
Haryana Revenue Toolkit (HRTK)

Development Khewat-Parcel Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.land_records.khewat_parcel import (
    KhewatParcel,
)

from hrtk.seed.seed_context import (
    create_context,
)


def seed_khewat_parcels(
    context: ApplicationContext,
) -> None:
    """
    Seed development Khewat-Parcel relationships.
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

    #
    # Build lookups
    #

    khewats = {
        k.khewat_no: k
        for k in context.khewat_service.find_by_village(
            village.id,
        )
    }

    parcels = {}

    for parcel in context.parcel_service.list():

        rectangle = (
            parcel.number.rectangle
        )

        parcels.setdefault(
            rectangle,
            [],
        ).append(
            parcel,
        )

    #
    # Assign parcels
    #

    service = (
        context.khewat_parcel_service
    )

    for number in range(
        1,
        21,
    ):

        khewat = khewats.get(
            str(number),
        )

        if khewat is None:

            continue

        for parcel in sorted(
            parcels.get(
                number,
                [],
            ),
            key=lambda p: int(
                p.number.killa,
            ),
        ):

            if service.exists(
                khewat.id,
                parcel.id,
            ):

                continue

            service.register(

                KhewatParcel(

                    khewat_id=khewat.id,

                    parcel_id=parcel.id,

                    remarks="Development Seed",
                )

            )

            print(
                f"Khewat {number} -> "
                f"{parcel.number}"
            )


def main() -> None:
    """
    Run the seeder.
    """

    context = create_context()

    seed_khewat_parcels(
        context,
    )


if __name__ == "__main__":
    main()