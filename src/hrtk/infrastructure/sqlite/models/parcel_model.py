"""
Haryana Revenue Toolkit (HRTK)

SQLite Parcel Model.
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

from hrtk.infrastructure.sqlite.base import (
    Base,
)


class ParcelModel(Base):
    """
    SQLite representation of a Parcel.
    """

    __tablename__ = "parcels"

    __table_args__ = (
        UniqueConstraint(
            "entity_id",
            name="uq_parcel_entity_id",
        ),
        UniqueConstraint(
            "rectangle",
            "killa",
            name="uq_parcel_number",
        ),
    )

    # ---------------------------------------------------------
    # Internal SQLite Primary Key
    # ---------------------------------------------------------

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    # ---------------------------------------------------------
    # Application UUID
    # ---------------------------------------------------------

    entity_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Parcel Number
    # ---------------------------------------------------------

    rectangle: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    killa: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    # ---------------------------------------------------------
    # Area
    # ---------------------------------------------------------

    kanal: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    marla: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    sarsai: Mapped[int] = mapped_column(
        Integer,
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