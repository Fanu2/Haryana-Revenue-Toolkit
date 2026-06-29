"""
Haryana Revenue Toolkit (HRTK)

Unit tests for VillageTable.
"""

from __future__ import annotations

from PySide6.QtWidgets import QAbstractItemView

from hrtk.domain.village import Village
from hrtk.presentation.village.village_model import VillageModel
from hrtk.presentation.village.village_table import VillageTable
from hrtk.repositories.village_repository import VillageRepository
from hrtk.services.village_service import VillageService


def make_service() -> VillageService:
    repository = VillageRepository()
    return VillageService(repository)


def make_model() -> VillageModel:
    return VillageModel(make_service())


def make_table() -> VillageTable:
    return VillageTable(make_model())


def make_village() -> Village:
    return Village(
        code="001",
        name="Sirsa",
        tehsil="Sirsa",
        district="Sirsa",
    )


# ---------------------------------------------------------
# Construction
# ---------------------------------------------------------


def test_table_can_be_created(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert isinstance(table, VillageTable)


def test_model_is_attached(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert isinstance(table.model(), VillageModel)


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------


def test_sorting_enabled(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert table.isSortingEnabled()


def test_alternating_row_colors(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert table.alternatingRowColors()


def test_selection_behavior(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert (
        table.selectionBehavior()
        == QAbstractItemView.SelectRows
    )


def test_selection_mode(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert (
        table.selectionMode()
        == QAbstractItemView.SingleSelection
    )


def test_editing_disabled(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert (
        table.editTriggers()
        == QAbstractItemView.NoEditTriggers
    )


# ---------------------------------------------------------
# Selected Village
# ---------------------------------------------------------


def test_selected_village_empty(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert table.selected_village() is None


# ---------------------------------------------------------
# Representation
# ---------------------------------------------------------


def test_repr(qtbot) -> None:
    table = make_table()

    qtbot.addWidget(table)

    assert "VillageTable" in repr(table)in repr(table)