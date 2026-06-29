"""
Haryana Revenue Toolkit (HRTK)

Unit tests for BaseDialog.
"""

from hrtk.presentation.common.base_dialog import BaseDialog
from hrtk.presentation.common.form_mode import FormMode


def test_create_dialog(qtbot) -> None:
    dialog = BaseDialog(FormMode.CREATE)

    qtbot.addWidget(dialog)

    assert dialog.is_create_mode
    assert not dialog.is_edit_mode


def test_edit_dialog(qtbot) -> None:
    dialog = BaseDialog(FormMode.EDIT)

    qtbot.addWidget(dialog)

    assert dialog.is_edit_mode
    assert not dialog.is_create_mode


def test_mode_property(qtbot) -> None:
    dialog = BaseDialog(FormMode.CREATE)

    qtbot.addWidget(dialog)

    assert dialog.mode is FormMode.CREATE