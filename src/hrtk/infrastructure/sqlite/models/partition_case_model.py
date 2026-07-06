"""
Haryana Revenue Toolkit (HRTK)

SQLite Partition Case Model.
"""

from __future__ import annotations

from uuid import uuid4

from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from hrtk.infrastructure.sqlite.base import Base


class PartitionCaseModel(Base):
    """
    SQLite representation of a partition case.
    """

    __tablename__ = "partition_cases"

    #
    # Primary Key
    #

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    #
    # Relationships
    #

    village_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    khewat_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    #
    # Record
    #

    jamabandi_year: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Draft",
    )

    remarks: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )
