"""
Haryana Revenue Toolkit (HRTK)

SQLite Khewat Model.
"""

from __future__ import annotations

from sqlalchemy import (
    Boolean,
    Integer,
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

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
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