"""
Haryana Revenue Toolkit (HRTK)

Seed Context.

Creates a fully initialized ApplicationContext
for development database seeding.
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
    Create an initialized application context.
    """

    application = Application()

    return application.context