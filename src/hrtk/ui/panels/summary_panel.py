"""
Haryana Revenue Toolkit (HRTK)

Reusable Summary Panel.
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


class SummaryPanel(QFrame):
    """
    Generic summary panel used throughout HRTK.

    Displays a title and a dynamic list of
    label/value pairs.

    This widget contains no business logic.
    """

    def __init__(
        self,
        title: str = "Summary",
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

        self._title.setText(
            title,
        )

    def title(
        self,
    ) -> str:

        return self._title.text()

    def set_value(
        self,
        label: str,
        value: str,
    ) -> None:
        """
        Create or update one summary value.
        """

        if label not in self._rows:

            value_label = QLabel()

            value_label.setAlignment(
                Qt.AlignRight
                | Qt.AlignVCenter,
            )

            self._rows[label] = value_label

            self._form.addRow(
                QLabel(label),
                value_label,
            )

        self._rows[label].setText(
            value,
        )

    def set_values(
        self,
        values: dict[str, str],
    ) -> None:
        """
        Update multiple values.
        """

        for label, value in values.items():

            self.set_value(
                label,
                value,
            )

    def value(
        self,
        label: str,
    ) -> str:

        if label not in self._rows:

            return ""

        return self._rows[label].text()

    def values(
        self,
    ) -> dict[str, str]:

        return {
            label: widget.text()
            for label, widget
            in self._rows.items()
        }

    def labels(
        self,
    ) -> list[str]:

        return list(
            self._rows.keys(),
        )

    def clear(
        self,
    ) -> None:
        """
        Clear displayed values only.

        Existing rows are intentionally
        retained to avoid Qt ownership
        issues.
        """

        for widget in (
            self._rows.values()
        ):

            widget.clear()

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

        self._layout.setSpacing(
            8,
        )

        self._form.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self._form.setHorizontalSpacing(
            20,
        )

        self._form.setVerticalSpacing(
            6,
        )

        self._title.setAlignment(
            Qt.AlignCenter,
        )

        font = self._title.font()

        font.setBold(
            True,
        )

        font.setPointSize(
            font.pointSize() + 1,
        )

        self._title.setFont(
            font,
        )