"""
Haryana Revenue Toolkit (HRTK)

Village Toolbar.
"""

from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class VillageToolbar(QToolBar):
    """
    Toolbar for Village Management.
    """

    def __init__(self) -> None:
        super().__init__("Village Toolbar")

        self.setMovable(False)

        self._create_actions()

    def _create_actions(self) -> None:
        """Create toolbar actions."""

        self.new_action = QAction("New", self)
        self.edit_action = QAction("Edit", self)
        self.delete_action = QAction("Delete", self)
        self.refresh_action = QAction("Refresh", self)

        self.addAction(self.new_action)
        self.addAction(self.edit_action)
        self.addAction(self.delete_action)

        self.addSeparator()

        self.addAction(self.refresh_action)

    def enable_editing(self, enabled: bool) -> None:
        """
        Enable or disable editing actions.
        """

        self.edit_action.setEnabled(enabled)
        self.delete_action.setEnabled(enabled)

    def __repr__(self) -> str:
        return (
            "VillageToolbar("
            f"actions={len(self.actions())})"
        )