"""
Haryana Revenue Toolkit (HRTK)

Developer Demo Database Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from tools.seed.village_seeder import (
    VillageSeeder,
)

from tools.seed.owner_seeder import (
    OwnerSeeder,
)

from tools.seed.jamabandi_seeder import (
    JamabandiSeeder,
)

from tools.seed.khewat_seeder import (
    KhewatSeeder,
)

from tools.seed.parcel_seeder import (
    ParcelSeeder,
)

from tools.seed.ownership_seeder import (
    OwnershipSeeder,
)


class DemoDataSeeder:
    """
    Creates a complete demonstration database.
    """

    def __init__(
        self,
    ) -> None:

        self._context = ApplicationContext()

    @property
    def context(
        self,
    ) -> ApplicationContext:

        return self._context

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def run(
        self,
    ) -> None:

        self._banner()

        VillageSeeder(
            self.context,
        ).run()

        OwnerSeeder(
            self.context,
        ).run()

        JamabandiSeeder(
            self.context,
        ).run()

        KhewatSeeder(
            self.context,
        ).run()

        ParcelSeeder(
            self.context,
        ).run()

        OwnershipSeeder(
            self.context,
        ).run()
        

        self._pending(
            "Partitions",
        )

        self._pending(
            "Allocations",
        )

        self._summary()

    # ---------------------------------------------------------

    @staticmethod
    def _banner(
    ) -> None:

        print()
        print("=" * 72)
        print("HARYANA REVENUE TOOLKIT")
        print("Developer Toolkit")
        print("Demo Database Seeder")
        print("=" * 72)
        print()

    @staticmethod
    def _pending(
        module: str,
    ) -> None:

        print(
            f"{module:<20} Pending"
        )

    def _summary(
        self,
    ) -> None:

        print()
        print("=" * 72)
        print("Demo database seeding completed.")
        print("=" * 72)
        print()

        self.context.shutdown()


def main() -> None:
    """
    Run the demo database seeder.
    """

    DemoDataSeeder().run()


if __name__ == "__main__":
    main()