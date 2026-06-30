"""
Haryana Revenue Toolkit (HRTK)

SQLite Database Utilities.
"""

from __future__ import annotations

from hrtk.infrastructure.sqlite.base import Base
from hrtk.infrastructure.sqlite.session import engine


def create_database() -> None:
    """
    Create all database tables.
    """

    Base.metadata.create_all(
        bind=engine,
    )