"""
Haryana Revenue Toolkit (HRTK)

Unit tests for FormMode.
"""

from hrtk.presentation.common.form_mode import FormMode


def test_create_mode_exists() -> None:
    assert FormMode.CREATE.name == "CREATE"


def test_edit_mode_exists() -> None:
    assert FormMode.EDIT.name == "EDIT"


def test_modes_are_different() -> None:
    assert FormMode.CREATE is not FormMode.EDIT