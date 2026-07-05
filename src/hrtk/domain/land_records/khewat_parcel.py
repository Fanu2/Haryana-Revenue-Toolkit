"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel relationship entity.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity


@dataclass(
    slots=True,
)
class KhewatParcel(
    BaseEntity,
):
    """
    Relationship between one
    Khewat and one Parcel.
    """

    khewat_id: UUID

    parcel_id: UUID

    remarks: str = ""

    @property
    def has_remarks(
        self,
    ) -> bool:
        """
        Return True if remarks exist.
        """

        return bool(
            self.remarks.strip()
        )

    def update_remarks(
        self,
        remarks: str,
    ) -> None:
        """
        Update remarks.
        """

        self.remarks = remarks.strip()

    def __str__(
        self,
    ) -> str:
        return (
            f"KhewatParcel("
            f"{self.khewat_id} -> "
            f"{self.parcel_id}"
            f")"
        )