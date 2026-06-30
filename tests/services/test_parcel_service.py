"""
Haryana Revenue Toolkit (HRTK)

Unit tests for ParcelService.
"""

from __future__ import annotations

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)
from hrtk.repositories.parcel_repository import (
    ParcelRepository,
)
from hrtk.services.parcel_service import (
    ParcelService,
)


class FakeParcelRepository(ParcelRepository):
    """
    In-memory repository for unit tests.
    """

    def __init__(self) -> None:
        self._data: dict[
            tuple[int, str],
            Parcel,
        ] = {}

    def add(
        self,
        parcel: Parcel,
    ) -> None:

        key = (
            parcel.number.rectangle,
            parcel.number.killa,
        )

        self._data[key] = parcel

    def update(
        self,
        parcel: Parcel,
    ) -> None:

        self.add(parcel)

    def remove(
        self,
        number: ParcelNumber,
    ) -> None:

        key = (
            number.rectangle,
            number.killa,
        )

        self._data.pop(
            key,
            None,
        )

    def get(
        self,
        number: ParcelNumber,
    ) -> Parcel | None:

        key = (
            number.rectangle,
            number.killa,
        )

        return self._data.get(key)

    def list(
        self,
    ) -> list[Parcel]:

        return list(
            self._data.values(),
        )

    def exists(
        self,
        number: ParcelNumber,
    ) -> bool:

        return (
            self.get(number)
            is not None
        )


def make_parcel() -> Parcel:
    """
    Create a sample parcel.
    """

    return Parcel(
        number=ParcelNumber(
            rectangle=24,
            killa="7",
        ),
        area=Area.from_kms(
            kanal=2,
            marla=13,
            sarsai=4,
        ),
        remarks="Test Parcel",
    )


def test_create_parcel() -> None:

    repository = FakeParcelRepository()

    service = ParcelService(
        repository,
    )

    parcel = make_parcel()

    service.create(
        parcel,
    )

    assert service.exists(
        parcel.number,
    )


def test_duplicate_parcel() -> None:

    repository = FakeParcelRepository()

    service = ParcelService(
        repository,
    )

    parcel = make_parcel()

    service.create(
        parcel,
    )

    import pytest

    with pytest.raises(
        ValueError,
    ):

        service.create(
            parcel,
        )


def test_get_parcel() -> None:

    repository = FakeParcelRepository()

    service = ParcelService(
        repository,
    )

    parcel = make_parcel()

    service.create(
        parcel,
    )

    loaded = service.get(
        parcel.number,
    )

    assert loaded is not None

    assert (
        loaded.number.rectangle
        == 24
    )


def test_list() -> None:

    repository = FakeParcelRepository()

    service = ParcelService(
        repository,
    )

    service.create(
        make_parcel(),
    )

    assert len(
        service.list()
    ) == 1


def test_exists() -> None:

    repository = FakeParcelRepository()

    service = ParcelService(
        repository,
    )

    parcel = make_parcel()

    assert not service.exists(
        parcel.number,
    )

    service.create(
        parcel,
    )

    assert service.exists(
        parcel.number,
    )