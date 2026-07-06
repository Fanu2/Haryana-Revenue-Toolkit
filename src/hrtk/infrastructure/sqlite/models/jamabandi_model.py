"""
Haryana Revenue Toolkit (HRTK)

SQLite Jamabandi Model.
"""

from __future__ import annotations

from uuid import uuid4

from sqlalchemy import (
    Boolean,
    String,
    UniqueConstraint,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from hrtk.infrastructure.sqlite.base import (
    Base,
)


class JamabandiModel(Base):
    """
    SQLite representation of a Jamabandi.
    """

    __tablename__ = "jamabandis"

    __table_args__ = (
        UniqueConstraint(
            "village_id",
            "khewat_id",
            "year",
            name="uq_jamabandi_village_khewat_year",
        ),
    )

    # ---------------------------------------------------------
    # Primary Key
    # ---------------------------------------------------------

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    # ---------------------------------------------------------
    # References
    # ---------------------------------------------------------

    village_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    khewat_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    # ---------------------------------------------------------
    # Jamabandi Record
    # ---------------------------------------------------------

    year: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    khatauni_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    remarks: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Active",
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )