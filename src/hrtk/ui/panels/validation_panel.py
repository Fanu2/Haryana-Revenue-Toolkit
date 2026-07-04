"""
Haryana Revenue Toolkit (HRTK)

Reusable Validation Panel.
"""

from __future__ import annotations

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QFormLayout,
    QFrame,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class ValidationPanel(QFrame):
    """
    Generic validation panel used
    throughout HRTK.
    """

    VALID = "✓"
    WARNING = "⚠"
    ERROR = "✗"

    def __init__(
        self,
        title: str = "Validation",
        parent: QWidget | None = None,
    ) -> None:

        super().__init__(parent)

        self._title = QLabel(title)

        self._rows: dict[str, QLabel] = {}

        self._layout = QVBoxLayout(self)

        self._form = QFormLayout()

        self._configure()

        self._layout.addWidget(
            self._title,
        )

        self._layout.addLayout(
            self._form,
        )

        self._layout.addStretch()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_title(
        self,
        title: str,
    ) -> None:

        self._title.setText(title)

    def title(
        self,
    ) -> str:

        return self._title.text()

    def set_status(
        self,
        label: str,
        symbol: str,
        message: str = "",
    ) -> None:
        """
        Create or update a validation item.
        """

        text = symbol

        if message:

            text = f"{symbol} {message}"

        if label not in self._rows:

            value_label = QLabel()

            value_label.setAlignment(
                Qt.AlignLeft
                | Qt.AlignVCenter,
            )

            self._rows[label] = value_label

            self._form.addRow(
                QLabel(label),
                value_label,
            )

        self._rows[label].setText(text)

    def set_valid(
        self,
        label: str,
        message: str = "Valid",
    ) -> None:

        self.set_status(
            label,
            self.VALID,
            message,
        )

    def set_warning(
        self,
        label: str,
        message: str = "Warning",
    ) -> None:

        self.set_status(
            label,
            self.WARNING,
            message,
        )

    def set_error(
        self,
        label: str,
        message: str = "Error",
    ) -> None:

        self.set_status(
            label,
            self.ERROR,
            message,
        )

    def clear(
        self,
    ) -> None:
        """
        Clear displayed values only.
        """

        for widget in self._rows.values():

            widget.clear()

    def labels(
        self,
    ) -> list[str]:

        return list(self._rows.keys())

    def values(
        self,
    ) -> dict[str, str]:

        return {
            label: widget.text()
            for label, widget
            in self._rows.items()
        }

    # ---------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------

    def _configure(
        self,
    ) -> None:

        self.setFrameShape(
            QFrame.StyledPanel,
        )

        self.setFrameShadow(
            QFrame.Raised,
        )

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred,
        )

        self._layout.setContentsMargins(
            10,
            10,
            10,
            10,
        )

        self._layout.setSpacing(8)

        self._form.setHorizontalSpacing(20)

        self._form.setVerticalSpacing(6)

        self._title.setAlignment(
            Qt.AlignCenter,
        )

        font = self._title.font()

        font.setBold(True)

        font.setPointSize(
            font.pointSize() + 1,
        )

        self._title.setFont(font)