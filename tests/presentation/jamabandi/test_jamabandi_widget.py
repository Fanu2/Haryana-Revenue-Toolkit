"""
Haryana Revenue Toolkit (HRTK)

Tests for JamabandiWidget.
"""

from hrtk.presentation.jamabandi.jamabandi_widget import (
    JamabandiWidget,
)


def test_widget_import():
    """
    Verify the widget can be imported.
    """

    assert JamabandiWidget is not None