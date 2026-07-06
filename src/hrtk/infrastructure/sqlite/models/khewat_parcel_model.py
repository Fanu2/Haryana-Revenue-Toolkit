"""
Haryana Revenue Toolkit (HRTK)

SQLite Khewat Parcel Model.
"""

from __future__ import annotations

from uuid import uuid4

from sqlalchemy import (
    String,
    UniqueConstraint,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from hrtk.infrastructure.sqlite.base import Base


class KhewatParcelModel(Base):
    """
    SQLite representation of a
    Khewat-Parcel relationship.
    """

    __tablename__ = "khewat_parcels"

    __table_args__ = (
        UniqueConstraint(
            "khewat_id",
            "parcel_id",
            name="uq_khewat_parcel",
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
    # Relationship
    # ---------------------------------------------------------

    khewat_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        index=True,
    )

    parcel_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    remarks: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )

    def __repr__(
        self,
    ) -> str:
        return (
            "KhewatParcelModel("
            f"khewat_id={self.khewat_id!r}, "
            f"parcel_id={self.parcel_id!r}"
            ")"
        )
