"""
Haryana Revenue Toolkit (HRTK)

Developer Context.
"""

from __future__ import annotations

from hrtk.application.application import (
    Application,
)

from hrtk.application.application_context import (
    ApplicationContext,
)


def create_context() -> ApplicationContext:
    """
    Create a fully initialized HRTK
    application context.
    """

    application = Application()

    return application.context