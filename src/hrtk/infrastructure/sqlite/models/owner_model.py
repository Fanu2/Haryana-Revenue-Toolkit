"""
Haryana Revenue Toolkit (HRTK)

SQLite Owner Model.
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


class OwnerModel(Base):
    """
    SQLite representation of an owner.
    """

    __tablename__ = "owners"

    __table_args__ = (
        UniqueConstraint(
            "owner_code",
            name="uq_owner_code",
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
    # Owner
    # ---------------------------------------------------------

    owner_code: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    owner_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    father_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        default="",
    )

    address: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )

    mobile: Mapped[str] = mapped_column(
        String(30),
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