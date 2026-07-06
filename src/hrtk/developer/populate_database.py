"""
Haryana Revenue Toolkit (HRTK)

Development Database Population.
"""

from __future__ import annotations

from hrtk.developer.developer_context import (
    create_context,
)

from hrtk.developer.populate_villages import (
    populate_villages,
)


def populate_database() -> None:

    context = create_context()

    print()
    print("=" * 60)
    print("POPULATING DEVELOPMENT DATABASE")
    print("=" * 60)

    populate_villages(
        context,
    )

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    populate_database()
