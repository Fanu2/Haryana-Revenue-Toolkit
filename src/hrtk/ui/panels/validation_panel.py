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


class ValidationPanel(
    QFrame,
):
    """
    Generic validation panel used
    throughout HRTK.

    Displays validation items with
    status indicators.

    No business logic belongs here.
    """

    VALID = "✓"

    WARNING = "⚠"

    ERROR = "✗"

    def __init__(
        self,
        title: str = "Validation",
        parent: QWidget | None = None,
    ) -> None:

        super().__init__(
            parent,
        )

        self._title = QLabel(
            title,
        )

        self._rows: dict[
            str,
            QLabel,
        ] = {}

        self._layout = QVBoxLayout(
            self,
        )

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
        """
        Set the panel title.
        """

        self._title.setText(
            title,
        )

    def title(
        self,
    ) -> str:
        """
        Return the panel title.
        """

        return self._title.text()

    def set_status(
        self,
        label: str,
        symbol: str,
        message: str = "",
    ) -> None:
        """
        Create or update a validation row.
        """

        text = symbol

        if message:

            text = (
                f"{symbol} {message}"
            )

        if label not in self._rows:

            value_label = QLabel()

            value_label.setAlignment(
                Qt.AlignLeft
                | Qt.AlignVCenter,
            )

            self._rows[label] = (
                value_label
            )

            self._form.addRow(
                QLabel(label),
                value_label,
            )

        self._rows[label].setText(
            text,
        )

    def set_valid(
        self,
        label: str,
        message: str = "Valid",
    ) -> None:
        """
        Mark a validation item as valid.
        """

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
        """
        Mark a validation item as warning.
        """

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
        """
        Mark a validation item as error.
        """

        self.set_status(
            label,
            self.ERROR,
            message,
        )

    def status(
        self,
        label: str,
    ) -> str:
        """
        Return the displayed status.
        """

        if label not in self._rows:

            return ""

        return self._rows[
            label
        ].text()

    def labels(
        self,
    ) -> list[str]:
        """
        Return all validation labels.
        """

        return list(
            self._rows.keys(),
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all validation items.
        """

        for label in list(
            self._rows.keys(),
        ):

            self.remove_item(
                label,
            )

    # ---------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------

    def _configure(
        self,
    ) -> None:
        """
        Configure the panel appearance.
        """

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

    # ---------------------------------------------------------
    # Bulk Operations
    # ---------------------------------------------------------

    def set_items(
        self,
        items: dict[
            str,
            tuple[str, str],
        ],
    ) -> None:
        """
        Replace all validation items.

        Dictionary format:

        {
            "Ownership": ("✓", "Valid"),
            "Area": ("⚠", "Balance Remaining"),
        }
        """

        self.clear()

        for label, (
            symbol,
            message,
        ) in items.items():

            self.set_status(
                label,
                symbol,
                message,
            )

    def values(
        self,
    ) -> dict[
        str,
        str,
    ]:
        """
        Return displayed values.
        """

        return {

            label: value.text()

            for label, value
            in self._rows.items()

        }

    def remove_item(
        self,
        label: str,
    ) -> None:
        """
        Remove one validation item.
        """

        if label not in self._rows:

            return

        value_label = self._rows.pop(
            label,
        )

        for row in range(
            self._form.rowCount(),
        ):

            item = self._form.itemAt(
                row,
                QFormLayout.LabelRole,
            )

            if item is None:

                continue

            widget = item.widget()

            if (
                isinstance(
                    widget,
                    QLabel,
                )
                and widget.text() == label
            ):

                self._form.removeRow(
                    row,
                )

                widget.deleteLater()

                value_label.deleteLater()

                break

    # ---------------------------------------------------------
    # Private Helpers
    # ---------------------------------------------------------

    def _has_item(
        self,
        label: str,
    ) -> bool:
        """
        Return True if the
        validation item exists.
        """

        return (
            label in self._rows
        )
    
