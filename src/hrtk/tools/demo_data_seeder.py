"""
Haryana Revenue Toolkit (HRTK)

Application wrapper for the Developer Demo Database Seeder.
"""

from __future__ import annotations

from tools.demo_data_seeder import (
    DemoDataSeeder as _DemoDataSeeder,
)


class DemoDataSeeder(_DemoDataSeeder):
    """
    Application wrapper.

    The real implementation lives in the project's
    developer tools package.
    """

    pass


__all__ = [
    "DemoDataSeeder",
]