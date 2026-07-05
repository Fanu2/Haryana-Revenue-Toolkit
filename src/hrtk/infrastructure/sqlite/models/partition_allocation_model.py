"""
Haryana Revenue Toolkit (HRTK)

SQLite Partition Allocation Model.
"""

from __future__ import annotations

from sqlalchemy import Integer, String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from hrtk.infrastructure.sqlite.base import Base


class PartitionAllocationModel(Base):
    """
    SQLite representation of a partition allocation.
    """

    __tablename__ = "partition_allocations"

    #
    # Primary Key
    #

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    #
    # Domain Identity
    #

    entity_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        unique=True,
    )

    #
    # Relationships
    #

    partition_case_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    owner_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    #
    # Allocation
    #

    parcel_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    allocated_area: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    remarks: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )