"""
Haryana Revenue Toolkit (HRTK)

Unit tests for VillageToolbar.
"""

from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QLineEdit

from hrtk.presentation.village.village_toolbar import VillageToolbar


def make_toolbar() -> VillageToolbar:
    return VillageToolbar()


# ---------------------------------------------------------
# Construction
# ---------------------------------------------------------


def test_toolbar_can_be_created(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    assert isinstance(toolbar, VillageToolbar)


def test_toolbar_title(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    assert toolbar.windowTitle() == "Village"


# ---------------------------------------------------------
# Actions
# ---------------------------------------------------------


def test_action_count(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    actions = [
        action
        for action in toolbar.actions()
        if isinstance(action, QAction)
        and action.text()
    ]

    assert len(actions) == 5


def test_action_names(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    names = [
        action.text()
        for action in toolbar.actions()
        if action.text()
    ]

    assert names == [
        "Add",
        "Edit",
        "Deactivate",
        "Refresh",
        "Export",
    ]


# ---------------------------------------------------------
# Search
# ---------------------------------------------------------


def test_search_box_exists(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    widgets = toolbar.findChildren(QLineEdit)

    assert len(widgets) == 1


def test_search_placeholder(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    widget = toolbar.findChild(QLineEdit)

    assert widget.placeholderText() == "Search villages..."


def test_search_text_property(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    widget = toolbar.findChild(QLineEdit)

    widget.setText("Sirsa")

    assert toolbar.search_text == "Sirsa"


def test_clear_search(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    widget = toolbar.findChild(QLineEdit)

    widget.setText("Sirsa")

    toolbar.clear_search()

    assert toolbar.search_text == ""


# ---------------------------------------------------------
# Representation
# ---------------------------------------------------------


def test_repr(qtbot) -> None:
    toolbar = make_toolbar()

    qtbot.addWidget(toolbar)

    assert "VillageToolbar" in repr(toolbar)