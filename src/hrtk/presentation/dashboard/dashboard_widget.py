"""
Haryana Revenue Toolkit (HRTK)

Dashboard Widget.

The application's home page.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.application_context import ApplicationContext


class DashboardWidget(QWidget):
    """
    HRTK dashboard.

    Displays application information and infrastructure status.
    """

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__()

        self._context = context

        self._build_ui()

    @property
    def context(self) -> ApplicationContext:
        """Return the application context."""
        return self._context

    def _build_ui(self) -> None:
        """Construct the dashboard."""

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)

        layout.addStretch()

        # ---------------------------------------------------------
        # Title
        # ---------------------------------------------------------

        title = QLabel("Haryana Revenue Toolkit")
        title_font = QFont()
        title_font.setPointSize(22)
        title_font.setBold(True)

        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)

        # ---------------------------------------------------------
        # Subtitle
        # ---------------------------------------------------------

        subtitle = QLabel(
            "Digital Land Revenue Management System"
        )

        subtitle_font = QFont()
        subtitle_font.setPointSize(12)

        subtitle.setFont(subtitle_font)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(subtitle)

        layout.addSpacing(30)

        # ---------------------------------------------------------
        # Status Card
        # ---------------------------------------------------------

        card = QFrame()
        card.setFrameShape(QFrame.Shape.StyledPanel)

        card_layout = QVBoxLayout(card)

        card_layout.addWidget(
            QLabel("✓ Workspace Initialized")
        )

        card_layout.addWidget(
            QLabel("✓ Configuration Loaded")
        )

        card_layout.addWidget(
            QLabel("✓ Logging Ready")
        )

        layout.addWidget(card)

        layout.addSpacing(20)

        # ---------------------------------------------------------
        # Workspace
        # ---------------------------------------------------------

        workspace_title = QLabel("Workspace")

        workspace_font = QFont()
        workspace_font.setBold(True)

        workspace_title.setFont(workspace_font)

        layout.addWidget(workspace_title)

        workspace_path = QLabel(
            str(self.context.workspace.root)
        )

        workspace_path.setWordWrap(True)

        layout.addWidget(workspace_path)

        layout.addSpacing(20)

        # ---------------------------------------------------------
        # Version
        # ---------------------------------------------------------

        version = QLabel("Version 0.2.0 Alpha")

        version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(version)

        layout.addStretch()

    def __repr__(self) -> str:
        return "DashboardWidget()"