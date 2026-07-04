"""
Haryana Revenue Toolkit (HRTK)

SQLite Jamabandi Model.
"""

from __future__ import annotations

from sqlalchemy import (
    Boolean,
    Column,
    String,
    Text,
)

from hrtk.infrastructure.sqlite.base import Base


class JamabandiModel(Base):
    """
    SQLite model representing
    a Jamabandi record.
    """

    __tablename__ = "jamabandis"

    #
    # Identity
    #

    id = Column(
        String,
        primary_key=True,
    )

    #
    # Relationships
    #

    village_id = Column(
        String,
        nullable=False,
        index=True,
    )

    #
    # Record Details
    #

    year = Column(
        String,
        nullable=False,
        index=True,
    )

    mutation_no = Column(
        String,
        nullable=False,
        default="",
    )

    remarks = Column(
        Text,
        nullable=False,
        default="",
    )

    #
    # Status
    #

    finalized = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    active = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    def __repr__(
        self,
    ) -> str:
        """
        Developer representation.
        """

        return (
            "JamabandiModel("
            f"year={self.year!r}, "
            f"village_id={self.village_id!r}"
            ")"
        )