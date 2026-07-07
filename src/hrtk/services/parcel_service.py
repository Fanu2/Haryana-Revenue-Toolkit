"""
Haryana Revenue Toolkit (HRTK)

Parcel Service.
"""

from __future__ import annotations

from uuid import UUID

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

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def create(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Create a new parcel.
        """

        if (
            self._repository.find_by_number(
                parcel.number,
            )
            is not None
        ):
            raise ValueError(
                f"Parcel '{parcel.number}' already exists."
            )

        self._repository.add(
            parcel,
        )

    def update(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Update an existing parcel.
        """

        if not self._repository.exists(
            parcel.id,
        ):
            raise ValueError(
                f"Parcel '{parcel.number}' does not exist."
            )

        self._repository.update(
            parcel,
        )

    def delete(
        self,
        parcel_id: UUID,
    ) -> None:
        """
        Delete a parcel.
        """

        if not self._repository.exists(
            parcel_id,
        ):
            raise ValueError(
                "Parcel does not exist."
            )

        self._repository.remove(
            parcel_id,
        )

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def get_by_id(
        self,
        parcel_id: UUID,
    ) -> Parcel | None:
        """
        Return a parcel by UUID.
        """

        return self._repository.get(
            parcel_id,
        )

    def find_by_number(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:
        """
        Return a parcel by Rectangle/Killa.
        """

        return self._repository.find_by_number(
            number,
        )

    def exists(
        self,
        parcel_id: UUID,
    ) -> bool:

        return self._repository.exists(
            parcel_id,
        )

    def list(
        self,
    ) -> list[Parcel]:
        """
        Return all parcels.
        """

        return self._repository.list()

    def all(
        self,
    ) -> list[Parcel]:
        """
        Compatibility method.
        """

        return self.list()