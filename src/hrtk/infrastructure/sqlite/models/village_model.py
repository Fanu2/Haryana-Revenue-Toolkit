"""
Haryana Revenue Toolkit (HRTK)

SQLite Village Model.
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


class VillageModel(Base):
    """
    SQLite representation of a revenue village.
    """

    __tablename__ = "villages"

    __table_args__ = (
        UniqueConstraint(
            "code",
            name="uq_village_code",
        ),
    )

    # ---------------------------------------------------------
    # Primary Key (UUID)
    # ---------------------------------------------------------

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    # ---------------------------------------------------------
    # Revenue Identity
    # ---------------------------------------------------------

    code: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    tehsil: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    district: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    state: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="Haryana",
    )

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )