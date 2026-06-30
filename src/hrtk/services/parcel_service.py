"""
Haryana Revenue Toolkit (HRTK)

Parcel Service.
"""

from __future__ import annotations

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)
from hrtk.repositories.parcel_repository import (
    ParcelRepository,
)


class ParcelService:
    """
    Application service for Parcel operations.
    """

    def __init__(
        self,
        repository: ParcelRepository,
    ) -> None:
        self._repository = repository

    def create(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Create a new parcel.
        """

        if self._repository.exists(
            parcel.number,
        ):
            raise ValueError(
                f"Parcel '{parcel.number}' already exists."
            )

        self._repository.add(
            parcel,
        )

    def get(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:
        """
        Return a parcel by number.
        """

        return self._repository.get(
            number,
        )

    def exists(
        self,
        number: ParcelNumber,
    ) -> bool:
        """
        Determine whether a parcel exists.
        """

        return self._repository.exists(
            number,
        )

    def list(
        self,
    ) -> list[Parcel]:
        """
        Return all parcels.
        """

        return self._repository.list()