"""
Haryana Revenue Toolkit (HRTK)

Demo Database Seeder.
"""

from pathlib import Path


def main() -> None:

    print("=" * 60)
    print("HRTK Demo Database Seeder")
    print("=" * 60)

    db = (
        Path.home()
        / ".hrtk"
        / "hrtk.db"
    )

    print(f"Database : {db}")

    print("Ready to seed demo data.")


if __name__ == "__main__":
    main()