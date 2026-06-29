"""
Haryana Revenue Toolkit (HRTK)

Main Toolbar.
"""

from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class MainToolbar(QToolBar):
    """
    Main application toolbar.
    """

    def __init__(self) -> None:
        super().__init__("Main Toolbar")

        self.setMovable(False)

        self._create_actions()

    def _create_actions(self) -> None:
        """Create toolbar actions."""

        self.new_action = QAction("New", self)
        self.open_action = QAction("Open", self)
        self.save_action = QAction("Save", self)

        self.undo_action = QAction("Undo", self)
        self.redo_action = QAction("Redo", self)

        self.zoom_in_action = QAction("Zoom In", self)
        self.zoom_out_action = QAction("Zoom Out", self)

        self.addAction(self.new_action)
        self.addAction(self.open_action)
        self.addAction(self.save_action)

        self.addSeparator()

        self.addAction(self.undo_action)
        self.addAction(self.redo_action)

        self.addSeparator()

        self.addAction(self.zoom_in_action)
        self.addAction(self.zoom_out_action)