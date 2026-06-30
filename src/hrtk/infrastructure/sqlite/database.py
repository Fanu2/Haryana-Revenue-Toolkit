"""
Haryana Revenue Toolkit (HRTK)

SQLite Database Utilities.
"""

from __future__ import annotations

from hrtk.infrastructure.sqlite.base import Base
from hrtk.infrastructure.sqlite.session import engine


def create_database() -> None:
    """
    Create all database tables if they do not exist.

    This function is intended for normal
    application startup.
    """

    Base.metadata.create_all(
        bind=engine,
    )


def reset_database() -> None:
    """
    Drop and recreate every database table.

    This function is intended only for
    automated integration tests.

    Every test starts with a completely
    clean SQLite database.
    """

    Base.metadata.drop_all(
        bind=engine,
    )

    Base.metadata.create_all(
        bind=engine,
    )