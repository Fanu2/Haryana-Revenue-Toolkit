"""
Haryana Revenue Toolkit (HRTK)

SQL Repository Base.
"""

from __future__ import annotations

from contextlib import AbstractContextManager
from typing import Any

from sqlalchemy.orm import Session

from hrtk.infrastructure.common.unit_of_work import (
    unit_of_work,
)


class SQLRepository:
    """
    Base class for SQL repositories.

    Provides a common way to obtain
    transactional SQLAlchemy sessions.
    """

    @staticmethod
    def session() -> AbstractContextManager[Session]:
        """
        Return a transactional session.

        Usage
        -----
        with self.session() as session:
            ...
        """
        return unit_of_work()

    @staticmethod
    def commit(
        session: Session,
    ) -> None:
        """
        Explicit commit helper.

        Normally unnecessary because
        unit_of_work() commits automatically,
        but available for clarity.
        """

        session.commit()

    @staticmethod
    def flush(
        session: Session,
    ) -> None:
        """
        Flush pending SQL statements.
        """

        session.flush()

    @staticmethod
    def refresh(
        session: Session,
        entity: Any,
    ) -> None:
        """
        Refresh an ORM entity.
        """

        session.refresh(entity)