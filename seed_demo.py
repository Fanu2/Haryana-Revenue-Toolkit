"""
Haryana Revenue Toolkit (HRTK)

Demo Database Seeder Launcher.
"""

from hrtk.tools.demo_data_seeder import DemoDataSeeder


def main() -> None:

    seeder = DemoDataSeeder()

    seeder.run()


if __name__ == "__main__":
    main()