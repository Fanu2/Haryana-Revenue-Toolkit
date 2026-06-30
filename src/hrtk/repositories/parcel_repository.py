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
    Repository contract for Parcel entities.
    """

    def add(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Add a new parcel.
        """
        ...

    def update(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Update an existing parcel.
        """
        ...

    def remove(
        self,
        number: ParcelNumber,
    ) -> None:
        """
        Remove a parcel.
        """
        ...

    def get(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:
        """
        Return a parcel by number.
        """
        ...

    def list(
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
        Determine whether a parcel exists.
        """
        ...