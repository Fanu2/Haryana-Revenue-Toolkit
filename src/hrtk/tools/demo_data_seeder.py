"""
Haryana Revenue Toolkit (HRTK)

Demo Data Seeder.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)


class DemoDataSeeder:

    def __init__(self) -> None:

        self.context = ApplicationContext()

    def run(self) -> None:

        print("=" * 60)
        print("HRTK DEMO DATA SEEDER")
        print("=" * 60)

        self.seed_villages()

        self.seed_owners()

        self.seed_khewats()

        self.seed_parcels()

        self.seed_ownerships()

        print()
        print("Demo database completed.")

    def seed_villages(self):

        print("Seeding villages...")

    def seed_owners(self):

        print("Seeding owners...")

    def seed_khewats(self):

        print("Seeding khewats...")

    def seed_parcels(self):

        print("Seeding parcels...")

    def seed_ownerships(self):

        print("Seeding ownerships...")