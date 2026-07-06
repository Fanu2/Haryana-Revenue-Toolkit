"""
Haryana Revenue Toolkit (HRTK)

Development Database Seeder.

Run with:

python -m hrtk.seed.seed_database
"""

from __future__ import annotations

from hrtk.seed.seed_context import (
    create_context,
)

from hrtk.seed.seed_villages import (
    seed_villages,
)

from hrtk.seed.seed_owners import (
    seed_owners,
)

from hrtk.seed.seed_khewats import (
    seed_khewats,
)

from hrtk.seed.seed_parcels import (
    seed_parcels,
)

from hrtk.seed.seed_ownership import (
    seed_ownership,
)

from hrtk.seed.seed_khewat_parcels import (
    seed_khewat_parcels,
)

from hrtk.seed.seed_jamabandis import (
    seed_jamabandis,
)

from hrtk.seed.seed_partitions import (
    seed_partitions,
)


def seed_database() -> None:
    """
    Populate a fresh development database.
    """

    context = create_context()

    print("=" * 70)
    print("HRTK DEVELOPMENT DATABASE SEED")
    print("=" * 70)

    seed_villages(context)

    seed_owners(context)

    seed_khewats(context)

    seed_parcels(context)

    seed_ownership(context)

    seed_khewat_parcels(context)

    seed_jamabandis(context)

    seed_partitions(context)

    print()
    print("=" * 70)
    print("DATABASE SUCCESSFULLY SEEDED")
    print("=" * 70)


if __name__ == "__main__":
    seed_database()