"""
Haryana Revenue Toolkit (HRTK)

Parcel Repository Interface.
"""

from __future__ import annotations

from typing import Protocol

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)


class ParcelRepository(Protocol):
    """
    Repository interface for Parcel entities.
    """

    def save(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Save a parcel.
        """
        ...

    def find_by_number(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:
        """
        Find a parcel by its number.
        """
        ...

    def find_all(
        self,
    ) -> list[Parcel]:
        """
        Return all parcels.
        """
        ...

    def exists(
        self,
        number: ParcelNumber,
    ) -> bool:
        """
        Return True if the parcel exists.
        """
        ...

    def delete(
        self,
        number: ParcelNumber,
    ) -> None:
        """
        Delete a parcel.
        """
        ...