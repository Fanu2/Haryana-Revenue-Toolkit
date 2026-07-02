"""
Haryana Revenue Toolkit (HRTK)

Reset Ownership Records

Deletes ALL ownership records.
Villages, Owners, Khewats and Khasras are NOT affected.
"""

from sqlalchemy import text

from hrtk.infrastructure.sqlite.session import SessionFactory


def main() -> None:

    print("=" * 70)
    print("RESET OWNERSHIP TABLE")
    print("=" * 70)

    confirm = input(
        "Delete ALL ownership records? (YES to continue): "
    )

    if confirm != "YES":
        print("Cancelled.")
        return

    with SessionFactory() as session:

        count = session.execute(
            text(
                "SELECT COUNT(*) FROM ownerships"
            )
        ).scalar_one()

        print(f"\nExisting ownership records : {count}")

        session.execute(
            text(
                "DELETE FROM ownerships"
            )
        )

        session.commit()

    print("\nOwnership table successfully cleared.")
    print("You may now recreate ownership records from the UI.")


if __name__ == "__main__":
    main()