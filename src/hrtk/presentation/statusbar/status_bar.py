"""
Haryana Revenue Toolkit (HRTK)

Status Bar.
"""

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QStatusBar


class StatusBar(QStatusBar):
    """
    Main application status bar.
    """

    def __init__(self) -> None:
        super().__init__()

        self._build()

    def _build(self) -> None:

        self.showMessage("Ready")

        self.workspace_label = QLabel("Workspace: Ready")
        self.config_label = QLabel("Configuration: Loaded")
        self.logging_label = QLabel("Logging: Ready")
        self.version_label = QLabel("v0.2 Alpha")

        self.addPermanentWidget(self.workspace_label)
        self.addPermanentWidget(self.config_label)
        self.addPermanentWidget(self.logging_label)
        self.addPermanentWidget(self.version_label)