"""
Haryana Revenue Toolkit (HRTK)

Ownership Presentation Package.
"""

from .ownership_widget import OwnershipWidget
from .ownership_dialog import OwnershipDialog
from .ownership_model import OwnershipTableModel
from .ownership_table import OwnershipTable
from .ownership_toolbar import OwnershipToolbar

__all__ = [
    "OwnershipWidget",
    "OwnershipDialog",
    "OwnershipTableModel",
    "OwnershipTable",
    "OwnershipToolbar",
]