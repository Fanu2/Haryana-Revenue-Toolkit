"""
Haryana Revenue Toolkit (HRTK)

Khewat Parcel Dialog.

Reserved for future use.

The Khewat–Parcel module is implemented as a full
workspace instead of a modal CRUD dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class KhewatParcelDialog(QDialog):
    """
    Compatibility dialog.

    Relationship management is performed in the
    Khewat–Parcel Workspace.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.setWindowTitle(
            "Khewat–Parcel Relationship"
        )

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel(
                "Relationship management is available\n"
                "through the Khewat–Parcel Workspace."
            )
        )

        close_button = QPushButton("Close")

        close_button.clicked.connect(self.accept)

        layout.addWidget(close_button)