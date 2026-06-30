"""
Haryana Revenue Toolkit (HRTK)

SQLite Parcel Model.
"""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from hrtk.infrastructure.sqlite.base import Base


class ParcelModel(Base):
    """
    SQLite representation of a parcel.
    """

    __tablename__ = "parcels"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    rectangle: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    killa: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

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

    remarks: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="Active",
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )