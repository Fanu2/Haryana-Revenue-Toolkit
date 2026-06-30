"""
Haryana Revenue Toolkit (HRTK)

Unit of Work.
"""

from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.orm import Session

from hrtk.infrastructure.sqlite.session import (
    SessionFactory,
)


@contextmanager
def unit_of_work() -> Generator[
    Session,
    None,
    None,
]:
    """
    Create a transactional database session.
    """

    session = SessionFactory()

    try:

        yield session

        session.commit()

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()