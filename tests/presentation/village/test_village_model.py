"""
Haryana Revenue Toolkit (HRTK)

Unit tests for VillageModel.
"""

from __future__ import annotations

from PySide6.QtCore import Qt

from hrtk.domain.village import Village
from hrtk.presentation.village.village_model import VillageModel
from hrtk.repositories.village_repository import VillageRepository
from hrtk.services.village_service import VillageService


def make_service() -> VillageService:
    """
    Create a VillageService for testing.
    """
    repository = VillageRepository()
    return VillageService(repository)


def make_model() -> VillageModel:
    """
    Create a VillageModel for testing.
    """
    return VillageModel(make_service())


def make_village() -> Village:
    """
    Create a valid Village.
    """
    return Village(
        code="001",
        name="Sirsa",
        tehsil="Sirsa",
        district="Sirsa",
    )


# ---------------------------------------------------------
# Construction
# ---------------------------------------------------------


def test_model_can_be_created() -> None:
    model = make_model()

    assert isinstance(model, VillageModel)


def test_service_property() -> None:
    model = make_model()

    assert model.service is not None


# ---------------------------------------------------------
# Empty Model
# ---------------------------------------------------------


def test_empty_row_count() -> None:
    model = make_model()

    assert model.rowCount() == 0


def test_column_count() -> None:
    model = make_model()

    assert model.columnCount() == 6


# ---------------------------------------------------------
# Refresh
# ---------------------------------------------------------


def test_refresh() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    model = VillageModel(service)

    model.refresh()

    assert model.rowCount() == 1


# ---------------------------------------------------------
# Village Lookup
# ---------------------------------------------------------


def test_village_lookup() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    model = VillageModel(service)

    assert model.village(0) is village


def test_invalid_village_lookup() -> None:
    model = make_model()

    assert model.village(100) is None


# ---------------------------------------------------------
# Headers
# ---------------------------------------------------------


def test_headers() -> None:
    model = make_model()

    expected = (
        "Code",
        "Name",
        "Tehsil",
        "District",
        "State",
        "Status",
    )

    for column, header in enumerate(expected):
        assert (
            model.headerData(
                column,
                Qt.Horizontal,
            )
            == header
        )


# ---------------------------------------------------------
# Display Data
# ---------------------------------------------------------


def test_display_data() -> None:
    service = make_service()

    village = make_village()

    service.register(village)

    model = VillageModel(service)

    index = model.index(
        0,
        VillageModel.COLUMN_NAME,
    )

    assert (
        model.data(index)
        == "Sirsa"
    )


def test_status_display() -> None:
    service = make_service()

    village = make_village()

    village.deactivate()

    service.register(village)

    model = VillageModel(service)

    index = model.index(
        0,
        VillageModel.COLUMN_STATUS,
    )

    assert (
        model.data(index)
        == "Inactive"
    )


# ---------------------------------------------------------
# Representation
# ---------------------------------------------------------


def test_repr() -> None:
    model = make_model()

    assert "VillageModel" in repr(model)