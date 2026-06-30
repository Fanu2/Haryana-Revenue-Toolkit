"""
Haryana Revenue Toolkit (HRTK)

SQLite Base Repository.
"""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class SQLiteBaseRepository(Generic[T]):
    """
    Base class for SQLite repositories.

    Version 1 intentionally contains no CRUD logic.
    It provides a common inheritance point for all
    SQLite repositories.
    """

    pass