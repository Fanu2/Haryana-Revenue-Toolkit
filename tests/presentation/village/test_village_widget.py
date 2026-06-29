"""
Haryana Revenue Toolkit (HRTK)

Unit tests for VillageWidget.
"""

from __future__ import annotations

from PySide6.QtWidgets import QVBoxLayout

from hrtk.presentation.village.village_model import VillageModel
from hrtk.presentation.village.village_table import VillageTable
from hrtk.presentation.village.village_toolbar import VillageToolbar
from hrtk.presentation.village.village_widget import VillageWidget
from hrtk.repositories.village_repository import VillageRepository
from hrtk.services.village_service import VillageService


def make_service() -> VillageService:
    repository = VillageRepository()
    return VillageService(repository)


def make_widget() -> VillageWidget:
    return VillageWidget(make_service())


# ---------------------------------------------------------
# Construction
# ---------------------------------------------------------


def test_widget_can_be_created(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert isinstance(widget, VillageWidget)


# ---------------------------------------------------------
# Components
# ---------------------------------------------------------


def test_widget_has_toolbar(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert isinstance(widget.toolbar, VillageToolbar)


def test_widget_has_table(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert isinstance(widget.table, VillageTable)


def test_widget_has_model(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert isinstance(widget.model, VillageModel)


# ---------------------------------------------------------
# Layout
# ---------------------------------------------------------


def test_widget_has_layout(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert isinstance(widget.layout(), QVBoxLayout)


def test_layout_contains_two_widgets(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert widget.layout().count() == 2


def test_toolbar_is_first_widget(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert widget.layout().itemAt(0).widget() is widget.toolbar


def test_table_is_second_widget(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert widget.layout().itemAt(1).widget() is widget.table


# ---------------------------------------------------------
# Representation
# ---------------------------------------------------------


def test_repr(qtbot) -> None:
    widget = make_widget()

    qtbot.addWidget(widget)

    assert "VillageWidget" in repr(widget)