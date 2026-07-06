"""
Haryana Revenue Toolkit (HRTK)

Development Ownership Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.ownership import (
    Ownership,
)

from hrtk.domain.value_objects.fraction import (
    Fraction,
)

from hrtk.seed.seed_context import (
    create_context,
)


def seed_ownership(
    context: ApplicationContext,
) -> None:
    """
    Seed development ownership records.
    """

    owner_service = context.owner_service
    khewat_service = context.khewat_service
    ownership_service = context.ownership_service

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
    # Development ownership pattern
    #

    ownership_data = [

        ("O001", "1", Fraction(1, 2)),
        ("O002", "1", Fraction(1, 2)),

        ("O003", "2", Fraction(1, 1)),

        ("O004", "3", Fraction(1, 3)),
        ("O005", "3", Fraction(2, 3)),

        ("O006", "4", Fraction(1, 4)),
        ("O007", "4", Fraction(1, 4)),
        ("O008", "4", Fraction(1, 2)),
    ]

    owners = {
        owner.owner_code: owner
        for owner in owner_service.find_by_village(
            village.id,
        )
    }

    khewats = {
        k.khewat_no: k
        for k in khewat_service.find_by_village(
            village.id,
        )
    }

    for owner_code, khewat_no, share in ownership_data:

        owner = owners.get(
            owner_code,
        )

        khewat = khewats.get(
            khewat_no,
        )

        if owner is None or khewat is None:

            print(
                f"Skipping {owner_code} / "
                f"{khewat_no}"
            )

            continue

        if ownership_service.exists(
            owner.id,
            khewat.id,
        ):

            print(
                f"{owner_code} -> "
                f"Khewat {khewat_no} exists."
            )

            continue

        ownership = Ownership(

            owner_id=owner.id,

            khewat_id=khewat.id,

            share=share,

            remarks="Development Seed",
        )

        ownership_service.register(
            ownership,
        )

        print(
            f"Created Ownership : "
            f"{owner_code} -> "
            f"Khewat {khewat_no} "
            f"({share})"
        )


def main() -> None:
    """
    Run the ownership seeder.
    """

    context = create_context()

    seed_ownership(
        context,
    )


if __name__ == "__main__":
    main()