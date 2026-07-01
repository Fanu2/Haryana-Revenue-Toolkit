"""
Haryana Revenue Toolkit (HRTK)

SQLite Ownership Model.
"""

from __future__ import annotations

from uuid import uuid4

from sqlalchemy import (
    Boolean,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from hrtk.infrastructure.sqlite.base import Base


class OwnershipModel(Base):

    __tablename__ = "ownerships"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    owner_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    khewat_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    numerator: Mapped[int] = mapped_column(
        nullable=False,
    )

    denominator: Mapped[int] = mapped_column(
        nullable=False,
    )

    remarks: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )