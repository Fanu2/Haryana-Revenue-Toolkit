"""
Haryana Revenue Toolkit (HRTK)

SQLite Khewat Model.
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

from hrtk.infrastructure.sqlite.base import Base


class KhewatModel(Base):
    """
    SQLite representation of a Khewat.
    """

    __tablename__ = "khewats"

    __table_args__ = (
        UniqueConstraint(
            "village_id",
            "khewat_no",
            name="uq_village_khewat",
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
    # Village
    # ---------------------------------------------------------

    village_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    # ---------------------------------------------------------
    # Khewat
    # ---------------------------------------------------------

    khewat_no: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    old_khewat_no: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="",
    )

    jamabandi_year: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="",
    )

    remarks: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )